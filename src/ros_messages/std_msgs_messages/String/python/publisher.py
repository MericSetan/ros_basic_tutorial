#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import String

def string_publisher_example():

    # start node
    rospy.init_node("String_Publisher")

    # create publisher object
    pub = rospy.Publisher("your_topic",String,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    String_message = String()

    # define message
    String_message.data = "Hello World"

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(String_message)

        # add delay
        rate.sleep()
    


    
if __name__ == '__main__':
    try:
        string_publisher_example()
    except rospy.ROSInterruptException:
        pass
