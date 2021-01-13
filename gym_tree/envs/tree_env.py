import gym
from gym import error, spaces, utils
from gym.utils import seeding

class TreeEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):


    # Action Space is the 

    self.action_space = None


    # Observation Space is the current encoding (string form)

    self.observation_space = None


    pass

  def step(self, action):
    pass

  def reset(self):
    pass

  def render(self, mode='human'):
    pass

  def close(self):
    pass