APP_ID := "ru.katy248.download-center"
SCHEMAS_DIR := "/usr/share/glib-2.0/schemas"
INSTALL_DIR := "~/.local/share/" + APP_ID 

compile-blueprints:
    blueprint-compiler compile ./download-center/MainWindow.blp --output ./data/MainWindow.ui
    blueprint-compiler compile ./download-center/DownloadsPage.blp --output ./data/DownloadsPage.ui
    blueprint-compiler compile ./download-center/LoginPage.blp --output ./data/LoginPage.ui
    blueprint-compiler compile ./download-center/DownloadRow.blp --output ./data/DownloadRow.ui
    blueprint-compiler compile ./download-center/SettingsPage.blp --output ./data/SettingsPage.ui

# [dir('data')]
compile-gschema:
    sudo cp ./data/{{ APP_ID }}.gschema.xml {{ SCHEMAS_DIR }}
    sudo glib-compile-schemas {{ SCHEMAS_DIR }}

build: compile-blueprints
    glib-compile-resources ./data/{{ APP_ID }}.gresource.xml

run: build
    python -m download-center

install: build compile-gschema
    mkdir -p {{ INSTALL_DIR }}
    desktop-file-validate data/{{ APP_ID }}.desktop
    sudo cp data/{{ APP_ID }}.desktop /usr/share/applications
    sudo cp data/icons/128x128.png /usr/share/icons/hicolor/128x128/apps/{{ APP_ID }}.png
    gtk4-update-icon-cache
    cp ./data/ru.katy248.download-center.gresource {{ INSTALL_DIR }}}
