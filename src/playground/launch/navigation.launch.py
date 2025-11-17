# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from nav2_common.launch import RewrittenYaml
from launch.actions import GroupAction
from launch_ros.actions import SetRemap, Node


def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('nav2_bringup')
    package_dir = get_package_share_directory("playground")
    launch_dir = os.path.join(package_dir, 'launch')
    params_dir = os.path.join(package_dir, "config")
    nav2_params = os.path.join(params_dir, "nav2_params.yaml")
    configured_params = RewrittenYaml(
        source_file=nav2_params, root_key="", param_rewrites="", convert_types=True
    )


    nav_group = GroupAction([
        # SetRemap(src='/scan', dst='/wamv/sensors/lidars/lidar_wamv_sensor/scan'),
        SetRemap(src='/scan', dst='/wamv/sensors/lidars/lidar_wamv_sensor/points'),
        SetRemap(src='/odom', dst='/odometry/global'),

    IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(bringup_dir, "launch", "navigation_launch.py")
        ),
        launch_arguments={
            "use_sim_time": "True",
            "params_file": configured_params,
            "autostart": "True"
        }.items()
    ),

    Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['--frame-id', '/wamv/wamv/base_link', '--child-frame-id', '/base_link']
        ),
    Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['--frame-id', '/wamv/wamv/base_link', '--child-frame-id', '/base_footprint']
        ),    
    ])



    return LaunchDescription([nav_group])
