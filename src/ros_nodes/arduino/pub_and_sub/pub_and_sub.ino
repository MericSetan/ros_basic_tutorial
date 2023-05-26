// include roslib and ros messages
#include <ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/String.h>  

// create a ros object
ros::NodeHandle  nh;

// callback function 
void callback_function(std_msgs::Int32 &msg){
  received_msg = msg;
}

// create a message
std_msgs::String message;
std_msgs::Int32 received_msg;

// create publisher & subscriber
ros::Publisher pub("topic_name_to_pub", &message);
ros::Subscriber<std_msgs::Int32> sub("topic_name_to_sub", &callback_function);

void setup() {
  // start node
  nh.initNode();
  
  // define publisher & subscriber
  nh.advertise(pub);  
  nh.subscribe(sub);
}

void loop() {

  nh.spinOnce();
  
  // define message
  message.data = "Hello im using ROS";

  if(received_msg.data > 10){   
    // publish message
    pub.publish(&message);
  }
    

  delay(500);
}
