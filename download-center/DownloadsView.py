from gi.repository import Gtk, Adw
from .api import get_files


@Gtk.Template.from_file("./download-center/DownloadsView.ui")
class DownloadsView(Gtk.Box):
    __gtype_name__ = "DownloadsView"

    def __init__(self):
        super().__init__()
        print(get_files())
