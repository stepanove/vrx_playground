## VRX playground

VSCode development environment for experimenting with [VRX simulation environment](https://github.com/osrf/vrx).

At the moment it just allows to run the simulation in a devcontainer, control WAM-V with a joystic or via Gazebo's telop GUI. 
```
colcon build --merge-install --symlink-install
source install/setup.bash && ros2 launch playground playground.launch.py
```
<img width="2557" height="1408" alt="screenshot" src="https://github.com/user-attachments/assets/af6c7bea-a853-4831-955a-5bfb4064f148" />
