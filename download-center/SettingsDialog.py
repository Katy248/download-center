from gi.repository import Adw, Gtk, Gio
from .config import SETTINGS, DEVELOPMENT
from locale import gettext as _
import os


@Gtk.Template.from_resource("/ru/katy248/download-center/SettingsDialog.ui")
class SettingsDialog(Adw.PreferencesDialog):
    __gtype_name__ = "SettingsPage"

    persistence_row = Gtk.Template.Child()
    license_key_row = Gtk.Template.Child()
    show_donation_dialog_row = Gtk.Template.Child()

    dev_group: Adw.PreferencesGroup = Gtk.Template.Child()

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
        SETTINGS.bind(
            "show-donation-dialog",
            self.show_donation_dialog_row,
            "active",
            Gio.SettingsBindFlags.DEFAULT,
        )
        if DEVELOPMENT:
            donation_btn = Adw.ButtonRow(title=_("Present donation dialog"))
            donation_btn.connect("activated", self.on_donation_btn_clicked)
            self.dev_group.add(donation_btn)

            entrances_count = Adw.ActionRow(
                title=_("Entrances count"),
                css_classes=["property", "numeric"],
                subtitle=str(SETTINGS.get_int("entrance-count")),
            )
            self.dev_group.add(entrances_count)
        else:
            self.dev_group.hide()

    def on_donation_btn_clicked(self, btn):
        from .DonationDialog import DonationDialog

        dialog = DonationDialog()
        dialog.present(self)

    @Gtk.Template.Callback()
    def on_clear_cache_activated(self, btn):
        from .config import CACHE_DIR

        try:
            for filename in os.listdir(CACHE_DIR):
                file_path = os.path.join(CACHE_DIR, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(CACHE_DIR)

            toast = Adw.Toast.new(_("Cache cleared"))
            toast.set_timeout(2)
            self.add_toast(toast)
        except OSError as e:
            toast = Adw.Toast.new(_("Failed to clear cache: %s") % e.strerror)
            toast.set_timeout(5)
            self.add_toast(toast)
