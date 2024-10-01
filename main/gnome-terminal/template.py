pkgname = "gnome-terminal"
pkgver = "3.54.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "libuuid-devel",
    "nautilus-devel",
    "pcre2-devel",
    "vte-gtk3-devel",
]
pkgdesc = "GNOME terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"https://gitlab.gnome.org/GNOME/gnome-terminal/-/archive/{pkgver}/gnome-terminal-{pkgver}.tar.gz"
sha256 = "77370b4a00d0cda9ef339ff3aa809d266f3b937f00875176904c5bbefb76ae79"
# Upstream claims "LTO very much NOT supported"
# https://gitlab.gnome.org/GNOME/gnome-terminal/-/blob/09c8b31168460c325ac00820759d6eefdf3957ab/meson.build#L226
options = ["!cross", "!lto"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("nautilus-gnome-terminal-extension")
def _(self):
    self.pkgdesc = "GNOME terminal extension for Nautilus"
    self.depends += [self.parent]
    self.install_if = [self.parent, "nautilus"]

    return [
        "usr/lib/nautilus",
        "usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml",
    ]
