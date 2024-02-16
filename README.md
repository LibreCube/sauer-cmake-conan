# Cube 2: Sauerbraten + CMake + Conan

This repository contains the source code of [Cube 2: Sauerbraten](http://sauerbraten.org)
without any of the binary blobs from SVN and the makefile/Visual Studio solution/XCode project files,
with a small exception for the Sauerbraten logo.

Instead, I have added CMake and Conan support for it.


## Requirements

  * [CMake](https://cmake.org) >= 3.19.0
  * [Conan](https://conan.io) >= 1.63.0 < 2
  * a C++17 compiler


## Build

Execute Conan, something like:

> conan install . --build missing -pr:b default -pr:h default

then CMake configure with the generated CMake Toolchain file

> cmake --preset default

then CMake build

> cmake --build --preset release

and finally, CMake install.

> cmake --install .


## Content Download

Currently, the Sauerbraten content needs to be downloaded manually, in oder to use the executables from this project.

Please note that these instructions contain version specific links and directory names. The current version is `5692`.

Once you have a successful build, go to the [Sauerbraten Sourceforge page](https://sourceforge.net/p/sauerbraten/code/5692/tree/) and click on `Download Snapshot`.

In the root of your build directory, create a new directory path called

> packages/sauerbraten/1.5692/

Extract the downloaded snapshot in this newly created directory.

For future updates, download the related snapshot, create a new version directory and extract the snapshot there. You might want to delete the old version directories in order to free disk space, but you can also keep it, if you plan to switch between different versions.


## License

Like the Sauerbraten source code, all files within this repository are ZLIB licensed.
If some non-free file from Sauerbraten (e.g. any of the media files)
slid through my check this is considered a bug,
please inform me about this.

All third-party dependencies which are getting pulled in by Conan during build time have their own respective licenses.
