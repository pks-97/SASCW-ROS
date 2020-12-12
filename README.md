# SASCW-ROS
![alt text](https://github.com/pks-97/SASCW-ROS/blob/main/catkin_scw/Stair%20Climbing%20Wheelchair.PNG)


This repository is a ROS implementation of Martin Pecka's paper, [Fast Simulation of Vehicles with Non-deformable Tracks](https://arxiv.org/pdf/1703.04316.pdf). We have created a ROS wrapper of the [gazebo plugin](https://bitbucket.org/pchidamb/fast-track/src/master/). 

For an accurate pose estimation we have employed the [Extended Kalman Filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter#:~:text=In%20estimation%20theory%2C%20the%20extended,the%20current%20mean%20and%20covariance) (EKF).
We utilize [fovis_ros](http://wiki.ros.org/fovis_ros) for visual state estimation and use IMU data to perform sensor fusion in the EKF. 
