# encoding: utf-8

"""ref
[动手学强化学习](https://github.com/boyu-ai/Hands-on-RL)
"""

import numpy as np

from base_env import BaseEnv


class BernoulliBandit(BaseEnv):
    """伯努利多臂老虎机,输入K表示拉杆个数"""

    def __init__(self, K, **kwargs):
        self.probs = np.random.uniform(
            size=K
        )  # 随机生成K个0～1的数,作为拉动每根拉杆的获奖
        # 概率
        self.best_idx = np.argmax(self.probs)  # 获奖概率最大的拉杆
        self.best_prob = self.probs[self.best_idx]  # 最大的获奖概率
        self.K = K

    def step(self, k, **kwargs):
        # 当玩家选择了k号拉杆后,根据拉动该老虎机的k号拉杆获得奖励的概率返回1（获奖）或0（未
        # 获奖）
        if np.random.rand() < self.probs[k]:
            return 1
        else:
            return 0

    def reset(self, **kwargs):
        pass

    def render(self, **kwargs):
        pass
