pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
gnome.compile_resources(
    project_id,
    'gresource.xml',
    source_dir: ['.'],
    gresource_bundle: true,
    install: true,
    install_dir: pkgdatadir,
)
install_data(
    'ru.katy248.download-center.gschema.xml',
    install_dir: get_option('prefix') / get_option('datadir') / 'glib-2.0/schemas',
)

gnome.post_install(
    glib_compile_schemas: true,
    gtk_update_icon_cache: true,
    update_desktop_database: true,
)
