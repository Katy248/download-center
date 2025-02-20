from gi.repository import Gtk, Adw

from .DownloadsView import DownloadsView
from .LoginView import LoginView
from .auth import AUTH_STATE

MAIN_WINDOW: Adw.ApplicationWindow = None


@Gtk.Template.from_file("./download-center/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    view: Adw.ToolbarView = Gtk.Template.Child()

    def __init__(self, app: Adw.Application, **kwargs):
        super().__init__(application=app, **kwargs)

        view = None
        if AUTH_STATE.is_authenticated():
            view = DownloadsView()
        else:
            view = LoginView(self.on_authenticate)

        self.view.set_content(view)
        MAIN_WINDOW = self
        # AUTH_STATE.connect("notify", self.on_authenticate)
        # self.set_content(DownloadsView())

    def on_authenticate(self):
        # print("Change views")
        downloads_view = DownloadsView()
        self.view.set_content(downloads_view)
