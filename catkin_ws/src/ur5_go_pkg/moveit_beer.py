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
        self.default_joint_states = [-2.39110, -1.082104, 2.216568, -1.46607, -0.76794, 3.368485]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)


        # 2 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.356194, -1.431169, 2.28638, -1.65806, -0.855211, 3.700098]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
     	rospy.sleep(0.1)


        # 3 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.00713, -1.23918, 1.884955, -1.41371, -1.18682, 3.473205]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 4 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.024582, -0.80285, 1.710423, -1.01229, -1.099557, 3.176499]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 5 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.64060, -0.62832, 1.36135, -0.80285, -1.71042, 3.141593]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 6 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.18682, -0.85521, 1.727876, -1.16937, -2.28638, 2.914699]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 7 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.57079, -1.727876, 2.1816615, -1.954768, -1.605702, 1.53589]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 8 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-0.73303, -1.16937, 2.757620, -3.281218, -2.757620, 1.39626]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)


        # 9 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.024581, -2.338741, -2.775073, -2.600540, -1.204277, -0.26179]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)



        # 10 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-1.780235, -2.426007, 2.670353, -2.53073, -1.4486, -0.13963]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 9.5 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.98451, -1.186823,  2.705260, -1.623156, -0.488692, -3.106686]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 10 chushidian设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.705260, -1.04719, 2.356194, -1.27409, -0.64577, -3.141593]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

        # 10a 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.58308, -1.76278, 2.391101, -1.6057029, -0.83776, -2.30383]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)

	# 1 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        # Specify default (idle) joint states (unit: (radians))
        self.default_joint_states = [-2.39110, -1.082104, 2.216568, -1.46607, -0.76794, -2.9146998]
        self.arm.set_joint_value_target(self.default_joint_states)
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(0.1)






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
