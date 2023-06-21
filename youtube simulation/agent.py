import random
import numpy as np

from behavior_reference import BEHAVIOR_ARCHETYPE_PARAMETERS

class Agent:
    """ Class which defines agents within the YouTube simulation. Stores agent characteristics, current state and log. """

    def __init__(self, random_seed):
        # Sasha note: I am not 100% on what any of this means; I'm just copy-pasting from my reference file. 
        # Obviously, this will change later.
        """  """

        self.agent_id = None # unique identification number for agent
        self.state = {} # characterizes agents current state
        self.log = "" # logs agent history as text
        self.random_seed = random_seed

        for behavior_type, behavior_dict in BEHAVIOR_ARCHETYPE_PARAMETERS.items():
            age_class_sum = behavior_dict["percent_no_child_rides"] + behavior_dict["percent_no_adult_rides"] + behavior_dict["percent_no_preference"]
            # deal with fuzzy float addition
            if not 0.98 <= age_class_sum <= 1.0:
                raise AssertionError(
                    f"Behavior Archtype {behavior_type} characteristics percent_no_child_rides, percent_no_adult_rides,"
                    "and percent_no_preference, must add up to 1"
                )
        
        def initialize_agent():
            # nothing here yet
            print("hi")
