import gym
import numpy as np


env =  gym.make('Acrobot-v1')

#variables
actions = env.action_space
Q = []
N = []
test = [1,2,3,4,5,6]
eps = 0.7
A = 0
#initialize Q and N for every action
for i in range(actions.n):
    Q.append(0)
    N.append(0)



#exploration explotation trade off
for episodes in range(1,20):
    env.reset()
    for t in range(100):
        env.render()
        p = np.random.uniform(0,1)
        a = actions.sample()

        if p > eps:
            A = np.argmax(Q)
            print("primero",A)
        else:
            A = np.random.choice(range(actions.n))
            print("segundo",A)

        observation, reward, done, info = env.step(A)

        R = reward
        N[A] = N[A] + 1
        Q[A] = Q[A] + (1/N[A])*(R-Q[A])
        print("variable Q ",Q)
        print("variable N", N)
        if done:
            print("termine")
            break
env.close()
