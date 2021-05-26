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
        rospy.sleep(0.1)
        

        # 1 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.02974, -0.68067, 1.04719, -0.90757, -2.04203, 2.87979]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)




        # 2 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.48352, -0.78539, 0.90757, -0.8377, -1.57079, 3.29867]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 3 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.71042, -0.78539, 0.90757, -0.83775, -1.58824, 3.29867]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)



        # 4 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.93731, -0.78539, 0.90757, -0.83775, -1.58824, 3.29867]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 5 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-2.565634, -1.151917, 1.745329, -1.23918, -0.802851, 3.473205]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 6 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-3.228859, -1.32645, 2.25147, -1.06465, -0.68067, 3.36848]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)

        # 06a （左边末端）设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-3.124139, -1.151917, 2.68781, -1.815142, -0.59341, 3.4033920]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 0000 default position设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.69296, -1.69296, 1.518436, 1.448623, 1.5707963, 3.001966]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 7 正中央位置 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.518436, -2.513274, 2.513274, 0.54105, 1.710422, 3.19395]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)




        # 07a 贴地 右边底部起始 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-0.71558, -0.76794, 2.321288, -3.10668, 3.316125, 1.58825]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.5)


        # 07b 右边zhong 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-0.71558, -1.151917, 2.356194, -2.75762, 3.577924, 1.57079]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)



        # 88888 右边 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-0.855211, -0.69813, 1.25664, -0.95993, 3.944444, 2.84488]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)



        # 1a 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.396263, -0.62832, 0.994837, -1.06465, 4.69493, 3.193952]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 2a 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.83259, -0.54105, 0.80285, -0.90757, 4.642575, 2.914699]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)


        # 3a 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-2.33874, -0.488692, 0.942477, -0.59341, 5.166174, 3.07178]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)

        # final 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-2.74016, -0.82030, 1.762782, -0.977384, 5.550147, 3.1764992]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)

        # final02 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-3.10668, -1.60570, 2.391101, -1.378810, 5.53269, 3.682645]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.2)

        # 0000 default position设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.default_joint_states = [-1.69296, -1.69296, 1.518436, 1.448623, 1.5707963, 3.001966]
        self.arm.set_joint_value_target(self.default_joint_states)
	
	# 控制机械臂完成运动
      #  self.arm.go()
     #   rospy.sleep(0.2)



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
