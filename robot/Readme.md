///////////Instructions////////////////


1- Extract the zip and copy it in your workspace src

2- Load the package in workspace by commands: 
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash

- Robot Mapping SLAM
1. roslaunch robot_nav gazebo.launch
2. roslaunch robot_nav gmapping.launch
3. roslaunch robot_nav display.launch	
4. roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
5. rosrun map_server map_saver -f ~/map

- Robot Autonomous Navigation
1. roslaunch robot_nav gazebo.launch
2. roslaunch robot_sims robot.launch
Note: Use wD nov Goal to point the goal point in Rviz 

- Face Detection and Save the Image
1. roslaunch robot_nav gazebo.launch
2. roslaunch robot_sims robot.launch
3. rosrun robot_sims camera.py




