#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Bool

def bool_publisher_example():

    # start node
    rospy.init_node("Bool_Publisher")

    # create publisher object
    pub = rospy.Publisher("your_topic",Bool,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    bool_message = Bool()

    # define message
    bool_message.data = True

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(bool_message)

        # add delay
        rate.sleep()
    


    
if __name__ == '__main__':
    try:
        bool_publisher_example()
    except rospy.ROSInterruptException:
        pass
