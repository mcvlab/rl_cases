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
