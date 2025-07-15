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
desktop_file = 'ru.katy248.download-center.desktop'

dfv = find_program('desktop-file-validate', required: false)
if dfv.found()
    custom_target(
        'desktop-file-validation',
        input: desktop_file,
        command: [dfv, '@INPUT@'],
        output: '.',
    )
endif

i18n.merge_file(
    output: desktop_file,
    input: desktop_file,
    type: 'desktop',
    po_dir: meson.project_source_root() / 'po',
    install: true,
    install_dir: get_option('prefix') / get_option('datadir') / 'applications',
)

install_data(
    'download-center',
    install_dir: get_option('prefix') / get_option('bindir'),
)

install_data(
    'metainfo.xml',
    install_dir: get_option('prefix') / get_option('datadir') / 'metainfo',
    rename: 'ru.katy248.download-center.metainfo.xml',
)

gnome.post_install(
    glib_compile_schemas: true,
    gtk_update_icon_cache: true,
    update_desktop_database: true,
)
