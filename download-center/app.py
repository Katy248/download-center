from gi.repository import Adw, Gio
from .config import APP_ID
from .MainWindow import MainWindow, MAIN_WINDOW


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.set_resource_base_path("/ru/katy248/download-center")

        about_action = Gio.SimpleAction.new("win.about", None)
        about_action.connect(
            "change-state", lambda action, value: print(action, value, "Changed state")
        )
        about_action.connect("activate", self.on_about_activated)
        self.add_action(about_action)
        self.set_accels_for_action("win.about", ["<Control>h"])
        print(about_action.get_enabled())

    def do_activate(app: Adw.Application):
        window = MainWindow(app)
        window.present()

    def on_about_activated(self, action, _):
        dialog = Adw.AboutDialog()
        dialog.present(MAIN_WINDOW)
