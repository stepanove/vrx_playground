## VRX playground

VSCode development environment for experimenting with [VRX simulation environment](https://github.com/osrf/vrx).

The first start can take some time because Gazebo needs to download assets, be patient.

At the moment it just allows to run the simulation in a devcontainer, control WAM-V with a joystic or via Gazebo's telop GUI.
There are configs and launch files for Nav2 stack (based on tutorial [Navigating using GPS Localization](https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html)), it even works somehow, but don't expect too much.
```
colcon build --merge-install --symlink-install
source install/setup.bash && ros2 launch playground playground.launch.py
```

<img width="2553" height="1409" alt="screenshot" src="https://github.com/user-attachments/assets/44d09a29-70cf-4658-879f-35bde5a64d7c" />
