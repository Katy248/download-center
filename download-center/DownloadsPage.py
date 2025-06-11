from gi.repository import Gtk, Adw, Gio
from gettext import gettext as _
from .api import get_files
from .DownloadRow import DownloadRow
from .auth import logout
from .SettingsPage import SettingsPage
from .actions import settings_action


@Gtk.Template.from_resource("/ru/katy248/download-center/DownloadsPage.ui")
class DownloadsPage(Adw.NavigationPage):
    __gtype_name__ = "DownloadsPage"
    current_builds_group = Gtk.Template.Child()
    redos7_builds_group = Gtk.Template.Child()
    redos8_builds_group = Gtk.Template.Child()
    astra_builds_group = Gtk.Template.Child()
    logout_button: Gtk.Button = Gtk.Template.Child()
    content_box: Gtk.Box = Gtk.Template.Child()

    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.data = get_files()
        self.current_builds_group.set_description(self.data["version"])
        self.fill_build_group(self.redos7_builds_group, "redos7")
        self.fill_build_group(self.redos8_builds_group, "redos8")
        self.fill_build_group(self.astra_builds_group, "astra")

        settings_action.connect("activate", self.to_settings_page)

    def fill_build_group(self, group: Adw.PreferencesGroup, build_name: str):
        builds = [b for b in self.data["rpm"] if b["build"] == build_name]
        for build in builds:
            row = DownloadRow(build)
            group.add(row)
            row.connect("download-started", self.on_download_started)
            row.connect("download-finished", self.on_download_finished)

    def on_download_started(self, _: DownloadRow, file_url: str, output_file: str):
        self.add_toast(_("Started downloading to %s") % output_file)

    def on_download_finished(self, _: DownloadRow, file_url: str, output_file: str):
        self.add_toast(_("Finished downloading to %s") % output_file)

    def add_toast(self, msg):
        toast = Adw.Toast.new(msg)
        toast.set_timeout(2)
        self.toast_overlay.add_toast(toast)

    @Gtk.Template.Callback()
    def on_logout_button_clicked(self, args):
        logout()

    # @Gtk.Template.Callback()
    def to_settings_page(self, _, __):
        self.get_parent().push(SettingsPage())
