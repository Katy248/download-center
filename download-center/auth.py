from .api import login
from .config import SETTINGS


class AuthState:
    __license_key: str
    __authenticated: bool = False

    def __init__(self):
        key = SETTINGS.get_string("license-key")
        if key is not None:
            self.authenticate(key)

    def authenticate(self, license_key: str):
        self.__authenticated = login(license_key)
        if self.__authenticated:
            SETTINGS.set_string("license-key", license_key)

    def is_authenticated(self):
        return self.__authenticated


AUTH_STATE = AuthState()
