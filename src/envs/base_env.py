# encoding: utf-8


class BaseEnv:
    """环境的基类"""

    def __init__(self, **kwargs):
        pass

    def step(self, **kwargs):
        pass

    def reset(self, **kwargs):
        pass

    def render(self, **kwargs):
        pass
