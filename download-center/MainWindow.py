from gi.repository import Gtk, Adw

from .DownloadsPage import DownloadsPage
from .LoginPage import LoginPage
from .auth import AuthState, AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL

MAIN_WINDOW: Adw.ApplicationWindow = None


@Gtk.Template.from_file("./download-center/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    view: Adw.ToolbarView = Gtk.Template.Child()

    def __init__(self, app: Adw.Application, **kwargs):
        global MAIN_WINDOW
        MAIN_WINDOW = self

        super().__init__(application=app, **kwargs)

        self.change_view(AUTH_STATE.is_authenticated())

        AUTH_STATE.connect(AUTHENTICATED_CHANGED_SIGNAL, self.on_authenticated)

    def to_logout_view(self):
        self.view.replace([LoginPage()])

    def to_downloads_view(self):
        self.view.replace([DownloadsPage()])

    def change_view(self, authenticated: bool):
        if authenticated:
            self.to_downloads_view()
        else:
            self.to_logout_view()

    def on_authenticated(self, _: AuthState, authenticated: bool):
        self.change_view(authenticated)
