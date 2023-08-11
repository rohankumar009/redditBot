import praw
import time

# Reddit API credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    username='YOUR_REDDIT_USERNAME',
    password='YOUR_REDDIT_PASSWORD',
    user_agent='YOUR_USER_AGENT'
)

# Subreddit and keyword to monitor
subreddit_name = 'YOUR_SUBREDDIT_NAME'
keyword = '!mention_bot'  # The keyword that the bot responds to
