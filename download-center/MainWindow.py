from gi.repository import Gtk, Adw, Gio

from .config import APP_NAME, RELEASE_NOTES_FILE, VERSION, SETTINGS

from .DownloadsPage import DownloadsPage
from .LoginPage import LoginPage
from .auth import AuthState, AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL
from .actions import settings_action
from .SettingsDialog import SettingsDialog

from gettext import gettext as _

MAIN_WINDOW: Adw.ApplicationWindow | None = None


@Gtk.Template.from_resource("/ru/katy248/download-center/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    view: Adw.NavigationView = Gtk.Template.Child()

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

        SETTINGS.bind(
            "window-width", self, "default-width", Gio.SettingsBindFlags.DEFAULT
        )
        SETTINGS.bind(
            "window-height", self, "default-height", Gio.SettingsBindFlags.DEFAULT
        )

        self.handle_entrances()

    def handle_entrances(self):
        entrances = SETTINGS.get_int("entrance-count")
        if entrances > 0:
            from .DonationDialog import DonationDialog

            dialog = DonationDialog()
            # dialog.set_title(_("Help this app"))
            # box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            # dialog.set_child(box)
            # box.append(Adw.HeaderBar(css_classes=["flat"]))
            # box.set_margin_bottom(20)
            # box.set_margin_top(20)
            # box.set_margin_start(20)
            # box.set_margin_end(20)

            # header = Gtk.Label(
            #     label=_(
            #         "Cool app, isn't it? So maybe help it improve?",
            #     )
            # )
            # header.add_css_class("title-1")
            # header.set_wrap(True)
            # box.append(header)
            # box.append(
            #     Gtk.Label(
            #         wrap=True,
            #         label=_(
            #             "You have entered the application {} times. You can help it to improve with donation or source code contribution"
            #         ).format(entrances),
            #     )
            # )

            dialog.present(self)

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
        dialog.set_license_type(Gtk.License.UNKNOWN)
        dialog.set_version(VERSION)
        dialog.set_website("https://gitlab.com/Katy248/download-center")
        dialog.set_issue_url("https://gitlab.com/Katy248/download-center/-/issues")
        dialog.set_follows_content_size(False)

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
