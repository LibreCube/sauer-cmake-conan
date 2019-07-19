cmake_minimum_required(VERSION 3.13.0 FATAL_ERROR)

set(CMAKE_SYSTEM_VERSION 10.0 CACHE TYPE INTERNAL FORCE)

project(sauerbraten)

################################################################################
# Set target arch type if empty. Visual studio solution generator provides it.
################################################################################
if(NOT CMAKE_VS_PLATFORM_NAME)
    set(CMAKE_VS_PLATFORM_NAME "x64")
endif()
message("${CMAKE_VS_PLATFORM_NAME} architecture in use")

if(NOT ("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32"
     OR "${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64"))
    message(FATAL_ERROR "${CMAKE_VS_PLATFORM_NAME} arch is not supported!")
endif()

################################################################################
# Global configuration types
################################################################################
set(CMAKE_CONFIGURATION_TYPES
    "Debug"
    "Profile"
    "Release"
    CACHE STRING "" FORCE
)

################################################################################
# Global compiler options
################################################################################
if(MSVC)
    # remove default flags provided with CMake for MSVC
    set(CMAKE_CXX_FLAGS "")
    set(CMAKE_CXX_FLAGS_DEBUG "")
    set(CMAKE_CXX_FLAGS_PROFILE "")
    set(CMAKE_CXX_FLAGS_RELEASE "")
endif()

################################################################################
# Global linker options
################################################################################
if(MSVC)
    # remove default flags provided with CMake for MSVC
    set(CMAKE_EXE_LINKER_FLAGS "")
    set(CMAKE_MODULE_LINKER_FLAGS "")
    set(CMAKE_SHARED_LINKER_FLAGS "")
    set(CMAKE_STATIC_LINKER_FLAGS "")
    set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS}")
    set(CMAKE_MODULE_LINKER_FLAGS_DEBUG "${CMAKE_MODULE_LINKER_FLAGS}")
    set(CMAKE_SHARED_LINKER_FLAGS_DEBUG "${CMAKE_SHARED_LINKER_FLAGS}")
    set(CMAKE_STATIC_LINKER_FLAGS_DEBUG "${CMAKE_STATIC_LINKER_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS_PROFILE "${CMAKE_EXE_LINKER_FLAGS}")
    set(CMAKE_MODULE_LINKER_FLAGS_PROFILE "${CMAKE_MODULE_LINKER_FLAGS}")
    set(CMAKE_SHARED_LINKER_FLAGS_PROFILE "${CMAKE_SHARED_LINKER_FLAGS}")
    set(CMAKE_STATIC_LINKER_FLAGS_PROFILE "${CMAKE_STATIC_LINKER_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS}")
    set(CMAKE_MODULE_LINKER_FLAGS_RELEASE "${CMAKE_MODULE_LINKER_FLAGS}")
    set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS}")
    set(CMAKE_STATIC_LINKER_FLAGS_RELEASE "${CMAKE_STATIC_LINKER_FLAGS}")
endif()

################################################################################
# Nuget packages function stub.
################################################################################
function(use_package TARGET PACKAGE VERSION)
    message(WARNING "No implementation of use_package. Create yours.")
endfunction()

################################################################################
# Common utils
################################################################################
include(CMake/Utils.cmake)

################################################################################
# Additional Global Settings(add specific info there)
################################################################################
include(CMake/GlobalSettingsInclude.cmake OPTIONAL)

################################################################################
# Use solution folders feature
################################################################################
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

################################################################################
# Sub-projects
################################################################################



























project(sauerbraten CXX)

################################################################################
# Source groups
################################################################################
set(engine
    ../engine/3dgui.cpp
    ../engine/animmodel.h
    ../engine/bih.cpp
    ../engine/bih.h
    ../engine/blend.cpp
    ../engine/blob.cpp
    ../engine/client.cpp
    ../engine/command.cpp
    ../engine/console.cpp
    ../engine/cubeloader.cpp
    ../engine/decal.cpp
    ../engine/depthfx.h
    ../engine/dynlight.cpp
    ../engine/engine.h
    ../engine/explosion.h
    ../engine/glare.cpp
    ../engine/grass.cpp
    ../engine/iqm.h
    ../engine/lensflare.h
    ../engine/lightmap.cpp
    ../engine/lightmap.h
    ../engine/lightning.h
    ../engine/main.cpp
    ../engine/material.cpp
    ../engine/md2.h
    ../engine/md3.h
    ../engine/md5.h
    ../engine/menus.cpp
    ../engine/model.h
    ../engine/movie.cpp
    ../engine/mpr.h
    ../engine/normal.cpp
    ../engine/obj.h
    ../engine/octa.cpp
    ../engine/octa.h
    ../engine/octaedit.cpp
    ../engine/octarender.cpp
    ../engine/pch.cpp
    ../engine/physics.cpp
    ../engine/pvs.cpp
    ../engine/ragdoll.h
    ../engine/rendergl.cpp
    ../engine/rendermodel.cpp
    ../engine/renderparticles.cpp
    ../engine/rendersky.cpp
    ../engine/rendertarget.h
    ../engine/rendertext.cpp
    ../engine/renderva.cpp
    ../engine/server.cpp
    ../engine/serverbrowser.cpp
    ../engine/shader.cpp
    ../engine/shadowmap.cpp
    ../engine/skelmodel.h
    ../engine/smd.h
    ../engine/sound.cpp
    ../engine/textedit.h
    ../engine/texture.cpp
    ../engine/texture.h
    ../engine/vertmodel.h
    ../engine/water.cpp
    ../engine/world.cpp
    ../engine/world.h
    ../engine/worldio.cpp
)
source_group("engine" FILES ${engine})

set(fpsgame
    ../fpsgame/ai.cpp
    ../fpsgame/ai.h
    ../fpsgame/aiman.h
    ../fpsgame/capture.h
    ../fpsgame/client.cpp
    ../fpsgame/collect.h
    ../fpsgame/ctf.h
    ../fpsgame/entities.cpp
    ../fpsgame/extinfo.h
    ../fpsgame/fps.cpp
    ../fpsgame/game.h
    ../fpsgame/monster.cpp
    ../fpsgame/movable.cpp
    ../fpsgame/pch.cpp
    ../fpsgame/render.cpp
    ../fpsgame/scoreboard.cpp
    ../fpsgame/server.cpp
    ../fpsgame/waypoint.cpp
    ../fpsgame/weapon.cpp
)
source_group("fpsgame" FILES ${fpsgame})

set(shared
    ../shared/command.h
    ../shared/crypto.cpp
    ../shared/cube.h
    ../shared/ents.h
    ../shared/geom.cpp
    ../shared/geom.h
    ../shared/glemu.cpp
    ../shared/glemu.h
    ../shared/glexts.h
    ../shared/iengine.h
    ../shared/igame.h
    ../shared/pch.cpp
    ../shared/stream.cpp
    ../shared/tools.cpp
    ../shared/tools.h
    ../shared/zip.cpp
)
source_group("shared" FILES ${shared})

set(ALL_FILES
    ${engine}
    ${fpsgame}
    ${shared}
)

################################################################################
# Target
################################################################################
add_executable(${PROJECT_NAME} ${ALL_FILES})

add_precompiled_header(${PROJECT_NAME} "cube.h" ".")

use_props(${PROJECT_NAME} "${CMAKE_CONFIGURATION_TYPES}" "${DEFAULT_CXX_PROPS}")
set(ROOT_NAMESPACE sauerbraten)

################################################################################
# Target name
################################################################################
if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    set_target_properties(${PROJECT_NAME} PROPERTIES
        TARGET_NAME_DEBUG   "sauerbraten_debug"
        TARGET_NAME_PROFILE "sauerbraten"
        TARGET_NAME_RELEASE "sauerbraten"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    set_target_properties(${PROJECT_NAME} PROPERTIES
        TARGET_NAME_DEBUG   "sauerbraten_debug"
        TARGET_NAME_PROFILE "sauerbraten"
        TARGET_NAME_RELEASE "sauerbraten"
    )
endif()
################################################################################
# Output directory
################################################################################
if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    set_target_properties(${PROJECT_NAME} PROPERTIES
        OUTPUT_DIRECTORY_DEBUG   "${CMAKE_CURRENT_SOURCE_DIR}/../../bin/"
        OUTPUT_DIRECTORY_PROFILE "${CMAKE_CURRENT_SOURCE_DIR}/../../bin/"
        OUTPUT_DIRECTORY_RELEASE "${CMAKE_CURRENT_SOURCE_DIR}/../../bin/"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    set_target_properties(${PROJECT_NAME} PROPERTIES
        OUTPUT_DIRECTORY_DEBUG   "${CMAKE_CURRENT_SOURCE_DIR}/../../bin64/"
        OUTPUT_DIRECTORY_PROFILE "${CMAKE_CURRENT_SOURCE_DIR}/../../bin64/"
        OUTPUT_DIRECTORY_RELEASE "${CMAKE_CURRENT_SOURCE_DIR}/../../bin64/"
    )
endif()
################################################################################
# Include directories
################################################################################
if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    target_include_directories(${PROJECT_NAME} PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../enet/include;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../include;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../engine;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../fpsgame;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../shared"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    target_include_directories(${PROJECT_NAME} PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../enet/include;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../include;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../engine;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../fpsgame;"
        "${CMAKE_CURRENT_SOURCE_DIR}/../shared"
    )
endif()

################################################################################
# Compile definitions
################################################################################
if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    target_compile_definitions(${PROJECT_NAME} PRIVATE
        "$<$<CONFIG:Debug>:"
            "_DEBUG"
        ">"
        "$<$<CONFIG:Profile>:"
            "NDEBUG"
        ">"
        "$<$<CONFIG:Release>:"
            "NDEBUG"
        ">"
        "WIN32;"
        "_WINDOWS;"
        "_MBCS"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    target_compile_definitions(${PROJECT_NAME} PRIVATE
        "$<$<CONFIG:Debug>:"
            "_DEBUG"
        ">"
        "$<$<CONFIG:Profile>:"
            "NDEBUG"
        ">"
        "$<$<CONFIG:Release>:"
            "NDEBUG"
        ">"
        "WIN32;"
        "_WINDOWS;"
        "_MBCS"
    )
endif()

################################################################################
# Compile and link options
################################################################################
if(MSVC)
    if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
        target_compile_options(${PROJECT_NAME} PRIVATE
            $<$<CONFIG:Debug>:
                /GL;
                /Od;
                /RTCs;
                /MTd;
                /Zi;
                /EHa
            >
            $<$<CONFIG:Profile>:
                /Gm-;
                /O2;
                /GF;
                /Oy;
                /MT;
                /Gy-;
                /Zi;
                /Ot;
                ${DEFAULT_CXX_EXCEPTION_HANDLING};
                /GS-;
                /Zc:forScope
            >
            $<$<CONFIG:Release>:
                /GL;
                /Gm-;
                /O2;
                /Ob2;
                /GF;
                /Oy;
                /MT;
                /Gy-;
                /fp:except-;
                ${DEFAULT_CXX_DEBUG_INFORMATION_FORMAT};
                /Ot;
                /EHa;
                /GS-;
                /Zc:forScope
            >
            /W3;
            /fp:fast
        )
    elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
        target_compile_options(${PROJECT_NAME} PRIVATE
            $<$<CONFIG:Debug>:
                /GL;
                /Od;
                /RTCs;
                /MTd;
                /Zi;
                /EHa
            >
            $<$<CONFIG:Profile>:
                /Gm-;
                /O2;
                /GF;
                /Oy;
                /MT;
                /Gy-;
                /Zi;
                /Ot;
                ${DEFAULT_CXX_EXCEPTION_HANDLING};
                /GS-;
                /Zc:forScope
            >
            $<$<CONFIG:Release>:
                /GL;
                /Gm-;
                /O2;
                /Ob2;
                /GF;
                /Oy;
                /MT;
                /Gy-;
                /fp:except-;
                ${DEFAULT_CXX_DEBUG_INFORMATION_FORMAT};
                /Ot;
                /EHa;
                /GS-;
                /Zc:forScope
            >
            /W3;
            /fp:fast
        )
    endif()
    if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
        target_link_options(${PROJECT_NAME} PRIVATE
            $<$<CONFIG:Debug>:
                /LTCG;
                /INCREMENTAL
            >
            $<$<CONFIG:Profile>:
                /INCREMENTAL:NO
            >
            $<$<CONFIG:Release>:
                /LTCG;
                /OPT:REF;
                /OPT:ICF;
                /INCREMENTAL:NO
            >
            /NOLOGO;
            /DEBUG;
            /SUBSYSTEM:WINDOWS;
            /MACHINE:I386;
            /SAFESEH:NO
        )
    elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
        target_link_options(${PROJECT_NAME} PRIVATE
            $<$<CONFIG:Debug>:
                /LTCG;
                /INCREMENTAL
            >
            $<$<CONFIG:Profile>:
                /INCREMENTAL:NO
            >
            $<$<CONFIG:Release>:
                /LTCG;
                /OPT:REF;
                /OPT:ICF;
                /INCREMENTAL:NO
            >
            /NOLOGO;
            /DEBUG;
            /SUBSYSTEM:WINDOWS;
            /MACHINE:X64;
            /SAFESEH:NO
        )
    endif()
endif()

################################################################################
# Dependencies
################################################################################
if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    string(CONCAT ADDITIONAL_LIBRARY_DEPENDENCIES
        "$<$<CONFIG:Debug>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "SDL2_mixer;"
            "ws2_32;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
        "$<$<CONFIG:Profile>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "ws2_32;"
            "SDL2_mixer;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
        "$<$<CONFIG:Release>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "ws2_32;"
            "SDL2_mixer;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    string(CONCAT ADDITIONAL_LIBRARY_DEPENDENCIES
        "$<$<CONFIG:Debug>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "SDL2_mixer;"
            "ws2_32;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
        "$<$<CONFIG:Profile>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "ws2_32;"
            "SDL2_mixer;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
        "$<$<CONFIG:Release>:"
            "enet;"
            "zdll;"
            "opengl32;"
            "SDL2;"
            "SDL2_image;"
            "ws2_32;"
            "SDL2_mixer;"
            "winmm;"
            "dbghelp;"
            "kernel32;"
            "user32"
        ">"
    )
endif()
target_link_libraries(${PROJECT_NAME} PUBLIC "${ADDITIONAL_LIBRARY_DEPENDENCIES}")

if("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "Win32")
    target_link_directories(${PROJECT_NAME} PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../lib"
    )
elseif("${CMAKE_VS_PLATFORM_NAME}" STREQUAL "x64")
    target_link_directories(${PROJECT_NAME} PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../lib64"
    )
endif()

