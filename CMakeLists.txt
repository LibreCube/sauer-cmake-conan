cmake_minimum_required(VERSION 3.10.0 FATAL_ERROR)
set(PROJECT_NAME sauerbraten)

################### Variables. ####################

# Output Variables
set(OUTPUT_DEBUG Debug/bin)
set(OUTPUT_RELEASE Release/bin)

############## CMake Project ################
#        The main options of project        #
#############################################

project(${PROJECT_NAME} CXX)

# Define Release by default.
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release")
  message(STATUS "Build type not specified: Use Release by default.")
endif(NOT CMAKE_BUILD_TYPE)

############## Artefacts Output #################
# Defines outputs , depending Debug or Release. #
#################################################

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_DEBUG}")
  set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_DEBUG}")
  set(CMAKE_EXECUTABLE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_DEBUG}")
else()
  set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_REL}")
  set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_REL}")
  set(CMAKE_EXECUTABLE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${OUTPUT_REL}")
endif()

################# Flags ################
# Defines Flags for Windows and Linux. #
########################################

set(BUILD_C_FLAGS "-DCLIENT")
set(BUILD_CXX_FLAGS "-DCLIENT")

set (CMAKE_CXX_STANDARD 11)

if(MSVC)
   set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /W3 /GL /Od /Zi")
   set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /W3 /GL /Od /Zi")
   SET(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} /LTCG")
endif(MSVC)
if(NOT MSVC)
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
   if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
       set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
   endif()

   set(BUILD_C_FLAGS "${BUILD_C_FLAGS} -fomit-frame-pointer -Wall -fsigned-char")
   set(BUILD_CXX_FLAGS "${BUILD_CXX_FLAGS} -fno-exceptions -fno-rtti")
endif(NOT MSVC)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(BUILD_TARGET_X64 1)
else()
    set(BUILD_TARGET_X86 1)
endif()

if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    set(BUILD_FLAGS "${BUILD_FLAGS} -DWINDOWS")
    if(BUILD_TARGET_X64)
        set(BUILD_FLAGS "${BUILD_FLAGS} -DWIN64")
    else()
        set(BUILD_FLAGS "${BUILD_FLAGS} -DWIN32")
    endif()
endif()

set(BUILD_DEBUG_FLAGS   "${BUILD_FLAGS} -D_DEBUG -DBUILD_DEBUG -DCLIENT")
set(BUILD_RELEASE_FLAGS "${BUILD_FLAGS} -DNDEBUG -DBUILD_NO_DEBUG")

set(BUILD_C_DEBUG_FLAGS "${BUILD_C_FLAGS} ${BUILD_DEBUG_FLAGS}")
set(BUILD_CXX_DEBUG_FLAGS "${BUILD_CXX_FLAGS} ${BUILD_DEBUG_FLAGS}")

set(BUILD_C_RELEASE_FLAGS "${BUILD_C_FLAGS} ${BUILD_RELEASE_FLAGS}")
set(BUILD_CXX_RELEASE_FLAGS "${BUILD_CXX_FLAGS} ${BUILD_RELEASE_FLAGS}")

set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} ${BUILD_C_DEBUG_FLAGS}")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} ${BUILD_CXX_DEBUG_FLAGS}")
message(STATUS "Set debug mode flags (${BUILD_DEBUG_FLAGS}) (Current mode: ${CMAKE_BUILD_TYPE}, compiler: ${CMAKE_CXX_COMPILER_ID})")

set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} ${BUILD_C_RELEASE_FLAGS}")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} ${BUILD_CXX_RELEASE_FLAGS}")
message(STATUS "Set release mode flags (${BUILD_RELEASE_FLAGS}) (Current mode: ${CMAKE_BUILD_TYPE}, compiler: ${CMAKE_CXX_COMPILER_ID})")



# --- Conan --- #
# Download Conan
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.14/conan.cmake"
            "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

# Include Conan CMake wrapper
include(${CMAKE_BINARY_DIR}/conan.cmake)

# Make sure we have a recent Conan version
conan_check(VERSION 1.17.0 REQUIRED) ## TODO: Doesn't work on some Windows configurations, upstream bug?

# Install Bincrafters Conan repository if not already installed
conan_add_remote(NAME bincrafters INDEX 2
        URL https://api.bintray.com/conan/bincrafters/public-conan)

# Execute `conan install ...` for the packages in conanfile.txt
conan_cmake_run(CONANFILE conanfile.txt
        BASIC_SETUP
        BUILD outdated)


################ Files ################

include_directories(src/shared src/engine src/fpsgame)

# TODO: remove
# get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
#foreach(dir ${dirs})
#    message(STATUS "dir='${dir}'")
#endforeach()

add_definitions(-DCLIENT)

# Add executable to build.
add_executable(${PROJECT_NAME}
        src/shared/crypto.cpp
        src/shared/cube2font.c
        src/shared/geom.cpp
        src/shared/glemu.cpp
        src/shared/pch.cpp
        src/shared/stream.cpp
        src/shared/tools.cpp
        src/shared/zip.cpp
        src/engine/3dgui.cpp
        src/engine/bih.cpp
        src/engine/blend.cpp
        src/engine/blob.cpp
        src/engine/client.cpp
        src/engine/command.cpp
        src/engine/console.cpp
        src/engine/cubeloader.cpp
        src/engine/decal.cpp
        src/engine/dynlight.cpp
        src/engine/glare.cpp
        src/engine/grass.cpp
        src/engine/lightmap.cpp
        src/engine/main.cpp
        src/engine/material.cpp
        src/engine/menus.cpp
        src/engine/movie.cpp
        src/engine/normal.cpp
        src/engine/octa.cpp
        src/engine/octaedit.cpp
        src/engine/octarender.cpp
        src/engine/pch.cpp
        src/engine/physics.cpp
        src/engine/pvs.cpp
        src/engine/rendergl.cpp
        src/engine/rendermodel.cpp
        src/engine/renderparticles.cpp
        src/engine/rendersky.cpp
        src/engine/rendertext.cpp
        src/engine/renderva.cpp
        src/engine/server.cpp
        src/engine/serverbrowser.cpp
        src/engine/shader.cpp
        src/engine/shadowmap.cpp
        src/engine/sound.cpp
        src/engine/texture.cpp
        src/engine/water.cpp
        src/engine/world.cpp
        src/engine/worldio.cpp
        src/fpsgame/ai.cpp
        src/fpsgame/client.cpp
        src/fpsgame/entities.cpp
        src/fpsgame/fps.cpp
        src/fpsgame/monster.cpp
        src/fpsgame/movable.cpp
        src/fpsgame/pch.cpp
        src/fpsgame/render.cpp
        src/fpsgame/scoreboard.cpp
        src/fpsgame/server.cpp
        src/fpsgame/waypoint.cpp
        src/fpsgame/weapon.cpp
)

# enet.lib;zdll.lib;opengl32.lib;SDL2.lib;SDL2_image.lib;ws2_32.lib;SDL2_mixer.lib;winmm.lib;dbghelp.lib;kernel32.lib;user32.lib

target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS} opengl32)

foreach(dir ${CONAN_LIBS})
    message(STATUS "lib='${dir}'")
endforeach()
