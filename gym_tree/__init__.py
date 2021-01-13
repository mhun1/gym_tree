from gym.envs.registration import register

register(
    id='tree-v0',
    entry_point='gym_tree.envs:TreeEnv',
)
