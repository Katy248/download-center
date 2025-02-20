from http.client import HTTPSConnection
import json

BASE_ADDR = "update-center.red-soft.ru"

JWT_TOKEN: str
__jwt: str
__client = HTTPSConnection(BASE_ADDR)

def login(key: str):
    __client.request('POST', '/auth/login',headers={"Content-Type":"application/json"},body=json.dumps({"key":key}))

    response = __client.getresponse()
    str_resp = response.read().decode('utf-8')
    print(str_resp)

    if not response.status == 200:
        response.close()
        return False 
    
    response.close()
    return json.loads(str_resp)

def set_jwt_token(token: str):
    # nonlocal JWT_TOKEN
    JWT_TOKEN = token

def get_files(current=True):
    __client.request('GET', '/download/files?type=current',headers={ "Authorization": f"Bearer {__jwt}"})

    response = __client.getresponse()
    str_resp = response.read().decode('utf-8')
    print(str_resp)

    if not response.status == 200:
        response.close()
        return False 
    
    response.close()
    return json.loads(str_resp)
