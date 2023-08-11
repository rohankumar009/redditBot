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

def main():
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"Monitoring comments in /r/{subreddit_name}...")
    
    for comment in subreddit.stream.comments():
        if keyword in comment.body:
            print(f"Found a mention: {comment.body}")
            reply_text = "Hello there! I noticed you mentioned me. How can I assist you?"
            
            try:
                comment.reply(reply_text)
                print("Replied successfully!")
            except Exception as e:
                print("An error occurred while replying:", str(e))
            
        time.sleep(10)  # Sleep for 10 seconds before checking for new comments
