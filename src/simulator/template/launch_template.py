NODE_TEMPLATE = """
  <node
    pkg="ros_ign_gazebo"
    type="create"
    name= "model{index}"
    output="screen"
    args="-world scene_base -file $(find simulator)/models/{category}/{model}/model.sdf -name model{index} -order {index} -x {x} -y {y} -z {z} -Y {yaw} -P {pitch} -R {roll}">
  </node>
"""

LAUNCH_FILE_TEMPLATE = """<?xml version="1.0"?>
<launch>
  <include file="$(find ros_ign_gazebo)/launch/ign_gazebo.launch">
    <arg name="ign_args" value="-r  $(find simulator)/scene_base.sdf"/>
  </include>

  <node
    pkg="ros_ign_gazebo"
    type="create"
    name= "wall"
    output="screen"
    args="-world scene_base -file $(find simulator)/models/wall/model.sdf -name wall -order 0 -x 0 -y 0 -z 0 -Y 0 -P 0 -R 1.570756">
  </node>
  
  {node_setup}
</launch>
"""
