pkgname = "zig-bin"
pkgver = "0.14.0"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
pkgdesc = "Zig programming language toolchain"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/download/{pkgver}/zig-linux-{'powerpc64le' if self.profile().arch == 'ppc64le' else self.profile().arch}-{pkgver}.tar.xz"
sha256 = "473ec26806133cf4d1918caf1a410f8403a13d979726a9045b421b685031a982"


def install(self):
    self.install_license("LICENSE")
    self.install_files("lib", "usr/lib/zig/")
    self.install_file("zig", "usr/lib/zig/", mode=0o755)
    self.install_dir("usr/bin")
    self.install_link("usr/bin/zig", "../lib/zig/zig")
    self.install_files("doc", "usr/share/doc", name="zig")
