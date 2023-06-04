#!/usr/bin/env python3

# import rospy and service
import rospy
from ros_basic_tutorial.srv import my_service

def callback(request):

    # counter from our srv file 
    counter = request.counter

    if counter == 10: 
        return "it's ten."
    
def response():
    
    # create node
    rospy.init_node("server_node")

    # create service 
    rospy.Service("counter",my_service,callback)

    # interaction and listening loop 
    rospy.spin()

if __name__ == '__main__':
    try:
        response()
    except rospy.ROSInterruptException:
        pass
