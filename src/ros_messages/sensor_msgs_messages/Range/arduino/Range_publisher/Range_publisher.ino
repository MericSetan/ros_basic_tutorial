// include roslib and ros messages
#include <ros.h>
#include <sensor_msgs/Range.h>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
sensor_msgs::Range message;

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
  message.header.stamp = nh.now();
  message.header.frame_id = "front_usm";

  // sensor features 
  message.radiation_type = sensor_msgs::Range::ULTRASOUND; // INFRARED,LASER,ULTRASOUND or UNKNOWN
  message.field_of_view = 0.261799; // radian 
  message.min_range = 0.2;
  message.max_range = 5.0;
  message.range = 2.4;
  
  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
