# Reconstruction-with-a-camera-based-for-static-manipulator
This repository demonstrates UR5 move around with different texture model in Gazebo and ROS, then reconstructed in colmap. 

Installation
This project was tested in Ubuntu 18.04 with ROS Melodic, COLMAP-3.6-cuda. 
Make sure you have installed Python2.7 and some useful libraries/packages, such as Numpy, cv2, etc.in ROS.
Install ROS Melodic, Gazebo, RViz, Moveit, official universal robot.
Link for universal robot: universal_robots - ROS Wiki
Link for COLMAP Installation: Installation — COLMAP 3.7 documentation

Install this repository from Source
First set up a catkin workspace (see this tutorials).
Then clone the repository into the src/ folder. It should look like /path/to/your/catkin_ws/… 
Make sure to source the correct setup file according to your workspace hierarchy, then use catkin_make to compile.

Download official universal robot to workspace, universal_robots - ROS Wiki
Assuming your official universal robot folder is ~/catkin_ws, you should use the following commands:
$ cd ~/catkin_ws/src
$ git clone https://github.com/Natsuw/Reconstruction-with-a-camera-based-for-static-manipulator.git
$ cd ..
$ catkin_make
$ source devel/setup.bash

Under catkin_ws/src there are four folders. Two for image saver(xxx_image_saver)
One is the official universal_robot, and the other is ur5_go_pkg.

Replace and Change Files 
Opefile ur5_joint_limited_robot.urdf.xacro under ur_ws/src/universal_robot/ur_description/urdf/, and make the following change to the joint limit:
  shoulder_pan_lower_limit="${-2*pi}" shoulder_pan_upper_limit="${2*pi}"

Under directory catkin_ws/src/ur5_go_pkg/src, there are two folders which are launch and worlds, copy and paste to catkin_ws/src/universal_robot/ur_gazebo

Build the code under directory catkin_ws/
$ catkin_make
$ source devel/setup.bash 

Run the code with ROS and Gazebo 
For the BLOCK model
# launch Gazebo with UR5 and block model 
$ roslaunch ur_gazebo view_test_ur5.launch 
# launch Moveit 
$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
# The main file for UR5 run
$ rosrun ur5_go_pkg moveit_block_demo.py
# Save image in ur5_image_save
$ rosrun ur5_go_pkg block_vision.py

# Code are not using, only for testing
roslaunch ur5_moveit_config moveit_rviz.launch config:=true (not using, show in moveit)
rqt_image_view (not using, image view) 

For the Beer model
$ roslaunch ur_gazebo view_beer_ur5.launch 
$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
$ rosrun ur5_go_pkg moveit_beer.py
$ rosrun ur5_go_pkg beer_vision.py

