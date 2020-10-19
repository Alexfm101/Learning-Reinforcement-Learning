import  gym
import  numpy as np
env = gym.make('CartPole-v1')

class randomAgent():
    def  __init__(self):
        pass




for episode in range(20):
    observation = env.reset()
    for timestep in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation,reward,done,info = env.step(action)
        if done:
            print("episode finished after {} timestep".format(timestep + 1))
        pass
    pass
