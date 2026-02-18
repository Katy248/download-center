import asyncio
import gettext
import locale
import sys
import threading

from gi.repository import Gio  # type: ignore

from .auth import AUTH_STATE
from .config import APP_NAME, GRESOURCE_FILE, LOCALE_DIR, VERSION
from .utils import print_log

if __name__ == "__main__":
    print_log(f"{APP_NAME} version {VERSION}")

    _ = gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
    _ = gettext.textdomain(APP_NAME)

    _ = locale.textdomain(APP_NAME)
    _ = locale.bindtextdomain(APP_NAME, LOCALE_DIR)

    resource = Gio.Resource.load(GRESOURCE_FILE)
    Gio.resources_register(resource)
    from .app import Application

    app = Application()

    ui_thread = threading.Thread(target=app.run, args=([]))
    ui_thread.start()

    asyncio.run(AUTH_STATE.check_auth())

    ui_thread.join()
