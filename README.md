# Shapenet Simulator: A Simulator using Multiple Shapenet Model Objects with Semantic Rendering
Liren Jin, University of Bonn

## Environment Setup
For using the simulator, you need to install [docker](https://docs.docker.com/engine/install/) and [nvidia run time](https://nvidia.github.io/nvidia-container-runtime/) support.

```commandline
git clone git@github.com:liren-jin/shapenet_simulator.git
cd shapenet_simulator
docker build . -t shapenet-simulator:v0
```
## Generate a Scene
The simulator supports generation of random scenes.
We use python to generate files that can be used for the simulator, e.g., launch and sdf files, use requirement.txt to install necessary python packages. 

For the first time or when new models are added into the repo, we generate individual model sdf:
```commandline
cd src/simulation
python3 model_sdf_generator.py
```

We also need a scene sdf file describing all scene properties:
```commandline
python3 scene_sdf_generator.py
```
For customizing scene properties, using simulator/cfg/scene_cfg.yaml.

To generate a new launch file to launch scene and models:
```commandline
python3 launch_file_generator.py -N <number of objects>
```


## Basic Usage
After you create a new simulation, you can run:
```commanline
xhost +local:docker
make 
make simulation
```

If everything goes well, you should see an Ignition-Gazebo user interface, press the start button to start the simulation.
It may take a few seconds untill all objects stay static. You can also stop the simulation, which will not affect the rendering and camera movement. 

required topic:
- /set_camera_pose geometry_msgs/Pose

published topics:
- /rgbd/camera_info sensor_msgs/CameraInfo
- /rgbd/depth_image sensor_msgs/Image
- /rgbd/image sensor_msgs/Image
- /semantic/labels_map sensor_msgs/Image



## Models Pre-Processing
Shapenet model can be download from [here](https://shapenet.org/download/shapenetcore).
Select your models and copy them to src/simulator/models folder. Catogrize the models based on their semantic class (allowed category names are shown in constants.py file). An example would be :
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
