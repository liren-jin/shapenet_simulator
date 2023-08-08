# Shapenet Simulator: A Simulator with Multiple Shapenet Model Objects
Liren Jin

## Environment Setup
For using the simulator, you need to install [docker](https://docs.docker.com/engine/install/) and [nvidia run time](https://nvidia.github.io/nvidia-container-runtime/) support.

```commandline
git clone git@github.com:liren-jin/shapenet_simulator.git
cd shapenet_simulator
docker build . -t shapenet-simulator:v0
```

## Basic Usage
```commanline
make 
make simulation
```

If everything goes well, you should see an Ignition-Gazebo user interface, press the start button to start the simulation. 

required topic:
- /set_camera_pose geometry_msgs/Pose

published topics:
- /rgbd/camera_info sensor_msgs/CameraInfo
- /rgbd/depth_image sensor_msgs/Image
- /rgbd/image sensor_msgs/Image
- /semantic/labels_map sensor_msgs/Image


## Different Scenes
The simulator supports generation of random scenes. To do so, open a new terminal,
```commandline
cd src/simulation
python3 scene_sdf_generator.py -N <number of objects>
```
you can run "make simulation" again to see the new scene imported in the simulator.

## Models Pre-Processing
coming soon