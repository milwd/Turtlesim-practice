#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool


if __name__ == '__main__':
	rospy.init_node('kids_node')
	
	rospy.wait_for_service('spawn')
	try:
		spawner = rospy.ServiceProxy('spawn', Spawn)
		spawner(2., 2., 0., 'turtle2')
	except Exception as e:
		raise Exception("COULD NOT CREATE TURTLE 2!")
	rospy.loginfo("turtle2 locked and loaded")
	
	
	t1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	t2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	t_pub  = rospy.Publisher('name', Bool, queue_size=5)
	
	while not rospy.is_shutdown():
		try:
			t, vx, vy, ang = input('ENTER INPUT (turtle1/2 lin_x lin_y ang): ').split()
		except Exception as e:
			raise Exception("THE PROGRAM NEEDS 3 VALUES FOR NAME X Y.")
		if not (t == 'turtle1' or t == 'turtle2'):
			raise Exception("NAME SHOULD BE turtle1 OR turtle2!")
		t_pub.publish(Bool(False) if t == 'turtle1' else Bool(True)) 
		
		motion = Twist()
		motion.linear.x, motion.linear.y, motion.angular.z = float(vx), float(vy), float(ang)
		t1_pub.publish(motion) if t == 'turtle1' else t2_pub.publish(motion)
		rospy.sleep(1)
		
		motion = Twist()
		t1_pub.publish(motion)
		t2_pub.publish(motion)
		
	print('happy ROSing')
