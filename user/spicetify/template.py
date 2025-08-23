pkgname = "spicetify"
pkgver = "2.41.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Command-line tool to customize Spotify client"
license = "LGPL-2.1-only"
url = "https://spicetify.app"
source = f"https://github.com/spicetify/cli/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7a3e6ae327753060fac9fa0686e57b871ef92598752a1314ef0f5b1cde571230"
# no tests available
options = ["!check"]


def install(self):
    self.install_dir("usr/lib/spicetify")
    self.install_file(
        "build/cli", "usr/lib/spicetify", mode=0o755, name="spicetify"
    )
    self.install_dir("usr/bin")
    self.install_link("usr/bin/spicetify", "../lib/spicetify/spicetify")

    for f in [
        "CustomApps",
        "Extensions",
        "jsHelper",
        "Themes",
        "css-map.json",
        "globals.d.ts",
    ]:
        self.install_files(f, "usr/lib/spicetify/")

    self.install_license("LICENSE")
