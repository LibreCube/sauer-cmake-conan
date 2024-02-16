from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain
from conan.tools.files import copy
import os 


class Sauerbraten(ConanFile):
    name = "sauerbraten"
    version = "r5692"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    def requirements(self):
        self.requires("enet/1.3.17")
        self.requires("sdl/2.28.3")
        self.requires("sdl_image/2.6.3")
        self.requires("sdl_mixer/2.0.4")
        self.requires("zlib/1.3")

    def tool_requirements(self):
        self.requires("cmake/3.28.1")

    def configure(self):
        self.options["enet"].shared = True
        self.options["sdl"].shared = True
        self.options["sdl_image"].shared = True
        # "sdl2_image:jpg": "libjpeg",
        self.options["sdl_mixer"].shared = True
        self.options["zlib"].shared = True

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        cdeps = CMakeDeps(self)
        cdeps.generate()

        target_dir = "bin_unix"
        if self.settings.os == "Windows":
            if self.settings.arch == "x86_64":
                target_dir = "bin64"
            else:
                target_dir = "bin"

        target_licenses_root = os.path.join(self.build_folder, target_dir, "licenses")

        for dep in self.dependencies.values():
            copy(self, "*.dylib", dep.cpp_info.libdirs[0], os.path.join(self.build_folder, target_dir))
            copy(self, "*.dll", dep.cpp_info.libdirs[0], os.path.join(self.build_folder, target_dir))
            copy(self, "*.dll", dep.cpp_info.bindirs[0], os.path.join(self.build_folder, target_dir))

            target_licenses = os.path.join(target_licenses_root, dep.ref.name)
            copy(self, "*", os.path.join(dep.package_folder, "licenses"), target_licenses)

        fo = open(os.path.join(self.build_folder, "version.txt"), "w")
        fo.write(self.version[1:])
        fo.close()
