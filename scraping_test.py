
import praw
import pandas as pd

# client id = 9EnSdWZmZivnHGX7RXhmXg
# secret id = ifA2P4BZ0RprGNuYXv8jVuHMcCnB3A
# user agent = sasha scraping

# https://www.reddit.com/api/v1/authorize?client_id=9EnSdWZmZivnHGX7RXhmXg&response_type=code&
#     state=josiecharlotte&redirect_uri=http://localhost:8080&duration=permanent&scope=read


 
reddit_read_only = praw.Reddit(client_id="9EnSdWZmZivnHGX7RXhmXg",         # your client id
                               client_secret="	ifA2P4BZ0RprGNuYXv8jVuHMcCnB3A",      # your client secret
                               user_agent="sasha scraping summer research 2023 i love my pet cats",# your user agent
                               username="capitalistmelon")        
 
 
subreddit = reddit_read_only.subreddit("FireEmblemThreeHouses")


# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
print("Description:", subreddit.description)