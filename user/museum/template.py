pkgname = "museum"
pkgver = "1.7.22"
pkgrel = 0
build_wrksrc = "server"
build_style = "go"
make_build_args = ["./cmd/museum"]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["dinit-chimera", "libsodium-devel"]
depends = ["postgresql"]
pkgdesc = "E2EE photo gallery"
license = "AGPL-3.0-only"
url = "https://ente.io"
source = f"https://github.com/ente-io/ente/archive/photosd-v{pkgver}.tar.gz"
sha256 = "0bc462dd8470a5858550b05caf52010c426535e0ff3b6e03e6149418e6e14d5e"
broken_symlinks = ["usr/share/museum/museum.yaml"]
# test requires manual setup
options = ["!check"]


def prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    for data in [
        "configurations",
        "migrations",
        "mail-templates",
        "web-templates",
    ]:
        self.install_files(data, "usr/share/museum")
    self.install_link(
        "usr/share/museum/museum.yaml", "../../../etc/museum/museum.yaml"
    )
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "museum")
    self.install_license(self.srcdir / "LICENSE")
