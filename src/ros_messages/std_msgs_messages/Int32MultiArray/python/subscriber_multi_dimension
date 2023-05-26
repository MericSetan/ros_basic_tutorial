#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32MultiArray

def callback_function(message):

    
    # get meesage data
    array_data = message.data

    # get row and column datas
    rows = message.layout.dim[0].size
    cols = message.layout.dim[1].size
    
    new_array = []
    index = 0

    # check dimensions
    if len(array_data) != rows * cols:
        rospy.loginfo("There is an error.Check message description!")

    # dilate data
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(array_data[index])
            index += 1
        new_array.append(row)
    # new_array = [[array_data[i * cols + j] for j in range(cols)] for i in range(rows)]
    print(new_array)

    
def Int32MultiArray_subscriber_example():

    # start node
    rospy.init_node("Int32MultiArray_Subscriber_Node")

    # create subscriber
    rospy.Subscriber('topic_name', Int32MultiArray, callback_function)

    # interaction and listening loop 
    rospy.spin()

        
            
if __name__ == '__main__':
    try:
        Int32MultiArray_subscriber_example()
    except rospy.ROSInterruptException:
        pass
