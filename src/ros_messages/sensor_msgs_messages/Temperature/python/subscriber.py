#!/usr/bin/env python3

#import rospy and messages
import rospy
from sensor_msgs.msg import Temperature

def callback_function(message):

    print("received message : ",message)
    print("received temperature : ",message.temperature)

    # also youu can print
    # message.variance
    # message.header.stamp
    # message.header.frame_id
    # message.header.seq

def subscriber_example():

    # start node
    rospy.init_node("Temperature_Subscriber_Node")

    # create subscriber
    rospy.Subscriber('topic_name', Temperature, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        subscriber_example()
    except rospy.ROSInterruptException:
        pass
