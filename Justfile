build:
    blueprint-compiler compile ./download-center/MainWindow.blp --output ./download-center/MainWindow.ui
    blueprint-compiler compile ./download-center/DownloadsView.blp --output ./download-center/DownloadsView.ui
    blueprint-compiler compile ./download-center/LoginView.blp --output ./download-center/LoginView.ui

run: build
    python -m download-center
