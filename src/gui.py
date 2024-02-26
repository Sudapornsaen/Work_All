#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
canvas = Canvas(frame, width=200, height=200)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
def lt():
	print("lt")
	cmd = Twist()
	cmd.linear.y = 0.5
	cmd.angular.z= 0.0
	pub.publish(cmd)
def rt():
	print("rt")
	cmd = Twist()
	cmd.linear.y = -1.5
	cmd.angular.z= 0.0
	pub.publish(cmd)
def ll():
	print("ll")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= 1
	pub.publish(cmd)
def rr():
	print("rr")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= -1
	pub.publish(cmd)
def reset():
	rospy.wait_for_service("reset")
	test_bg = rospy.ServiceProxy("reset", Empty)
	test_bg()
	
		
B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

B5 = Button(text = "LL", command=ll)
B5.place(x=200, y=80)

B6 = Button(text = "RR", command=rr)
B6.place(x=300, y=80)

B7 = Button(text = "Reset", command=reset)
B7.place(x=240, y=80)


frame.mainloop()
