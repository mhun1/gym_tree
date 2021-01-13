import gym

env = gym.make('gym_tree:tree-v0')
observation = env.reset()



#POSSIBLE ACTIONS:

# ADD NODE TO TREE
## -> binary operators -> +,-,*,/
## -> constants
# ADD NOTHING TO TREE
# DELETE NODE OF TREE

# REWARDS:

# if TREE DEPTH is small -> give positive reward if adding node
# if TREE DEPTH is too high -> give negative reward if adding node
# stop at a high TREE DEPTH -> done=True



for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  if done:
    observation = env.reset()
env.close()