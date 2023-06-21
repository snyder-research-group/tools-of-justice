import numpy as np

class Activity:
    """ Class which defines Activities within the YouTube simulation. Stores activity characteristics, current state and log. """

    # A user can do one of the following activities in relation to a video:
        # Click: select a video to watch (should this be establish_relation(v_id) instead?)
        # Watch: actually watch the video (does this really need to be separate from click?). Increments views for a video.
        # Thumbs_up: give a video a thumbs up