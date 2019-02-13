def ImageGenerator():
    import os
    from RedditScrapper import Scrapper
    files = os.listdir('Temp_images')
    if(len(files) == 0):
        status = Scrapper()
        if(status == 1):
            files = os.listdir('Temp_images')
        else:
            print('There is not many jpg, jpeg or png image in this subreddit, Choose another subreddit')
    print(files)
    for img in files:
        yield (os.path.abspath('Temp_images/' + img).replace('\\', '/'))
