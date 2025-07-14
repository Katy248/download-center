from gi.repository import Gio
from .config import APP_NAME, GRESOURCE_FILE, LOCALE_DIR, VERSION
import locale

if __name__ == "__main__":
    print(APP_NAME, VERSION)
    locale.bindtextdomain(APP_NAME, LOCALE_DIR)
    locale.textdomain(APP_NAME)

    resource = Gio.Resource.load(GRESOURCE_FILE)
    Gio.resources_register(resource)

    from .app import Application

    app = Application()
    app.run([])
