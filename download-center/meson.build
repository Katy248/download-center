config = configuration_data()
config.set('PKGDIR', pkgdatadir)
config.set('VERSION', meson.project_version())
config.set('LOCALEDIR', localedir)
config.set('DEVELOPMENT', get_option('development'))

config_source_file = configure_file(
    output: 'config.py',
    input: 'config.py',
    configuration: config,
)

sources = files(
    'DonationDialog.py',
    'DownloadRow.py',
    'DownloadsPage.py',
    'LoginPage.py',
    'MainWindow.py',
    'SettingsDialog.py',
    '__init__.py',
    '__main__.py',
    'actions.py',
    'api.py',
    'app.py',
    'auth.py',
)
sources += config_source_file

python = import('python').find_installation('python3')

python.install_sources(sources, subdir: meson.project_name())

blueprints = custom_target(
    'blueprints',
    input: files(
        'DonationDialog.blp',
        'DownloadRow.blp',
        'DownloadsPage.blp',
        'LoginPage.blp',
        'MainWindow.blp',
        'SettingsDialog.blp',
    ),
    output: 'data',
    command: [
        find_program('blueprint-compiler'),
        'batch-compile',
        '../data',
        '@CURRENT_SOURCE_DIR@',
        '@INPUT@',
    ],
    build_by_default: true,
)
