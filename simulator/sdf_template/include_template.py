INCLUDE_TEMPLATE = """
    <!-- object {index} -->
    <include>
        <uri>model://models/{category}/{model}</uri>
        <name>model{index}</name>
        <pose>{x} {y} {z} 1.570796 0 {yaw}</pose>
        <plugin filename="ignition-gazebo-label-system" name="ignition::gazebo::systems::Label">
            <label>{label}</label>
        </plugin>
    </include>
"""
