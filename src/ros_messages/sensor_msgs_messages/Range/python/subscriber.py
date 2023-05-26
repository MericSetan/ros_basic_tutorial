#!/usr/bin/env python3

#import rospy and messages
import rospy
from sensor_msgs.msg import Range

def callback_function(message):

    print("received message : ",message)
    print("received distance : ",message.range)

    # also you can print

    # message.header.frame_id
    # message.header.stamp
    # message.radiation_type
    # message.field_of_view 
    # message.min_range
    # message.max_range
    

def Range_subscriber_example():

    # start node
    rospy.init_node("Range_Subscriber_Node")

    # create subscriber
    rospy.Subscriber('topic_name', Range, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        Range_subscriber_example()
    except rospy.ROSInterruptException:
        pass
