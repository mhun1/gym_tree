from gym.envs.registration import register

register(
    id='learning_env-v0',
    entry_point='gym_tree.envs:LearningEnv',
)
