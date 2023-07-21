import numpy as np
from video import Video
import random

class Activity:
    """ Class which defines Activities within the YouTube simulation."""

    # A user can do one of the following activities in relation to a video:
        # Click on a recommended video: select a video to watch (establish_relation(v_id))
        # Watch: actually watch the video. Increments views for a video.
        # Thumbs_up: give a video a thumbs up


    # def establish_relation(current_vid, clicked_vid, self):
    #     self.related = True;
    #     return related;

    # def is_related(vid_1, vid_2):
    #     return establish_relation(vid_1, vid_2).related

    def give_thumbs_up(video):
        video.thumbs_up += 1; # this works! hooray!



    def watch(video):
        # Increment how many views the video got
        video.views += 1;
        # Add the video length to total time spent watching today


        # The below information has to be collected outside of the function
        # thumbs_up_given_today = 0
        # thumbs_up_skipped_today = 0

        # Coin flip to determine if give_thumbs_up is called
        coin_flip = random.choice([0,1])
        if(coin_flip):
            Activity.give_thumbs_up(video)
            print("Thumbs up given")
            # thumbs_up_given_today += 1
        else:
            print("No thumbs up given")
            # thumbs_up_skipped_today += 1

        # print(thumbs_up_given_today)
        # print(thumbs_up_skipped_today)

    
    def random_vid(list_of_vids):
        return random.choice(list_of_vids)
