# First demo using "pendulo invertido" for learn how to write code for using gym

import sys
import gym
from agents.randomAgent import RandomAgent


#define enviroment

env = gym.make('CartPole-v1')

#define agent

agent = RandomAgent(env.action_space)

reward = 0
done = False


#training

for episodes in range(5):

    #inicializo el entrenamiento
    observation = env.reset()

    while True:
        env.render()
        action = agent.action(observation,reward,done)
        observation,reward,done,info = env.step(action)
        if done:
            print(observation)
            break



env.close()
