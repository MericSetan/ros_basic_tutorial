// include roslib and ros messages
#include <ros.h>
#include <sensor_msgs/Temperature.h>
    
// create a ros object
ros::NodeHandle  nh;

// callback function 
void callback_function(sensor_msgs::Temperature &msg){
  float temperature = msg.temperature;

  /* also you can get
  msg.temperature 
  msg.header.stamp 
  msg.header.frame_id 
  msg.variance 
  */
}
  
// create subscriber 
ros::Subscriber<sensor_msgs::Temperature> sub("topic_name", &callback_function);

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
