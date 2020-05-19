# UR5 manual for ElsaLab
Simple setup for controlling UR5, including:
* Control UR5 with ROS sending angles for each motors
* 

# If you use ASUS X441S (white little laptop)
UR5 Driver has been intalled.
Here are the steps to control ur5 robot arm
1. Turn on UR5. It could take 2-3 minutes.
![](IMG_20200519_180527.jpg "a")
2. Follow the several steps as the images below
3. Go to the laptop. Connect the Ethernet to UR5, and select wired conection *UR5*
4. Go to terminal `$ roslaunch ur_robot_driver ur5_bringup.launch robot_ip:=192.168.56.101
`
5. Start UR5 program as the images show below
6. Start another terminal, `$ rosrun rqt_joint_trajectory_controller rqt_joint_tractory_controller
`

It's important to reset joints' positions before turning off UR5. Here's the prosedure:
1. Open program init_

## UR5 Hardware Information
MODEL: UR5(CB31UR5) (CB3)

## UR5 Software Version
URSoftware 3.10.0

## Laptop
```
$ uname -a
Linux elsalab-GP62MVR-7RF 4.15.0-99-generic #100~16.04.1-Ubuntu SMP Wed Apr 22 23:56:30 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

## Step 1
`source install_ros_melody.sh`

---
## Driver
[Go to UR5 github page](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver)