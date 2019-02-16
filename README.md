# Wallpaper-Updater

It downloads the images from a given subreddit(Currently only from r/wallpapers) based on the top week images and updates your wallpaper daily.

## How to install

1. Clone the repo
2. Install the BackgroundService.py as a windows service using
   `python.exe BackgroundService.py install`
3. Go to services app (by searching in the search bar or typing `services.msc` in the run dialog)
4. Locate Wallpaper Updater and start it.
5. (**OPTIONAL**) Change the startup type from manual to automatic to keep the background service persistent even after reboots
6. Enjoy your sweet wallpapers!
