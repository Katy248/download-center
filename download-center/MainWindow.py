from gi.repository import Gtk, Adw, Gio

from .config import VERSION, SETTINGS, DEVELOPMENT

from .DownloadsPage import DownloadsPage
from .LoginPage import LoginPage
from .auth import AuthState, AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL
from .actions import settings_action
from .SettingsDialog import SettingsDialog

from locale import gettext as _

MAIN_WINDOW: Adw.ApplicationWindow | None = None


@Gtk.Template.from_resource("/ru/katy248/download-center/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"
    view: Adw.NavigationView = Gtk.Template.Child()

    def __init__(self, app: Adw.Application, **kwargs):
        global MAIN_WINDOW
        MAIN_WINDOW = self

        super().__init__(application=app, **kwargs)

        if DEVELOPMENT:
            self.add_css_class("devel")

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

        SETTINGS.set_int("entrance-count", SETTINGS.get_int("entrance-count") + 1)
        SETTINGS.apply()

        self.check_entrances_and_notify()

        show_dialog = SETTINGS.get_boolean("show-donation-dialog")
        if not show_dialog:
            return

        entrances = SETTINGS.get_int("entrance-count")
        if entrances % 3 == 0:
            from .DonationDialog import DonationDialog

            dialog = DonationDialog()
            dialog.present(self)

    def check_entrances_and_notify(self):
        entrances = SETTINGS.get_int("entrance-count")
        title: str | None = None
        if entrances == 0:
            title = _("What are you trying to debug?")
        if entrances == 42:
            title = _("The Ultimate Question of Life, the Universe, and Everything")
        if entrances == 69:
            title = _("Nice!")
        if entrances == 228:
            title = _("228")
        if entrances == 420:
            title = _("420")
        if entrances == 666:
            title = _("Bang! Bang! Bang! Pull my devil trigger")
        if entrances == 1488:
            title = _("You nazi, aren't you? If you are, go fuck yourself")

        if title is not None:
            body = _(
                "Congratulations! This is your %s visit. Hope you like this app"
            ) % str(entrances)

            notification = Gio.Notification.new(title)
            notification.set_body(body)
            Gio.Application.get_default().send_notification(
                "cool-number-%d" % entrances, notification
            )

    def on_settings_activated(self, action, _):
        dialog = SettingsDialog()
        dialog.present(self)

    def on_about_activated(self, action, args):
        dialog = Adw.AboutDialog()
        dialog = Adw.AboutDialog.new_from_appdata(
            "/ru/katy248/download-center/ru.katy248.download-center.metainfo.xml",
            VERSION,
        )
        dialog.add_link(_("Support development"), "https://boosty.to/katy248/donate")
        dialog.set_artists(["Katy248 <petrovanton247@gmail.com>"])
        dialog.set_developers(["Katy248 <petrovanton247@gmail.com>"])
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
