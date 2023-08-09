LAUNCH_FILE_TEMPLATE = """<?xml version="1.0"?>
<launch>

  <include file="$(find ros_ign_gazebo)/launch/ign_gazebo.launch">
    <arg name="ign_args" value="-r  $(find simulator)/scene_base.sdf"/>
  </include>

  {node_setup}
</launch>
"""
