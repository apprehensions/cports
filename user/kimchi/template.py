pkgname = "kimchi"
# No stable release yet
_commit = "63ffe933897eadaceb4b502a4ee7570b8f84f40e"
pkgver = "0.0.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [ "GOFLAGS=-buildmode=pie" ]
hostmakedepends = [ "go", "scdoc", "libcap-progs" ]
pkgdesc = "Bare-bones HTTP server"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://codeberg.org/emersion/kimchi"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "224ff49a9aee6209394d5230aec0477f1a6a66e5af70dfc45fb29365d64bcd07"
file_modes = {
    "usr/bin/kimchi": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/kimchi": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]

def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))

def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "kimchi")
    self.install_license("LICENSE")
