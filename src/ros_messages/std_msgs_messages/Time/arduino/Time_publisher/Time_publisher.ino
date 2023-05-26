// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Time.h>>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Time message;

// create publisher
ros::Publisher pub("topic_name", &message);

void setup() {
  // start node
  nh.initNode();
  
  // define publisher
  nh.advertise(pub);  
}

void loop() {
  // get time
  unsigned long currentTime = millis();
  
  // create message
  message.data.sec = currentTime / 1000;
  message.data.nsec = (currentTime % 1000) * 1000000;
  
  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
