// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Int32MultiArray message;

// create publisher
ros::Publisher pub("topic_name", &message);

void setup() {
  // start node
  nh.initNode();
  
  // define publisher
  nh.advertise(pub);  
}

void loop() { 
  // create an float array
  float int_array[] = {1,2,3};

  // define message
  message.data = int_array;
  message.data_length = sizeof(int_array) / sizeof(int); // array lenght = 3

  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
