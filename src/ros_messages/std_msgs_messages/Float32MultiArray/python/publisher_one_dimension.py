#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Float32MultiArray

def Float32MultiArray_publisher_example():

    # start node
    rospy.init_node("Float32MultiArray_Publisher")

    # create publisher object
    pub = rospy.Publisher("your_topic",Float32MultiArray,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    Float32MultiArray_message = Float32MultiArray()

    # define message
    Float32MultiArray_message.data = [1.87,2.32,3.67]

    """
    if you want to publish multi-dim array like [[1.3,2.23,3.56],[4.78,5.34,6.90]]. 
    You should use the "dim" parameter.
    For more info...
    http://docs.ros.org/en/api/std_msgs/html/msg/MultiArrayLayout.html
    """
    
    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(Float32MultiArray_message)

        # add delay
        rate.sleep()
    

if __name__ == '__main__':
    try:
        Float32MultiArray_publisher_example()
    except rospy.ROSInterruptException:
        pass




