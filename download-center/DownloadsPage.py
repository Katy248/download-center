import typing
from gi.repository import Gtk, Adw
from locale import gettext as _
from .api import get_files
from .DownloadRow import DownloadRow
from .auth import logout
from .DocumentationRow import DocumentationRow


@Gtk.Template.from_resource("/ru/katy248/download-center/DownloadsPage.ui")
class DownloadsPage(Adw.NavigationPage):
    __gtype_name__ = "DownloadsPage"
    redos7_builds_group: Adw.PreferencesGroup = Gtk.Template.Child()
    redos8_builds_group: Adw.PreferencesGroup = Gtk.Template.Child()
    astra_builds_group: Adw.PreferencesGroup = Gtk.Template.Child()
    logout_button: Gtk.Button = Gtk.Template.Child()
    content_box: Gtk.Box = Gtk.Template.Child()
    window_title: Adw.WindowTitle = Gtk.Template.Child()
    docs_group: Adw.PreferencesGroup = Gtk.Template.Child()

    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.setup_builds()

    def setup_builds(self):
        self.data = get_files()
        if self.data is None:
            return

        self.window_title.set_subtitle(_("Current build: %s") % self.data["version"])
        self.window_title.set_title(self.get_title())

        self.fill_build_group(self.redos7_builds_group, "redos7")
        self.fill_build_group(self.redos8_builds_group, "redos8")
        self.fill_build_group(self.astra_builds_group, "astra")

        self.fill_docs(self.data)

    def fill_build_group(self, group: Adw.PreferencesGroup, build_name: str):
        if self.data is None:
            print("[WARNING] Can't fill build group: data is None")
            group.set_visible(False)
            return
        if self.data["rpm"] is None:
            print("[WARNING] Can't fill build group: 'rpm' key is None")
            group.set_visible(False)
            return
        builds = [b for b in self.data["rpm"] if b["build"] == build_name]
        if len(builds) == 0:
            print("[WARNING] No builds found for build %s" % build_name)
            group.set_visible(False)
            return
        for build in builds:
            row = DownloadRow(build)
            group.add(row)
            row.connect("download-started", self.on_download_started)
            row.connect("download-finished", self.on_download_finished)

    def on_download_started(self, row: DownloadRow, file_url: str, output_file: str):
        self.add_toast(_("Started downloading to %s") % output_file)

    def fill_docs(self, data: dict[str, typing.Any]):
        print(data["docs"])
        for d in data["docs"]:
            row = DocumentationRow(d)
            self.docs_group.add(row)

    def change_doc_file_name(self, file_name: str) -> str:
        return file_name.replace(".pdf", "").replace("_", " ")

    def on_download_finished(self, row: DownloadRow, file_url: str, output_file: str):
        self.add_toast(_("Finished downloading to %s") % output_file)

    def add_toast(self, msg: str):
        toast = Adw.Toast.new(msg)
        toast.set_timeout(2)
        self.toast_overlay.add_toast(toast)

    @Gtk.Template.Callback()
    def on_logout_button_clicked(self, args):
        logout()

    # @Gtk.Template.Callback()
    # def to_settings_page(self, _, __):
    #     self.get_parent().push(SettingsPage())
