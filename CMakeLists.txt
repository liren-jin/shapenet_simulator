cmake_minimum_required(VERSION 3.10.2 FATAL_ERROR)

project(simulator)

# Find the Ignition_Transport library
find_package(ignition-transport11 QUIET REQUIRED OPTIONAL_COMPONENTS log)
find_package(roscpp REQUIRED)
find_package(geometry_msgs REQUIRED)
set(IGN_TRANSPORT_VER ${ignition-transport11_VERSION_MAJOR})

include_directories(${CMAKE_BINARY_DIR})
include_directories(${roscpp_INCLUDE_DIRS})
include_directories(${geometry_msgs_INCLUDE_DIRS})

add_executable(camera_controller simulator/camera_controller.cpp)
target_link_libraries(camera_controller ignition-transport${IGN_TRANSPORT_VER}::core ${roscpp_LIBRARIES} ${geometry_msgs_LIBRARIES})