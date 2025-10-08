import json
from gi.repository import Gtk, Adw, GLib, Gio
from .config import APP_ID
from .api import BASE_ADDR, get_headers
import os
from locale import gettext as _
import requests

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", APP_ID)

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)


@Gtk.Template.from_resource("/ru/katy248/download-center/DocumentationRow.ui")
class DocumentationRow(Adw.ActionRow):
    __gtype_name__ = "DocumentationRow"

    def __init__(self, document_data: dict[str, str]):
        super().__init__()
        self.data = document_data
        self.set_title(self.change_doc_file_name(document_data["file_name"]))

    def change_doc_file_name(self, file_name: str) -> str:
        return file_name.replace(".pdf", "").replace("_", " ")

    @Gtk.Template.Callback()
    def on_view_button_clicked(self, button):
        output_file = os.path.join(CACHE_DIR, self.data["file_name"])
        if not os.path.exists(output_file):
            self.download(output_file)

        file = Gio.File.new_for_path(output_file)
        launcher = Gtk.FileLauncher.new(file)
        launcher.launch()

    def download(self, output_file: str):
        with open(output_file, "wb") as fs_file:
            response = requests.post(
                BASE_ADDR + "/download/files",
                data=json.dumps({"file": self.data["download_link"]}),
                headers=get_headers(with_auth=True, with_json_content=True),
            )
            if response.ok:
                fs_file.write(response.content)
            else:
                print(
                    "[ERROR]: Response status code is %d. Body dump: %s"
                    % (response.status_code, response.content)
                )
                error_dialog = Adw.AlertDialog()
                error_dialog.set_heading(_("Failed download file"))
                error_dialog.set_body(
                    _(
                        "There is error occurred while downloading file '%s'. Response status code is %d"
                    )
                    % (self.get_title(), response.status_code)
                )
                error_dialog.add_response("ok", _("Terrible"))
                error_dialog.present(self)
