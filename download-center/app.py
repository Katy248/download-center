from gi.repository import Adw, Gio
from .config import APP_ID, APP_NAME
from .MainWindow import MainWindow, MAIN_WINDOW


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.set_resource_base_path("/ru/katy248/download-center")

        self.set_accels_for_action("win.about", ["<Control>h"])

    def do_activate(app: Adw.Application):
        window = MainWindow(app)
        window.present()
