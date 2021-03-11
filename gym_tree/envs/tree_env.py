import gym
from gym import error, spaces, utils
from gym.utils import seeding

class LearningEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, num_actions=8, num_parameters=3):

    # possible amount of actions
    self.action_space = spaces.Discrete(num_actions*num_parameters)

    # TP | TN | FP | FN
    self.observation_space = spaces.Box(0.0,1e7,(4,))
    self.num_actions = num_actions
    self.num_parameters = num_parameters

  def decode_action(self, action):
      i = 1
      while i <= self.num_parameters:
        if action < i * self.num_actions:
          break
        i += 1
      return (action % self.num_actions, i)

  def step(self, action):
    pass

  def reset(self):
    pass

  def render(self, mode='human'):
    pass

  def close(self):
    pass