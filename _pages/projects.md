---
layout: page
title: Projects
permalink: /projects/
description: A collection of projects that I have worked on.
nav: true
nav_order: 3
---

<div class="projects">
  <h2>Roadrunner</h2>
  <div class="row">
      <div class="col-sm mt-3 mt-md-0">
          <iframe width="100%" height="450" src="https://www.youtube.com/embed/9kae-UAME1U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
  </div>
  <div class="caption">
    Meet “Roadrunner": a bipedal, wheeled robot for multi-modal locomotion
  </div>
  <p style="text-align:justify">
  "Roadrunner” is a new bipedal wheeled robot prototype designed for multi-modal locomotion. It weighs around 15kg (33 lb.) and can seamlessly switch between its side-by-side and in-line wheel modes and stepping configurations depending on what is required for navigating its environment. The robot’s legs are entirely symmetric, allowing it to point its knees forward or backward, which can be used to avoid obstacles or manage specific movements.

  A single control policy was trained to handle both side-by-side and in-line driving. Several behaviors, including standing up from various ground configurations and balancing on one wheel, were successfully deployed zero-shot on the hardware.
  </p>

  <hr>

  <h2>Introducing Stretch</h2>
  <div class="row">
      <div class="col-sm mt-3 mt-md-0">
          <iframe width="100%" height="450" src="https://www.youtube.com/embed/yYUuWWnfRsk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
  </div>
  <div class="caption">
    Introducing Stretch | Boston Dynamics
  </div>
  <p style="text-align:justify">
  Stretch is a mobile robot designed for warehouse automation. It features a unique omnidirectional base and a high-reach arm, enabling it to move pallets and packages efficiently within a facility. The robot is equipped with advanced perception and control systems to handle dynamic environments and complex manipulation tasks.
  </p>

  <hr>


  <h2>ALMA</h2>
  <div class="row">
      <div class="col-sm mt-3 mt-md-0">
          <iframe width="100%" height="450" src="https://www.youtube.com/embed/XrcLXX4AEWE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
  </div>
  <div class="caption">
      ALMA - Articulated Locomotion and Manipulation for a Torque-Controllable Robot. Featured at IEEE International Conference on Robotics and Automation (ICRA) 2019.
  </div>
  <p style="text-align:justify">
  We present a motion planning and control framework for ANYmal, a torque-controlled quadrupedal robot equipped with a six degrees of freedom robotic arm capable of performing dynamic locomotion while executing manipulation tasks. The online motion planning framework, together with a whole-body control based on a hierarchical optimization algorithm, enable the system to walk, trot and pace while executing tasks such as fixed-position end-effector control, reactive human-robot collaboration and torso posture optimization to increase the arm’s kinematic reachability. The torque controllability of the whole system enables the implementation of compliant behaviour, allowing a user to safely interact with the robot in a very natural way. We verify our framework on the real robot by performing tasks such as opening a door or carrying a payload together with a human.
  </p>

  <hr>

  <h2>Dynamic Locomotion</h2>
  <div class="row">
      <div class="col-sm mt-3 mt-md-0">
          <iframe width="100%" height="450" src="https://www.youtube.com/embed/Gvcvs80yZvU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
  </div>
  <div class="caption">
      Dynamic Locomotion Through Online Nonlinear Motion Optimization for Quadrupedal Robots. Featured at IEEE Robotic and Automation Letters (RA-L) 2018.
  </div>
  <p style="text-align:justify">
  This letter presents a realtime motion planning and control method that enables a quadrupedal robot to execute dynamic gaits including trot, pace, and dynamic lateral walk, as well as gaits with full flight phases such as jumping, pronking, and running trot. The proposed method also enables smooth transitions between these gaits. Our approach relies on an online zero-moment point based motion planner which continuously updates the reference motion trajectory as a function of the contact schedule and the state of the robot. The reference footholds for each leg are obtained by solving a separate optimization problem. The resulting optimized motion plans are tracked by a hierarchical whole-body controller. Our framework has been tested in simulation and on ANYmal, a fully torque-controllable quadrupedal robot, both in simulation and on the actual robot.
  </p>

  <hr>

  <h2>Perception-less Adaptation</h2>
  <div class="row">
      <div class="col-sm mt-3 mt-md-0">
          <iframe width="100%" height="450" src="https://www.youtube.com/embed/AjiLCbJUYKI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
  </div>
  <div class="caption">
      Perception-less terrain adaptation through whole body control and hierarchical optimization. Featured at IEEE-RAS 16th International Conference on Humanoid Robots (Humanoids) 2016.
  </div>
  <p style="text-align:justify">
  This paper presents a control approach based on a whole body control framework combined with hierarchical optimization. Locomotion is formulated as multiple tasks (e.g. maintaining balance or tracking a desired motion of one of the limbs) which are solved in a prioritized way using QP solvers. It is shown how complex locomotion behaviors can purely emerge from robot-specific inequality tasks (i.e. torque or reaching limits) together with the optimization of balance and system manipulability. Without any specific motion planning, this prioritized task optimization leads to a natural adaption of the robot to the terrain while walking and hence enables blind locomotion over rough grounds. The presented framework is implemented and successfully tested on ANYmal, a torque controllable quadrupedal robot. It enables the machine to walk while accounting for slippage and torque limitation constraints, and even step down from an unperceived 14 cm obstacle. Thereby, ANYmal exploits the maximum reach of the limbs and automatically adapts the body posture and height.
  </p>

</div>
