def Scrapper(subredditname='wallpapers'):
    import praw
    import re
    import requests
    import os
    import webbrowser

    reddit = praw.Reddit(client_id='VZ1fX-VhJXo91w',
                         client_secret=None,
                         user_agent='testscript by /u/ByakuyaV',
                         redirect_uri='https://github.com/vinaysb/Wallpaper-Updater')
    webbrowser.open(reddit.auth.url(['identity'], '...', implicit=True))
    # print(reddit.auth.authorize(code))
    print(reddit.user.me())

    subreddit = reddit.subreddit(subredditname)
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
        os.makedirs('Temp_Images', exist_ok=True)
        with open('Temp_Images/' + file_name, "wb") as f:
            f.write(r.content)  # Fill the image file

        img_count += 1


Scrapper()
