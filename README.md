## VRX playground

VSCode development environment for experimenting with [VRX simulation environment](https://github.com/osrf/vrx).

This project uses git submodules, don't forget to clone it recursively.
```
git clone https://github.com/stepanove/vrx_playground.git --recursive
```


The first start can take some time because Gazebo needs to download assets, be patient.

At the moment it just allows to run the simulation in a devcontainer, control WAM-V with a joystic or via Gazebo's telop GUI.
There are configs and launch files for Nav2 stack (based on tutorial [Navigating using GPS Localization](https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html)), it even works somehow, but don't expect too much.

The easiest way to run this project is to use VSCode. There is a devcontainer configuration and tasks for building and launching the simulation.
Alternatively you can build and start it from VSCode terminal using something like this: 
```
colcon build --merge-install --symlink-install
source install/setup.bash && ros2 launch playground playground.launch.py
```
Depending on your host system, you may need to do some additional configuration to enable X11 forwarding. For example, you could try executing the following command in the host terminal:
```
xhost local:$USER
```

<img width="2553" height="1409" alt="screenshot" src="https://github.com/user-attachments/assets/44d09a29-70cf-4658-879f-35bde5a64d7c" />
