pkgname = "breeze-icons"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBINARY_ICONS_RESOURCE=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "python-lxml",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = [
    "fdupes",
]
pkgdesc = "Breeze icon themes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-or-later"
url = "https://api.kde.org/frameworks/breeze-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/breeze-icons-{pkgver}.tar.xz"
sha256 = "2d8ccc427ec864b6417eabe3aafe9b1f6857bf2a4fdcd0dc5c006413148e66d9"
broken_symlinks = [
    # broken symbolic links to 24
    "usr/share/icons/breeze*/animations/24@*x",  # breeze{,-dark}/animations/24@{2,3}x
    "usr/share/icons/breeze/emotes/24@*x",  # 24@{2,3}x
    # broken symbolic link to fingerprint.svg
    "usr/share/icons/breeze/actions/24/fingerprint-symbolic.svg",
]
hardening = ["vis"]


@subpackage("breeze-icons-devel")
def _(self):
    return self.default_devel()