from http.client import OK
import json
import requests
import datetime

BASE_ADDR = "https://update-center.red-soft.ru"

__jwt: str | None = None
__license_key: str | None = None
__last_auth: datetime.datetime = datetime.datetime.fromtimestamp(0)


def get_headers(
    with_json_content: bool = False, with_auth: bool = False
) -> dict[str, str]:
    global __jwt
    headers = {}
    if with_json_content:
        headers["Content-Type"] = "application/json"
    if with_auth:
        if __jwt is not None:
            headers["Authorization"] = f"Bearer {__jwt}"
        else:
            print("[ERROR] Failed add authorization header, JWT token is empty")

    return headers


def __auth(license_key: str) -> bool:
    global __jwt, __license_key, __last_auth
    response = requests.post(
        BASE_ADDR + "/auth/login",
        headers=get_headers(with_json_content=True),
        data=json.dumps({"key": license_key}),
    )

    if not response.status_code == OK:
        print(
            f"[ERROR] Auth failed with status code {response.status_code}. Body dump: {response.content}"
        )
        return False
    js = response.json()

    __license_key = license_key
    __jwt = js["access_token"]
    __last_auth = datetime.datetime.now()
    return True


def __check_auth() -> bool:
    if __jwt == None:
        return False
    if __license_key == None:
        return False

    if datetime.datetime.now().minute - __last_auth.minute >= 10:
        return __auth(__license_key)

    return True


def login(license_key: str):
    return __auth(license_key)


def logout():
    global __jwt, __license_key, __last_auth
    __jwt = None
    __license_key = None


def get_files():
    if not __check_auth():
        return False

    response = requests.get(
        BASE_ADDR + "/download/files?type=current",
        headers=get_headers(with_auth=True),
    )

    if not response.status_code == OK:
        return False

    return response.json()


def get_changelogs(changelogs_file_url: str) -> bytes:
    response = requests.post(
        BASE_ADDR + "/download/files",
        data=json.dumps({"file": changelogs_file_url}),
        headers=get_headers(with_auth=True, with_json_content=True),
    )
    return response.content
