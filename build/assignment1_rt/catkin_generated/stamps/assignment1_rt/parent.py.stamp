#!/usr/bin/env python3

import rospy 
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math


def t1_cb(p):
	global t1
	t1 = p
	
def t2_cb(p):
	global t2
	t2 = p
	
def t1_s_cb(p):
	global tls
	print("CALLBACL E TLS")
	tls = p


if __name__ == '__main__':
	t1, t2, stuck = None, None, False
	tls = Twist()

	rospy.init_node('parent_node')
	
	t1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	t2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	
	stuck_notifier = rospy.Publisher('is_stuck', Bool, queue_size=4)
	rospy.Subscriber('/turtle1/pose', Pose, t1_cb) 
	rospy.Subscriber('/turtle2/pose', Pose, t2_cb) 
	rospy.Subscriber('/turtle1/cmd_vel', Twist, t1_s_cb)
	#rate = rospy.Rate(1000) 
	while not rospy.is_shutdown():
		if t1 and t2:
			distance = math.sqrt((t1.x - t2.x) ** 2 + (t1.y - t2.y) ** 2)
			stuck1, stuck2 = False, False
			if t1.x > 9 or t1.x < 1 or t1.y > 9 or t1.y < 1:
				tls.linear.x, tls.linear.y = -1.*tls.linear.x, -1.*tls.linear.y
				stuck1 = True
			if t2.x > 9 or t2.x < 1 or t2.y > 9 or t2.y < 1:
				stuck2 = True
			if stuck1:
				#motion = Twist()
				print("TLS:", tls)
				t1_pub.publish(tls)
				rospy.sleep(1)
			
			
			if stuck2:
				motion = Twist()
				t2_pub.publish(motion)
			stuck_notifier.publish(stuck1)
			
			if distance < 1.4:
				rospy.loginfo('What about social distancing then ...')
				t1_pub.publish(Twist())
				t2_pub.publish(Twist())
		#rate.sleep()
			
	
