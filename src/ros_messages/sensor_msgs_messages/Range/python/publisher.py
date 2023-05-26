#!/usr/bin/env python3

#import rospy and messages
import rospy
from sensor_msgs.msg import Range

def Range_publisher_example():

    # start node
    rospy.init_node("Range_publisher_node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Range,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    
    Range_message = Range()
    Range_message.header.stamp = rospy.Time.now()
    Range_message.header.frame_id = 'front_usm'

    # sensor features 
    Range_message.radiation_type = Range.ULTRASOUND #INFRARED,LASER,ULTRASOUND or UNKNOWN
    Range_message.field_of_view = 0.261799  # radian
    Range_message.min_range = 0.2
    Range_message.max_range = 5.0

    # distance 
    Range_message.range = 2.54

    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():

        # publish message
        pub.publish(Range_message)
        
        # add delay
        rate.sleep()

         
            
if __name__ == '__main__':
    try:
        Range_publisher_example()
    except rospy.ROSInterruptException:
        pass

"""
rostopic echo /your_topic 
---out---

    header: 
    seq: 1
    stamp: 
        secs: 1685108140
        nsecs: 120282173
    frame_id: "front_usm"
    radiation_type: 0
    field_of_view: 0.10000000149011612
    min_range: 0.20000000298023224
    max_range: 5.0
    range: 2.5399999618530273

"""