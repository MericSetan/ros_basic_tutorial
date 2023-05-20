#!/usr/bin/env python3

#import rospy and messages
import rospy
from std_msgs.msg import Int32,String

# run these commands in different consoles to test:
# 1 : rostopic echo /pub_topic 
# 2 : rostopic pub /sub_topic std_msgs/Int32 "data: 12" 

class PubWithSubClass():

    def __init__(self):

        # start node
        rospy.init_node("node_name")

        # create self publisher object
        self.pub = rospy.Publisher("pub_topic",String,queue_size = 10) # topic_name, message_type, queue_size

        # create subscriber
        rospy.Subscriber('sub_topic', Int32, self.callback_function)

        # interaction and listening loop 
        rospy.spin()
    

    def callback_function(self,sub_message):

        if sub_message.data > 5:
            # define message to publish
            msg_to_be_publish = "{} > 5".format(sub_message.data)
            # publish message 
            self.pub.publish(msg_to_be_publish)
        else: 
            # define message to publish
            msg_to_be_publish = "{} <= 5".format(sub_message.data)
            # publish message 
            self.pub.publish(msg_to_be_publish)


        

if __name__ == '__main__':
    try:
        object = PubWithSubClass()
    except rospy.ROSInterruptException:
        pass