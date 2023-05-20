#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

class PublisherClass():

    def __init__(self):

        # start node
        rospy.init_node("node_name")

        # create self publisher object
        self.pub = rospy.Publisher("your_topic",Int32,queue_size = 10) # topic_name, message_type, queue_size

        # create message
        self.message = Int32()

        # create rate to publish once per second 
        self.rate = rospy.Rate(1)  # 1 Hz 

    def publisher_function(self):

        # create loop to publish
        while not rospy.is_shutdown():

            for i in range(10):
                # define your message
                self.message = i

                # publish message
                self.pub.publish(self.message)
                
                # add delay
                self.rate.sleep()

        # kill node after a loop if you want
        #rospy.signal_shutdown("end the publisher")  

if __name__ == '__main__':
    try:
        object = PublisherClass()
        object.publisher_function()
    except rospy.ROSInterruptException:
        pass