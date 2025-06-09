gnome.compile_resources(
    project_id,
    'gresource.xml',
    source_dir: ['.'],
    gresource_bundle: true,
    install: true,
    install_dir: pkgdatadir,
    dependencies: [blueprints],
)
install_data(
    'ru.katy248.download-center.gschema.xml',
    install_dir: get_option('prefix') / get_option('datadir') / 'glib-2.0/schemas',
)
install_data(
    'ru.katy248.download-center.svg',
    install_dir: get_option('datadir') / 'icons/hicolor/scalable/apps',
)
install_data(
    'ru.katy248.download-center.desktop',
    install_dir: get_option('prefix') / get_option('datadir') / 'applications',
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
