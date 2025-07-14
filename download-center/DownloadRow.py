from threading import Thread
from gi.repository import Adw, Gtk, GObject, Gio
import requests
from .api import BASE_ADDR
from typing import Callable


@Gtk.Template.from_resource("/ru/katy248/download-center/DownloadRow.ui")
class DownloadRow(Adw.ActionRow):
    __gtype_name__ = "DownloadRow"
    __gsignals__ = {
        "download-started": (GObject.SIGNAL_RUN_FIRST, None, (str, str)),
        "download-finished": (GObject.SIGNAL_RUN_FIRST, None, (str, str)),
    }

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

    @Gtk.Template.Callback()
    def on_hash_button_click(self, btn: Gtk.Button):
        self.download_hash(self.__hash_url)

    @Gtk.Template.Callback()
    def on_download_button_click(self, btn: Gtk.Button):
        self.download_rpm(self.__download_url)

    def select_output_and_download(
        self, file_url: str, callback_fn: Callable[[str, str], None]
    ) -> None:
        file_name = file_url.split("/")[-1]
        gio_file: Gio.File = Gio.File.new_for_path(file_name)

        file_dialog = Gtk.FileDialog()
        file_dialog.set_initial_file(gio_file)

        def callback(source: Gtk.FileDialog, res: Gio.AsyncResult):
            nonlocal gio_file
            gio_file = source.save_finish(res)
            filepath: str | None = gio_file.get_path()

            if not filepath == "" and filepath is not None:
                callback_fn(file_url, filepath)

        from .MainWindow import MAIN_WINDOW

        file_dialog.save(MAIN_WINDOW, callback=callback)

    def __download_file(self, file_url: str, output_file: str):
        self.emit("download-started", file_url, output_file)

        with open(output_file, "wb") as fs_file:
            response = requests.post(
                BASE_ADDR + "/download/files", data={"file": file_url}
            )
            fs_file.write(response.content)

        self.emit("download-finished", file_url, output_file)

    def __download_in_thread(self, file_url: str, output_file: str):
        thread = Thread(target=self.__download_file, args=(file_url, output_file))
        thread.start()

    def download_hash(self, file_url: str):
        self.select_output_and_download(file_url, self.__download_in_thread)

    def download_rpm(self, file_url: str):
        self.select_output_and_download(file_url, self.__download_in_thread)
