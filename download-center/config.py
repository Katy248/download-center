from gi.repository import Gio
import os


APP_NAME = "download-center"

APP_ID = f"ru.katy248.{APP_NAME}"

SETTINGS = Gio.Settings.new(APP_ID)


GRESOURCE_FILE = f"@PKGDIR@/{APP_ID}.gresource"
LOCALE_DIR = "@LOCALEDIR@"
VERSION = "@VERSION@"

RELEASE_NOTES_FILE = "@PKGDIR@/RELEASE_NOTES"

DEVELOPMENT : bool = @DEVELOPMENT@

if DEVELOPMENT:
    print(f"GResource file {GRESOURCE_FILE}")
    print(f"Locale dir {LOCALE_DIR}")
    print(f"Release notes file {RELEASE_NOTES_FILE}")

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", APP_ID)

