import gym
import numpy as np

class RandomAgent(object):
    """docstring for RandomAgent."""

    def __init__(self, action_space,observation_space):
        self.action_space = action_space
        self.observation_space = observation_space

    def actionSample(self,observation,reward,done):
        return self.action_space.sample()

    def actionSpace(self,observation,reward,done):
        return self.action_space

    def state(self,observation,reward,done):
        return self.observation_space.sample()

    def actionPolicy(self,policy):
        action = np.max(policy)
        return action
