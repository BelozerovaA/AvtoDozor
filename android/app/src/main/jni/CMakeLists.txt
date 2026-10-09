cmake_minimum_required(VERSION 3.13)

project(appmodules)

# Override add_library to convert absolute source file paths to relative paths.
# This prevents Ninja on Windows from exceeding the 260 character path limit (_MAX_PATH).
macro(add_library target)
    set(_add_lib_args)
    set(_arg_index 0)
    foreach(arg ${ARGN})
        math(EXPR _arg_index "${_arg_index} + 1")
        # The first argument after target is library type (e.g. SHARED, STATIC, INTERFACE, ALIAS) if present
        if(IS_ABSOLUTE "${arg}" AND EXISTS "${arg}")
            file(RELATIVE_PATH _rel_path "${CMAKE_CURRENT_SOURCE_DIR}" "${arg}")
            list(APPEND _add_lib_args "${_rel_path}")
        else()
            list(APPEND _add_lib_args "${arg}")
        endif()
    endforeach()
    _add_library(${target} ${_add_lib_args})
endmacro()

macro(target_sources target)
    set(_target_src_args)
    foreach(arg ${ARGN})
        if(IS_ABSOLUTE "${arg}" AND EXISTS "${arg}")
            file(RELATIVE_PATH _rel_path "${CMAKE_CURRENT_SOURCE_DIR}" "${arg}")
            list(APPEND _target_src_args "${_rel_path}")
        else()
            list(APPEND _target_src_args "${arg}")
        endif()
    endforeach()
    _target_sources(${target} ${_target_src_args})
endmacro()

include(${REACT_ANDROID_DIR}/cmake-utils/ReactNative-application.cmake)
