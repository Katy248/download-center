import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from .config import APP_ID
from .MainWindow import MainWindow


def on_activate(app: Adw.Application):
    window = MainWindow(app)
    window.present()


if __name__ == "__main__":
    app = Adw.Application(application_id=APP_ID)
    app.connect("activate", on_activate)
    app.run([])
