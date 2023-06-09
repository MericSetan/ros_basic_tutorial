#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

def callback_function(message):
    print("received message : ",message.data)

def Int32_subscriber_example():

    # start node
    rospy.init_node("Int32_subscriber_node")

    # create subscriber
    rospy.Subscriber('topic_name', Int32, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        Int32_subscriber_example()
    except rospy.ROSInterruptException:
        pass
