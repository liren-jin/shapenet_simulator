rosrun ros_ign_bridge parameter_bridge /rgbd/image@sensor_msgs/Image@ignition.msgs.Image \
                                       /rgbd/depth_image@sensor_msgs/Image@ignition.msgs.Image \
                                       /semantic/labels_map@sensor_msgs/Image@ignition.msgs.Image \
                                       rgbd/camera_info@sensor_msgs/CameraInfo@ignition.msgs.CameraInfo