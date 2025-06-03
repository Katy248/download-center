from gi.repository import Gio
from .config import APP_NAME, APP_ID

if __name__ == "__main__":
    resource = Gio.Resource.load(f"/usr/share/{APP_NAME}/{APP_ID}.gresource")
    resource._register()

    from .app import Application

    app = Application()
    app.run([])
