#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from std_msgs.msg import Float64, Float32

class MovePuzzlebot:
    def __init__(self):
        rospy.init_node('move_puzzlebot_node')
        
        self.position = [0.0, 0.0, 0.0]
        self.orientation = [0.0, 0.0, 0.0, 1.0]

        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.position_subscriber = rospy.Subscriber('/move_puzzlebot/position', Vector3, self.position_callback)
        self.angle_subscriber = rospy.Subscriber('/move_puzzlebot/angle', Float64, self.angle_callback)
        self.time_subscriber = rospy.Subscriber('/move_puzzlebot/time', Float32, self.time_callback)

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.rate = rospy.Rate(10)

        self.move_time = None
        self.move_start_time = None

        while not rospy.is_shutdown():
            if self.move_time is not None and self.move_start_time is not None:
                if rospy.get_time() - self.move_start_time <= self.move_time:
                    self.move_in_straight_line()
                else:
                    self.move_time = None
            self.rate.sleep()

    def odom_callback(self, msg):
        self.position[0] = msg.pose.pose.position.x
        self.position[1] = msg.pose.pose.position.y
        self.position[2] = msg.pose.pose.position.z

        self.orientation[0] = msg.pose.pose.orientation.x
        self.orientation[1] = msg.pose.pose.orientation.y
        self.orientation[2] = msg.pose.pose.orientation.z
        self.orientation[3] = msg.pose.pose.orientation.w

    def position_callback(self, msg):
        self.target_position = [msg.x, msg.y, msg.z]

    def angle_callback(self, msg):
        self.target_angle = msg.data

    def time_callback(self, msg):
        self.move_time = msg.data
        self.move_start_time = rospy.get_time()

    def move_in_straight_line(self):
        linear_velocity = Vector3()
        angular_velocity = Vector3()

        linear_velocity.x = 0.2 # set linear velocity as 0.2 m/s to move straight

        # calculate angular velocity
        (roll, pitch, yaw) = euler_from_quaternion(self.orientation)
        angular_velocity.z = 0.0

        # publish velocity
        self.velocity_publisher.publish(Twist(linear=linear_velocity, angular=angular_velocity))

if __name__ == '__main__':
    try:
        MovePuzzlebot()
    except rospy.ROSInterruptException:
        pass
