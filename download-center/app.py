from gi.repository import Adw, Gio, Gtk
from .config import APP_ID
from .MainWindow import MainWindow


WEB_URL = "https://update-center.red-soft.ru"


class Application(Adw.Application):
    window: MainWindow

    def __init__(self):
        super().__init__(application_id=APP_ID, flags=Gio.ApplicationFlags.NON_UNIQUE)
        self.set_resource_base_path("/ru/katy248/download-center")

        self.set_accels_for_action("win.about", ["<Control>question"])
        self.set_accels_for_action(
            "win.settings", ["<Ctrl>comma", "<Ctrl>slash", "<Ctrl>S"]
        )

        open_in_web_action = Gio.SimpleAction.new("open-in-web", None)
        open_in_web_action.connect("activate", self.on_open_in_web)
        self.add_action(open_in_web_action)

    def do_activate(self):
        self.window = MainWindow(self)
        self.window.present()

    def on_open_in_web(self, action, param):
        launcher = Gtk.UriLauncher.new(WEB_URL)
        launcher.launch(parent=self.window)
