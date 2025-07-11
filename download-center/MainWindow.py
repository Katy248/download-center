from gi.repository import Gtk, Adw, Gio

from .config import APP_NAME, RELEASE_NOTES_FILE, VERSION

from .DownloadsPage import DownloadsPage
from .LoginPage import LoginPage
from .auth import AuthState, AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL
from .actions import settings_action
from .SettingsDialog import SettingsDialog

from gettext import gettext as _

MAIN_WINDOW: Adw.ApplicationWindow = None


@Gtk.Template.from_resource("/ru/katy248/download-center/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    view: Adw.ToolbarView = Gtk.Template.Child()

    def __init__(self, app: Adw.Application, **kwargs):
        global MAIN_WINDOW
        MAIN_WINDOW = self

        super().__init__(application=app, **kwargs)

        self.change_view(AUTH_STATE.is_authenticated())

        AUTH_STATE.connect(AUTHENTICATED_CHANGED_SIGNAL, self.on_authenticated)

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about_activated)
        settings_action.connect("activate", self.on_settings_activated)
        self.add_action(about_action)
        self.add_action(settings_action)

    def on_settings_activated(self, action, _):
        dialog = SettingsDialog()
        dialog.present(self)

    def on_about_activated(self, action, _):
        dialog = Adw.AboutDialog()
        dialog.set_application_name(APP_NAME)
        dialog.set_application_icon("ru.katy248.download-center")
        dialog.set_artists(["Katy248 <petrovanton247@gmail.com>"])
        dialog.set_developers(["Katy248 <petrovanton247@gmail.com>"])
        dialog.set_developer_name("Katy248")
        dialog.set_license_type(Gtk.License.BSD)
        dialog.set_version(VERSION)
        dialog.set_website("https://gitlab.com/Katy248/download-center")
        dialog.set_issue_url("https://gitlab.com/Katy248/download-center/-/issues")
        dialog.set_follows_content_size(False)
        dialog.set_release_notes_version(VERSION)

        print(f"[DEBUG {APP_NAME}] RELEASE_NOTES_FILE: {RELEASE_NOTES_FILE}")

        with open(RELEASE_NOTES_FILE, "rb") as notes_file:
            dialog.set_release_notes(notes_file.read().decode("utf-8"))
        dialog.present(self)

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
