from rllab.core.serializable import Serializable
from rllab.envs.mujoco.walker2d_env import Walker2DEnv
from .mujoco_env_safe import SafeMujocoEnv


class SafeWalker2DEnv(SafeMujocoEnv, Serializable):
    MODEL_CLASS = Walker2DEnv
