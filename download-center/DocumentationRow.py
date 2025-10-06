from gi.repository import Gtk, Adw


@Gtk.Template.from_resource("/ru/katy248/download-center/DocumentationRow.ui")
class DocumentationRow(Adw.ActionRow):
    __gtype_name__ = "DocumentationRow"

    def __init__(self, document_data: dict[str, str]):
        super().__init__()
        self.set_title(self.change_doc_file_name(document_data["file_name"]))

    def change_doc_file_name(self, file_name: str) -> str:
        return file_name.replace(".pdf", "").replace("_", " ")
