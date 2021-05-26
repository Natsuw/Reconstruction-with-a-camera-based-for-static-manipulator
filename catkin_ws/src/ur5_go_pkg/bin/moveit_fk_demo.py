#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019 Wuhan PS-Micro Technology Co., Itd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy, sys
import moveit_commander

from copy import deepcopy
from geometry_msgs.msg import Twist
import moveit_msgs.msg
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from time import sleep



class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
	# Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
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

        
        # 设置机械臂运动的允许误差值
        # Allow some leeway in position (meters) and orientation (radians)
        self.arm.set_goal_joint_tolerance(0.001)

        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)
        self.arm.set_planning_time(0.1)


        # 设置允许的最大速度和加速度 max and min speed
        self.arm.set_max_acceleration_scaling_factor(0.5)
        self.arm.set_max_velocity_scaling_factor(0.5)
        
        # 控制机械臂先回到初始化位置
        self.arm.set_named_target('home')
        self.arm.go()
        rospy.sleep(1)
        

        # 1 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-0.87266, -0.87266, 1.623156, -0.122173, 2.07694, 3.17649]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(1)


        # 2 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.46607, -0.48869, 0.73303, 1.76278, 1.51843, 3.28121]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(1)

        # 3 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-2.14675, -0.2967, 0.68067, 1.65806, 1.29154,  0.03490]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(1)


        # 4 default position设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.57691, -1.71667, 1.79266, -1.67721, -1.5705, 0.0]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(2)


        # Set the internal state to the current state
	# 把初始位置换位default joint state的位置
       # self.arm.set_start_state_to_current_state()
      #  plan = self.arm.plan()
       # self.arm.execute(plan)

        # Get the current pose so we can add it as a waypoint
       # start_pose = self.arm.get_current_pose(self.end_effector_link).pose


        # Stop any current arm movement
        self.arm.stop()



        # 5 控制机械臂先回到初始化位置
       # self.arm.set_named_target('home')
       # self.arm.go()
       # rospy.sleep(1)
        
        # 关闭并退出moveit
        #Shut down MoveIt! cleanly
        rospy.loginfo("Shutting down Moveit!")
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
