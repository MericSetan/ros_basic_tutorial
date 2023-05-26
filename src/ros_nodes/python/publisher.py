#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

def publisher_example():

    # start node
    rospy.init_node("my_publisher_node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Int32,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    message = Int32()

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        for i in range(10):
            # define your message
            message.data = i

            # publish message
            pub.publish(message)
            
            # add delay
            rate.sleep()

        # kill node after a loop if you want
        #rospy.signal_shutdown("end the publisher")   
            
if __name__ == '__main__':
    try:
        publisher_example()
    except rospy.ROSInterruptException:
        pass
