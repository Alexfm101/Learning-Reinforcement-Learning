import gym
import numpy as np


env =  gym.make('CartPole-v0')

#variables
actions = env.action_space
Q = []
N = []
test = [1,2,3,4,5,6]
eps = 0.5
for i in range(actions.n):
    Q.append(0)
    N.append(0)

#functions

def bandit(a,env):
    observation, reward, done, info = env.step(a)
    return reward
    pass

#exploration explotation trade off
while True:
    env.reset()
    for t in range(100):


        a = actions.sample()
        reward  = bandit(a,env)
        print(a)
