// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Time.h>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Time received_msg;

unsigned long sec,nsec;

// callback function 
void callback_function(std_msgs::Time &msg){
  received_msg = msg;

  msg.data.sec = sec;
  msg.data.nsec = nsec;
  
}
  
// create subscriber 
ros::Subscriber<std_msgs::Time> sub("topic_name", &callback_function);

void setup() {
 
  // start node
  nh.initNode();

  // subscribe topic 
  nh.subscribe(sub);

}

void loop() {
  // update ROS communication
  nh.spinOnce();
}
