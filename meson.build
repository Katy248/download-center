project('download-center', version: '0.0.2', meson_version: '>=1.4.1')

project_id = 'ru.katy248.download-center'

gnome = import('gnome')

pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()

subdir('download-center')
subdir('data')
subdir('po')

install_data('RELEASE_NOTES', install_dir: pkgdatadir)
