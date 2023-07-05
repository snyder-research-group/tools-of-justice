import random
import numpy as np
from numpy.random import randint, rand
from behavior_reference import BEHAVIOR_ARCHETYPE_PARAMETERS


class Agent:
    """ Class which defines agents within the YouTube simulation. Stores agent characteristics, current state and log. """
    def __init__(self, currently_watching, archetype, agent_id, log):
        self.currently_watching = currently_watching;
        self.archetype = archetype;   # starts off with no archetype defined
        self.agent_id = agent_id; # unique identification number for agent
        self.log = log; # logs agent history as text

    def is_watching(self):
        return self.currently_watching
    
    def watching(self):
        self.currently_watching = True


    # So, what's the goal here? An agent's status is watching a video or not. Their attributes include their archetype and agent_id. 
    # State is stored in currently_watching.
    # An agent watches a video (how they decide which video to watch is more complicated), then may or may not click on another video.
    # In a given YouTube session, we need to keep track of the user's activities, and add up how many minutes of video they are watching.





# a = Agent()
# print("Is this person watching a video currently?: " + str(a.is_watching())) # the person is not watching by default
# a.watching() # the person clicks on a video
# print("Is this person watching a video currently?: " + str(a.is_watching())) # the person is now watching


# # Now, what we want to do is simulate how this idea spreads through a population. 
# # Say that there are N people in the population, and each day each person talks to k random other people. 
# # If someone talks to someone else who is watching a video, then the new person also begins to watch a video 
# # with probability p. 
# # We’ll start with one watching person and keep track of how the idea spreads

# N = 1000 # population size
# k = 5     # number of people each person talks to
# p = 0.1   # probability that someone is watching a video

# pop = [Agent() for i in range(N)] # our population
# pop[0].watching()


# # now let’s write a function that will simulate all interactions in a day

# for i in range(N):
#     if pop[i].is_watching():
#         # person i tells all their contacts to watch a video
#         contacts = randint(N, size=k)
#         for j in contacts:
#             if rand() < p:
#                 pop[j].watching()


# # we want to count how many people are watching a video at the end of the day
# def count_watching(pop):
#     return sum(p.is_watching() for p in pop)

# print(count_watching(pop))


# # now let’s see how the watching population changes over time
# T = 100 # number of days to simulate
# counts = [count_watching(pop)]
# for t in range(T):
#     # update the population
#     for i in range(N):
#         if pop[i].is_watching():
#             # person i enlightens all their contacts
#             contacts = randint(N, size=k)
#             for j in contacts:
#                 if rand() < p:
#                     pop[j].watching()
                    
#     # add to our counts
#     counts.append(count_watching(pop))

# import matplotlib.pyplot as plt

# plt.plot(counts)
# plt.show()
