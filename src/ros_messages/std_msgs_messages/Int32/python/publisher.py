#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

def int32_publisher_example():

    # start node
    rospy.init_node("Float32_Publisher")

    # create publisher object
    pub = rospy.Publisher("your_topic",Int32,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    Int32_message = Int32()

    # define message
    Int32_message.data = 6

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(Int32_message)

        # add delay
        rate.sleep()
    


if __name__ == '__main__':
    try:
        int32_publisher_example()
    except rospy.ROSInterruptException:
        pass
