# Workspace compartido Gazebo
Workspace para correr simulacion de Gazebo y controlar con teleop twist

### Para correr
* En una terminal correr ```roscore```
* En segunda terminal, en folder ```*/shared_ws``` correr ```catkin_make```
* ```source devel/setup.bash```
* ```roslaunch puzzlebot_world puzzlebot_simple_world.launch```
* En tercera terminal correr ```rosrun teleop_twist_keyboard teleop_twist_keyboard.py```

##### Instrucciones teleop twist
* K --> Detener
* U --> Derecho lineal Izquierda Angular
* I --> Derecho lineal
* O --> Derecho lineal Derecha Angular
* J --> Angular Izquierda
* L --> Angular derecha
* M --> Atras lineal Izquierda Angular
* < --> Atras lineal
* \> --> Atras lineal Derecha Angular