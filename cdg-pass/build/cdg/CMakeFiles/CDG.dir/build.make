# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.5.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.5.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/zmay/Projects/cs612/passes

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/zmay/Projects/cs612/passes/build

# Include any dependencies generated for this target.
include cdg/CMakeFiles/CDG.dir/depend.make

# Include the progress variables for this target.
include cdg/CMakeFiles/CDG.dir/progress.make

# Include the compile flags for this target's objects.
include cdg/CMakeFiles/CDG.dir/flags.make

cdg/CMakeFiles/CDG.dir/CDG.cpp.o: cdg/CMakeFiles/CDG.dir/flags.make
cdg/CMakeFiles/CDG.dir/CDG.cpp.o: ../cdg/CDG.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/zmay/Projects/cs612/passes/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object cdg/CMakeFiles/CDG.dir/CDG.cpp.o"
	cd /Users/zmay/Projects/cs612/passes/build/cdg && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CDG.dir/CDG.cpp.o -c /Users/zmay/Projects/cs612/passes/cdg/CDG.cpp

cdg/CMakeFiles/CDG.dir/CDG.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CDG.dir/CDG.cpp.i"
	cd /Users/zmay/Projects/cs612/passes/build/cdg && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/zmay/Projects/cs612/passes/cdg/CDG.cpp > CMakeFiles/CDG.dir/CDG.cpp.i

cdg/CMakeFiles/CDG.dir/CDG.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CDG.dir/CDG.cpp.s"
	cd /Users/zmay/Projects/cs612/passes/build/cdg && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/zmay/Projects/cs612/passes/cdg/CDG.cpp -o CMakeFiles/CDG.dir/CDG.cpp.s

cdg/CMakeFiles/CDG.dir/CDG.cpp.o.requires:

.PHONY : cdg/CMakeFiles/CDG.dir/CDG.cpp.o.requires

cdg/CMakeFiles/CDG.dir/CDG.cpp.o.provides: cdg/CMakeFiles/CDG.dir/CDG.cpp.o.requires
	$(MAKE) -f cdg/CMakeFiles/CDG.dir/build.make cdg/CMakeFiles/CDG.dir/CDG.cpp.o.provides.build
.PHONY : cdg/CMakeFiles/CDG.dir/CDG.cpp.o.provides

cdg/CMakeFiles/CDG.dir/CDG.cpp.o.provides.build: cdg/CMakeFiles/CDG.dir/CDG.cpp.o


# Object files for target CDG
CDG_OBJECTS = \
"CMakeFiles/CDG.dir/CDG.cpp.o"

# External object files for target CDG
CDG_EXTERNAL_OBJECTS =

cdg/libCDG.so: cdg/CMakeFiles/CDG.dir/CDG.cpp.o
cdg/libCDG.so: cdg/CMakeFiles/CDG.dir/build.make
cdg/libCDG.so: cdg/CMakeFiles/CDG.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/zmay/Projects/cs612/passes/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module libCDG.so"
	cd /Users/zmay/Projects/cs612/passes/build/cdg && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CDG.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
cdg/CMakeFiles/CDG.dir/build: cdg/libCDG.so

.PHONY : cdg/CMakeFiles/CDG.dir/build

cdg/CMakeFiles/CDG.dir/requires: cdg/CMakeFiles/CDG.dir/CDG.cpp.o.requires

.PHONY : cdg/CMakeFiles/CDG.dir/requires

cdg/CMakeFiles/CDG.dir/clean:
	cd /Users/zmay/Projects/cs612/passes/build/cdg && $(CMAKE_COMMAND) -P CMakeFiles/CDG.dir/cmake_clean.cmake
.PHONY : cdg/CMakeFiles/CDG.dir/clean

cdg/CMakeFiles/CDG.dir/depend:
	cd /Users/zmay/Projects/cs612/passes/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/zmay/Projects/cs612/passes /Users/zmay/Projects/cs612/passes/cdg /Users/zmay/Projects/cs612/passes/build /Users/zmay/Projects/cs612/passes/build/cdg /Users/zmay/Projects/cs612/passes/build/cdg/CMakeFiles/CDG.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : cdg/CMakeFiles/CDG.dir/depend

