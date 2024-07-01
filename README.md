## PC setup

### install-dependent-ros-packages :


```
$ sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
  ```

### Install TurtleBot3 packages :
```
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
```

## save the world in gazebo
Copy the model of your world in models directory of gazebo

example :

I have choosen Hospital model from the repo:

https://github.com/mlherd/Dataset-of-Gazebo-Worlds-Models-and-Maps.git

![example gazebo files](images/gazebo.png)

Your gazebo should look like this.


## Visualizing the robot environment using RVIZ


### Launch Simulation World
 Open terminal run the following commands in your workspace 

```
$ export TURTLEBOT3_MODEL=burger
$ export GAZEBO_MODEL_PATH=/home/anamika/.gazebo/models/hospital/hospital_models/
$ roslaunch my_pack turtlebot3_custom_world.launch 
# 
```
### Run SLAM Node
Open a new terminal and run the SLAM node.

```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### Run Teleoperation Node
Open a new terminal and run the teleoperation node

```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
### Save Map
When the map is created successfully, open a new terminal and save the map using the following command

```
$ rosrun map_server map_saver -f ~/map
```
