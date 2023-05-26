// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>>
    
// create a ros object
ros::NodeHandle  nh;

// create a message
std_msgs::Float32MultiArray message;

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
  float float_array[] = {1.2, 4.1, 9.88};

  // define message
  message.data = float_array;
  message.data_length = sizeof(float_array) / sizeof(float); // array lenght = 3

  // publish message
  pub.publish(&message);
  
  // update ROS communication
  nh.spinOnce();
  
  delay(500);
}
