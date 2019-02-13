import praw

reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret="CLIENT_SECRET", password='PASSWORD',
                     user_agent='USERAGENT', username='USERNAME')

subreddit = reddit.subreddit('reddit_api_test')

for idx, submission in enumerate(subreddit.top('week')):
    print(submission)
    if(idx == 4):
        break
