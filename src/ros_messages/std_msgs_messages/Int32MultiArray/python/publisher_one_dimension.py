#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32MultiArray

def Int32MultiArray_publisher_example():

    # start node
    rospy.init_node("Int32MultiArray_Publisher_Node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Int32MultiArray,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    Int32MultiArray_message = Int32MultiArray()

    # define message
    Int32MultiArray_message.data = [1,2,3]

    """
    if you want to publish multi-dim array like [[1,2,3],[4,5,6]]. 
    You should use the "dim" parameter.
    For more info...
    http://docs.ros.org/en/api/std_msgs/html/msg/MultiArrayLayout.html
    """
    
    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(Int32MultiArray_message)

        # add delay
        rate.sleep()
    

if __name__ == '__main__':
    try:
        Int32MultiArray_publisher_example()
    except rospy.ROSInterruptException:
        pass




