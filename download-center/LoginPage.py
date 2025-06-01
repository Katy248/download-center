from gi.repository import Gtk, Adw, Gio
from .config import SETTINGS

from .auth import AUTH_STATE, AUTHENTICATED_CHANGED_SIGNAL


@Gtk.Template.from_file("./download-center/LoginPage.ui")
class LoginPage(Adw.NavigationPage):
    __gtype_name__ = "LoginPage"

    login_button: Gtk.Button = Gtk.Template.Child()
    license_entry: Adw.EntryRow = Gtk.Template.Child()
    persistence_check: Gtk.Switch = Gtk.Template.Child()
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

    def on_login_button_click(self, btn: Gtk.Button):
        key = self.license_entry.get_text()
        if key is None or len(key) <= 0:
            self.add_toast("Invalid license key")
            return

        if not AUTH_STATE.authenticate(key):
            self.add_toast("Invalid license key")

    def add_toast(self, msg):
        toast = Adw.Toast.new(msg)
        toast.set_timeout(1)
        self.toast_overlay.add_toast(toast)
