from typing import final

from gi.repository import GObject

from .api import login
from .api import logout as api_logout
from .config import APP_ID, SETTINGS
from .utils import print_error, print_log

AUTHENTICATED_CHANGED_SIGNAL = "authenticated_changed"
AUTHENTICATION_FAILED_SIGNAL = "authentication_failed"


class AuthState(GObject.Object):
    __gtype_name__: str = "AuthState"
    __gsignals__ = {
        AUTHENTICATED_CHANGED_SIGNAL: (GObject.SignalFlags.RUN_FIRST, None, (bool,)),
        AUTHENTICATION_FAILED_SIGNAL: (GObject.SignalFlags.RUN_FIRST, None, (str,)),
    }
    authenticated: GObject.Property = GObject.Property(type=bool, default=False)

    def __init__(self):

        super().__init__()

    async def check_auth(self):
        print_log("Checking authentication")
        key = SETTINGS.get_string("license-key")
        _ = await self.authenticate(key)
        self.emit(AUTHENTICATED_CHANGED_SIGNAL, self.authenticated)
        print_log(f"Authentication state: authenticated - {self.authenticated}")

    async def authenticate(self, license_key: str) -> bool:
        if license_key == "":
            self.authenticated = False
            self.emit(AUTHENTICATED_CHANGED_SIGNAL, self.authenticated)
            return self.authenticated
        try:
            print_log("Start authenticating")
            self.authenticated = login(license_key)
        except Exception as e:
            print_error(f"Failed to authenticate: {e}")
            self.emit(AUTHENTICATED_CHANGED_SIGNAL, self.authenticated)
            self.emit(AUTHENTICATION_FAILED_SIGNAL, str(e))
            return False

        if self.authenticated and SETTINGS.get_boolean("stay-logged-in"):
            SETTINGS.set_string("license-key", license_key)

        self.emit(AUTHENTICATED_CHANGED_SIGNAL, self.authenticated)
        return self.authenticated

    def is_authenticated(self) -> bool:
        return self.authenticated

    def logout(self):
        success = SETTINGS.set_string("license-key", "")
        if not success:
            print_error("Failed unset license key")

        api_logout()
        self.emit(AUTHENTICATED_CHANGED_SIGNAL, False)


AUTH_STATE = AuthState()


def logout():
    AUTH_STATE.logout()
