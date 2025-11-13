import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    package_name='playground'

    bridge_params = os.path.join(get_package_share_directory(package_name),'config','gz_bridge.yaml')
    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ]
    )

    controller = Node(
        package=package_name,
        executable="naive_controller",
        parameters=[{"use_sim_time": True}]        
    )

    joy = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('vrx_gz'),'launch','usv_joy_teleop.py'
                )])
    )

    sim = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('vrx_gz'), 'launch', 'competition.launch.py')]),
                    launch_arguments={'gz_args': ['world ', 'sydney_regatta'], 'extra_gz_args':['-v1'] }.items()
             )
    
    localization = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('playground'), 'launch', 'dual_ekf_navsat.launch.py')])
             )

    rviz = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('playground'), 'launch', 'rviz.launch.py')])
             )

    return LaunchDescription([ros_gz_bridge, controller, joy,
                               sim,
                               localization,
                               rviz,
                               ])
