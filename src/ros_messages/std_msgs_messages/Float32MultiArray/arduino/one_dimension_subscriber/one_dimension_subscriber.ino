// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
 

// create a ros object
ros::NodeHandle  nh;

// received array
float list[] = {0.0,0.0,0.0};

// callback function 
void callback_function(std_msgs::Float32MultiArray &msg){
  
  msg.data = list;
  
}
  
// create subscriber 
ros::Subscriber<std_msgs::Float32MultiArray> sub("topic_name", &callback_function);

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
