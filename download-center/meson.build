sources = files(
    'DownloadRow.py',
    'DownloadsPage.py',
    'LoginPage.py',
    'MainWindow.py',
    'SettingsPage.py',
    '__init__.py',
    '__main__.py',
    'api.py',
    'app.py',
    'auth.py',
    'config.py',
)

python = import('python').find_installation('python3')

python.install_sources(sources, subdir: meson.project_name())
