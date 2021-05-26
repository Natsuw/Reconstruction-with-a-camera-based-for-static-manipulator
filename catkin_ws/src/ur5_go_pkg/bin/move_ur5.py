#!/usr/bin/env python

import rospy, sys, numpy as np
import moveit_commander
from copy import deepcopy
from geometry_msgs.msg import Twist
import moveit_msgs.msg
from sensor_msgs.msg import Image
from ur5_notebook.msg import Tracker
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from time import sleep
tracker = Tracker()



class ur5_mp:
    def __init__(self, reset=False):
        rospy.init_node("move_ur5", anonymous=False)

        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the move group for the ur5_arm
        self.arm = moveit_commander.MoveGroupCommander('manipulator')

        # Get the name of the end-effector link
        self.end_effector_link = self.arm.get_end_effector_link()

        # Set the reference frame for pose targets
        reference_frame = "base_link"

        # Set the ur5_arm reference frame accordingly
        self.arm.set_pose_reference_frame(reference_frame)

        # Allow replanning to increase the odds of a solution
        self.arm.allow_replanning(True)

        # Allow some leeway in position (meters) and orientation (radians)
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)
        self.arm.set_planning_time(0.1)
        self.arm.set_max_acceleration_scaling_factor(.5)
        self.arm.set_max_velocity_scaling_factor(.5)
        
        if(not reset):
            return
        # Get the current pose so we can add it as a waypoint

        # Specify default (idle) joint states
        self.default_joint_states = self.arm.get_current_joint_values()
        self.default_joint_states[0] = -1.57691
        self.default_joint_states[1] = -1.71667
        self.default_joint_states[2] = 1.79266
        self.default_joint_states[3] = -1.67721
        self.default_joint_states[4] = -1.5705
        self.default_joint_states[5] = 0.0

        self.arm.set_joint_value_target(self.default_joint_states)

        # Set the internal state to the current state
        self.arm.set_start_state_to_current_state()
        plan = self.arm.plan()

        self.arm.execute(plan)


    def execute(self, x,y,z):
        # Get the current pose so we can add it as a waypoint
        start_pose = self.arm.get_current_pose(self.end_effector_link).pose

        # Initialize the waypoints list
        self.waypoints= []
        self.pointx = []
        self.pointy = []
        # Set the first waypoint to be the starting pose
        # Append the pose to the waypoints list
        wpose = deepcopy(start_pose)

        # Set the next waypoint to the right 0.5 meters

        wpose.position.x = x
        wpose.position.y = y
        wpose.position.z = z

        wpose.orientation.x = 0.4811
        wpose.orientation.y = 0.4994
        wpose.orientation.z = -0.5121
        wpose.orientation.w = 0.5069

        self.pointx.append(wpose.position.x)
        self.pointy.append(wpose.position.y)
        self.waypoints.append(deepcopy(wpose))
        # Set the internal state to the current state
        # self.arm.set_pose_target(wpose)

        self.arm.set_start_state_to_current_state()

        # Plan the Cartesian path connecting the waypoints

        plan, fraction = self.arm.compute_cartesian_path(self.waypoints, 0.01, 0.0, True)


        # plan = self.arm.plan()

        # If we have a complete plan, execute the trajectory
        if 1-fraction < 0.2:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            num_pts = len(plan.joint_trajectory.points)
            rospy.loginfo("\n# intermediate waypoints = "+str(num_pts))
            self.arm.execute(plan)
            rospy.loginfo("Path execution complete.")
        else:
            rospy.loginfo("Path planning failed")
    # print self.points

def main(argv):
    print(len(argv), argv)
    if(len(argv) < 4):
        mp=ur5_mp(True)
        mp.execute(0.1,-0.4,0.4)
    else:
        mp=ur5_mp(False)
        mp.execute(float(argv[1]), float(argv[2]),float(argv[3]))


main(sys.argv)
