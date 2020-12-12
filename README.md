# SASCW-ROS

<p align="center">
  <img width="300" height="300" src="https://github.com/pks-97/SASCW-ROS/blob/main/catkin_scw/Stair%20Climbing%20Wheelchair.PNG">
</p>

This repository contains the ROS implementation of Martin Pecka's paper, [Fast Simulation of Vehicles with Non-deformable Tracks](https://arxiv.org/pdf/1703.04316.pdf). We have created a ROS wrapper of the [gazebo plugin](https://bitbucket.org/pchidamb/fast-track/src/master/). 

For an accurate pose estimation we have employed the [Extended Kalman Filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter#:~:text=In%20estimation%20theory%2C%20the%20extended,the%20current%20mean%20and%20covariance) (EKF).
We utilize [fovis_ros](http://wiki.ros.org/fovis_ros) for visual state estimation and use IMU data to perform sensor fusion in the EKF. EKF is implemented using the [robot_pose_ekf](http://wiki.ros.org/robot_pose_ekf), the results could be visualized in Rviz using [odom_to_trajectory](https://github.com/udacity/odom_to_trajectory).

## Dependencies
In Ununtu 16.04,
- [**ROS Kinetic**](http://wiki.ros.org/kinetic/Installation)
- [**Gazebo 9**](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=9.0)
- [**Rviz**](https://howtoinstall.co/en/ubuntu/xenial/rviz)
- [**Python 3**](https://www.python.org/download/releases/3.0/)
