from gi.repository import Adw, Gio
from .config import APP_ID
from .MainWindow import MainWindow


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID, flags=Gio.ApplicationFlags.NON_UNIQUE)
        self.set_resource_base_path("/ru/katy248/download-center")

        self.set_accels_for_action("win.about", ["<Control>question"])
        self.set_accels_for_action("win.settings", ["<Ctrl>slash", "<Ctrl>S"])

    def do_activate(self):
        window = MainWindow(self)
        window.present()
