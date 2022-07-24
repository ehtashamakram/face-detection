#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge

face_cascade = cv2.CascadeClassifier('/home/roboticshub/catkin_ws/src/robot/robot_sims/scripts/cascade_frontalface_default.xml')

def image_callback(msg):
    bridge = cv_bridge.CvBridge()
    cv2.namedWindow("camera", 1)
    img = bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # read the input image to detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:       
        # draw a rectangle whenever a face is detected
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imwrite('/home/roboticshub/catkin_ws/src/robot/robot_sims/images/image.png',img)

    cv2.imshow("camera", img)
    cv2.waitKey(3)

# Get a move_base action client
rospy.init_node('face_detection')
image_sub = rospy.Subscriber('/camera/image',Image, image_callback)
rospy.spin()