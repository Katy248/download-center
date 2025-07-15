from gi.repository import Gtk, Adw, Gio
from .config import SETTINGS
from gettext import gettext as _


@Gtk.Template.from_resource("/ru/katy248/download-center/DonationDialog.ui")
class DonationDialog(Adw.Dialog):
    __gtype_name__ = "DonationDialog"
    show_dialog_check_button: Gtk.CheckButton = Gtk.Template.Child()
    donate_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        SETTINGS.bind(
            "show-donation-dialog",
            self.show_dialog_check_button,
            "active",
            Gio.SettingsBindFlags.INVERT_BOOLEAN,
        )

        self.donate_button.connect("clicked", self.on_donate_clicked)

    def on_donate_clicked(self, button):
        dialog = Adw.AlertDialog.new(
            _("No money"),
            _("Currently there is no way to donate((( But thank you for try!"),
        )
        dialog.add_response("ok", _("Ok"))
        dialog.connect(
            "response",
            lambda dialog, response: SETTINGS.set_boolean(
                "show-donation-dialog", False
            ),
        )
        dialog.present(self)
