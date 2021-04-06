# Multi Armed Bandits

## k-armed bandit problem

In this case you are facing repeatedly with a choice among k different actions. After each choice, you receive a reward chosen from a stationary probability distribution that depends on the action that you selected.

Your objective is to maximize the expect total reward over some period of time. One Example is the game of guess where the coin is under a spleen. Each spleen is the "k", your action is to select a spleen and when you guessed where is the coin you receive a reward (10$) you have to maximize the mount of money that you receive in a period of time.

In each "k" action we have a expected reward given that that action is selected, its call de "Value of the action".  

<!-- falta agregar las ecuaciones de value action pag 26 sutton -->

When you mantain estimates values of the action, at any time step, there is a least one of the actions with a greatest value. This actions are called **Greedy action** and when you use it, it is called **exploiting** and when you not select one of this actions you are **exploring**. 

**Exploitation** is good when you need maximize the expected reward on the one time step, but **exploration** may produce greater total reward in the long run. It is not posible to exploit or explore at the same action selection.

## methods to balance exploration and exploitation





