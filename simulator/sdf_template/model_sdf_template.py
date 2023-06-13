MODEL_SDF_TEMPLATE = """
<?xml version="1.0" ?>
    <sdf version="1.6">
        <model name="{model_name}">
            <inertial>
                <mass>10</mass>
                <inertia>
                    <ixx>1</ixx>
                    <ixy>0</ixy>
                    <ixz>0</ixz>
                    <iyy>1</iyy>
                    <iyz>0</iyz>
                    <izz>1</izz>
                </inertia>
            </inertial>
            <link name="link">
                <visual name="visual">
                    <geometry>
                        <mesh>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <uri>model://models/{category}/{model_name}/models/model_normalized.obj</uri>
                        </mesh>
                    </geometry>
                </visual>
                <collision name="collision">
                    <geometry>
                        <mesh>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <uri>model://models/{category}/{model_name}/models/model_normalized.obj</uri>
                        </mesh>
                    </geometry>
                </collision>
            </link>
        </model>
    </sdf>
"""

MODEL_CONFIG_TEMPLATE = """
<?xml version="1.0"?>
<model>
  <name>{model_name}</name>
  <version>1.0</version>
  <sdf version="1.6">model.sdf</sdf>

  <author>
    <name>{author}</name>
    <email>{email}</email>
  </author>

  <description>
    {model_name}
  </description>
</model>
"""
