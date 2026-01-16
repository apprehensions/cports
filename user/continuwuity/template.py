pkgname = "continuwuity"
pkgver = "0.5.3"
pkgrel = 0
build_style = "cargo"
make_check_env = {"CONTINUWUITY_DATABASE_PATH": "/tmp/tuwunel-smoketest.db"}
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-rustfmt"]
makedepends = ["dinit-chimera", "rust-std", "liburing-devel", "linux-headers", "zstd-devel"]
pkgdesc = "Community-driven Matrix homeserver"
license = "Apache-2.0"
url = "https://continuwuity.org"
source = f"https://forgejo.ellis.link/continuwuation/continuwuity/archive/v{pkgver}.tar.gz"
sha256 = "2d339e0940d781b332e88f8dd7058773612e7be822bfd0e3cad7e1e5cab16a20"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/conduwuit")
    self.install_file("conduwuit-example.toml", "usr/share/examples/continuwuity")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "continuwuity")
    self.install_license("LICENSE")
