pkgname = "tlstunnel"
pkgver = "0.5.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags= "
    + "-X main.configPath=/etc/tlstunnel/config "
    + "-X main.certDataPath=/var/lib/tlstunnel",
    "./cmd/tlstunnel",
]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
makedepends = ["dinit-chimera"]
pkgdesc = "TLS reverse proxy"
license = "MIT"
url = "https://codeberg.org/emersion/tlstunnel"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3eb0a3030aa9c2d955766705d37a3590032c71fcc656bcdf4644d88031dc4571"
file_modes = {
    "usr/bin/tlstunnel": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/tlstunnel": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "tlstunnel.1")


def post_install(self):
    self.install_man("tlstunnel.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "tlstunnel")
    self.install_license("LICENSE")
