# Shapenet Simulator: A Simulator with Multiple Shapenet Model Objects
Liren Jin

## Environment Setup
For using the simulator, you need to install [docker](https://docs.docker.com/engine/install/) and [nvidia run time](https://nvidia.github.io/nvidia-container-runtime/) support.

```commandline
git clone git@github.com:liren-jin/shapenet_simulator.git
cd shapenet_simulator
docker build . -t shapenet-simulator:v0
```

## Generate a Scene
The simulator supports generation of random scenes.

For the first time or when new models are added into the repo, we generate individual model sdf:
```commandline
cd src/simulation
python3 model_sdf_generator.py
```
To generate a new scene:
```commandline
python3 scene_sdf_generator.py -N <number of objects>
```
A file called new_scene.sdf should now be added into the simulator folder.

## Basic Usage
After you create a scene, you can run:
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



## Models Pre-Processing
Shapenet model can be download from [here](https://shapenet.org/download/shapenetcore).
Select your models and copy them to src/simulator/models folder. Catogrize the models based on their semantic class. An example would be :
```
src/simulator/models
|
|___ car
|    |__ model1
|    |__ model2
|    |__ ...
|
|__ ship
|   |__ model1
|   |__ model2
|   |__ ...
|
|__ ...


```