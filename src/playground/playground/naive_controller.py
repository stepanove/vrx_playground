import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import TwistStamped
from rclpy.qos import QoSProfile, QoSDurabilityPolicy
from geometry_msgs.msg import PoseStamped

class NaiveController(Node):
    def __init__(self):
        print('Starting naive_controller...')
        super().__init__('naive_controller')
        
        pub_qos = QoSProfile(depth=1, 
                             durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        self.right_thrust_pub = self.create_publisher(Float64, 
                                                      '/wamv/thrusters/right/thrust', 
                                                      qos_profile=pub_qos)
        self.left_thrust_pub = self.create_publisher(Float64, 
                                                     '/wamv/thrusters/left/thrust', 
                                                     qos_profile=pub_qos)
        self.left_thrust_msg = Float64()
        self.right_thrust_msg = Float64()
        
        self.linear_gain=2000.;
        self.angular_gain=500.; 

        self.twist_sub = self.create_subscription(TwistStamped, '/cmd_vel',self.twistCB,1)


    def twistCB(self, msg):
        #Assume that thruster's direction is fixed and steer with the thrust difference only.
        #This is enough for somewhat reasonable steering using Gazebo's teleop or teleop_twist_keyboard. 
        self.left_thrust_msg.data = msg.twist.linear.x*self.linear_gain - msg.twist.angular.z*self.angular_gain;
        self.right_thrust_msg.data = msg.twist.linear.x*self.linear_gain + msg.twist.angular.z*self.angular_gain;
        self.right_thrust_pub.publish(self.right_thrust_msg)       
        self.left_thrust_pub.publish(self.left_thrust_msg)


def main(args=None):
    rclpy.init(args=args)
    controller = NaiveController()
    rclpy.spin(controller)


if __name__ == '__main__':
    main()