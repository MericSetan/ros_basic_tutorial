#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Time

def Time_publisher_example():

    # start node
    rospy.init_node("Time_Publisher")

    # create publisher object
    pub = rospy.Publisher("your_topic",Time,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    Time_message = Time()

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # define message
        Time_message.data = rospy.get_rostime()

        # publish message
        pub.publish(Time_message)

        # add delay
        rate.sleep()
    

if __name__ == '__main__':
    try:
        Time_publisher_example()
    except rospy.ROSInterruptException:
        pass
