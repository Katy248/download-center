from gi.repository import Gtk, Adw, Gio
from .config import SETTINGS
from locale import gettext as _

from .auth import AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL


@Gtk.Template.from_resource("/ru/katy248/download-center/LoginPage.ui")
class LoginPage(Adw.NavigationPage):
    __gtype_name__ = "LoginPage"

    login_button: Gtk.Button = Gtk.Template.Child()
    license_entry: Adw.EntryRow = Gtk.Template.Child()
    persistence_check: Adw.SwitchRow = Gtk.Template.Child()
    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.login_button.connect("clicked", self.on_login_button_click)
        SETTINGS.bind(
            "stay-logged-in",
            self.persistence_check,
            "active",
            Gio.SettingsBindFlags.DEFAULT,
        )
        self.license_entry.connect("changed", self.on_text_changed)

    def on_text_changed(self, _: Adw.PasswordEntryRow):
        self.license_entry.remove_css_class("error")
        key = self.license_entry.get_text()
        if len(key) <= 0:
            self.license_entry.add_css_class("error")

    def on_login_button_click(self, btn: Gtk.Button):
        key = self.license_entry.get_text()
        if key is None or len(key) <= 0:
            self.add_toast(_("Invalid license key"))
            self.license_entry.add_css_class("error")
            return

        if not AUTH_STATE.authenticate(key):
            self.add_toast(_("Failed to authenticate"))
            self.license_entry.add_css_class("error")

    def add_toast(self, msg):
        toast = Adw.Toast.new(msg)
        toast.set_timeout(1)
        self.toast_overlay.add_toast(toast)
