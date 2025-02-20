from gi.repository import Gtk, Adw
from .api import get_files
from .DownloadRow import DownloadRow
from .state import NOTIFY_FUNC


@Gtk.Template.from_file("./download-center/DownloadsView.ui")
class DownloadsView(Gtk.Box):
    __gtype_name__ = "DownloadsView"
    current_builds_group = Gtk.Template.Child()
    redos7_builds_group = Gtk.Template.Child()
    redos8_builds_group = Gtk.Template.Child()

    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        data = get_files()
        self.current_builds_group.set_description(data["version"])
        # for build in data["rpm"]:
        #     self.current_builds_group.add(DownloadRow(build))
        redos7_builds = [b for b in data["rpm"] if b["build"] == "redos7"]
        for build in redos7_builds:
            self.redos7_builds_group.add(DownloadRow(build))
        redos8_builds = [b for b in data["rpm"] if b["build"] == "redos8"]
        for build in redos8_builds:
            self.redos8_builds_group.add(DownloadRow(build))

        NOTIFY_FUNC = self.add_toast

    def add_toast(self, msg):
        print("Prints msg:", msg)
        toast = Adw.Toast(msg)
        self.toast_overlay.add_toast(toast)
