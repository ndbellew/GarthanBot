from praw import Reddit
from config import Config
import pandas as pd

reddit_read_only = Reddit(client_id=Config.REDDIT_CLIENT_ID,
                          client_secret=Config.REDDIT_SECRET,
                          user_agent=Config.REDDIT_USER_AGENT)

def getSubreddit(title):
    subreddit = reddit_read_only.subreddit(title)
    return subreddit

def printPosts(NumofPosts, subreddit):
    for post in subreddit.hot(limit=NumofPosts):
        print(post.title)
        
def main():
    subreddit = getSubreddit("webcomics")
    
    # Scraping the top posts of the current month
    
    printPosts(5, subreddit)

main()