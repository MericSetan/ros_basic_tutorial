// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Bool.h>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Bool received_msg;

// callback function 
void callback_function(std_msgs::Bool &msg){
  received_msg = msg;
}
  
// create subscriber 
ros::Subscriber<std_msgs::Bool> sub("topic_name", &callback_function);

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
