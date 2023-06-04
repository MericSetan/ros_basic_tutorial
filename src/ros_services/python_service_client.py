#!/usr/bin/env python3

# import rospy and service
import rospy
from ros_basic_tutorial.srv import my_service

def client():
    
    # wait for the service
    rospy.wait_for_service("counter")

    # create service proxy
    service_control  =rospy.ServiceProxy("counter",my_service)

    for i in range(15):
        print(i)
        try:
            # call the service
            callback = service_control(i)
            print(callback) 
        except:
            pass
            
       
if __name__ == '__main__':
    try:
        client()
    except rospy.ROSInterruptException:
        pass
