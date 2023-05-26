// include roslib and ros messages
#include <ros.h>
#include <sensor_msgs/Temperature.h>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
sensor_msgs::Temperature message;

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
  message.temperature = 25.5;
  message.header.stamp = nh.now();
  message.header.frame_id = "battery";
  message.variance = 0.1; //default 0.0
  
  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
