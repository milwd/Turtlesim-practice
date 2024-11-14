#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist


if __name__ == '__main__':
	rospy.init_node('kids_node')
	
	rospy.wait_for_service('spawn')
	try:
		spawner = rospy.ServiceProxy('spawn', Spawn)
		spawner(1., 1., 0., 'turtle2')
	except Exception as e:
		raise Exception("COULD NOT CREATE TURTLE 2!")
	rospy.loginfo("turtle2 locked and loaded")
	
	rate = rospy.Rate(1)
	print("rate:", rate)
	
	t1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	t2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	
	while not rospy.is_shutdown():
		usr_input = input('enter inp').split()
		t, vx, vy = usr_input
		motion = Twist()
		motion.linear.x, motion.linear.y = float(vx), float(vy)
		
		t1_pub.publish(motion) if t == 'turtle1' else t2_pub.publish(motion)
		
		rospy.sleep(1)
		
		motion = Twist()
		t1_pub.publish(motion)
		t2_pub.publish(motion)	
		
	print('happy rosing')
