NODE_TEMPLATE = """
  <node
    pkg="ros_ign_gazebo"
    type="create"
    name= "model{index}"
    output="screen"
    args="-world scene_base -file $(find simulator)/models/{category}/{model}/model.sdf -name model{index} -order {index} -allow_renaming true -x {x} -y {y} -z {z} -Y {yaw} -P {pitch} -R {roll}">
  </node>
"""
