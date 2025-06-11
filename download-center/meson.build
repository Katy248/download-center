config = configuration_data()
config.set('PKGDIR', pkgdatadir)
config.set('VERSION', meson.project_version())

config_source_file = configure_file(
    output: 'config.py',
    input: 'config.py',
    configuration: config,
)

sources = [
    'actions.py',
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
    config_source_file,
]

python = import('python').find_installation('python3')

python.install_sources(sources, subdir: meson.project_name())

blueprints = custom_target(
    'blueprints',
    input: files(
        'DownloadRow.blp',
        'DownloadsPage.blp',
        'LoginPage.blp',
        'MainWindow.blp',
        'SettingsPage.blp',
    ),
    output: 'data',
    command: [
        find_program('blueprint-compiler'),
        'batch-compile',
        '../data',
        '@CURRENT_SOURCE_DIR@',
        '@INPUT@',
    ],
)
