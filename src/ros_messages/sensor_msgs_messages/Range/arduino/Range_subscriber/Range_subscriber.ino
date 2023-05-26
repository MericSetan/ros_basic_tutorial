// include roslib and ros messages
#include <ros.h>
#include <sensor_msgs/Range.h>
    
// create a ros object
ros::NodeHandle  nh;

// callback function 
void callback_function(sensor_msgs::Range &msg){
  float distance = msg.range;

  /* also you can get
   msg.header.frame_id
   msg.header.stamp
   msg.radiation_type
   msg.field_of_view 
   msg.min_range
   msg.max_range*/
}
  
// create subscriber 
ros::Subscriber<sensor_msgs::Range> sub("topic_name", &callback_function);

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
