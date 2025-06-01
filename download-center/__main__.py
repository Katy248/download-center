from gi.repository import Adw, Gio

from .config import APP_ID
from .MainWindow import MainWindow, MAIN_WINDOW


def on_about_activated(action, _):
    dialog = Adw.AboutDialog()
    dialog.present(MAIN_WINDOW)


def on_activate(app: Adw.Application):
    window = MainWindow(app)
    window.present()

    about_action = Gio.SimpleAction(name="win.about")
    about_action.connect("activate", on_about_activated)
    window.add_action(about_action)

    app.set_accels_for_action("win.about", ["<Control>H"])


if __name__ == "__main__":
    app = Adw.Application(application_id=APP_ID)
    app.connect("activate", on_activate)
    app.run([])
