from gi.repository import Adw
from .config import APP_ID, SETTINGS
from .MainWindow import MainWindow


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.set_resource_base_path("/ru/katy248/download-center")

        self.set_accels_for_action("win.about", ["<Control>question"])
        self.set_accels_for_action("win.settings", ["<Ctrl>slash", "<Ctrl>S"])

        self.add_entrance()

    def add_entrance(self):
        SETTINGS.set_int("entrance-count", SETTINGS.get_int("entrance-count") + 1)

    def do_activate(self):
        window = MainWindow(self)
        window.present()
