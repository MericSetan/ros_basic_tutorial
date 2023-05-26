#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Bool

def callback_function(message):
    print("received message : ",message.data)

def Bool_subscriber_example():

    # start node
    rospy.init_node("Bool_subscriber_node")

    # create subscriber
    rospy.Subscriber('topic_name', Bool, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        Bool_subscriber_example()
    except rospy.ROSInterruptException:
        pass
