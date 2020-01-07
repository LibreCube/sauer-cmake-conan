# Cube 2: Sauerbraten + CMake + Conan

This repository contains the source code of [Cube 2: Sauerbraten](http://sauerbraten.org)
without any of the binary blobs from SVN and the makefile/Visual Studio solution/XCode project files,
with a small exception for the Sauerbraten logo.

Instead, I have added CMake and Conan support for it.


## Requirements 
  * [CMake](https://cmake.org) >= 3.10.0
  * [Conan](https://conan.io) >= 1.21.0
  * a C++17 compiler


## License
Like the Sauerbraten source code, all files within this repository are ZLIB licensed.
If some non-free file from Sauerbraten (e.g. any of the media files) 
slid through my check this is considered a bug, 
please inform me about this.

All third-party dependencies which are getting pulled in by Conan during build time 
have their own respective licenses.
