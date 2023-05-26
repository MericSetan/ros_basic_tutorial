#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import String

def callback_function(message):
    print("received message : ",message.data)

def String_subscriber_example():

    # start node
    rospy.init_node("String_subscriber_node")

    # create subscriber
    rospy.Subscriber('topic_name', String, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        String_subscriber_example()
    except rospy.ROSInterruptException:
        pass
