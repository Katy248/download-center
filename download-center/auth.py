from .api import login, set_jwt_token

class AuthState():
    __license_key: str
    __authenticated: bool = False

    def __init__(self):
        ...

    def authenticate(self, license_key: str):
        print("Authentication")
        self.__license_key = license_key
        result = login(license_key)
        if not result: return
        

        self.__access_token = result["access_token"]
        set_jwt_token(self.__access_token)

        self.__authenticated = True
    
    def is_authenticated(self): return self.__authenticated 


AUTH_STATE = AuthState()
