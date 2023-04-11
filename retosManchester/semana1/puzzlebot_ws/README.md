# Workspace de Puzzlebot
Workspace de Puzzlebot para el mini challenge de la semana 1


Para primera vez correr los siguientes comandos:
* `sudo apt-get install ros-melodic-ros-control ros-melodic-ros-controllers`
* `sudo apt-get install ros-melodic-teleop-twist-keyboard`

### Launch de pista

* En una nueva terminal, ir al folder del workspace
* `catkin make`
* `source devel/setup.bash`
* `roslaunch puzzlebot_word puzzlebot_simple_world.launch`

### Para controlar el Puzzlebot con el teclado
* En una nueva terminal, ir al folder del workspace
* source devel/setup.bash
* `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

### Resto de Funcionalidades
