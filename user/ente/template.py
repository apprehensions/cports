pkgname = "ente"
pkgver = "0.2.3"
pkgrel = 0
build_wrksrc = "cli"
build_style = "go"
make_build_args = [f"-ldflags=-X main.AppVersion={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Utility for exporting data from Ente"
license = "AGPL-3.0-only"
url = "https://github.com/ente-io/ente"
source = f"{url}/archive/refs/tags/cli-v{pkgver}.tar.gz"
sha256 = "6bd4ab7b60bf15dd52fbf531d7fa668660caf85c60ef8c4b4f619b777068b4e3"


def prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def install(self):
    self.install_bin("build/cli", name="ente")
    self.install_license(self.srcdir / "LICENSE")
