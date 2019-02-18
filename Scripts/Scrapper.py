def Scrapper(dir_path, subreddit_name):
    import praw
    import re
    import requests
    import os
    from RefreshTokenGen import RefreshToken

    reftoken = RefreshToken()
    reddit = praw.Reddit(client_id='szAEvLMd-fUyIQ',
                         client_secret='RUbLmQVrDRVQ3UvxWtRHAFgPyGg',
                         user_agent='testscript by /u/ByakuyaV',
                         refresh_token=reftoken)

    subreddit = reddit.subreddit(subreddit_name)
    img_count = 0
    errors = 0
    for submission in subreddit.top('week'):
        if(errors >= 50):
            return(0)  # Fail

        if(img_count == 7):
            return(1)  # Success

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
        os.makedirs(dir_path + 'Temp_Images', exist_ok=True)
        with open(dir_path + 'Temp_Images/' + file_name, "wb") as f:
            f.write(r.content)  # Fill the image file

        img_count += 1
