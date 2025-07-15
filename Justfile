PROJECT_NAME := "download-center"
BUILD_DIR := "builddir"

setup:
    meson setup {{ BUILD_DIR }} --reconfigure

build: setup
    meson compile -C {{ BUILD_DIR }}

install: build
    meson install -C {{ BUILD_DIR }}

run: install
    cd .. && {{ PROJECT_NAME }}
