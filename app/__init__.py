from praw import Reddit
from config import Config
import pandas as pd

reddit_read_only = Reddit(client_id=Config.REDDIT_CLIENT_ID,
                          client_secret=Config.REDDIT_SECRET)