#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32MultiArray,MultiArrayLayout,MultiArrayDimension

def Int32MultiArray_publisher_example():

    # start node
    rospy.init_node("Int32MultiArray_Publisher_Node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Int32MultiArray,queue_size = 10) # topic_name, message_type, queue_size

    array_to_send = [[1, 2, 3],
                     [4, 5, 6]]
    
    # create message
    Int32MultiArray_message = Int32MultiArray()
    Int32MultiArray_message.data = [item for sublist in array_to_send for item in sublist]

    # Describe array dimension
    Int32MultiArray_message.layout.dim.append(MultiArrayDimension())
    Int32MultiArray_message.layout.dim.append(MultiArrayDimension())
    Int32MultiArray_message.layout.dim[0].label = "rows"
    Int32MultiArray_message.layout.dim[0].size = len(array_to_send)
    Int32MultiArray_message.layout.dim[0].stride = len(array_to_send) * len(array_to_send[0])
    Int32MultiArray_message.layout.dim[1].label = "cols"
    Int32MultiArray_message.layout.dim[1].size = len(array_to_send[0])
    Int32MultiArray_message.layout.dim[1].stride = len(array_to_send[0])

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




