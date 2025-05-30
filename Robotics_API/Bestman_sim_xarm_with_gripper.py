# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
# @FileName       : Bestman_sim_xarm.py
# @Time           : 2024-08-03 15:08:13
# @Author         : yk
# @Email          : yangkui1127@gmail.com
# @Description:   : xarm robot
"""

import math
import time

import numpy as np
import pybullet as p
from scipy.spatial.transform import Rotation as R

from .Bestman_sim import Bestman_sim
from .Pose import Pose


class Bestman_sim_xarm_with_gripper(Bestman_sim):
    """
    A class representing a simulation for the Bestman robot equipped with a xarm arm.
    """

    def __init__(self, client, visualizer, cfg):
        """
        Initialize the Bestman_sim_xarm with the given parameters.

        Args:
            client (int): The PyBullet client ID.
            visualizer (bool): Flag indicating whether visualization is enabled.
            cfg (dict): Configuration settings.
        """
        
        # Init parent class: BestMan_sim
        super().__init__(client, visualizer, cfg)


        self.dims = 0
        self.pose_range = [-1,1]

    # ----------------------------------------------------------------
    # Functions for arm
    # ----------------------------------------------------------------

    def sim_get_sync_arm_pose(self):
        """
        Get synchronized pose of the robot arm with the base.
        """
        base_pose = self.sim_get_current_base_pose()
        arm_pose = Pose(
            [*base_pose.get_position()[:2], self.arm_place_height],
            base_pose.get_orientation(),
        )
        return arm_pose

    # ----------------------------------------------------------------
    # Functions for gripper
    # ----------------------------------------------------------------

    def sim_open_gripper(self):
        """open gripper"""
        self.sim_move_gripper(self.gripper_range[1])
        print("[BestMan_Sim][Gripper] \033[34mInfo\033[0m: Gripper open!")

    def sim_close_gripper(self):
        """close gripper"""
        self.sim_move_gripper(self.gripper_range[0])
        print("[BestMan_Sim][Gripper] \033[34mInfo\033[0m: Gripper close!")

    def sim_move_gripper(self, open_width):
        """move gripper to special width

        Args:
            open_width (float): gripper open width
        """
        # TODO

    def sim_interactive_control_eef(self, duration=20):
        print("[BestMan_Sim][Gripper] \033[34mInfo\033[0m: Interact start!")
        debug_eff_pose = self.sim_get_current_eef_pose()
        eff_position = debug_eff_pose.position
        self.dims = len(eff_position) 
        debug_bar = []
        debug_eff_position = eff_position

        if self.dims != None and self.dims != 0:
            for i in range(self.dims):
                per_debug_bar = p.addUserDebugParameter(
                        f"translation{i}", self.pose_range[0], self.pose_range[1], eff_position[i]
                    )
                debug_bar.append(per_debug_bar)
        start_time = time.time()
        while time.time() - start_time < duration:
            for i in range(self.dims):
                debug_eff_position[i] = p.readUserDebugParameter(debug_bar[i])
            debug_eff_pose.position = debug_eff_position
            self.sim_move_eef_to_goal_pose(debug_eff_pose)
        print("[BestMan_Sim][Gripper] \033[34mInfo\033[0m: Interact over!")



 