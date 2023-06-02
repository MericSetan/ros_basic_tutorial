#!/usr/bin/env python3

# import required libs
import rospy
import actionlib
# they occur spontaneously with action
from ros_basic_tutorial.msg import my_actionAction,my_actionGoal

def callback(info):
    print(info.feedback)

def make_a_request():

    rospy.init_node("client_node") 

    # create the action client
    client = actionlib.SimpleActionClient("counter",my_actionAction)

    # wait for the server
    client.wait_for_server()

    # create the goal
    request = my_actionGoal()
    request.request = 10

    # send the goal and set the feedback callback
    client.send_goal(request,feedback_cb=callback)
    
    # wait for the result
    client.wait_for_result()
    print(client.get_result().response)
     

if __name__ == '__main__':
    try:
        make_a_request()
    except rospy.ROSInterruptException:
        pass

