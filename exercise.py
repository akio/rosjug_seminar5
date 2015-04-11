#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def current_goal_callback(msg):
    pass

rospy.init_node('excesize')

goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1, latch=True)

goal = PoseStamped()
goal.header.seq = 0
goal.header.frame_id = 'world'
goal.header.stamp = rospy.Time.now() #+ rospy.Duration(5, 0)
goal.pose.position.x = 3.5
goal.pose.position.y = 3.5
goal.pose.position.z = 0.0
goal.pose.orientation.x = 0.0
goal.pose.orientation.y = 0.0
goal.pose.orientation.z = 0.0
goal.pose.orientation.w = 1.0

goal_pub.publish(goal)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
