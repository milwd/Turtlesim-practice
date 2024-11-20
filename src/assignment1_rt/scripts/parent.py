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
	
def t_n_cb(p):
	global name
	name = 'turtle1' if p == Bool(False) else 'turtle2'
	
def t1_s_cb(p):
	global tls
	tls = p

def check_stuck(t):
	return t.x > 9 or t.x < 1 or t.y > 9 or t.y < 1

def check_distance(t1, t2):
	global dist_pub
	distance = math.sqrt((t1.x - t2.x) ** 2 + (t1.y - t2.y) ** 2)
	dist_pub.publish(distance)
	return distance < 1.2
	
def go_back(turtle):
	global t1, t2, tls, t1_pub, t2_pub
	tls.linear.x, tls.linear.y = -1.*tls.linear.x, -1.*tls.linear.y
	if turtle == 'turtle1':
		#print("im here 1")
		t1_pub.publish(tls)
		while check_stuck(t1): 
			continue
		else:
			motion = Twist()
			t1_pub.publish(motion)
	elif turtle == 'turtle2':
		#print("im here 2")
		t2_pub.publish(tls)
		while check_stuck(t2): 
			continue
		else:
			motion = Twist()
			t2_pub.publish(motion)
			
def get_far(turtle):
	global t1, t2, tls, t1_pub, t2_pub
	tls.linear.x, tls.linear.y = -1.*tls.linear.x, -1.*tls.linear.y
	if turtle == 'turtle1':
		t1_pub.publish(tls)
		while check_distance(t1, t2): 
			continue
		else:
			motion = Twist()
			t1_pub.publish(motion)
	elif turtle == 'turtle2':
		t2_pub.publish(tls)
		while check_distance(t1, t2): 
			continue
		else:
			motion = Twist()
			t2_pub.publish(motion)


if __name__ == '__main__':
	t1, t2, tls, name = None, None, None, None
	
	rospy.init_node('parent_node')
	
	t1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	t2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('/turtle1/pose', Pose, t1_cb) 
	rospy.Subscriber('/turtle2/pose', Pose, t2_cb) 
	rospy.Subscriber('/turtle1/cmd_vel', Twist, t1_s_cb)
	rospy.Subscriber('/turtle2/cmd_vel', Twist, t1_s_cb)
	rospy.Subscriber('name', Bool, t_n_cb)
	dist_pub = rospy.Publisher('distance', Float32, queue_size=10)
	
	while not rospy.is_shutdown():
		if t1 and t2:
			stuck1 = check_stuck(t1)
			stuck2 = check_stuck(t2)
			distck = check_distance(t1, t2)
			
			if stuck1 or stuck2:
				rospy.loginfo(name + ', Come back. You will get lost!')
				go_back(name)
			if distck:
				rospy.loginfo('What about social distancing then ...')
				get_far(name)
	print("Good game!")
	
