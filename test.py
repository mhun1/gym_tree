import gym

env = gym.make('gym_tree:learning_env-v0')

for _ in range(10):
  #env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  print(action)
  #print(env.action_space.sample())
  #print(env.observation_space.sample())
  #observation, reward, done, info = env.step(action)




env.close()
