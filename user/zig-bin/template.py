pkgname = "zig-bin"
pkgver = "0.15.2"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
pkgdesc = "Zig programming language toolchain"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/download/{pkgver}/zig-{'powerpc64le' if self.profile().arch == 'ppc64le' else self.profile().arch}-linux-{pkgver}.tar.xz"
sha256 = "02aa270f183da276e5b5920b1dac44a63f1a49e55050ebde3aecc9eb82f93239"


def install(self):
    self.install_license("LICENSE")
    self.install_files("lib", "usr/lib/zig/")
    self.install_file("zig", "usr/lib/zig/", mode=0o755)
    self.install_dir("usr/bin")
    self.install_link("usr/bin/zig", "../lib/zig/zig")
    self.install_files("doc", "usr/share/doc", name="zig")
