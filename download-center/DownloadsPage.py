from gi.repository import Gtk, Adw
from .api import get_files
from .DownloadRow import DownloadRow
from .auth import logout
from .SettingsPage import SettingsPage


@Gtk.Template.from_file("./download-center/DownloadsPage.ui")
class DownloadsPage(Adw.NavigationPage):
    __gtype_name__ = "DownloadsPage"
    current_builds_group = Gtk.Template.Child()
    redos7_builds_group = Gtk.Template.Child()
    redos8_builds_group = Gtk.Template.Child()
    logout_button: Gtk.Button = Gtk.Template.Child()

    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        data = get_files()
        self.current_builds_group.set_description(data["version"])

        redos7_builds = [b for b in data["rpm"] if b["build"] == "redos7"]
        for build in redos7_builds:
            row = DownloadRow(build)
            self.redos7_builds_group.add(row)
            row.connect("download-started", self.on_download_started)
            row.connect("download-finished", self.on_download_finished)

        redos8_builds = [b for b in data["rpm"] if b["build"] == "redos8"]
        for build in redos8_builds:
            row = DownloadRow(build)
            self.redos8_builds_group.add(row)
            row.connect("download-started", self.on_download_started)
            row.connect("download-finished", self.on_download_finished)

    def on_download_started(self, _: DownloadRow, file_url: str, output_file: str):
        self.add_toast(f"Started downloading to {output_file}")

    def on_download_finished(self, _: DownloadRow, file_url: str, output_file: str):
        self.add_toast(f"Finished downloading to {output_file}")

    def add_toast(self, msg):
        toast = Adw.Toast.new(msg)
        toast.set_timeout(2)
        self.toast_overlay.add_toast(toast)

    @Gtk.Template.Callback()
    def on_logout_button_clicked(self, args):
        logout()

    @Gtk.Template.Callback()
    def on_settings_button_clicked(self, _):
        self.get_parent().push(SettingsPage())
