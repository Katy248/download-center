from .api import login, logout as api_logout
from .config import SETTINGS

from gi.repository import GObject


AUTHENTICATED_CHANGED_SIGNAL = "authenticated_changed"


class AuthState(GObject.Object):
    __gtype_name__ = "AuthState"
    __gsignals__ = {
        AUTHENTICATED_CHANGED_SIGNAL: (GObject.SignalFlags.RUN_FIRST, None, (bool,))
    }
    authenticated = GObject.Property(type=bool, default=False)

    def __init__(self):
        super().__init__()
        key = SETTINGS.get_string("license-key")
        if key is not None:
            self.authenticate(key)

    def authenticate(self, license_key: str) -> bool:
        self.authenticated = login(license_key)
        if self.authenticated:
            self.emit(AUTHENTICATED_CHANGED_SIGNAL, True)
            SETTINGS.set_string("license-key", license_key)
        return self.authenticated

    def is_authenticated(self):
        return self.authenticated

    def logout(self):
        SETTINGS.set_string("license-key", "")
        api_logout()
        self.emit(AUTHENTICATED_CHANGED_SIGNAL, False)


AUTH_STATE = AuthState()


def logout():
    AUTH_STATE.logout()
