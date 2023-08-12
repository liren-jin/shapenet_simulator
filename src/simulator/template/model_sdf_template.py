MODEL_SDF_TEMPLATE = """
<?xml version="1.0" ?>
    <sdf version="1.6">
        <model name="{model_name}">
            <link name="link">
                <inertial>
                    <mass>{mass}</mass>
                    <inertia>
                        <ixx>{inertia[0]}</ixx>
                        <iyy>{inertia[1]}</iyy>
                        <izz>{inertia[2]}</izz>
                    </inertia>
                </inertial>
                <visual name="visual">
                    <geometry>
                        <mesh>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <uri>models/model_normalized.obj</uri>
                        </mesh>
                    </geometry>
                </visual>
                <collision name="collision">
                    <geometry>
                        <mesh>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <uri>collision.stl</uri>
                        </mesh>
                    </geometry>
                </collision>
            </link>
            <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
                <label>{label}</label>
            </plugin>
        </model>
    </sdf>
"""

MODEL_SDF_TEMPLATE_SIMPLE = """
<?xml version="1.0" ?>
    <sdf version="1.6">
        <model name="{model_name}">
            <link name="link">
                <inertial>
                    <mass>{mass}</mass>
                    <inertia>
                        <ixx>{inertia[0]}</ixx>
                        <iyy>{inertia[1]}</iyy>
                        <izz>{inertia[2]}</izz>
                    </inertia>
                </inertial>
                <visual name="visual">
                    <geometry>
                        <mesh>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <uri>/models/model_normalized.obj</uri>
                        </mesh>
                    </geometry>
                </visual>
                <collision name="collision">
                    <pose>{origin[0]} {origin[1]} {origin[2]} 0 0 0</pose>
                    <geometry>
                        <box>
                            <scale>{scale[0]} {scale[1]} {scale[2]}</scale>
                            <size>{bounding_box[0]} {bounding_box[1]} {bounding_box[2]}</size>
                        </box>
                    </geometry>
                </collision>
            </link>
            <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
                <label>{label}</label>
            </plugin>
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
    a {category} model
  </description>
</model>
"""
