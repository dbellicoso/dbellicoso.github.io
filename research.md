---
layout: default
title: Research
permalink: /research/
---
<h1>
Research
</h1>

#### ALMA - Articulated Locomotion and Manipulation for a Torque-Controllable Robot
###### May, 2019 &#183; IEEE International Conference on Robotics and Automation (ICRA)

<div class="container">
  <iframe width="560" height="315" padding-bottom="10px" src="https://www.youtube.com/embed/XrcLXX4AEWE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p style="text-align:justify">
We present a motion planning and control framework for ANYmal, a torque-controlled quadrupedal robot equipped with a six degrees of freedom robotic arm capable of performing dynamic locomotion while executing manipulation tasks. The online motion planning framework, together with a whole-body control based on a hierarchical optimization algorithm, enable the system to walk, trot and pace while executing tasks such as fixed-position end-effector control, reactive human-robot collaboration and torso posture optimization to increase the arm’s kinematic reachability. The torque controllability of the whole system enables the implementation of compliant behaviour, allowing a user to safely interact with the robot in a very natural way. We verify our framework on the real robot by performing tasks such as opening a door or carrying a payload together with a human.
</p>
<div style="padding-top:30px"></div>


#### Dynamic Locomotion Through Online Nonlinear Motion Optimization for Quadrupedal Robots
###### July, 2018 &#183; IEEE Robotic and Automation Letters (RA-L)
<div class="container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Gvcvs80yZvU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div style="padding-top:10px"></div>
<p style="text-align:justify">
This letter presents a realtime motion planning and control method that enables a quadrupedal robot to execute dynamic gaits including trot, pace, and dynamic lateral walk, as well as gaits with full flight phases such as jumping, pronking, and running trot. The proposed method also enables smooth transitions between these gaits. Our approach relies on an online zero-moment point based motion planner which continuously updates the reference motion trajectory as a function of the contact schedule and the state of the robot. The reference footholds for each leg are obtained by solving a separate optimization problem. The resulting optimized motion plans are tracked by a hierarchical whole-body controller. Our framework has been tested in simulation and on ANYmal, a fully torque-controllable quadrupedal robot, both in simulation and on the actual robot.
</p>
<div style="padding-top:30px"></div>


#### Perception-less terrain adaptation through whole body control and hierarchical optimization
###### November, 2016 &#183; IEEE-RAS 16th International Conference on Humanoid Robots (Humanoids)

<div class="container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/AjiLCbJUYKI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div style="padding-top:10px"></div>
<p style="text-align:justify">
This paper presents a control approach based on a whole body control framework combined with hierarchical optimization. Locomotion is formulated as multiple tasks (e.g. maintaining balance or tracking a desired motion of one of the limbs) which are solved in a prioritized way using QP solvers. It is shown how complex locomotion behaviors can purely emerge from robot-specific inequality tasks (i.e. torque or reaching limits) together with the optimization of balance and system manipulability. Without any specific motion planning, this prioritized task optimization leads to a natural adaption of the robot to the terrain while walking and hence enables blind locomotion over rough grounds. The presented framework is implemented and successfully tested on ANYmal, a torque controllable quadrupedal robot. It enables the machine to walk while accounting for slippage and torque limitation constraints, and even step down from an unperceived 14 cm obstacle. Thereby, ANYmal exploits the maximum reach of the limbs and automatically adapts the body posture and height.
</p>
<div style="padding-top:30px"></div>
