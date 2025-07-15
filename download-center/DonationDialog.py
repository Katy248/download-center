from gi.repository import Gtk, Adw, Gio
from .config import SETTINGS


@Gtk.Template.from_resource("/ru/katy248/download-center/DonationDialog.ui")
class DonationDialog(Adw.Dialog):
    __gtype_name__ = "DonationDialog"
    show_dialog_check_button: Gtk.CheckButton = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        SETTINGS.bind(
            "show-donation-dialog",
            self.show_dialog_check_button,
            "active",
            Gio.SettingsBindFlags.INVERT_BOOLEAN,
        )
