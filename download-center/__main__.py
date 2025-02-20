import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from .MainWindow import MainWindow

APP_NAME = "download-center"

APP_ID = f"ru.red-soft.{APP_NAME}"


def on_activate(app: Adw.Application):
    window = MainWindow(app)
    window.present()


if __name__ == "__main__":
    app = Adw.Application(application_id=APP_ID)
    app.connect("activate", on_activate)
    app.run([])
