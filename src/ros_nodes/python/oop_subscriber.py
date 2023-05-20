#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

class SubscriberNode:

    def __init__(self):
        # start node
        rospy.init_node('node_name', anonymous=True)

        # create publisher
        rospy.Subscriber('topic_name', Int32, self.callback_function)

        # interaction and listening loop 
        rospy.spin()

    def callback_function(self, message):
        # run this command in the console to test : rostopic  pub /topic_name std_msgs/Int32 "data: 24" 

        # write log and console 
        rospy.loginfo("received message is : %s", message.data)

        #print("received message : ",message.data)


if __name__ == '__main__':
    try:
        object = SubscriberNode()
    except rospy.ROSInterruptException:
        pass