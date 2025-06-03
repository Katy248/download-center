from gi.repository import Adw, Gtk, Gio
from .config import SETTINGS


@Gtk.Template.from_resource("/ru/katy248/download-center/SettingsPage.ui")
class SettingsPage(Adw.NavigationPage):
    __gtype_name__ = "SettingsPage"

    persistence_row = Gtk.Template.Child()
    license_key_row = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        SETTINGS.bind(
            "stay-logged-in",
            self.persistence_row,
            "active",
            Gio.SettingsBindFlags.DEFAULT,
        )
        SETTINGS.bind(
            "license-key",
            self.license_key_row,
            "text",
            Gio.SettingsBindFlags.DEFAULT,
        )
