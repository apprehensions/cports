pkgname = "cambalache"
pkgver = "0.97.8"
_commit = "6e0b383eba841efbded3c2dac0cf05128107480e"  # no proper tag yet
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "libadwaita-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "meson",
    "pkgconf",
    "python-lxml",
    "wlroots0.18-devel",
]
makedepends = [
    "gtksourceview-devel",
    "libhandy-devel",
    # "python-devel",
    "python-gobject-devel",
    "wayland-protocols",
]
depends = [
    "gsettings-desktop-schemas",
    "python-gobject",
    "python-lxml",
]
checkdepends = ["python-pytest"]
pkgdesc = "New RAD tool for Gtk 4 and 3"
license = "LGPL-2.1-only"
url = "https://gitlab.gnome.org/jpu/cambalache"
source = [
    f"{url}/-/archive/{_commit}/cambalache-{_commit}.tar.gz",
    "https://gitlab.gnome.org/jpu/casilda/-/archive/0.9.2/casilda-0.9.2.tar.gz",
]
source_paths = [".", "subprojects/casilda"]
sha256 = [
    "c90706709830c2a4299d1ed721bb922af5ede6563d0f142fa5ad7b3ae61c1fbe",
    "c0d06f952d6c518bad95b414d37a6a7b9b6d8af1a74f105e632f210864618034",
]
# until GObject is fixed
options = ["!check"]

