in one terminal
```commanline
cd src/simulator
python3 scene_sdf_generator.py -N <object number>
ign gazebo new_scene.sdf 
```
in another terminal
```commandline
source devel/setup.bash
roslaunch simulator ros_bridge.launch
```
required topic:
- /set_camera_pose geometry_msgs/Pose

published topics:
- /rgbd/camera_info sensor_msgs/CameraInfo
- /rgbd/depth_image sensor_msgs/Image
- /rgbd/image sensor_msgs/Image
- /semantic/labels_map sensor_msgs/Image