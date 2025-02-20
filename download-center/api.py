from http.client import HTTPSConnection, OK
import json
import requests
from gi.repository import Gtk, Gio, GLib
import datetime
from threading import Thread
from .state import DOWNLOADING, notify

BASE_ADDR = "https://update-center.red-soft.ru"

__jwt: str
__license_key: str
__last_auth: datetime.datetime = datetime.datetime.fromtimestamp(0)
# __client = HTTPSConnection(BASE_ADDR)


def __auth(license_key: str) -> bool:
    global __jwt, __license_key, __last_auth
    response = requests.post(
        BASE_ADDR + "/auth/login",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"key": license_key}),
    )

    if not response.status_code == OK:
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


def login(key: str):
    return __auth(key)


def get_files(current=True):
    if not __check_auth():
        return False

    response = requests.get(
        BASE_ADDR + "/download/files?type=current",
        headers={"Authorization": f"Bearer {__jwt}"},
    )

    if not response.status_code == OK:
        return False

    return response.json()


def __download_file(file: str):
    from .MainWindow import MAIN_WINDOW

    print("Start downloading")
    DOWNLOADING = True

    file_name = file.split("/")[-1]
    gio_file = Gio.File.new_for_path(file_name)

    file_dialog = Gtk.FileDialog()
    file_dialog.set_initial_file(gio_file)

    def callback(source, res):
        nonlocal gio_file
        gio_file = source.save_finish(res)

    file_dialog.save(MAIN_WINDOW, callback=callback)
    with open(gio_file.get_path(), "wb") as fs_file:
        response = requests.post(BASE_ADDR + "/download/files", data={"file": file})
        fs_file.write(response.content)

    DOWNLOADING = False
    notify('File "%s" downloaded' % file_name)
    print("End downloading")


def __download_in_thread(file: str):
    thread = Thread(target=__download_file, args=(file,))
    thread.start()


def download_hash(file: str):
    __download_in_thread(file)


def download_rpm(file: str):
    __download_in_thread(file)
