import gym


class RandomAgent(object):
    """docstring for RandomAgent."""

    def __init__(self, action_space):
        self.action_space = action_space

    def action(self,observation,reward,done):
        return self.action_space.sample()
