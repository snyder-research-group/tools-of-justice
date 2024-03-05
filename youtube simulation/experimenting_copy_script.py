# %% [markdown]
# # YouTube Simulation: Just Middle Agents (in notebook form)

# %% [markdown]
# ### Initializing environment packages and variables 📚

# %%
# Importing libraries/packages
import random
import numpy as numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from tqdm.notebook import tqdm

# Importing class files
from agent import Agent
from video import Video
from activity import Activity
from behavior_reference import BEHAVIOR_ARCHETYPE_PARAMETERS
from behavior_reference import AGENT_ARCHETYPE_DISTRIBUTION

# %%
# Defining our macro values to be referenced later on
NUM_VIDEOS = 10000;
NUM_AGENTS = 100;
RAND_SYSTEM_TOGGLE = False
REC_SYSTEM_TOGGLE = False
SCORE_SYSTEM_TOGGLE = True

# %% [markdown]
# ### Creation of Video Objects 🎥

# %%

# Generate random view count (views range from 1 to 1 million)

# random seed
random.seed(27)

random_view_counts = []
for i in range(NUM_VIDEOS):
    r = random.randint(1, 1000000)
    random_view_counts.append(r)


# Generate random (unique) video ids
# resultant random numbers list
random_video_ids = []
extremeness_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# traversing the loop 1000 times
for i in range(NUM_VIDEOS):

    # r=random.randint(1,100000)
    # # checking whether the generated random number is not in the
    # # randomList
    # if r not in random_video_ids:
    #     # appending the random number to the resultant list, if the condition is true
        random_video_ids.append(i)


# Generate random video length
random_vid_lengths = []
for i in range(NUM_VIDEOS):
    r = random.randint(1, 80)
    random_vid_lengths.append(r)

# Generate random video extremeness
random_extremeness = []
for i in range(NUM_VIDEOS):
    r = random.choice(extremeness_values)
    random_extremeness.append(r)


# Generate random number of thumbs up
random_thumbs_up = []
for i in range(NUM_VIDEOS):
    r = random.randint(0, 50000)
    random_thumbs_up.append(r)


# Use the above arrays to create video objects
all_videos = []
for i in range(NUM_VIDEOS):   # create videos


    # Grab the data points for the video
    views = random_view_counts[i];
    vid_id = random_video_ids[i];
    length = random_vid_lengths[i];
    extremeness = random_extremeness[i];
    thumbs_up = random_thumbs_up[i];

    # Create the video object
    random_vid = Video(views, vid_id, length, extremeness, thumbs_up);

    # Add the video object to our array of videos
    all_videos.append(random_vid);

# %% [markdown]
# In the cell below, we can test that the video objects are created properly.

# %%
# Let's make sure this worked.

# print("Information for the first three videos:");
# for i in range(3):
#     print("Views: " + str(all_videos[i].views));
#     print("Video ID: " + str(all_videos[i].vid_id));
#     # print("Length: " + str(all_videos[i].length) +  " minutes");
#     print("Extremeness: " + str(all_videos[i].extremeness));
#     # print("Thumbs up count: " + str(all_videos[i].thumbs_up));
#     print("");

# # # Let's test the watch function
# for i in range(10):
#     Activity.watch(all_videos[i])

# %% [markdown]
# ### Creating our Agents 👩‍🔬


# %% [markdown]
# Completely Random Agent Creation:

# %%
# We need to generate a random value for each agent attribute, then compile those into one agent object.
# Currently, their preferences are generated from the archetype. Thus, we need a different method to create the agents.
# Maybe make a dummy archetype for each agent, that happens in each run of the for loop? Where each agent's attributes are generated?
from random import randint
from behavior_reference import BEHAVIOR_ARCHETYPE_PARAMETERS

# random seed
random.seed(27)

our_agents = [];    # holds all of our agents
id_counter = 0;     # creates an ID number for each agent

archetypes_list = []

for i in range(NUM_AGENTS):    

    # We need to create a dummy archetype here, then assign that to the user.
    # Can we just add one to the archetype distribution file, where all values are randomly generated?
    # Dummy archetype with random values generated for each field
    rand_video_threshold = randint(15,90)
    rand_yt_time_threshold = randint(45,120)
    affiliations = ['left', 'right', 'middle']
    rand_political_affiliation = random.choice(affiliations)
    rand_video_extremity = random.random()  # don't use a random float   
    # video_extremities = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # rand_video_extremity = random.choice(video_extremities)
    rand_popularity_threshold = randint(2000,500000)


    target_dict = {}


    random_archetype = {
        "longest_vid_threshold": rand_video_threshold,   #will watch videos up to 1.5 hours long
        "yt_time_threshold": rand_yt_time_threshold,       #will spend up to two hours on YouTube per day
        "political_affiliation":  rand_political_affiliation,
        "video_extremity": rand_video_extremity,         #will watch videos that rate high on extreme-ness
        "popularity_threshold": rand_popularity_threshold   #will watch any video with at least 2000 views
    }

    for dictionary in random_archetype:
        target_dict.update(random_archetype)

    archetypes_list.append(random_archetype)


    # print(random_archetype["video_extremity"])

    our_agent = Agent(False, archetypes_list[id_counter], id_counter, "");
    our_agents.append(our_agent);
    id_counter += 1;


# %% [markdown]
# Once again, we can grab some data to test that these agents were created successfully.

# %%
# for i in range(6,10):   # just a frew random agents versus showing the whole list
#     print("Agent ID: " + str(our_agents[i].agent_id) + "\tArchetype: " + our_agents[i].archetype);



agent_number = 0

# for i in range(3):
#     daily_agent = our_agents[agent_number]
#     daily_agent_archetype = daily_agent.archetype


#     # Get the values for our agent's archetype

#     daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
#     daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
#     daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
#     daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
#     daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]


#     print("Agent #" + str(agent_number))
#     # print("Archetype: " + str(daily_agent_archetype))
#     print("Overall affiliation: " + str(daily_agent_pol_aff))
#     print("L(a): " + str(daily_agent_longest_vid))
#     print("P(a): " + str(daily_agent_pop_thresh))
#     print("E(a): " + str(daily_agent_vid_extr))
#     print("")

#     agent_number += 1

#     # display_vid_attrs_weighted(all_videos[900])

#     print("")


# %% [markdown]
# ### Simulating a Day 📅

# %% [markdown]
# So, what does an agent do in a given day?
# 
# * Click on a video (they will be provided with a random video at start of day)
#     * Decide to watch the video if it aligns with their archetype parameters
#     * Actually watch the video
#     * Increment the video views
#     * Add the video length to their total time spent watching for today
#     * Flip a coin to determine if a thumbs up is left
#     * If total time spent watching for today is under their archetype's daily limit, find a new video.
#         * If over time, stop watching and end the day.
# 

# %% [markdown]
# #### Defining Functions

# %%
# Function to click on a video (agent will be provided with a random video at start of day)
def suggest_video(video_list, NUM_VIDEOS):
    # With the recommendation algorithm, this will probably become obsolete.
    random_video_id = random.randrange(NUM_VIDEOS);
    return video_list[random_video_id];
    

# Function to print the attributes of a video object
def display_vid_attrs(our_video):
    rand_vid_views = our_video.views
    rand_vid_id = our_video.vid_id
    rand_vid_length = our_video.length
    rand_vid_extremeness = our_video.extremeness
    rand_vid_thumbsup = our_video.thumbs_up

    print("Video ID: " + str(rand_vid_id))
    print("View Count: " + str(rand_vid_views))
    print("Length: " + str(rand_vid_length) + " minutes")
    print("Extremeness: " + str(rand_vid_extremeness))
    print("Thumbs Up Count: " + str(rand_vid_thumbsup))


# Function to display an agent's ID and archetype
def display_agent(our_agent):
    print("Agent ID: " + str(our_agent.agent_id));
    print("Archetype: " + str(our_agent.archetype))


# I copied this from https://www.geeksforgeeks.org/python-reversing-list/#
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

def Average(list):
    avg = sum(list) / len(list)
    return float(avg)



# %% [markdown]
# ### Defining the Scoring System Functions
# 
# From 2/2/24: I'm now trying to loosen some of the extremeness requirements for the scoring system, in order to allow users to watch a greater variety of extremenesses.

# %%
ALPHA_WEIGHT = 0.2    # weight placed on video length
BETA_WEIGHT = 0.15     # weight placed on video popularity
GAMMA_WEIGHT = 0.5     # weight placed on video alignment (how similar extremeness is to user's)
DELTA_WEIGHT = 0.15    # weight placed on extremeness of the video

# %%
def display_vid_attrs_weighted(our_video):
    rand_vid_views = our_video.views
    rand_vid_id = our_video.vid_id
    rand_vid_length = our_video.length
    rand_vid_extremeness = our_video.extremeness

    print("Video #" + str(rand_vid_id))
    print("P(v): " + str(rand_vid_views))
    print("L(v): " + str(rand_vid_length) + " minutes")
    print("E(v): " + str(rand_vid_extremeness))


# Calculates a weighted sum model score for a given user and video.
# The lower the score, the better fit the video is for the agent.
def calculate_score(our_agent, our_video):
    alpha = 0.2     # weight placed on video length
    beta = 0.15    # weight placed on video popularity
    gamma = 0.5     # weight placed on video alignment (how similar extremeness is to user's)
    delta = 0.15    # weight placed on extremeness of the video

    our_agent_archetype = our_agent.archetype

    # Length values
    lv = our_video.length
    la = BEHAVIOR_ARCHETYPE_PARAMETERS[our_agent_archetype]["longest_vid_threshold"]

    # Popularity values
    pv = our_video.views
    pa = BEHAVIOR_ARCHETYPE_PARAMETERS[our_agent_archetype]["popularity_threshold"]

    # Extremeness values
    ev = our_video.extremeness
    ea = BEHAVIOR_ARCHETYPE_PARAMETERS[our_agent_archetype]["video_extremity"]

    score = (alpha * abs(lv-la)) - (beta * abs(pv-pa)) + (gamma * abs(ev-ea)) + (delta * ev)

    return score


# Calculates a weighted sum model score for a given user and list of videos.
# The lower the score, the better fit the video is for the agent.
# This version normalizes by dividing each value by the POSSIBLE max.
def calculate_score_multiple_vids(our_agent, our_videos):
    alpha = ALPHA_WEIGHT     # weight placed on video length
    beta = BETA_WEIGHT     # weight placed on video popularity
    gamma = GAMMA_WEIGHT     # weight placed on video alignment (how similar extremeness is to user's)
    delta = DELTA_WEIGHT    # weight placed on extremeness of the video

    our_agent_archetype = our_agent.archetype
    agent_number = our_agent.agent_id

    video_scores = []

    # Max values for the video qualities
    max_length = 80
    max_pop = 1000000
    max_align = 1
    max_extr = 1


    daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
    daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
    daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
    daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
    daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]


    for i in range(NUM_VIDEOS):
        # Length values
        our_video = our_videos[i]
        l_return = 0  # return value now that we're using a threshold
        lv = our_video.length
        la = archetypes_list[agent_number]["longest_vid_threshold"]
        # agents favor shorter videos. so if lv is > la above the length, give a 0. if lv<la, a 1 or something scaled appropriately.
        if(lv > la):    # video length is greater than our archetype's preference
            l_return = 0
        else:
            # l_return = lv / max_length
            l_return = 1

        # wants videos below threshold---we want the value to be bigger, so this one gets a minus

        # Popularity values
        p_return = -1
        pv = our_video.views
        pa = archetypes_list[agent_number]["popularity_threshold"]
        # logging.debug(print("pv: " + str(pv) + " vs pa: " + str(pa)))
        # make 0 if below threshold, but scaled appropriately if above
        # instead of the abs it;ll be either a zero or a positive number, keep the minus sign
        if(pv < pa): # video popularity is less than our archetype's preference
            # logging.debug(print("pv<a"))
            p_return = 0
        else:
            # logging.debug(print("pv>pa"))
            p_return = 1
            # p_return = pv / max_pop
        
        
        # Extremeness values
        ev = our_video.extremeness
        ea = archetypes_list[agent_number]["video_extremity"]
        e_return = ev

        #added 2/12/24: making sure delta rewards videos on both extreme ends
        # if((ev <= 0.2) or (ev >= 0.8)):
        #     e_return = 0.5
        # else:
        #     e_return = 0



        # For small score = good, + in front of components user wants small, and - for components user wants big
        # + in front of component that YouTube wants small
        score = -(alpha * l_return) - (beta * p_return) + (gamma * (abs(ev-ea)/max_align)) - (delta * e_return)/max_extr

        video_scores.append((i, score))

    # Freeze 1 row, then sort by second column.
    sorted_video_scores = sorted(video_scores,key=lambda x: x[1])

    return sorted_video_scores


# 1/19/24: do profiling (shows how much time different parts of the code take to run)


# for debugging: try setting everything except one var to 0 to see what's hapening
# Maybe an issue with the actual watching portion?


# %% [markdown]
# The below cell tests the functions defined above.

# %%

# Testing with Agent #10

agent_number = 57
daily_agent = our_agents[agent_number]
daily_agent_archetype = daily_agent.archetype

# These two need to be declared OUTSIDE of the run for each video.
# So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
# Otherwise, they don't actually get updated each time.
agent_minutes_watched_today = 0   # how many minutes the agent has watched today
agent_vids_watched_today = 0  # how many videos the agent watched today


# Get the values for our agent's archetype
# The below values are for the completely random agents.
daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]

# daily_agent_longest_vid = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["longest_vid_threshold"]
# daily_agent_yt_threshold = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["yt_time_threshold"]
# daily_agent_pol_aff = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["political_affiliation"]
# daily_agent_vid_extr = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["video_extremity"]
# daily_agent_pop_thresh = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["popularity_threshold"]

# print("Agent #" + str(agent_number))
# print("Archetype: " + str(daily_agent_archetype))
# print("Overall affiliation: " + str(daily_agent_pol_aff))
# print("L(a): " + str(daily_agent_longest_vid))
# print("P(a): " + str(daily_agent_pop_thresh))
# print("E(a): " + str(daily_agent_vid_extr))
# print("")
# # display_vid_attrs_weighted(all_videos[900])

# print("")

# Calculates an agent's score for every single video in the list of all videos.
agent_scores = calculate_score_multiple_vids(daily_agent, all_videos)

'''
for i = agent_id:
video_id = sorted_video_scores[i][0]
video score = sorted_video_scores[i][1]
'''


# Freeze 1 row, then sort by second column.
sorted_video_scores = sorted(agent_scores,key=lambda x: x[1])

# Shows the top ten scoring videos for the provided agent.
# for i in range(1000):
#     video_extremeness = all_videos[sorted_video_scores[i][0]].extremeness
#     print("Video ID: " + str(sorted_video_scores[i][0]) + "\tScore: " + str(sorted_video_scores[i][1]) +"\tExtremeness: " + str(video_extremeness))

# To minimize score: sort in ascending order
# Component of weighted sum/score: does the user want that to be big or small?
# For small score = good, + in front of components user wants small, and - for components user wants big


# Potentially have a dictionary where the keys are the video ids and the values are the objects
# Once you have all the videos you can just write a dictionary comprehension (Python term), see below:
# lookup_dict = {vid[id]: vid for vid in all_videos}
# for each vid in all_videos, add an entry to this dictionary where the entry is the ID, colon, video
# now you'll have a dictionary that lets you look up the object for any video id

lookup_dict = {vid.vid_id: vid for vid in all_videos}
# We have to pass the ID from the scoring array into lookup_dict[put the id from the scoring array here]
# print(lookup_dict[sorted_video_scores[5525][0]])
# display_vid_attrs(lookup_dict[sorted_video_scores[1][0]])

# # '''
# # Recall that for i = agent_id:
# # video_id = sorted_video_scores[i][0]
# # video score = sorted_video_scores[i][1]
# # lookup_dict[video_id]
# # '''


# # e.g. to get video of id #6449, lookup_dict[6449]. This would just return the video object!



# %% [markdown]
# #### The Daily Simulation Code
# 
# The below code is where all of the watching actually happens for each agent.
# As of now, it only runs for one day, but making more days is as simple as just putting everything inside a  ```for i in range(NUM_DAYS)``` loop.



ALPHA_WEIGHT = 0.2    # weight placed on video length
BETA_WEIGHT = 0.15     # weight placed on video popularity
GAMMA_WEIGHT = 0.5     # weight placed on video alignment (how similar extremeness is to user's)
DELTA_WEIGHT = 0.15    # weight placed on extremeness of the video


gamma_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
gamma_lines_extr = []    # needs to hold the xy values (x_score and y_score)
gamma_lines_min = []
gamma_lines_vids = []


for g in range(len(gamma_values)):  # runs for each gamma value
    print("gamma: " + str(gamma_values[g]))

    # need to pass each of these gamma values into the simulation
    # and then put x_score and y_score into a 2D array so those tuples can be graphed (all on the same graph)

    def calculate_score_multiple_vids_test(our_agent, our_videos, alpha, beta, gamma, delta):
        alpha = alpha     # weight placed on video length
        beta = beta     # weight placed on video popularity
        gamma = gamma     # weight placed on video alignment (how similar extremeness is to user's)
        delta = delta    # weight placed on extremeness of the video

        our_agent_archetype = our_agent.archetype
        agent_number = our_agent.agent_id

        video_scores = []

        # Max values for the video qualities
        max_length = 80
        max_pop = 1000000
        max_align = 1
        max_extr = 1

        daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
        daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
        daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
        daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
        daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]


        for i in range(NUM_VIDEOS):
            # Length values
            our_video = our_videos[i]
            l_return = 0  # return value now that we're using a threshold
            lv = our_video.length
            la = archetypes_list[agent_number]["longest_vid_threshold"]
            # agents favor shorter videos. so if lv is > la above the length, give a 0. if lv<la, a 1 or something scaled appropriately.
            if(lv > la):    # video length is greater than our archetype's preference
                l_return = 0
            else:
                # l_return = lv / max_length
                l_return = 1

            # wants videos below threshold---we want the value to be bigger, so this one gets a minus

            # Popularity values
            p_return = -1
            pv = our_video.views
            pa = archetypes_list[agent_number]["popularity_threshold"]
            # logging.debug(print("pv: " + str(pv) + " vs pa: " + str(pa)))
            # make 0 if below threshold, but scaled appropriately if above
            # instead of the abs it;ll be either a zero or a positive number, keep the minus sign
            if(pv < pa): # video popularity is less than our archetype's preference
                # logging.debug(print("pv<a"))
                p_return = 0
            else:
                # logging.debug(print("pv>pa"))
                p_return = 1
                # p_return = pv / max_pop
            
            
            # Extremeness values
            ev = our_video.extremeness
            ea = archetypes_list[agent_number]["video_extremity"]
            e_return = ev

            #added 2/12/24: making sure delta rewards videos on both extreme ends
            # if((ev <= 0.2) or (ev >= 0.8)):
            #     e_return = 0.5
            # else:
            #     e_return = 0

            # For small score = good, + in front of components user wants small, and - for components user wants big
            # + in front of component that YouTube wants small
            score = -(alpha * l_return) - (beta * p_return) + (gamma * (abs(ev-ea)/max_align)) - (delta * e_return)/max_extr

            video_scores.append((i, score))

        # Freeze 1 row, then sort by second column.
        sorted_video_scores = sorted(video_scores,key=lambda x: x[1])

        return sorted_video_scores



    ## Run simulation


        
    total_minutes_watched_today = 0   # how many minutes the agent has watched today
    total_vids_watched_today = 0  # how many videos the agent watched today
    agent_minutes_watched_today_array = []
    agent_vids_watched_today_array = []
    agent_extremeness_array = []
    videos_watched_extremeness_array = []
    extr_of_each_agent_video_all = []

    '''
    Change the ERROR below to DEBUG to trigger all of the print statements. 
    They're there mostly as tests from when I was debugging and such.
    However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
    '''
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)



    for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents
        
        # print("AGENT #" + str(i))
        # Establishing the values we need from our agent before any videos are watched
        daily_agent = our_agents[i]
        agent_number = daily_agent.agent_id
        extr_of_each_agent_video = []
        daily_agent_archetype = daily_agent.archetype

        # These two need to be declared OUTSIDE of the run for each video.
        # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
        # Otherwise, they don't actually get updated each time.
        agent_minutes_watched_today = 0   # how many minutes the agent has watched today
        agent_vids_watched_today = 0  # how many videos the agent watched today

        activity_log = []  # ids of the videos the agent watched today


        # Get the values for our agent's archetype

        daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
        daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
        daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
        daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
        daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]

        
        our_agents_videos = all_videos


        time_left_check = True; # means we have enough time for the agent to keep watching videos


        # From 11/5/23: using the score ranking system
        agent_scores = calculate_score_multiple_vids_test(daily_agent, all_videos, ALPHA_WEIGHT, BETA_WEIGHT, gamma_values[g], DELTA_WEIGHT)
        lookup_dict = {vid.vid_id: vid for vid in all_videos}



        # This is where the agent is actually watching videos.

        while(time_left_check == True):


            j = 0   # j is the counter for iterating through the scored videos after each watch.
            # suggested_video = lookup_dict[j]

            suggested_video = suggest_video(our_agents_videos, len(our_agents_videos))

            # Compare our agent's thresholds to the attributes of the video


            # Check minimum view threshold
            if(suggested_video.views >= daily_agent_pop_thresh):
                popularity_check = True
                logging.debug("Video is popular enough.")
            else:
                popularity_check = False
                logging.debug("Video is not popular enough.")

            # Check agent's max viewing length
            if(suggested_video.length < daily_agent_longest_vid):
                length_check = True
                logging.debug("Video is proper length.")
            else:
                length_check = False
                logging.debug("Video is too long.")

            # Check if watching this video would exceed the agent's daily threshold
            potential_mins_watched = agent_minutes_watched_today + suggested_video.length
            if(potential_mins_watched < daily_agent_yt_threshold):
                time_left_check = True
                logging.debug("Still time to watch this video.")
            else:
                time_left_check = False
                logging.debug("Not enough time left to watch this video.")

            # Check if this video is too extreme for the agent.


        
            # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
            if(daily_agent_pol_aff == "left"):
                # Will not watch anything under 0.5 extremeness
                # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
                if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
                    extreme_check = False
                    logging.debug("Video was too extreme.")
                else:
                    extreme_check = True
                    logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
            elif(daily_agent_pol_aff == "right"):
                # Will not watch anything above 0.5 extremeness
                # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
                if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
                    extreme_check = False
                    logging.debug("Video was too extreme.")
                else:
                    extreme_check = True
                    logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
            elif(daily_agent_pol_aff == "middle"):
                # print("Extremeness:" + str(suggested_video.extremeness))
                # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
                if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                    
                    extreme_check = False
                    logging.debug("Video was too extreme.")
                else:
                    extreme_check = True 

            # Other todo: find whatever bug/anomaly we mentioned was there

            Activity.watch(suggested_video)     # Agent actually watches the video.
            videos_watched_extremeness_array.append(suggested_video.extremeness)
            extr_of_each_agent_video.append(suggested_video.extremeness)
            agent_minutes_watched_today = agent_minutes_watched_today + suggested_video.length
            agent_vids_watched_today = agent_vids_watched_today + 1
            j += 1  # increments the iterator for the scored list videos 


            
        
        # From below here, the agent is done watching videos for the day

        total_minutes_watched_today = total_minutes_watched_today + agent_minutes_watched_today
        total_vids_watched_today = total_vids_watched_today + agent_vids_watched_today

        agent_minutes_watched_today_array.append(agent_minutes_watched_today)
        agent_vids_watched_today_array.append(agent_vids_watched_today)
        extr_of_each_agent_video_all.append(Average(extr_of_each_agent_video))
        
        
        # This array needs to get the extremeness threshold of each agent
        agent_extremeness_array.append(daily_agent_vid_extr)

        logging.debug("\nVideos watched today: " + str(agent_vids_watched_today))
        logging.debug("Minutes watched today: " + str(agent_minutes_watched_today))

    
    avg_videos_watched_extremeness_array = (sum(videos_watched_extremeness_array) / len(videos_watched_extremeness_array))



    if(SCORE_SYSTEM_TOGGLE):

        import statistics as statistics
        from statistics import mean
            
        total_minutes_watched_today_scoring = 0   # how many minutes the agent has watched today
        total_vids_watched_today_scoring = 0  # how many videos the agent watched today
        agent_minutes_watched_today_array_scoring = []
        agent_vids_watched_today_array_scoring = []
        agent_extremeness_array_scoring = []
        videos_watched_extremeness_array_scoring = []
        extr_of_each_agent_video_all_scoring = []
        j = 0

        '''
        Change the ERROR below to DEBUG to trigger all of the print statements. 
        They're there mostly as tests from when I was debugging and such.
        However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
        '''
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)


        for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents
            
            # print("AGENT #" + str(i))
            # Establishing the values we need from our agent before any videos are watched
            daily_agent = our_agents[i]
            agent_number = daily_agent.agent_id
            extr_of_each_agent_video_scoring = []

            # display_agent(daily_agent)
            # daily_agent_archetype = daily_agent.archetype     commented out 1/23/24 because it's not doing anything

            # These two need to be declared OUTSIDE of the run for each video.
            # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
            # Otherwise, they don't actually get updated each time.
            agent_minutes_watched_today_scoring = 0   # how many minutes the agent has watched today
            agent_vids_watched_today_scoring = 0  # how many videos the agent watched today


            activity_log = []  # ids of the videos the agent watched today


            # Get the values for our agent's archetype

            daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
            daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
            daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
            daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]

            
            
            agent_extremeness_array_scoring.append(daily_agent_vid_extr)


            daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]



            # When the recommendation system is toggled, gets our agent's pre-filtered list of videos based on their archetype.
            # For this cell, that check does not happen.

            our_agents_videos = all_videos


            time_left_check = True; # means we have enough time for the agent to keep watching videos

            agent_scores = calculate_score_multiple_vids_test(daily_agent, all_videos, ALPHA_WEIGHT, BETA_WEIGHT, gamma_values[g], DELTA_WEIGHT)
        
            
            lookup_dict = {vid.vid_id: vid for vid in all_videos}


            # This is where the agent is actually watching videos.

            while(time_left_check == True):

                suggested_video = lookup_dict[agent_scores[j][0]]

                # Comparing our agent's thresholds to the attributes of the video


                # Check minimum view threshold
                if(suggested_video.views >= daily_agent_pop_thresh):
                    popularity_check = True
                    logging.debug("Video is popular enough.")
                else:
                    popularity_check = False
                    logging.debug("Video is not popular enough.")

                # Check agent's max viewing length
                if(suggested_video.length < daily_agent_longest_vid):
                    length_check = True
                    logging.debug("Video is proper length.")
                else:
                    length_check = False
                    logging.debug("Video is too long.")

                # Check if watching this video would exceed the agent's daily threshold
                potential_mins_watched = agent_minutes_watched_today_scoring + suggested_video.length
                if(potential_mins_watched < daily_agent_yt_threshold):
                    time_left_check = True
                    logging.debug("Still time to watch this video.")
                else:
                    time_left_check = False
                    logging.debug("Not enough time left to watch this video.")

                # Check if this video is too extreme for the agent.

            
                # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
                if(daily_agent_pol_aff == "left"):
                    # Will not watch anything under 0.5 extremeness
                    # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
                    if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
                        extreme_check = False
                        logging.debug("Video was too extreme.")
                    else:
                        extreme_check = True
                        logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
                elif(daily_agent_pol_aff == "right"):
                    # Will not watch anything above 0.5 extremeness
                    # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
                    if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
                        extreme_check = False
                        logging.debug("Video was too extreme.")
                    else:
                        extreme_check = True
                        logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
                elif(daily_agent_pol_aff == "middle"):
                    # print("Extremeness:" + str(suggested_video.extremeness))
                    # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
                    if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                        
                        extreme_check = False
                        logging.debug("Video was too extreme.")
                    else:
                        extreme_check = True 

                # Other todo: find whatever bug/anomaly we mentioned was there

                Activity.watch(suggested_video)     # Agent actually watches the video.
                videos_watched_extremeness_array_scoring.append(suggested_video.extremeness)
                extr_of_each_agent_video_scoring.append(suggested_video.extremeness)
                agent_minutes_watched_today_scoring = agent_minutes_watched_today_scoring + suggested_video.length
                agent_vids_watched_today_scoring = agent_vids_watched_today_scoring + 1 

                j = j+1

        
            
            # From below here, the agent is done watching videos for the day

            total_minutes_watched_today_scoring = total_minutes_watched_today_scoring + agent_minutes_watched_today_scoring
            total_vids_watched_today_scoring = total_vids_watched_today_scoring + agent_vids_watched_today_scoring

            agent_minutes_watched_today_array_scoring.append(agent_minutes_watched_today_scoring)
            agent_vids_watched_today_array_scoring.append(agent_vids_watched_today_scoring)
            extr_of_each_agent_video_all_scoring.append(mean(extr_of_each_agent_video_scoring))
            
            
            # This array needs to get the extremeness threshold of each agent
        

            logging.debug("\nVideos watched today: " + str(agent_vids_watched_today_scoring))
            logging.debug("Minutes watched today: " + str(agent_minutes_watched_today_scoring))


        avg_videos_watched_extremeness_array_scoring = (sum(videos_watched_extremeness_array_scoring) / len(videos_watched_extremeness_array_scoring))
    
    

    ## Append x_score and y_score to 2D array

    #x1 (extremeness graph)
    gamma_lines_extr.append([numpy.arange(0, NUM_AGENTS), Reverse(extr_of_each_agent_video_all_scoring)])

    #x2 (minutes watched graph)    
    gamma_lines_min.append([Reverse(agent_extremeness_array), Reverse(agent_minutes_watched_today_array_scoring)])

    #x3 (vids watched graph)
    gamma_lines_min.append([Reverse(agent_extremeness_array), Reverse(agent_vids_watched_today_array_scoring)])



### AVG EXTREMENESS ################################################################
# %% [markdown]
# Avg. Extremeness of Videos Watched Per Agent Regression

import matplotlib as matplotlib
import pandas as pd

x1 = numpy.arange(0, NUM_AGENTS)
y1 = Reverse(extr_of_each_agent_video_all)



plt.scatter(x1,y1, color = 'white') # A bar chart
# plt.title('Avg. Extremeness of Videos Watched Per Agent', fontsize = 18)
plt.xlabel('Agents (0 - ' + str(NUM_AGENTS-1) + ')')
plt.ylabel('Avg. Extremeness')
# plt.axhline(numpy.nanmean(y), linestyle = '--', color = 'purple')

# defining display layout
plt.tight_layout()

plt.xticks(numpy.arange(0, 101, 10))
plt.yticks(numpy.arange(0, 1.1, 0.1))

#obtain m (slope) and b(intercept) of linear regression line
m, b = numpy.polyfit(x1, y1, 1)

#add linear regression line to scatterplot 
# plt.plot(x, m*x+b, label = "No system", lw = 3)



if(SCORE_SYSTEM_TOGGLE):
    
    x_score1 = numpy.arange(0, NUM_AGENTS)
    y_score1 = Reverse(extr_of_each_agent_video_all_scoring)

    plt.scatter(x_score1,y_score1, color = 'white')
    # plt.title('Avg. Extremeness of Videos Watched Per Agent, w/ Scoring', fontsize = 18)
    plt.xlabel('Agents (0 - ' + str(NUM_AGENTS-1) + ')')
    plt.ylabel('Avg. Extremeness')

    
    # plt.axhline(numpy.nanmean(y), linestyle = '--', color = 'green')

    # defining display layout
    # plt.tight_layout()

    plt.xticks(numpy.arange(0, 101, 10))
    plt.yticks(numpy.arange(0, 1.1, 0.1))



    #obtain m (slope) and b(intercept) of linear regression line
    m_score, b_score = numpy.polyfit(x_score1, y_score1, 1)

    #add linear regression line to scatterplot 
    # plt.plot(x_score, m_score*x_score+b_score)


plt.text(0.4, numpy.nanmean(y1)+0.2, "Avg: " + str(numpy.nanmean(y1)), fontsize = 10)
plt.text(0.4, numpy.nanmean(y_score1)-0.2, "Score Avg: " + str(numpy.nanmean(y_score1)), fontsize = 10)

for g in range(len(gamma_values)):
    gamma_x = gamma_lines_extr[g][0]
    gamma_y = gamma_lines_extr[g][1]
    sns.regplot(x = gamma_x, y = gamma_y, lowess=True, scatter = False, label = gamma_values[g])



plt.title('Avg. Extremeness of Videos Watched Per Agent, By Extremeness', fontsize = 18)
# sns.regplot(x = x1, y = y1, lowess=True, scatter = False, label = "None", line_kws={"color": "midnightblue"})
# # sns.regplot(x = x_rec, y = y_rec, lowess=True, scatter = False, label = "Rec", line_kws={"color": "royalblue"})
# # sns.regplot(x = x_rand, y = y_rand, lowess=True, scatter = False, label = "Rand", line_kws={"color": "cornflowerblue"})
# sns.regplot(x = x_score1, y = y_score1, lowess=True, scatter = False, label = "Score", line_kws={"color": "powderblue"})
plt.legend(labels=['None', '0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'], loc='upper right')

plt.show()


## END AVG EXTREMENESS PER AGENT ###############################################












# # %%
# total_minutes_watched_today = 0   # how many minutes the agent has watched today
# total_vids_watched_today = 0  # how many videos the agent watched today
# agent_minutes_watched_today_array = []
# agent_vids_watched_today_array = []
# agent_extremeness_array = []
# videos_watched_extremeness_array = []
# extr_of_each_agent_video_all = []

# '''
#    Change the ERROR below to DEBUG to trigger all of the print statements. 
#    They're there mostly as tests from when I was debugging and such.
#    However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
# '''
# logger = logging.getLogger()
# logger.setLevel(logging.ERROR)




# for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents
    
#     # print("AGENT #" + str(i))
#     # Establishing the values we need from our agent before any videos are watched
#     daily_agent = our_agents[i]
#     agent_number = daily_agent.agent_id
#     extr_of_each_agent_video = []
#     daily_agent_archetype = daily_agent.archetype

#     # These two need to be declared OUTSIDE of the run for each video.
#     # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
#     # Otherwise, they don't actually get updated each time.
#     agent_minutes_watched_today = 0   # how many minutes the agent has watched today
#     agent_vids_watched_today = 0  # how many videos the agent watched today


#     activity_log = []  # ids of the videos the agent watched today


#     # Get the values for our agent's archetype

#     daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
#     daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
#     daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
#     daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]
#     daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]

#     # daily_agent_longest_vid = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["longest_vid_threshold"]
#     # daily_agent_yt_threshold = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["yt_time_threshold"]
#     # daily_agent_pol_aff = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["political_affiliation"]
#     # daily_agent_vid_extr = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["video_extremity"]
#     # daily_agent_pop_thresh = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["popularity_threshold"]


#     # When the recommendation system is toggled, gets our agent's pre-filtered list of videos based on their archetype.
#     # For this cell, that check does not happen.

#     # note 11/3/23: I am changing our_agents_videos to see what happens with the scoring system. Or at least I need to.
#     # This has to eventually become sorted_video_scores. Either that, or we have to read the video IDs from the second column,
#     # and get all the videos that correspond to those IDs. I'm sure I can figure it out.
#     # Either I use a ton of references (connect the video ID in the scores array to the ID of each video in the big array),
#     # or maybe add the video objects in to the score array??? Would that be easier?
    
#     our_agents_videos = all_videos


#     time_left_check = True; # means we have enough time for the agent to keep watching videos


#     # From 11/5/23: using the score ranking system
#     agent_scores = calculate_score_multiple_vids(daily_agent, all_videos)
#     lookup_dict = {vid.vid_id: vid for vid in all_videos}



#     # This is where the agent is actually watching videos.

#     while(time_left_check == True):


#         j = 0   # j is the counter for iterating through the scored videos after each watch.
#         # suggested_video = lookup_dict[j]

#         # The below line is the original version, without the scoring system.
#         # UNCOMMENT to use the non-scoring system.
#         suggested_video = suggest_video(our_agents_videos, len(our_agents_videos))

#         # display_agent(daily_agent)
#         # # print("")
#         # display_vid_attrs(suggested_video)


#         # Compare our agent's thresholds to the attributes of the video


#         # Check minimum view threshold
#         if(suggested_video.views >= daily_agent_pop_thresh):
#             popularity_check = True
#             logging.debug("Video is popular enough.")
#         else:
#             popularity_check = False
#             logging.debug("Video is not popular enough.")

#         # Check agent's max viewing length
#         if(suggested_video.length < daily_agent_longest_vid):
#             length_check = True
#             logging.debug("Video is proper length.")
#         else:
#             length_check = False
#             logging.debug("Video is too long.")

#         # Check if watching this video would exceed the agent's daily threshold
#         potential_mins_watched = agent_minutes_watched_today + suggested_video.length
#         if(potential_mins_watched < daily_agent_yt_threshold):
#             time_left_check = True
#             logging.debug("Still time to watch this video.")
#         else:
#             time_left_check = False
#             logging.debug("Not enough time left to watch this video.")

#         # Check if this video is too extreme for the agent.


    
#         # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
#         if(daily_agent_pol_aff == "left"):
#             # Will not watch anything under 0.5 extremeness
#             # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
#             if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
#                 extreme_check = False
#                 logging.debug("Video was too extreme.")
#             else:
#                 extreme_check = True
#                 logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
#         elif(daily_agent_pol_aff == "right"):
#             # Will not watch anything above 0.5 extremeness
#             # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
#             if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
#                 extreme_check = False
#                 logging.debug("Video was too extreme.")
#             else:
#                 extreme_check = True
#                 logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
#         elif(daily_agent_pol_aff == "middle"):
#             # print("Extremeness:" + str(suggested_video.extremeness))
#             # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
#             if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                
#                 extreme_check = False
#                 logging.debug("Video was too extreme.")
#             else:
#                 extreme_check = True 

#         # Other todo: find whatever bug/anomaly we mentioned was there

#         Activity.watch(suggested_video)     # Agent actually watches the video.
#         videos_watched_extremeness_array.append(suggested_video.extremeness)
#         extr_of_each_agent_video.append(suggested_video.extremeness)
#         agent_minutes_watched_today = agent_minutes_watched_today + suggested_video.length
#         agent_vids_watched_today = agent_vids_watched_today + 1
#         j += 1  # increments the iterator for the scored list videos 


        
    
#     # From below here, the agent is done watching videos for the day

#     total_minutes_watched_today = total_minutes_watched_today + agent_minutes_watched_today
#     total_vids_watched_today = total_vids_watched_today + agent_vids_watched_today

#     agent_minutes_watched_today_array.append(agent_minutes_watched_today)
#     agent_vids_watched_today_array.append(agent_vids_watched_today)
#     extr_of_each_agent_video_all.append(Average(extr_of_each_agent_video))
    
    
#     # This array needs to get the extremeness threshold of each agent
#     agent_extremeness_array.append(daily_agent_vid_extr)

#     logging.debug("\nVideos watched today: " + str(agent_vids_watched_today))
#     logging.debug("Minutes watched today: " + str(agent_minutes_watched_today))


# avg_videos_watched_extremeness_array = (sum(videos_watched_extremeness_array) / len(videos_watched_extremeness_array))
# # print("TOTAL minutes watched today: " + str(total_minutes_watched_today))
# # print("TOTAL # of videos watched today: " + str(total_vids_watched_today))
# # print("Average extremeness of videos watched today: " + str(avg_videos_watched_extremeness_array))
# # print("Average extremeness per agents, all (almost same as above): " + str(Average(extr_of_each_agent_video_all)))


# # %% [markdown]
# # Below is the code that runs when the scoring system is implemented.

# # %%
# if(SCORE_SYSTEM_TOGGLE):

#     import statistics as statistics
#     from statistics import mean
        
#     total_minutes_watched_today_scoring = 0   # how many minutes the agent has watched today
#     total_vids_watched_today_scoring = 0  # how many videos the agent watched today
#     agent_minutes_watched_today_array_scoring = []
#     agent_vids_watched_today_array_scoring = []
#     agent_extremeness_array_scoring = []
#     videos_watched_extremeness_array_scoring = []
#     extr_of_each_agent_video_all_scoring = []
#     j = 0

#     '''
#     Change the ERROR below to DEBUG to trigger all of the print statements. 
#     They're there mostly as tests from when I was debugging and such.
#     However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
#     '''
#     logger = logging.getLogger()
#     logger.setLevel(logging.ERROR)




#     # For my own sanity, making a sorted array by each archetype because they repeat.
#     # And so each agent doesn't have to sort the entire list of videos.

#     # Create a dummy agent for each archetype.
#     dummy_agents = [];
#     dummy_id_counter = 0;

#     # Generate the progressive activist
#     for i in range(1):    
#         our_agent = Agent(False, "progressive_activist", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;

#     # Generate the traditional liberal
#     for i in range(1):    
#         our_agent = Agent(False, "traditional_liberal", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;

#     # Generate the passive liberal
#     for i in range(1):    
#         our_agent = Agent(False, "passive_liberal", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;
    
#     # Generate the politically disengaged
#     for i in range(1):    
#         our_agent = Agent(False, "politically_disengaged", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;
        
#     # Generate the moderate
#     for i in range(1):    
#         our_agent = Agent(False, "moderate", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;
        
#     # Generate the traditional conservative
#     for i in range(1):    
#         our_agent = Agent(False, "traditional_conservative", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;
    
#     # Generate the devoted conservative
#     for i in range(1):    
#         our_agent = Agent(False, "devoted_conservative", dummy_id_counter, "");
#         dummy_agents.append(our_agent);
#         dummy_id_counter += 1;


#     # Holds the scores for each archetype, so individual agents can call back to this instead of re-calculating each time.
#     progressive_activist_scores = calculate_score_multiple_vids(dummy_agents[0], all_videos)
#     traditional_liberal_scores = calculate_score_multiple_vids(dummy_agents[1], all_videos)
#     passive_liberal_scores = calculate_score_multiple_vids(dummy_agents[2], all_videos)
#     politically_disengaged_scores = calculate_score_multiple_vids(dummy_agents[3], all_videos)
#     moderate_scores = calculate_score_multiple_vids(dummy_agents[4], all_videos)
#     traditional_conservative_scores = calculate_score_multiple_vids(dummy_agents[5], all_videos)
#     devoted_conservative_scores = calculate_score_multiple_vids(dummy_agents[6], all_videos)




#     for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents
        
#         # print("AGENT #" + str(i))
#         # Establishing the values we need from our agent before any videos are watched
#         daily_agent = our_agents[i]
#         agent_number = daily_agent.agent_id
#         extr_of_each_agent_video_scoring = []

#         # display_agent(daily_agent)
#         # daily_agent_archetype = daily_agent.archetype     commented out 1/23/24 because it's not doing anything

#         # These two need to be declared OUTSIDE of the run for each video.
#         # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
#         # Otherwise, they don't actually get updated each time.
#         agent_minutes_watched_today_scoring = 0   # how many minutes the agent has watched today
#         agent_vids_watched_today_scoring = 0  # how many videos the agent watched today


#         activity_log = []  # ids of the videos the agent watched today


#         # Get the values for our agent's archetype

#         daily_agent_longest_vid = archetypes_list[agent_number]["longest_vid_threshold"]
#         daily_agent_yt_threshold = archetypes_list[agent_number]["yt_time_threshold"]
#         daily_agent_pol_aff = archetypes_list[agent_number]["political_affiliation"]
#         daily_agent_vid_extr = archetypes_list[agent_number]["video_extremity"]

        
        
#         agent_extremeness_array_scoring.append(daily_agent_vid_extr)


#         daily_agent_pop_thresh = archetypes_list[agent_number]["popularity_threshold"]



#         # When the recommendation system is toggled, gets our agent's pre-filtered list of videos based on their archetype.
#         # For this cell, that check does not happen.

#         our_agents_videos = all_videos


#         time_left_check = True; # means we have enough time for the agent to keep watching videos

#         agent_scores = calculate_score_multiple_vids(daily_agent, all_videos)
    
        
#         lookup_dict = {vid.vid_id: vid for vid in all_videos}


#         # This is where the agent is actually watching videos.

#         while(time_left_check == True):

#             suggested_video = lookup_dict[agent_scores[j][0]]

#             # Comparing our agent's thresholds to the attributes of the video


#             # Check minimum view threshold
#             if(suggested_video.views >= daily_agent_pop_thresh):
#                 popularity_check = True
#                 logging.debug("Video is popular enough.")
#             else:
#                 popularity_check = False
#                 logging.debug("Video is not popular enough.")

#             # Check agent's max viewing length
#             if(suggested_video.length < daily_agent_longest_vid):
#                 length_check = True
#                 logging.debug("Video is proper length.")
#             else:
#                 length_check = False
#                 logging.debug("Video is too long.")

#             # Check if watching this video would exceed the agent's daily threshold
#             potential_mins_watched = agent_minutes_watched_today_scoring + suggested_video.length
#             if(potential_mins_watched < daily_agent_yt_threshold):
#                 time_left_check = True
#                 logging.debug("Still time to watch this video.")
#             else:
#                 time_left_check = False
#                 logging.debug("Not enough time left to watch this video.")

#             # Check if this video is too extreme for the agent.

        
#             # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
#             if(daily_agent_pol_aff == "left"):
#                 # Will not watch anything under 0.5 extremeness
#                 # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
#                 if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
#             elif(daily_agent_pol_aff == "right"):
#                 # Will not watch anything above 0.5 extremeness
#                 # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
#                 if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
#             elif(daily_agent_pol_aff == "middle"):
#                 # print("Extremeness:" + str(suggested_video.extremeness))
#                 # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
#                 if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                    
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True 

#             # Other todo: find whatever bug/anomaly we mentioned was there

#             Activity.watch(suggested_video)     # Agent actually watches the video.
#             videos_watched_extremeness_array_scoring.append(suggested_video.extremeness)
#             extr_of_each_agent_video_scoring.append(suggested_video.extremeness)
#             agent_minutes_watched_today_scoring = agent_minutes_watched_today_scoring + suggested_video.length
#             agent_vids_watched_today_scoring = agent_vids_watched_today_scoring + 1 

#             j = j+1

    


            
        
#         # From below here, the agent is done watching videos for the day

#         total_minutes_watched_today_scoring = total_minutes_watched_today_scoring + agent_minutes_watched_today_scoring
#         total_vids_watched_today_scoring = total_vids_watched_today_scoring + agent_vids_watched_today_scoring

#         agent_minutes_watched_today_array_scoring.append(agent_minutes_watched_today_scoring)
#         agent_vids_watched_today_array_scoring.append(agent_vids_watched_today_scoring)
#         extr_of_each_agent_video_all_scoring.append(mean(extr_of_each_agent_video_scoring))
        
        
#         # This array needs to get the extremeness threshold of each agent
       

#         logging.debug("\nVideos watched today: " + str(agent_vids_watched_today_scoring))
#         logging.debug("Minutes watched today: " + str(agent_minutes_watched_today_scoring))


#     avg_videos_watched_extremeness_array_scoring = (sum(videos_watched_extremeness_array_scoring) / len(videos_watched_extremeness_array_scoring))
#     # print("TOTAL minutes watched today: " + str(total_minutes_watched_today_scoring))
#     # print("TOTAL # of videos watched today: " + str(total_vids_watched_today_scoring))
#     # print("Average extremeness of videos watched today: " + str(avg_videos_watched_extremeness_array_scoring))
#     # print("Average extremeness per agents, all (almost same as above): " + str(mean(extr_of_each_agent_video_all_scoring)))


# # %% [markdown]
# # Below is the code that runs when the recommendation system (NOT the score system) is set to be toggled. "Recommendation system" is a bit of a misnomer, considering this entire project is recommendation systems; this particular system filters the videos shown to a user by their individual preferences.

# # %%
# if(REC_SYSTEM_TOGGLE):

#     total_minutes_watched_today_rec = 0   # how many minutes the agent has watched today
#     total_vids_watched_today_rec = 0  # how many videos the agent watched today
#     agent_minutes_watched_today_array_rec = []
#     agent_vids_watched_today_array_rec = []
#     agent_extremeness_array_rec = []
#     videos_watched_extremeness_array_rec = []
#     extr_of_each_agent_video_all_rec = []

#     '''
#     Change the ERROR below to DEBUG to trigger all of the print statements. 
#     They're there mostly as tests from when I was debugging and such.
#     However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
#     '''
#     logger = logging.getLogger()
#     logger.setLevel(logging.ERROR)


#     for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents
        
#         # print("AGENT #" + str(i))
#         # Establishing the values we need from our agent before any videos are watched
#         daily_agent = our_agents[i]
#         extr_of_each_agent_video_rec = []
#         daily_agent_archetype = daily_agent.archetype

#         # These two need to be declared OUTSIDE of the run for each video.
#         # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
#         # Otherwise, they don't actually get updated each time.
#         agent_minutes_watched_today_rec = 0   # how many minutes the agent has watched today
#         agent_vids_watched_today_rec = 0  # how many videos the agent watched today


#         activity_log = []  # ids of the videos the agent watched today


#         # Get the values for our agent's archetype

#         daily_agent_longest_vid = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["longest_vid_threshold"]
#         daily_agent_yt_threshold = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["yt_time_threshold"]
#         daily_agent_pol_aff = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["political_affiliation"]
#         daily_agent_vid_extr = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["video_extremity"]
#         daily_agent_pop_thresh = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["popularity_threshold"]


#         # When the recommendation system is toggled, gets our agent's pre-filtered list of videos based on their archetype.
#         # For this cell, that check does not happen.
#         our_agents_videos = filter_vids(all_videos, daily_agent)


#         time_left_check = True; # means we have enough time for the agent to keep watching videos


#         # This is where the agent is actually watching videos.

#         while(time_left_check == True):

#             suggested_video = suggest_video(our_agents_videos, len(our_agents_videos))

#             # display_agent(daily_agent)
#             # # print("")
#             # display_vid_attrs(suggested_video)


#             # Compare our agent's thresholds to the attributes of the video


#             # Check minimum view threshold
#             if(suggested_video.views >= daily_agent_pop_thresh):
#                 popularity_check = True
#                 logging.debug("Video is popular enough.")
#             else:
#                 popularity_check = False
#                 logging.debug("Video is not popular enough.")

#             # Check agent's max viewing length
#             if(suggested_video.length < daily_agent_longest_vid):
#                 length_check = True
#                 logging.debug("Video is proper length.")
#             else:
#                 length_check = False
#                 logging.debug("Video is too long.")

#             # Check if watching this video would exceed the agent's daily threshold
#             potential_mins_watched = agent_minutes_watched_today_rec + suggested_video.length
#             if(potential_mins_watched < daily_agent_yt_threshold):
#                 time_left_check = True
#                 logging.debug("Still time to watch this video.")
#             else:
#                 time_left_check = False
#                 logging.debug("Not enough time left to watch this video.")

#             # Check if this video is too extreme for the agent.


        
#             # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
#             if(daily_agent_pol_aff == "left"):
#                 # Will not watch anything under 0.5 extremeness
#                 # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
#                 if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
#             elif(daily_agent_pol_aff == "right"):
#                 # Will not watch anything above 0.5 extremeness
#                 # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
#                 if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
#             elif(daily_agent_pol_aff == "middle"):
#                 # print("Extremeness:" + str(suggested_video.extremeness))
#                 # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
#                 if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                    
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True 

#             # Other todo: find whatever bug/anomaly we mentioned was there

#             Activity.watch(suggested_video)     # Agent actually watches the video.
#             videos_watched_extremeness_array_rec.append(suggested_video.extremeness)
#             extr_of_each_agent_video_rec.append(suggested_video.extremeness)
#             agent_minutes_watched_today_rec = agent_minutes_watched_today_rec + suggested_video.length
#             agent_vids_watched_today_rec = agent_vids_watched_today_rec + 1


            
        
#         # From below here, the agent is done watching videos for the day

#         total_minutes_watched_today_rec = total_minutes_watched_today_rec + agent_minutes_watched_today_rec
#         total_vids_watched_today_rec = total_vids_watched_today_rec + agent_vids_watched_today_rec

#         agent_minutes_watched_today_array_rec.append(agent_minutes_watched_today_rec)
#         agent_vids_watched_today_array_rec.append(agent_vids_watched_today_rec)

#         extr_of_each_agent_video_all_rec.append(Average(extr_of_each_agent_video_rec))
        
        
#         # This array needs to get the extremeness threshold of each agent
#         agent_extremeness_array_rec.append(daily_agent_vid_extr)

#         logging.debug("\nVideos watched today: " + str(agent_vids_watched_today_rec))
#         logging.debug("Minutes watched today: " + str(agent_minutes_watched_today_rec))


#     avg_videos_watched_extremeness_array_rec = (sum(videos_watched_extremeness_array_rec) / len(videos_watched_extremeness_array_rec))
    
#     # print("TOTAL minutes watched today: " + str(total_minutes_watched_today_rec))
#     # print("TOTAL # of videos watched today: " + str(total_vids_watched_today_rec))
#     # print("Average extremeness of videos watched today: " + str(avg_videos_watched_extremeness_array_rec))
#     # print("Average extremeness per agents, all (almost same as above): " + str(Average(extr_of_each_agent_video_all_rec)))


# # %% [markdown]
# # Below is the code that runs when the random clicking system is set to be toggled.

# # %%
# if(RAND_SYSTEM_TOGGLE):
#     total_minutes_watched_today_rand = 0   # how many minutes the agent has watched today
#     total_vids_watched_today_rand = 0  # how many videos the agent watched today
#     agent_minutes_watched_today_array_rand = []
#     agent_vids_watched_today_array_rand = []
#     agent_extremeness_array_rand = []
#     extr_of_each_agent_video_all_rand = []
#     videos_watched_extremeness_array_rand = []


#     '''
#     Change the ERROR below to DEBUG to trigger all of the print statements. 
#     They're there mostly as tests from when I was debugging and such.
#     However, if you want to see "real-time" info from the simulation as it's running, feel free to uncomment them.
#     '''
#     logger = logging.getLogger()
#     logger.setLevel(logging.ERROR)


#     for i in range(NUM_AGENTS): # runs through the simulation for every agent in our array of agents

        
#         # print("AGENT #" + str(i))
#         # Establishing the values we need from our agent before any videos are watched
#         daily_agent = our_agents[i]
#         daily_agent_archetype = daily_agent.archetype
#         extr_of_each_agent_video_rand = []

#         # These two need to be declared OUTSIDE of the run for each video.
#         # So, declare them within the day for a given agent, but OUTSIDE of the actual video selection checking loop.
#         # Otherwise, they don't actually get updated each time.
#         agent_minutes_watched_today_rand = 0   # how many minutes the agent has watched today
#         agent_vids_watched_today_rand = 0  # how many videos the agent watched today


#         activity_log = []  # ids of the videos the agent watched today


#         # Get the values for our agent's archetype

#         daily_agent_longest_vid = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["longest_vid_threshold"]
#         daily_agent_yt_threshold = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["yt_time_threshold"]
#         daily_agent_pol_aff = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["political_affiliation"]
#         daily_agent_vid_extr = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["video_extremity"]
#         daily_agent_pop_thresh = BEHAVIOR_ARCHETYPE_PARAMETERS[daily_agent_archetype]["popularity_threshold"]


#         # Get our agent's pre-filtered list of videos based on their archetype.
#         our_agents_videos = filter_vids(all_videos, daily_agent)


#         time_left_check = True; # means we have enough time for the agent to keep watching videos


#         # This is where the agent is actually watching videos.

#         while(time_left_check == True):

#             suggested_video = suggest_video(our_agents_videos, len(our_agents_videos))
            

#             # Compare our agent's thresholds to the attributes of the video

#             # Check minimum view threshold
#             if(suggested_video.views >= daily_agent_pop_thresh):
#                 popularity_check = True
#                 logging.debug("Video is popular enough.")
#             else:
#                 popularity_check = False
#                 logging.debug("Video is not popular enough.")

#             # Check agent's max viewing length
#             if(suggested_video.length < daily_agent_longest_vid):
#                 length_check = True
#                 logging.debug("Video is proper length.")
#             else:
#                 length_check = False
#                 logging.debug("Video is too long.")

#             # Check if watching this video would exceed the agent's daily threshold
#             potential_mins_watched = agent_minutes_watched_today_rand + suggested_video.length
#             if(potential_mins_watched < daily_agent_yt_threshold):
#                 time_left_check = True
#                 logging.debug("Still time to watch this video.")
#             else:
#                 time_left_check = False
#                 logging.debug("Not enough time left to watch this video.")

#             # Check if this video is too extreme for the agent.


        
#             # Left-leaning archetypes will watch anything at 0.5 and above. Right-leaning will watch 0.5 and below.
#             if(daily_agent_pol_aff == "left"):
#                 # Will not watch anything under 0.5 extremeness
#                 # If video extremeness is < 0.5 or higher than their extremeness value, do not watch.
#                 if((suggested_video.extremeness < 0.5) or (suggested_video.extremeness > daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between 0.5 and agent's archetype value).")
#             elif(daily_agent_pol_aff == "right"):
#                 # Will not watch anything above 0.5 extremeness
#                 # If video extremeness is > 0.5 or lower than their extremeness value (0.0 is extreme here), do not watch.
#                 if((suggested_video.extremeness > 0.5) or (suggested_video.extremeness < daily_agent_vid_extr)):
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True
#                     logging.debug("Video is within extremeness bounds (between agent's archetype value and 0.5).")
#             elif(daily_agent_pol_aff == "middle"):
#                 # print("Extremeness:" + str(suggested_video.extremeness))
#                 # figuring this archetype is like middle of the road, they'll watch between 0.4 and 0.6
#                 if((suggested_video.extremeness < 0.2) or (suggested_video.extremeness > 0.8)):
                    
#                     extreme_check = False
#                     logging.debug("Video was too extreme.")
#                 else:
#                     extreme_check = True 


            
#             if(RAND_SYSTEM_TOGGLE):
#                 # If all four checks pass, congrats! The agent will watch the video.
#                 # However, we should introduce some randomness to it.
#                 # Users will pick the current video 90% of the time, but have a 10% chance to watch another random video instead.
#                 # A random video, in this case, is one from the list of ALL videos.
#                 rand_vid_chance = random.random()   # generates a number between 0 and 1
#                 if(rand_vid_chance < 0.9):  # 90% chance the user watches videos as normal
#                     if(popularity_check and length_check and time_left_check and extreme_check):
#                         Activity.watch(suggested_video)     # Agent actually watches the video.
#                         agent_minutes_watched_today_rand = agent_minutes_watched_today_rand + suggested_video.length
#                         agent_vids_watched_today_rand = agent_vids_watched_today_rand + 1
#                         # print("\nTotal minutes watched today is now " + str(agent_minutes_watched_today) + ".")
#                 else:   # does a random roll from the list of ALL videos, and the agent watches that.


#                     # TODO: still do the time check!
#                     # Also, make the 90-10% chance thing something you can toggle---maybe you don't want to run it every time.
#                     # Also also, have it so when you DO want to run it, you can put the graphs side by side w/ the orginals.

#                     # Other todo: find whatever bug/anomaly we mentioned was there

#                     surprise_vid = suggest_video(all_videos, len(all_videos))
#                 Activity.watch(suggested_video)     # Agent actually watches the video.
#                 agent_minutes_watched_today_rand = agent_minutes_watched_today_rand + suggested_video.length
#                 agent_vids_watched_today_rand = agent_vids_watched_today_rand + 1
#                 extr_of_each_agent_video_rand.append(suggested_video.extremeness)
#                 videos_watched_extremeness_array_rand.append(suggested_video.extremeness)


            
        
#         # From below here, the agent is done watching videos for the day

#         total_minutes_watched_today_rand = total_minutes_watched_today_rand + agent_minutes_watched_today_rand
#         total_vids_watched_today_rand = total_vids_watched_today_rand + agent_vids_watched_today_rand

#         agent_minutes_watched_today_array_rand.append(agent_minutes_watched_today_rand)
#         agent_vids_watched_today_array_rand.append(agent_vids_watched_today_rand)
#         extr_of_each_agent_video_all_rand.append(Average(extr_of_each_agent_video_rand))
        
        
#         # This array needs to get the extremeness threshold of each agent
#         agent_extremeness_array_rand.append(daily_agent_vid_extr)

#         logging.debug("\nVideos watched today: " + str(agent_vids_watched_today_rand))
#         logging.debug("Minutes watched today: " + str(agent_minutes_watched_today_rand))


#     avg_videos_watched_extremeness_array_rand = (sum(videos_watched_extremeness_array_rand) / len(videos_watched_extremeness_array_rand))


#     # print("TOTAL minutes watched today: " + str(total_minutes_watched_today_rand))
#     # print("TOTAL # of videos watched today: " + str(total_vids_watched_today_rand))
#     # print("Average extremeness of videos watched today: " + str(avg_videos_watched_extremeness_array_rand))
#     # print("Average extremeness per agents, all (almost same as above): " + str(Average(extr_of_each_agent_video_all_rand)))




## GRAPHS ##


### AVG EXTREMENESS ################################################################
# %% [markdown]
# Avg. Extremeness of Videos Watched Per Agent Regression

import matplotlib as matplotlib
import pandas as pd

x1 = numpy.arange(0, NUM_AGENTS)
y1 = Reverse(extr_of_each_agent_video_all)



plt.scatter(x1,y1, color = 'white') # A bar chart
# plt.title('Avg. Extremeness of Videos Watched Per Agent', fontsize = 18)
plt.xlabel('Agents (0 - ' + str(NUM_AGENTS-1) + ')')
plt.ylabel('Avg. Extremeness')
# plt.axhline(numpy.nanmean(y), linestyle = '--', color = 'purple')

# defining display layout
plt.tight_layout()

plt.xticks(numpy.arange(0, 101, 10))
plt.yticks(numpy.arange(0, 1.1, 0.1))

#obtain m (slope) and b(intercept) of linear regression line
m, b = numpy.polyfit(x1, y1, 1)

#add linear regression line to scatterplot 
# plt.plot(x, m*x+b, label = "No system", lw = 3)



if(SCORE_SYSTEM_TOGGLE):
    
    x_score1 = numpy.arange(0, NUM_AGENTS)
    y_score1 = Reverse(extr_of_each_agent_video_all_scoring)

    plt.scatter(x_score1,y_score1, color = 'white')
    # plt.title('Avg. Extremeness of Videos Watched Per Agent, w/ Scoring', fontsize = 18)
    plt.xlabel('Agents (0 - ' + str(NUM_AGENTS-1) + ')')
    plt.ylabel('Avg. Extremeness')

    
    # plt.axhline(numpy.nanmean(y), linestyle = '--', color = 'green')

    # defining display layout
    plt.tight_layout()

    plt.xticks(numpy.arange(0, 101, 10))
    plt.yticks(numpy.arange(0, 1.1, 0.1))



    #obtain m (slope) and b(intercept) of linear regression line
    m_score, b_score = numpy.polyfit(x_score1, y_score1, 1)

    #add linear regression line to scatterplot 
    # plt.plot(x_score, m_score*x_score+b_score)


plt.text(0.4, numpy.nanmean(y1)+0.2, "Avg: " + str(numpy.nanmean(y1)), fontsize = 10)
plt.text(0.4, numpy.nanmean(y_score1)-0.2, "Score Avg: " + str(numpy.nanmean(y_score1)), fontsize = 10)



plt.title('Avg. Extremeness of Videos Watched Per Agent, By Extremeness', fontsize = 18)
sns.regplot(x = x1, y = y1, lowess=True, scatter = False, label = "None", line_kws={"color": "midnightblue"})
# sns.regplot(x = x_rec, y = y_rec, lowess=True, scatter = False, label = "Rec", line_kws={"color": "royalblue"})
# sns.regplot(x = x_rand, y = y_rand, lowess=True, scatter = False, label = "Rand", line_kws={"color": "cornflowerblue"})
sns.regplot(x = x_score1, y = y_score1, lowess=True, scatter = False, label = "Score", line_kws={"color": "powderblue"})
plt.legend(labels=['None', 'Score'])

plt.show()


## END AVG EXTREMENESS PER AGENT ###############################################




## MINUTES WATCHED ###################################################
# %% [markdown]
# Minutes Watched Per Agent, By Extremeness

# %%
# Let's graph each agent's extremeness with how much they watched per day.

import matplotlib as matplotlib

x2 = Reverse(agent_extremeness_array)

y2 = Reverse(agent_minutes_watched_today_array)

# Let's graph each agent with how much they watched per day.
# x axis = agents (0-199), y axis = minutes watched per agent


plt.scatter(x2,y2, color = 'white') # A bar chart
plt.title('Minutes Watched Per Agent', fontsize = 18)
plt.xlabel('Agent Extremeness')
plt.ylabel('Minutes Watched')
# plt.axhline(numpy.nanmean(y), linestyle = '--', color = 'blue')
# plt.text(0.4, numpy.nanmean(y)+ 100, "Avg: " + str(numpy.nanmean(y)), fontsize = 10)

# defining display layout
plt.tight_layout()

plt.yticks(numpy.arange(0, 300, 25))
# plt.show()


if(SCORE_SYSTEM_TOGGLE):
    # Reversing the arrays so extremenesses are in ascending order
        x_score2 = Reverse(agent_extremeness_array_scoring)
        y_score2 = Reverse(agent_minutes_watched_today_array_scoring)


        # Let's graph each agent with how much they watched per day.
        # x axis = agents (0-199), y axis = minutes watched per agent


        plt.scatter(x_score2,y_score2, color = 'white') # A bar chart
        plt.title('Minutes Watched Per Agent, w/ Scoring', fontsize = 18)
        plt.xlabel('Agent Extremeness')
        plt.ylabel('Minutes Watched')
        # plt.axhline(numpy.nanmean(y_score), linestyle = '--', color = 'blue')
        # plt.text(0.4, numpy.nanmean(y_score)+ 100, "Avg: " + str(numpy.nanmean(y_score)), fontsize = 10)

        # defining display layout
        plt.tight_layout()

        plt.yticks(numpy.arange(0, 300, 25))
        
        # plt.show()



plt.title('Minutes Watched Per Agent, By Extremeness', fontsize = 18)
sns.regplot(x = x2, y = y2, lowess=True, scatter = False, label = "None", line_kws={"color": "midnightblue"})
# sns.regplot(x = x_rec, y = y_rec, lowess=True, scatter = False, label = "Rec", line_kws={"color": "royalblue"})
# sns.regplot(x = x_rand, y = y_rand, lowess=True, scatter = False, label = "Rand", line_kws={"color": "cornflowerblue"})
sns.regplot(x = x_score2, y = y_score2, lowess=True, scatter = False, label = "Score", line_kws={"color": "powderblue"})
plt.text(0.3, numpy.nanmean(y2)+4, "Avg: " + str(numpy.nanmean(y2)), fontsize = 10)
plt.text(0.6, numpy.nanmean(y_score2)-5, "Score Avg: " + str(numpy.nanmean(y_score2)), fontsize = 10)
plt.legend(labels=['None', 'Rec', 'Rand', 'Score'])

plt.show()
plt.close()

## END KEEP ###########################################################



## NUMBER OF VIDS WATCHED ###############################################################

# Number of videos watched per agent, by extremeness
# x axis = agents (0-99), y axis = videos watched per agent

x3 = Reverse(agent_extremeness_array)
y3 = Reverse(agent_vids_watched_today_array)

plt.scatter(x3,y3, color = 'midnightblue') # A bar chart
plt.title('Videos Watched Per Agent, by Extr', fontsize = 18)
plt.xlabel('Agents Extremeness')
plt.ylabel('# of Videos Watched')
plt.axhline(numpy.nanmean(y3), linestyle = '--', color = 'hotpink')

# defining display layout
plt.tight_layout()

# Sets y-axis range from min in the array to 20, with intervals of 2
plt.yticks(numpy.arange(min(y3), 10, 2))


# plt.text(0.5, numpy.nanmean(y3) + 1, "Average: " + str(numpy.nanmean(y3)), size=10, rotation=0.,
#          ha="center", va="center",
#          bbox=dict(boxstyle="round",
#                    ec='hotpink',   # edge color: rbg values
#                    fc='pink',   # fill color: rbg values
#                    )
#          )

# plt.show()


if(SCORE_SYSTEM_TOGGLE):
    x_score3 = Reverse(agent_extremeness_array_scoring)
    y_score3 = Reverse(agent_vids_watched_today_array_scoring)

    plt.scatter(x_score3,y_score3, color = 'white') # A bar chart
    plt.title('Videos Watched Per Agent, w/ Scoring, by Extr', fontsize = 18)
    plt.xlabel('Agent Extremeness')
    plt.ylabel('# of Videos Watched')
    # plt.axhline(numpy.nanmean(y_score3), linestyle = '--', color = 'hotpink')

    # defining display layout
    plt.tight_layout()

    # Sets y-axis range from min in the array to 20, with intervals of 2
    plt.yticks(numpy.arange(min(y_score3), 10, 2))

    # plt.text(0.5, numpy.nanmean(y_score) + 1, "Average: " + str(numpy.nanmean(y_score)), size=10, rotation=0.,
    #         ha="center", va="center",
    #         bbox=dict(boxstyle="round",
    #                 ec='hotpink',   # edge color: rbg values
    #                 fc='pink',   # fill color: rbg values
    #                 )
    #         )

    # plt.show()


plt.title('# of Videos Watched Per Agent', fontsize = 18)
sns.regplot(x = x3, y = y3, lowess=True, scatter = False, label = "None", line_kws={"color": "midnightblue"})
# sns.regplot(x = x_rec, y = y_rec, lowess=True, scatter = False, label = "Rec", line_kws={"color": "royalblue"})
# sns.regplot(x = x_rand, y = y_rand, lowess=True, scatter = False, label = "Rand", line_kws={"color": "cornflowerblue"})
sns.regplot(x = x_score3, y = y_score3, lowess=True, scatter = False, label = "Score", line_kws={"color": "powderblue"})
plt.legend(labels=['None', 'Rec', 'Rand', 'Score'])

plt.close() # clear the plot

# plt.show()

## END NUMBER OF VIDS WATCHED ##########################################




## MINUTES WATCHED #####################################################

# %% [markdown]
# Number of vids watched per agent, by extremeness

import matplotlib as matplotlib

x4 = Reverse(agent_extremeness_array)

y4 = Reverse(agent_vids_watched_today_array)

# Let's graph each agent with how much they watched per day.
# x axis = agents (0-199), y axis = minutes watched per agent


# plt.scatter(x4,y4, color = 'white') # A bar chart
# plt.title('# of Videos Watched Per Agent, By Extremeness', fontsize = 18)
plt.xlabel('Agent Extremeness')
plt.ylabel('Minutes Watched')


# defining display layout
# plt.tight_layout()

plt.yticks(numpy.arange(0, 8, 0.5))


if(SCORE_SYSTEM_TOGGLE):
    # Reversing the arrays so extremenesses are in ascending order
        x_score4 = Reverse(agent_extremeness_array_scoring)
        y_score4 = Reverse(agent_vids_watched_today_array_scoring)


        # Let's graph each agent with how much they watched per day.
        # x axis = agents (0-199), y axis = minutes watched per agent


        # plt.scatter(x_score4,y_score4, color = 'white') # A bar chart
        # plt.title('# of Videos Watched Per Agent, w/ Scoring, By Extremeness', fontsize = 18)
        plt.xlabel('Agent Extremeness')
        plt.ylabel('Minutes Watched')



        # defining display layout
        # plt.tight_layout()

        plt.yticks(numpy.arange(0, 8, 0.5))
        


plt.title('# of Videos Watched Per Agent, By Extremeness', fontsize = 18)
sns.regplot(x = x4, y = y4, lowess=True, scatter = False, label = "None", line_kws={"color": "midnightblue"})
# sns.regplot(x = x_rec, y = y_rec, lowess=True, scatter = False, label = "Rec", line_kws={"color": "royalblue"})
# sns.regplot(x = x_rand, y = y_rand, lowess=True, scatter = False, label = "Rand", line_kws={"color": "cornflowerblue"})
sns.regplot(x = x_score4, y = y_score4, lowess=True, scatter = False, label = "Score", line_kws={"color": "powderblue"})
plt.text(0.4, numpy.nanmean(y4)-0.25, "Avg: " + str(numpy.nanmean(y4)), fontsize = 10)
plt.text(0.4, 4, "Score Avg: " + str(numpy.nanmean(y_score4)), fontsize = 10)
plt.legend(labels=['None', 'Rec', 'Random', 'Score'])

plt.show()
plt.close()

## END MINUTES WATCHED #################################################
