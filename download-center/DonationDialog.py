from gi.repository import Gtk, Adw, Gio
from .config import SETTINGS
from locale import gettext as _


@Gtk.Template.from_resource("/ru/katy248/download-center/DonationDialog.ui")
class DonationDialog(Adw.Dialog):
    __gtype_name__ = "DonationDialog"
    show_dialog_check_button: Gtk.CheckButton = Gtk.Template.Child()
    donate_button: Gtk.LinkButton = Gtk.Template.Child()
    dont_show_box: Gtk.Box = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if SETTINGS.get_int("entrance-count") < 10:
            self.dont_show_box.hide()

        SETTINGS.bind(
            "show-donation-dialog",
            self.show_dialog_check_button,
            "active",
            Gio.SettingsBindFlags.INVERT_BOOLEAN,
        )

        self.donate_button.connect("clicked", self.on_donate_clicked)

    def on_donate_clicked(self, button):
        dialog = Adw.AlertDialog.new(
            _("Thanks!"),
            _("Thank you for your donation!"),
        )
        dialog.add_response("ok", _("Ok"))

        def on_response(dialog, response):
            SETTINGS.set_boolean("show-donation-dialog", False)
            self.dont_show_box.set_visible(True)

        dialog.connect("response", on_response)
        dialog.present(self)
        self.close()
