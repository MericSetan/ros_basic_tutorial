#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32

def callback_function(message):
    # run this command in the console to test : rostopic  pub /topic_name std_msgs/Int32 "data: 24" 

    # write log and console 
    rospy.loginfo(" received message : %d ",message.data)

    #print("received message : ",message.data)

def subscriber_example():

    # start node
    rospy.init_node("my_subscriber_node")

    # create subscriber
    rospy.Subscriber('topic_name', Int32, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        subscriber_example()
    except rospy.ROSInterruptException:
        pass
