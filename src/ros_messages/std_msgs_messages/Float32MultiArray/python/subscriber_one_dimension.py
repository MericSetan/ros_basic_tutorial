#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Float32MultiArray

def callback_function(message):
    print("received message : ",message.data)

def Float32MultiArray_subscriber_example():

    # start node
    rospy.init_node("Float32MultiArray_Subscriber_Node")

    # create subscriber
    rospy.Subscriber('topic_name', Float32MultiArray, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        Float32MultiArray_subscriber_example()
    except rospy.ROSInterruptException:
        pass
