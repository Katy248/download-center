from gi.repository import Gio
from .config import APP_NAME, APP_ID
import locale

if __name__ == "__main__":
    # locale.bindtextdomain(APP_NAME, localedir)
    locale.textdomain(APP_NAME)

    resource = Gio.Resource.load(f"/usr/share/{APP_NAME}/{APP_ID}.gresource")
    resource._register()

    from .app import Application

    app = Application()
    app.run([])
