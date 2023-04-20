# Workspace compartido Gazebo
Workspace para correr simulacion de Gazebo y controlar con teleop twist

### Para correr
* En una terminal correr ```roscore```
* En segunda terminal, en folder ```*/shared_ws``` correr ```catkin_make```
* ```source devel/setup.bash```
* ```roslaunch puzzlebot_world puzzlebot_simple_world.launch```
* En tercera terminal correr ```rosrun teleop_twist_keyboard teleop_twist_keyboard.py```