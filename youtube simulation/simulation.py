import random
import numpy as np
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from agent import Agent
from video import Video
from activity import Activity
from behavior_reference import BEHAVIOR_ARCHETYPE_PARAMETERS

class Simulation:
    """Class file for the actual simulation (so far)."""

    """
    Within a given day, dozens of agents will click on videos.
    What needs to happen when an agent clicks on a video?
    - Video views++
    - Add video.length to total time spent watching today
    - Coin/dice roll to determine if thumbs up is given
    - If under daily limit, find a new video

    How do users find another video?

    if rand_next_suggested_video.extremeness is with 0.2 of current video
        click on next video
        establish_relationship()

    Continue this above cycle per agent until the total minutes watched exceeds the agent's archetype limit.
    Also, repeat all of the above for (let's start with) 100 agents in a given day.

    """


    # self.views = views;
    # self.vid_id = vid_id;
    # self.length = length;
    # self.extremeness = extremeness;
    # self.thumbs_up = thumbs_up;

    # The average video length is 11.7 minutes (https://www.statista.com/statistics/1026923/youtube-video-category-average-length/)
    # We need to randomly generate a bunch of videos, then save them into an array (or text file). 
    # v1 = Video(1000, 12345, 15, 0.5, 50);

    # Generate random view count (views range from 1 to 1 million)
    random_view_counts = []
    for i in range(1000):
        r = random.randint(1, 1000000)
        random_view_counts.append(r)


    # Generate random (unique) video ids
    # resultant random numbers list
    random_video_ids = []
    # traversing the loop 1000 times
    for i in range(1000):

        # r=random.randint(1,100000)
        # # checking whether the generated random number is not in the
        # # randomList
        # if r not in random_video_ids:
        #     # appending the random number to the resultant list, if the condition is true
            random_video_ids.append(i)


    # Generate random video length
    random_vid_lengths = []
    for i in range(1000):
        r = random.randint(1, 100)
        random_vid_lengths.append(r)

    # Generate random video extremeness
    random_extremeness = []
    for i in range(1000):
        r = random.randint(0*0,1*10)/10
        random_extremeness.append(r)


    # Generate random number of thumbs up
    random_thumbs_up = []
    for i in range(1000):
        r = random.randint(0, 50000)
        random_thumbs_up.append(r)


    # Use the above arrays to create video objects
    all_videos = []
    for i in range(1000):   # create 1000 videos

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
    

    # Let's make sure this worked.

    print("Information for the first three videos:");
    for i in range(3):
        print("Views: " + str(all_videos[i].views));
        print("Video ID: " + str(all_videos[i].vid_id));
        print("Length: " + str(all_videos[i].length) +  " minutes");
        print("Extremeness: " + str(all_videos[i].extremeness));
        print("Thumbs up count: " + str(all_videos[i].thumbs_up));
        print("");
    


    # Now that we've generated the videos, we can generate our agents.
    # Let's start with 100 agents.
    # This means we will have the following archetype counts:
    """
    AGENT_ARCHETYPE_DISTRIBUTION = {
        "progressive_activist": 8,
        "traditional_liberal": 11,
        "passive_liberal": 15,
        "politically_disengaged": 26,
        "moderate": 15,
        "traditional_conservative": 19,
        "devoted_conservative": 6
    }    
    """
    # So, 8 progressive activists, 11 traditional liberals, 15 passive liberals, 26 politically disengaged,
    # 15 moderates, 19 traditional conservatives, and 6 devoted conservatives.
    # Since we have 100 agents, their IDs can just be 1-100 in the order they are created.

    # Creating an array to hold our agents
    our_agents = [];

    id_counter = 0;
    # Generate the progressive activists (8)
    for i in range(8):    
        our_agent = Agent(False, "progressive_activist", id_counter, "");
        our_agents.append(our_agent);
        id_counter += 1;

    # Generate the traditional liberals (11)
    for i in range(11):
        our_agent = Agent(False, "traditional_liberal", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    
    # Generate the passive liberals (15)
    for i in range(15):
        our_agent = Agent(False, "passive_liberal", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    
    # Generate the politically disengaged (26)
    for i in range(26):
        our_agent = Agent(False, "politically_disengaged", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    
    # Generate the moderates (15)
    for i in range(15):
        our_agent = Agent(False, "moderate", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    
    # Generate the traditional conservatives (19)
    for i in range(19):
        our_agent = Agent(False, "traditional_conservative", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    
    # Generate the devoted conservatives (6)
    for i in range(6):
        our_agent = Agent(False, "devoted_conservatives", i, "");
        our_agents.append(our_agent);
        id_counter += 1;
    

    # Now, let's see if this actually works
    # for i in range(100):
    #     print("Count: " + str(our_agents[i].agent_id) + "\tArchetype: " + our_agents[i].archetype);

        

    

    # def __init__(self):
        # self.currently_watching = False
        # self.archetype = None   # starts off with no archetype defined
        # self.agent_id = None # unique identification number for agent
        # self.log = "" # logs agent history as text






    print("hello");