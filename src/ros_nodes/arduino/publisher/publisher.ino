// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Int32.h>
    

// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Int32 message;

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
  message.data = 10;
  
  // publish message
  pub.publish(&message);

  delay(500);
}
