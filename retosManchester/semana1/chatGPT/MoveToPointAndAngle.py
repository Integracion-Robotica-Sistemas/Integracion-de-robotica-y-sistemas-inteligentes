#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from std_msgs.msg import Float64

class MovePuzzlebot:
    def __init__(self):
        rospy.init_node('move_puzzlebot_node')
        
        self.position = [0.0, 0.0, 0.0]
        self.orientation = [0.0, 0.0, 0.0, 1.0]

        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.position_subscriber = rospy.Subscriber('/move_puzzlebot/position', Vector3, self.position_callback)
        self.angle_subscriber = rospy.Subscriber('/move_puzzlebot/angle', Float64, self.angle_callback)

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            self.move_to_target()
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

    def move_to_target(self):
        linear_velocity = Vector3()
        angular_velocity = Vector3()

        # calculate linear velocity
        distance = ((self.position[0] - self.target_position[0])**2 + (self.position[1] - self.target_position[1])**2)**0.5
        linear_velocity.x = min(distance, 0.3)
        linear_velocity.y = 0.0
        linear_velocity.z = 0.0

        # calculate angular velocity
        (roll, pitch, yaw) = euler_from_quaternion(self.orientation)
        angle_difference = self.target_angle - yaw
        if angle_difference > 3.14159:
            angle_difference -= 2*3.14159
        elif angle_difference < -3.14159:
            angle_difference += 2*3.14159
        angular_velocity.z = min(angle_difference, 0.5)

        # publish velocity
        self.velocity_publisher.publish(Twist(linear=linear_velocity, angular=angular_velocity))


if __name__ == '__main__':
    try:
        MovePuzzlebot()
    except rospy.ROSInterruptException:
        pass