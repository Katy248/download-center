from gi.repository import Gio
from .config import APP_NAME, APP_ID, GRESOURCE_FILE, LOCALE_DIR
import locale

if __name__ == "__main__":
    locale.bindtextdomain(APP_NAME, LOCALE_DIR)
    locale.textdomain(APP_NAME)

    resource = Gio.Resource.load(GRESOURCE_FILE)
    resource._register()

    from .app import Application

    app = Application()
    app.run([])
