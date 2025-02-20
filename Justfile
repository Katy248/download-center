APP_ID := "ru.red-soft.download-center"
SCHEMAS_DIR := "/usr/share/glib-2.0/schemas"

compile-blueprints:
    blueprint-compiler compile ./download-center/MainWindow.blp --output ./download-center/MainWindow.ui
    blueprint-compiler compile ./download-center/DownloadsView.blp --output ./download-center/DownloadsView.ui
    blueprint-compiler compile ./download-center/LoginView.blp --output ./download-center/LoginView.ui
    blueprint-compiler compile ./download-center/DownloadRow.blp --output ./download-center/DownloadRow.ui

# [dir('data')]
compile-gschema:
    sudo cp ./data/{{ APP_ID }}.gschema.xml {{ SCHEMAS_DIR }}
    sudo glib-compile-schemas {{ SCHEMAS_DIR }}

build: compile-blueprints

run: build
    python -m download-center
