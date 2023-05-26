#!/usr/bin/env python3

#import rospy and messages
import rospy
from sensor_msgs.msg import Temperature

def publisher_example():

    # start node
    rospy.init_node("my_publisher_node")

    # create publisher object
    pub = rospy.Publisher("your_topic",Temperature,queue_size = 10) # topic_name, message_type, queue_size

    # create message 
    message = Temperature()
    message.temperature = 25
    message.variance = 0.0  # default 0.0
    message.header.stamp = rospy.Time.now()  
    message.header.frame_id = "battery"  
    message.header.seq = 0  
    
    # create rate to publish once per second 
    rate = rospy.Rate(1)  # 1 Hz 

    while not rospy.is_shutdown():
 
        # publish message
        pub.publish(message)
        
        # add delay
        rate.sleep()
  
            
if __name__ == '__main__':
    try:
        publisher_example()
    except rospy.ROSInterruptException:
        pass

""" 
rostopic echo /your_topic 
--out--

header: 
  seq: 1
  stamp: 
    secs: 1685108207
    nsecs:  95741271
  frame_id: "battery"
temperature: 25.0
variance: 0.0

 """