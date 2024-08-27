import numpy as np
import gymnasium as gym
from PyFlyt.pz_envs.fixedwing_envs.ma_fixedwing_dogfight_env import (
    MAFixedwingDogfightEnv as DogFight,
)

# Environment Rules
#     This is a cannons only environment. Meaning there are no missiles.
#     An agent has to point its nose directly at the enemy for it to be considered a hit.
#     The gun is only effective within lethal range. Outside of this range, the gun deals no damage.
#     The gun automatically fires when it can, there is no action for the agent to fire the weapon.
#     This is similar to many fire control systems on modern aircraft.
#     An agent loses if it: a) Hits anything b) Flies out of bounds c) Loses all its health

env = DogFight(render_mode="human")
observations, infos = env.reset()
while env.agents:
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}

    observations, rewards, terminations, truncations, infos = env.step(actions)
    env.render()
env.close()
