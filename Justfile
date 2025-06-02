APP_ID := "ru.katy248.download-center"
SCHEMAS_DIR := "/usr/share/glib-2.0/schemas"
INSTALL_DIR := "~/.local/share/" + APP_ID 

compile-blueprints:
    blueprint-compiler compile ./download-center/MainWindow.blp --output ./download-center/MainWindow.ui
    blueprint-compiler compile ./download-center/DownloadsPage.blp --output ./download-center/DownloadsPage.ui
    blueprint-compiler compile ./download-center/LoginPage.blp --output ./download-center/LoginPage.ui
    blueprint-compiler compile ./download-center/DownloadRow.blp --output ./download-center/DownloadRow.ui
    blueprint-compiler compile ./download-center/SettingsPage.blp --output ./download-center/SettingsPage.ui

# [dir('data')]
compile-gschema:
    sudo cp ./data/{{ APP_ID }}.gschema.xml {{ SCHEMAS_DIR }}
    sudo glib-compile-schemas {{ SCHEMAS_DIR }}

build: compile-blueprints

run: build
    python -m download-center

install: 
    mkdir -p {{ INSTALL_DIR }}
    cp ./data/128x128.png {{ INSTALL_DIR }}
