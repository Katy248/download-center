PROJECT_NAME := "download-center"
BUILD_DIR := "builddir"

setup:
    meson setup {{ BUILD_DIR }} --reconfigure
    just --fmt --unstable

update-translations: setup
    meson compile -C {{ BUILD_DIR }} {{ PROJECT_NAME }}-pot
    meson compile -C {{ BUILD_DIR }} {{ PROJECT_NAME }}-update-po

build: update-translations
    meson compile -C {{ BUILD_DIR }}

install: build
    meson install -C {{ BUILD_DIR }}

run: install
    cd .. && {{ PROJECT_NAME }}
