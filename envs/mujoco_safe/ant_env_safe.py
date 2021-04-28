from rllab.core.serializable import Serializable
from rllab.envs.mujoco.ant_env import AntEnv
from .mujoco_env_safe import SafeMujocoEnv
import numpy as np


class SafeAntEnv(SafeMujocoEnv, Serializable):
    MODEL_CLASS = AntEnv
