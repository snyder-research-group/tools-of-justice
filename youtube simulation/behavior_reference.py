# These percentages are lifted directly from https://hiddentribes.us/.
AGENT_ARCHETYPE_DISTRIBUTION = {
    "progressive_activist": 0.08,
    "traditional_liberal": 0.11,
    "passive_liberal": 0.15,
    "politically_disengaged": 0.26,
    "moderate": 0.15,
    "traditional_conservative": .19,
    "devoted_conservative": 0.06
}


# Parameters describing behavior of Agent Archetypes
# Parameters
    # longest_vid_threshold: longest video length (in minutes) that user is willing to watch
    # yt_time_threshold: how long (in minutes) user will stay on YouTube
    # political_affiliation: not sure if I want to make this a 0/1 democrat/republican or use the sort of 
    # sliding scale above. maybe left/right/independent?
    # video_extremity: how extreme of a video a user will watch (0 is not extreme at all, 1 is very extreme)
    # popularity_threshold: how many views a video must have for a user of this archetype to click on it
    # prefers_algorithm: probably should be randomly generated for each user and not archetype-based;
    # determines whether or not user will click on algorithmically suggested videos (is this even needed?)
    
# Some notes
    # The numbers mirror each other from most to least extreme; "progressive activist" shares the same proclivities
    # as the "devoted conservative."
    # Despite sharing the same numbers, the differences in practice are a) watching left-wing versus right-wing videos,
    # and b) agent archetype distribution (34% on the left side of disengaged, 40% on the right).

# Some questions
    # Is prefers_algorithm even necessary?
    # Should extremity be weighted on a bipartisan scale---instead of 0-1 like it is now, maybe have 0.5 be neutral,
    # < 0.5 be liberally extreme, and > 0.5 be conservatively extreme?

BEHAVIOR_ARCHETYPE_PARAMETERS = {
    # Agent is willing to spend lots of time watching more "underground" and less-popular videos, for longer.
    # More "devoted" to watching videos aligned with their beliefs.
    "progressive_activist": {
        "longest_vid_threshold": 90,    #will watch videos up to 1.5 hours long
        "yt_time_threshold": 120,       #will spend up to two hours on YouTube per day
        "political_affiliation": "left",
        "video_extremity": 1.0,         #will watch videos that rate high on extreme-ness
        "popularity_threshold": 2000   #will watch any video with at least 2000 views
    },

    # Agent is willing to watch longer videos aligned with their beliefs, but not as long as the progressive activist.
    "traditional_liberal": {
        "longest_vid_threshold": 60,    #will watch videos up to 1 hour long
        "yt_time_threshold": 80,        #will spend up to one hour per day on YouTube   
        "political_affiliation": "left",
        "video_extremity": 0.8,         #will watch some extreme videos, but not much
        "popularity_threshold": 50000   #will watch any video with at least 50,000 views
    },

    # Agent will spend a little longer than average watching videos, but nothing incredibly extreme.
    "passive_liberal": {
        "longest_vid_threshold": 40,    #will watch videos up to 40 minutes long
        "yt_time_threshold": 60,        #will spend 50 minutes per day on YouTube
        "political_affiliation": "middle",
        "video_extremity": 0.6,         #will not watch anything too extreme  
        "popularity_threshold": 100000  #watches videos with at least 100k views
    },

    # Agent doesn't want to watch long videos. Will engage with popular, non-partisan content.
    "politically_disengaged": {
        "longest_vid_threshold": 15,    #won't watch any video longer than 15 minutes
        "yt_time_threshold": 45,        #will spend at most 40 minutes per day on YouTube (national average)
        "political_affiliation": "middle",
        "video_extremity": 0.5,         #does not want to watch videos that are extreme or partisan
        "popularity_threshold": 500000  #watches more popular videos; at least 500k views
    },

    # Agent will spend a little longer than average watching videos, but nothing incredibly extreme.
    "moderate": {
        "longest_vid_threshold": 40,    #will watch videos up to 40 minutes long
        "yt_time_threshold": 60,        #will spend 50 minutes per day on YouTube
        "political_affiliation": "middle",
        "video_extremity": 0.4,         #will not watch anything too extreme  
        "popularity_threshold": 100000  #watches videos with at least 50k views
    },

    # Agent is willing to watch longer videos aligned with their beliefs, but not as long as the devoted conservative.
    "traditional_conservative": {
        "longest_vid_threshold": 60,    #will watch videos up to 1 hour long
        "yt_time_threshold": 80,        #will spend up to one hour per day on YouTube   
        "political_affiliation": "right",
        "video_extremity": 0.2,         #will watch some extreme videos, but not much
        "popularity_threshold": 50000   #will watch any video with at least 50,000 views
    },

    # Agent is willing to spend lots of time watching more "underground" and less-popular videos, for longer.
    # More "devoted" to watching videos aligned with their beliefs.
    "devoted_conservative": {
        "longest_vid_threshold": 90,   #will watch videos up to 1.5 hours long
        "yt_time_threshold": 120,       #will spend up to two hours on YouTube per day
        "political_affiliation": "right",
        "video_extremity": 0.0,         #will watch videos that rate high on extreme-ness
        "popularity_threshold": 2000   #will watch any video with at least 2000 views
    },
    

}
