#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def run(val):
	if val.data == "hi":
		rospy.loginfo("Node: "+"Sawaddee")
	else:
		rospy.loginfo("Node2: "+"Yaa")

if __name__ == "__main__":
	sub = rospy.Subscriber("chatter",String,callback=run)
	rospy.init_node("Listener")
	rospy.spin()
