def Wallpaper():
    import ctypes
    from ImageGen import ImageGenerator
    import time
    from RedditScrapper import Scrapper
    import os

    img = ImageGenerator()
    for i in range(7):
        try:
            desktopbg = next(img)
        except StopIteration:
            Scrapper()
        print(desktopbg)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, desktopbg, 3)
        os.remove(desktopbg)
        time.sleep(10)
