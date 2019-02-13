import praw
import re
import requests
import os


def Scrapper(subredditname='wallpapers'):
    reddit = praw.Reddit(client_id='szAEvLMd-fUyIQ',
                         client_secret="RUbLmQVrDRVQ3UvxWtRHAFgPyGg", password='horse@1419',
                         user_agent='testscript by /u/ByakuyaV', username='ByakuyaV')

    subreddit = reddit.subreddit(subredditname)
    img_count = 0
    errors = 0
    for submission in subreddit.top('week'):
        if(errors >= 50):
            return(0)  # 'There is not many jpg, jpeg or png image in this subreddit, Choose another subreddit'

        if(img_count == 7):
            return(1)

        url = (submission.url)

        if not any(x in url for x in ['.jpg', '.png', '.jpeg']):  # Check if there are any images in the subreddit
            errors += 1
            continue

        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]
        if "." not in file_name:
            file_name += ".jpg"  # Create the image file

        r = requests.get(url)
        os.makedirs(subredditname + '_Temp_Images', exist_ok=True)
        with open(subredditname + '_Temp_Images/' + file_name, "wb") as f:
            f.write(r.content)  # Fill the image file

        img_count += 1
