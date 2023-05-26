#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Float32MultiArray,MultiArrayLayout,MultiArrayDimension

def Float32MultiArray_publisher_example():

    # start node
    rospy.init_node("Float32MultiArray_Publisher_Node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Float32MultiArray,queue_size = 10) # topic_name, message_type, queue_size


    array_to_send = [[1.0, 2.0, 3.0],
                     [4.0, 5.0, 6.0]]
    # Float32MultiArray mesajını oluşturun
    Float32MultiArray_message = Float32MultiArray()
    Float32MultiArray_message.data = [item for sublist in array_to_send for item in sublist]

    # Mesajın boyutlarını belirtin
    Float32MultiArray_message.layout.dim.append(MultiArrayDimension())
    Float32MultiArray_message.layout.dim.append(MultiArrayDimension())
    Float32MultiArray_message.layout.dim[0].label = "rows"
    Float32MultiArray_message.layout.dim[0].size = len(array_to_send)
    Float32MultiArray_message.layout.dim[0].stride = len(array_to_send) * len(array_to_send[0])
    Float32MultiArray_message.layout.dim[1].label = "cols"
    Float32MultiArray_message.layout.dim[1].size = len(array_to_send[0])
    Float32MultiArray_message.layout.dim[1].stride = len(array_to_send[0])

    
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




