from gi.repository import Adw, Gtk


@Gtk.Template.from_resource("/ru/katy248/download-center/FailedAuthPage.ui")
class FailedAuthPage(Adw.NavigationPage):
    __gtype_name__: str = "FailedAuthPage"

    def __init__(self, error: str):
        super().__init__()
        # self.error_label = self.get_object("error-label")
        # self.error_label.set_text(error)
