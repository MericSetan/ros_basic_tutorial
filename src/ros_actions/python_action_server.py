#!/usr/bin/env python3

# import required libs
import rospy
import actionlib
# they occur spontaneously with action
from ros_basic_tutorial.msg import my_actionAction,my_actionFeedback,my_actionActionResult


class Server():
    def __init__(self):
        rospy.init_node("action_server_node")  
        # create a server 
        self.server = actionlib.SimpleActionServer("counter",my_actionAction,
                                                   auto_start=False,
                                                   execute_cb=self.create_a_callback)
        self.server.start() # start server
        rospy.spin()

    def create_a_callback(self,rqst):
        feed_back = my_actionFeedback()
        
        rate  =rospy.Rate(1) # rate for check-time

        for i in range(rqst.request):
             
            feed_back.feedback = str(i) # create a feedback 
            self.server.publish_feedback(feed_back) # send the feedback
            rate.sleep()

        # create a result message
        my_actionActionResult().result.response = "it's done"   
        # send the result 
        self.server.set_succeeded(my_actionActionResult().result.response)

if __name__ == '__main__':
    try:
        object = Server()
    except rospy.ROSInterruptException:
        pass
