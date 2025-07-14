from gi.repository import Gtk, Adw


@Gtk.Template.from_resource("/ru/katy248/download-center/DonationDialog.ui")
class DonationDialog(Adw.Dialog):
    __gtype_name__ = "DonationDialog"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
