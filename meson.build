project('download-center', version: '0.2.6', meson_version: '>=1.4.1')

project_id = 'ru.katy248.download-center'

gnome = import('gnome')

pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
message('pkgdatadir: ' + pkgdatadir)

localedir = get_option('prefix') / get_option('localedir')

i18n = import('i18n')

subdir('download-center')
subdir('data')
subdir('po')

install_data('RELEASE_NOTES', install_dir: pkgdatadir)
