cmake_minimum_required(VERSION 3.5)
set(LLVM_DIR "/Users/zmay/Projects/clang-dev/build/lib/cmake/llvm/")
set(LLVM_CREATE_XCODE_TOOLCHAIN "ON")
#set(LLVM_DIR "/usr/local/opt/llvm/share/llvm/cmake/")
#set(LLVM_ENABLE_CXX1Y "ON")
#set(LLVM_ENABLE_LIBCXX "ON")

#http://stackoverflow.com/questions/17225956/developing-an-llvm-pass-with-cmake-out-of-llvm-source-directory

find_package(LLVM REQUIRED CONFIG)

message(STATUS "Found LLVM ${LLVM_PACKAGE_VERSION}")
message(STATUS "Using LLVMConfig.cmake in: ${LLVM_DIR}")

add_definitions(${LLVM_DEFINITIONS})
include_directories(${LLVM_INCLUDE_DIRS})

add_subdirectory(cdg)
