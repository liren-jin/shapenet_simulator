SCENE_SDF_TEMPLATE = """
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

    <physics type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>0</real_time_update_rate>
      <ode>
        <solver>
            <type>quick</type>
            <iters>50</iters>
        </solver>
        <constraints>
          <contact_max_correcting_vel>1</contact_max_correcting_vel>
        </constraints>
      </ode>
    </physics>

    <scene>
      <ambient>{ambient_light[0]} {ambient_light[1]} {ambient_light[2]} 1</ambient>
      <background>{background_color[0]} {background_color[1]} {background_color[2]} 1</background>
      <shadows>false</shadows>
    </scene>
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
        <ambient_light>{ambient_light[0]} {ambient_light[1]} {ambient_light[2]}</ambient_light>
        <background_color>{background_color[0]} {background_color[1]} {background_color[2]}</background_color>
        <camera_pose>-6 0 6 0 0.5 0</camera_pose>
      </plugin>

      <!-- Plugins that add functionality to the scene -->
      <!--plugin filename="EntityContextMenuPlugin" name="Entity context menu">
        <ignition-gui>
          <property key="state" type="string">floating</property>
          <property key="width" type="double">5</property>
          <property key="height" type="double">5</property>
          <property key="showTitleBar" type="bool">false</property>
        </ignition-gui>
      </plugin-->
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
      <!--plugin filename="EntityTree" name="Entity tree">
        <ignition-gui>
          <property type="string" key="state">docked_collapsed</property>
        </ignition-gui>
      </plugin-->

      <!-- Image Display Plugins for visualization -->
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>{semantic_topic}/colored_map</topic>
      </plugin>
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>{rgbd_topic}/image</topic>
      </plugin>
      <plugin filename="ImageDisplay" name="Image Display">
        <ignition-gui>
        </ignition-gui>
        <topic>{rgbd_topic}/depth_image</topic>
      </plugin>
    </gui>

    <light type="directional" name="sun">
      <cast_shadows>false</cast_shadows>
      <pose>0 0 20 0 0 0</pose>
      <diffuse>0.9 0.9 0.9 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
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
      <static>true</static>
      <pose>2 0 1.0 0 0.0 3.14</pose>
      <link name="link">
        <pose>0 0 0 0 0 0</pose>
        <inertial>
          <mass>1.0</mass>
          <inertia>
            <ixx>1.000</ixx>
            <iyy>1.000</iyy>
            <izz>1.000</izz>
          </inertia>
        </inertial>
        <collision name="collision">
          <geometry>
            <box>
              <size>0.05 0.1 0.1</size>
            </box>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <box>
              <size>0.05 0.1 0.1</size>
            </box>
          </geometry>
        </visual>

        <sensor name="rgbd_camera" type="rgbd_camera">
          <topic>{rgbd_topic}</topic>
          <camera>
            <horizontal_fov>{fov[0]}</horizontal_fov>
            <vertical_fov>{fov[1]}</vertical_fov>
            <image>
              <width>{resolution[0]}</width>
              <height>{resolution[1]}</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>20</far>
            </clip>
            <lens>
              <intrinsics>
                <fx>{focal[0]}</fx>
                <fy>{focal[1]}</fy>
                <cx>{c[0]}</cx>
                <cy>{c[1]}</cy>
                <s>0</s>
              </intrinsics>
            </lens>
          </camera>
          <always_on>1</always_on>
          <update_rate>{update_rate}</update_rate>
          <visualize>true</visualize>
        </sensor>

        <sensor name="semantic_segmentation_camera" type="segmentation">
          <topic>{semantic_topic}</topic>
          <camera>
            <segmentation_type>semantic</segmentation_type>
            <horizontal_fov>{fov[0]}</horizontal_fov>
            <vertical_fov>{fov[1]}</vertical_fov>
            <image>
              <width>{resolution[0]}</width>
              <height>{resolution[1]}</height>
            </image>
            <clip>
              <near>0.1</near>
              <far>20</far>
            </clip>
          </camera>
          <always_on>1</always_on>
          <update_rate>{update_rate}</update_rate>
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
        <!--visual name="visual">
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
        </visual-->
      </link>
    </model>

    <gravity>0.0 0.0 -15.0</gravity>
  </world>
</sdf>
"""
