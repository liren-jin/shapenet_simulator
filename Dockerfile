FROM ros:noetic

ARG DEBIAN_FRONTEND=noninteractive

# Set project folder
WORKDIR "/shapenet_simulator"

# Install basic packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils nano git curl wget python3-catkin-tools&&\
    rm -rf /var/lib/apt/lists/*

# Install ign gazebo
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list' && \
    wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add - && \
    apt-get update && \
    apt-get -y install libignition-gazebo6-dev


# Build simulator
SHELL ["/bin/bash", "-c"]
RUN apt-get install -y ros-noetic-ros-ign qt5-default
COPY src/ src/
RUN . /opt/ros/noetic/setup.bash &&\
    catkin build 
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc &&\
    echo "source /shapenet_simulator/devel/setup.bash" >> ~/.bashrc