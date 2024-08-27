# Fixedwing Dogfighting RL Agent

## Getting Started
To get started developing using repo, checkout the [GETTING_STARTED.md](GETTING_STARTED.md)

## The Algorithm
The *Proximal Policy Optimzation* algorithm is a neural network architecture that is an actor-critic model that helps stabilize training and reducing variance by 
 - Controlling how our agent behaves (policy) -> smaller updates during training are more likely to converge
 - Measures how good the action taken is

It improves stability by avoiding policy updates that are *too big*, ensuring that the  

Read more:
 - From [Huggingface](https://huggingface.co/learn/deep-rl-course/unit8/introduction)
 - From [OpenAI](https://spinningup.openai.com/en/latest/algorithms/ppo.html)
 
## TODO
- [x] Decide what RL algorithm to use
- [ ] Train
- [ ] Simulate