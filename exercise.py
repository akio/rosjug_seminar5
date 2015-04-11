#!/usr/bin/env python
# vim: fileencoding=utf-8

# rospy
import rospy
import math
from geometry_msgs.msg import Quaternion, PoseStamped
from tf.transformations import quaternion_from_euler

# 
rospy.init_node('excesize')

#
goal_pub = rospy.Publisher('/move_base_simple/goal',
                           PoseStamped,
                           queue_size=1,
                           latch=True)

goal = PoseStamped()
goal.header.frame_id = 'world'
goal.header.stamp = rospy.Time.now()
goal.pose.position.x = 3.5
goal.pose.position.y = 3.5
goal.pose.position.z = 0.0
q = quaternion_from_euler(0, 0, math.radians(90))
goal.pose.orientation = Quaternion(*q)

goal_pub.publish(goal)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
