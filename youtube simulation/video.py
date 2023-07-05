class Video:
    """ Class which defines Videos within the YouTube simulation. """
    
    # A video contains the following data points:
        # views: int,
        # vid_id: int,
        # length: int (minutes),
        # category: string,
        # thumbs_up: int (count),
        # suggestion_relation(v_id): boolean or int (checks if this video is related to another of id vid_id)

    # The Video class is allegorical to the Attraction class in Shapeland.


    def __init__(self, views, vid_id, length, extremeness, thumbs_up):
        self.views = views;
        self.vid_id = vid_id;
        self.length = length;
        self.extremeness = extremeness;
        self.thumbs_up = thumbs_up;
