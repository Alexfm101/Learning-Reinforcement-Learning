# First demo using "pendulo invertido" for learn how to write code for using gym

import sys
import gym
from agents.randomAgent import RandomAgent
import numpy as np

#define enviroment

env = gym.make('MountainCar-v0')

#define agent

agent = RandomAgent(env.action_space,env.observation_space)

reward = 0
done = False


#training

for episodes in range(5):

    #estado inicial del episodio
    observation = env.reset()

    print("estado inicial")
    print(env.observation_space.sample())
    count = 0
    while True:
        env.render()

        #accion del agente
        action = agent.actionSample(observation,reward,done)

        #estado actual del ambiente
        state = agent.state(observation,reward,done)

        observation,reward,done,info = env.step(action)
        print("estado {}".format(count))
        print(state)
        print("accion")
        print(action)
        count = count + 1
        if done:
            print("termine")
            break



env.close()
