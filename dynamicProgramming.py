
import gym
import numpy as np
from agents.randomAgent import RandomAgent
#enviroment
env = gym.make('FrozenLake-v0')

#randomPolicy
def randomPolicy(states,actions):
    return np.ones([observations,actions])/actions

def policyEvaluation(policy,gamma):
    vs = np.zeros(observations)
    while delta > theta:
        delta = 0
        for observation in range(observations):
            v = vs[observation]
            for action action_prop in enumerate(policy[observation]):
                #not finished

            delta = max(delta,np.abs(v-vs[observation]))

    return vs

policy = randomPolicy(env.observation_space.n,env.action_space.n)

#agente

agent = RandomAgent(env.action_space,env.observation_space)


for episodes in range(5):
    observation = env.reset()
    print("-----------episodio {}-----------".format(episodes))
    while True:
        env.render()

        #toma una accion de acuerdo a una politica random
        action = agent.actionPolicy(policy[observation])
        print(action)

        #realizar la accion
        observation,reward,done,info = env.step(action)

        if done:
            print("termine")
            break
