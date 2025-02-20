from gi.repository import Gtk, Adw

from .auth import AUTH_STATE


@Gtk.Template.from_file("./download-center/LoginView.ui")
class LoginView(Gtk.Box):
    __gtype_name__ = "LoginView"

    login_button: Gtk.Button = Gtk.Template.Child()
    license_entry: Adw.EntryRow = Gtk.Template.Child()
    persistence_check: Gtk.Switch = Gtk.Template.Child()

    def __init__(self, on_authenticate):
        super().__init__()
        self.persistence_check.set_visible(False)
        self.on_authenticate = on_authenticate 
        self.login_button.connect("clicked", self.on_login_button_click)

    def on_login_button_click(self, btn: Gtk.Button):
        key = self.license_entry.get_text()
        if len(key) <= 0: return

        AUTH_STATE.authenticate(key)
        if AUTH_STATE.is_authenticated():
            self.on_authenticate()
