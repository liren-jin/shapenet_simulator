SDF_TEMPLATE = """
<?xml version="1.0" ?>
    <sdf version="1.6">
        <!-- object 1 -->
        <include>
            <uri>model://models/{category[0]}/{model[0]}</uri>
            <pose>{x[0]} {y[0]} {z[0]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[0]}</label>
        </plugin>
        </include>

        <!-- object 2 -->
        <include>
            <uri>model://models/{category[1]}/{model[1]}</uri>
            <pose>{x[1]} {y[1]} {z[1]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[1]}</label>
        </plugin>
        </include>

        <!-- object 3 -->
        <include>
            <uri>model://models/{category[2]}/{model[2]}</uri>
            <pose>{x[2]} {y[2]} {z[2]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[2]}</label>
        </plugin>
        </include>

        <!-- object 4 -->
        <include>
            <uri>model://models/{category[3]}/{model[3]}</uri>
            <pose>{x[3]} {y[3]} {z[3]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[3]}</label>
        </plugin>
        </include>

        <!-- object 5 -->
        <include>
            <uri>model://models/{category[4]}/{model[4]}</uri>
            <pose>{x[4]} {y[4]} {z[4]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[4]}</label>
        </plugin>
        </include>
        
        <!-- object 6 -->
        <include>
            <uri>model://models/{category[4]}/{model[4]}</uri>
            <pose>{x[5]} {y[5]} {z[5]} 1.570796 0 -1.570796</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label[5]}</label>
        </plugin>
        </include>
    </sdf>
"""
