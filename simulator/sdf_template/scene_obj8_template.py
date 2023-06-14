SDF_TEMPLATE = """
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="scene_base">
    <plugin
      filename="ignition-gazebo-physics-system"
      name="ignition::gazebo::systems::Physics">
    </plugin>
    <plugin
      filename="ignition-gazebo-user-commands-system"
      name="ignition::gazebo::systems::UserCommands">
    </plugin>
    <plugin
      filename="ignition-gazebo-scene-broadcaster-system"
      name="ignition::gazebo::systems::SceneBroadcaster">
    </plugin>
    <plugin
      filename="ignition-gazebo-sensors-system"
      name="ignition::gazebo::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>

    <gui fullscreen="0">

      <!-- 3D scene -->
      <plugin filename="MinimalScene" name="3D View">
        <ignition-gui>
          <title>3D View</title>
          <property type="bool" key="showTitleBar">false</property>
          <property type="string" key="state">docked</property>
        </ignition-gui>

        <engine>ogre2</engine>
        <scene>scene</scene>
        <ambient_light>0.4 0.4 0.4</ambient_light>
        <background_color>0.8 0.8 0.8</background_color>
        <camera_pose>-6 0 6 0 0.5 0</camera_pose>
      </plugin>

      <!-- Plugins that add functionality to the scene -->
      <plugin filename="EntityContextMenuPlugin" name="Entity context menu">
        <ignition-gui>
          <property key="state" type="string">floating</property>
          <property key="width" type="double">5</property>
          <property key="height" type="double">5</property>
          <property key="showTitleBar" type="bool">false</property>
        </ignition-gui>
      </plugin>
      <plugin filename="GzSceneManager" name="Scene Manager">
        <ignition-gui>
          <property key="resizable" type="bool">false</property>
          <property key="width" type="double">5</property>
          <property key="height" type="double">5</property>
          <property key="state" type="string">floating</property>
          <property key="showTitleBar" type="bool">false</property>
        </ignition-gui>
      </plugin>
      <plugin filename="InteractiveViewControl" name="Interactive view control">
        <ignition-gui>
          <property key="resizable" type="bool">false</property>
          <property key="width" type="double">5</property>
          <property key="height" type="double">5</property>
          <property key="state" type="string">floating</property>
          <property key="showTitleBar" type="bool">false</property>
        </ignition-gui>
      </plugin>
      <plugin filename="CameraTracking" name="Camera Tracking">
        <ignition-gui>
          <property key="resizable" type="bool">false</property>
          <property key="width" type="double">5</property>
          <property key="height" type="double">5</property>
          <property key="state" type="string">floating</property>
          <property key="showTitleBar" type="bool">false</property>
        </ignition-gui>
      </plugin>

      <!-- World control -->
      <plugin filename="WorldControl" name="World control">
        <ignition-gui>
          <title>World control</title>
          <property type="bool" key="showTitleBar">false</property>
          <property type="bool" key="resizable">false</property>
          <property type="double" key="height">72</property>
          <property type="double" key="width">121</property>
          <property type="double" key="z">1</property>

          <property type="string" key="state">floating</property>
          <anchors target="3D View">
            <line own="left" target="left"/>
            <line own="bottom" target="bottom"/>
          </anchors>
        </ignition-gui>

        <play_pause>true</play_pause>
        <step>true</step>
        <start_paused>false</start_paused>
        <use_event>true</use_event>

      </plugin>

      <!-- World statistics -->
      <plugin filename="WorldStats" name="World stats">
        <ignition-gui>
          <title>World stats</title>
          <property type="bool" key="showTitleBar">false</property>
          <property type="bool" key="resizable">false</property>
          <property type="double" key="height">110</property>
          <property type="double" key="width">290</property>
          <property type="double" key="z">1</property>

          <property type="string" key="state">floating</property>
          <anchors target="3D View">
            <line own="right" target="right"/>
            <line own="bottom" target="bottom"/>
          </anchors>
        </ignition-gui>

        <sim_time>true</sim_time>
        <real_time>true</real_time>
        <real_time_factor>true</real_time_factor>
        <iterations>true</iterations>
      </plugin>

      <!-- Inspector -->
      <plugin filename="ComponentInspector" name="Component inspector">
        <ignition-gui>
          <property type="string" key="state">docked_collapsed</property>
        </ignition-gui>
      </plugin>

      <!-- Entity tree -->
      <plugin filename="EntityTree" name="Entity tree">
        <ignition-gui>
          <property type="string" key="state">docked_collapsed</property>
        </ignition-gui>
      </plugin>

      <!-- Image Display Plugins for visualization -->
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>semantic/colored_map</topic>
      </plugin>
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>semantic/labels_map</topic>
      </plugin>
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>rgbd/image</topic>
      </plugin>
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>rgbd/depth_image</topic>
      </plugin>
    </gui>

    <light type="directional" name="sun">
      <cast_shadows>false</cast_shadows>
      <pose>0 0 20 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>0 0 -1</direction>
    </light>

    <!-- Camera instance -->
    <model name="camera">
      <pose>6 0 2.0 0 0.0 3.14</pose>
      <link name="link">
        <pose>0 0 0 0 0 0</pose>
        <inertial>
          <mass>0.0</mass>
          <inertia>
            <ixx>0.000</ixx>
            <iyy>0.000</iyy>
            <izz>0.000</izz>
          </inertia>
        </inertial>
        <collision name="collision">
          <geometry>
            <box>
              <size>0.1 0.1 0.1</size>
            </box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box>
              <size>0.1 0.1 0.1</size>
            </box>
          </geometry>
        </visual>

        <sensor name="rgbd_camera" type="rgbd_camera">
          <topic>rgbd</topic>
          <camera>
            <horizontal_fov>1.57</horizontal_fov>
            <image>
              <width>400</width>
              <height>300</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>100</far>
            </clip>
          </camera>
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
        </sensor>

        <sensor name="semantic_segmentation_camera" type="segmentation">
          <topic>semantic</topic>
          <camera>
            <segmentation_type>semantic</segmentation_type>
            <horizontal_fov>1.57</horizontal_fov>
            <image>
              <width>400</width>
              <height>300</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>100</far>
            </clip>
            <!-- uncomment these lines to save segmentation data -->
            <!--
            <save enabled="true">
              <path>segmentation_data/semantic_camera</path>
            </save>
            -->
          </camera>
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
        </sensor>
      </link>
    </model>

    <!-- Basic models of the scene -->
    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>
      </link>
    </model>

    <!-- Multiple shapnet models -->

    <!-- object 1 -->
    <include>
        <uri>model://models/{category[0]}/{model[0]}</uri>
        <name>model1</name>
        <pose>{x[0]} {y[0]} {z[0]} 1.570796 0 {yaw[0]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[0]}</label>
        </plugin>
    </include>

    <!-- object 2 -->
    <include>
        <uri>model://models/{category[1]}/{model[1]}</uri>
        <name>model2</name>
        <pose>{x[1]} {y[1]} {z[1]} 1.570796 0 {yaw[1]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[1]}</label>
        </plugin>
    </include>

    <!-- object 3 -->
    <include>
        <uri>model://models/{category[2]}/{model[2]}</uri>
        <name>model3</name>
        <pose>{x[2]} {y[2]} {z[2]} 1.570796 0 {yaw[2]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[2]}</label>
        </plugin>
    </include>

    <!-- object 4 -->
    <include>
        <uri>model://models/{category[3]}/{model[3]}</uri>
        <name>model4</name>
        <pose>{x[3]} {y[3]} {z[3]} 1.570796 0 {yaw[3]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[3]}</label>
        </plugin>
    </include>

    <!-- object 5 -->
    <include>
        <uri>model://models/{category[4]}/{model[4]}</uri>
        <name>model5</name>
        <pose>{x[4]} {y[4]} {z[4]} 1.570796 0 {yaw[4]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[4]}</label>
        </plugin>
    </include>

    <!-- object 6 -->
    <include>
        <uri>model://models/{category[5]}/{model[5]}</uri>
        <name>model6</name>
        <pose>{x[5]} {y[5]} {z[5]} 1.570796 0 {yaw[5]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[5]}</label>
        </plugin>
    </include>

    <!-- object 7 -->
    <include>
        <uri>model://models/{category[6]}/{model[6]}</uri>
        <name>model7</name>
        <pose>{x[6]} {y[6]} {z[6]} 1.570796 0 {yaw[6]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[6]}</label>
        </plugin>
    </include>
    
    <!-- object 8 -->
    <include>
        <uri>model://models/{category[7]}/{model[7]}</uri>
        <name>model8</name>
        <pose>{x[7]} {y[7]} {z[7]} 1.570796 0 {yaw[7]}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[7]}</label>
        </plugin>
    </include>

  </world>
</sdf>
"""
