// include roslib and ros messages
#include <ros.h>
#include <std_msgs/String.h>>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::String message;

// create publisher
ros::Publisher pub("topic_name", &message);

void setup() {
  // start node
  nh.initNode();
  
  // define publisher
  nh.advertise(pub);  
}

void loop() {
  // define message
  message.data = "hello guys";
  
  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
