# encoding: utf-8


class BaseEnv:
    """环境的基类"""

    def __init__(self, **kwargs):
        raise NotImplementedError("please implement at first")

    def step(self, **kwargs):
        raise NotImplementedError("please implement at first")

    def reset(self, **kwargs):
        raise NotImplementedError("please implement at first")

    def render(self, **kwargs):
        raise NotImplementedError("please implement at first")

    def get_S(self):
        """获取状态空间"""
        raise NotImplementedError("please implement at first")

    def get_A(self):
        """获取动作空间"""
        raise NotImplementedError("please implement at first")

    def get_P(self):
        """获取状态转移矩阵"""
        raise NotImplementedError("please implement at first")

    def get_R(self):
        """获取奖励矩阵"""
        raise NotImplementedError("please implement at first")

    def get_gamma(self):
        """获取折扣因子"""
        raise NotImplementedError("please implement at first")
