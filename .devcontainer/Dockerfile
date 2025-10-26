FROM ghcr.io/osrf/vrx-devel:latest

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN userdel -r $(getent passwd ${USER_UID} | cut -d: -f1) || \
    groupdel $(getent group ${USER_GID} | cut -d: -f1) ||true \
    && groupadd --gid $USER_GID $USERNAME \
    && groupadd --system --gid 995 input ||true \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME --shell /bin/bash -G video,dialout,input\
    && apt update \
    && apt upgrade -y \
    && apt install -y sudo \
    terminator \
    evtest \
    ros-${ROS_DISTRO}-joy \
    ros-${ROS_DISTRO}-joy-teleop \
    ros-${ROS_DISTRO}-rqt* \
    ros-${ROS_DISTRO}-rviz2 \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

USER $USERNAME

RUN echo source /opt/ros/${ROS_DISTRO}/setup.bash >> ${HOME}/.bashrc
