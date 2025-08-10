gnome.compile_resources(
    project_id,
    'gresource.xml',
    source_dir: [meson.current_source_dir(), meson.current_build_dir()],
    gresource_bundle: true,
    install: true,
    install_dir: pkgdatadir,
    dependencies: [blueprints],
)
install_data(
    'ru.katy248.download-center.gschema.xml',
    install_dir: get_option('prefix') / get_option('datadir') / 'glib-2.0/schemas',
)
gnome.compile_schemas(depend_files: 'ru.katy248.download-center.gschema.xml')

install_data(
    'icons/ru.katy248.download-center.svg',
    install_dir: pkgdatadir / 'icons/hicolor/scalable/apps',
)
install_data(
    'icons/ru.katy248.download-center-symbolic.svg',
    install_dir: pkgdatadir / 'icons/hicolor/symbolic/apps',
)
icon_sizes = ['16', '24', '32', '48', '64', '128']

foreach i : icon_sizes
    install_data(
        'icons/ru.katy248.download-center-symbolic.svg',
        install_dir: pkgdatadir / 'icons/hicolor/' + i + 'x' + i + '/apps',
    )
endforeach

po_dir = meson.project_source_root() / 'po'

desktop_file = i18n.merge_file(
    output: 'ru.katy248.download-center.desktop',
    input: 'ru.katy248.download-center.desktop',
    type: 'desktop',
    po_dir: po_dir,
    install: true,
    install_dir: get_option('prefix') / get_option('datadir') / 'applications',
)

dfv = find_program('desktop-file-validate', required: false, disabler: true)
test(
    'Desktop file validation',
    dfv,
    args: [desktop_file],
)

appstream_file = i18n.merge_file(
    input: 'ru.katy248.download-center.metainfo.xml.in',
    output: 'ru.katy248.download-center.metainfo.xml',
    po_dir: po_dir,
    install: true,
    install_dir: get_option('prefix') / get_option('datadir') / 'metainfo',
)

appstreamcli = find_program('appstreamcli', required: false, disabler: true)
test(
    'Validate appstream file',
    appstreamcli,
    args: ['validate', '--no-net', '--explain', appstream_file],
)

install_data(
    'download-center',
    install_dir: get_option('prefix') / get_option('bindir'),
)

gnome.post_install(
    glib_compile_schemas: true,
    gtk_update_icon_cache: true,
    update_desktop_database: true,
)
