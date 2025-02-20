from gi.repository import Adw, Gtk
import webbrowser
from .api import download_hash, download_rpm
import asyncio


@Gtk.Template.from_file("./download-center/DownloadRow.ui")
class DownloadRow(Adw.ActionRow):
    __gtype_name__ = "DownloadRow"
    hash_button = Gtk.Template.Child()
    download_button = Gtk.Template.Child()

    __hash_url: str
    __download_url: str

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.set_title(data["rpm_file_name"])
        self.set_subtitle(f"{data['size']} Mb")

        self.__hash_url = data["hashsum_download_link"]
        self.__download_url = data["download_link"]

        self.hash_button.connect("clicked", self.on_hash_button_click)
        self.download_button.connect("clicked", self.on_download_button_click)

    def on_hash_button_click(self, btn):
        download_hash(self.__hash_url)

    def on_download_button_click(self, btn):
        download_rpm(self.__download_url)
