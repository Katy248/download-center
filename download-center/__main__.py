from gi.repository import Adw, Gio

from pathlib import Path

from .config import APP_ID
from .MainWindow import MainWindow, MAIN_WINDOW


def on_about_activated(action, _):
    dialog = Adw.AboutDialog()
    dialog.present(MAIN_WINDOW)


def on_activate(app: Adw.Application):
    window = MainWindow(app)
    window.present()


if __name__ == "__main__":
    app = Adw.Application(application_id=APP_ID)
    app.connect("activate", on_activate)
    app.set_resource_base_path("/ru/katy248/download-center")
    # res = Gio.Resource.load(f"{Path.home()}/.local/share/{APP_ID}/{APP_ID}.gresource")
    about_action = Gio.SimpleAction.new("win.about", None)

    about_action.connect(
        "change-state", lambda action, value: print(action, value, "Changed state")
    )
    about_action.connect("activate", on_about_activated)
    app.add_action(about_action)
    app.set_accels_for_action("win.about", ["<Control>h"])
    print(about_action.get_enabled())

    app.run([])
