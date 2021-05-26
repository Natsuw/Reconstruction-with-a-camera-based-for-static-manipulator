#! /usr/bin/python
#encoding:utf-8

# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()

cam0_path  = '/home/sky/catkin_ws/src/beer_image_saver/'    # image saver path

 
def callback(data):
    # define picture to_down' coefficient of ratio
    scaling_factor = 0.5
    global count,bridge
    count = count + 1
    if count == 1:
        count = 0
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
	rospy.sleep(0.2) #save image every 0.2 second

        timestr = "%.2f" % data.header.stamp.to_sec()
              #%.6f represent 6 deciaml places behind the decimal point  "%.2f" %  data.header.stamp.to_sec()；
        image_name = timestr+ ".jpg"
	 #image name : time duration.jpg
        cv2.imwrite(cam0_path + image_name, cv_img)  #save images；

           
        
	cv2.imshow("beer vision" , cv_img)
        cv2.waitKey(1)
    else:
        pass
 
def displayWebcam():
    rospy.init_node('webcam_display', anonymous=True)
 
    # make a video_object and init the video object
    global count,bridge
    count = 0
    bridge = CvBridge()
    rospy.Subscriber('/ur5/usbcam/image_raw', Image, callback)
    rospy.spin()
 
if __name__ == '__main__':
    displayWebcam()
