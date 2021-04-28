from rllab.core.serializable import Serializable
# from rllab.envs.mujoco.point_env import PointEnv
from ..mujoco.point_env import PointEnv
from .mujoco_env_safe import SafeMujocoEnv
import numpy as np


class SafePointEnv(SafeMujocoEnv, Serializable):
    MODEL_CLASS = PointEnv
