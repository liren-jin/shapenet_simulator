#include <iostream>
#include <string>
#include <ignition/msgs.hh>
#include <ignition/transport.hh>
#include <ros/ros.h>
#include <geometry_msgs/Pose.h>

class CameraController
{
public:
    CameraController()
    {
        ros_sub_ = ros_node_.subscribe("set_camera_pose", 1, &CameraController::pose_callback, this);
    }

    void pose_callback(const geometry_msgs::Pose::ConstPtr &msg)
    {
        ignition::msgs::Pose req;

        ignition::msgs::Vector3d position;
        position.set_x(msg->position.x);
        position.set_y(msg->position.y);
        position.set_z(msg->position.z);

        ignition::msgs::Quaternion orientation;
        orientation.set_w(msg->orientation.w);
        orientation.set_x(msg->orientation.x);
        orientation.set_y(msg->orientation.y);
        orientation.set_z(msg->orientation.z);

        std::string model_name = "camera";

        req.mutable_name()->assign(model_name);
        req.mutable_position()->CopyFrom(position);
        req.mutable_orientation()->CopyFrom(orientation);

        ignition::msgs::Boolean rep;
        bool result;
        unsigned int timeout = 300;
        bool executed = gazebo_node_.Request("/world/scene_base/set_pose", req, timeout, rep, result);
        if (executed)
        {
            if (result)

                std::cout << "Move camera to desired pose: "
                          << "position[" << req.position().x() << ","
                          << req.position().y() << ","
                          << req.position().z() << "], "
                          << "orientation[" << req.orientation().w() << ","
                          << req.orientation().x() << ","
                          << req.orientation().y() << ","
                          << req.orientation().z() << "]" << std::endl;
            else
                std::cout << "Service call failed" << std::endl;
        }
        else
            std::cerr << "Service call timed out" << std::endl;
    }

private:
    ros::NodeHandle ros_node_;
    ros::Subscriber ros_sub_;
    ignition::transport::Node gazebo_node_;
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "camera_controller");
    CameraController camera_controller;
    ros::spin();
    return 0;
}