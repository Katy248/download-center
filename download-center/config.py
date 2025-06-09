from gi.repository import Gio


APP_NAME = "download-center"

APP_ID = f"ru.katy248.{APP_NAME}"

SETTINGS = Gio.Settings(APP_ID)


GRESOURCE_FILE = f"@PKGDIR@/{APP_ID}.gresource"
LOCALE_DIR = "@PKGDIR@/locale"
VERSION = "@VERSION@"

RELEASE_NOTES_FILE = "@PKGDIR@/RELEASE_NOTES"
