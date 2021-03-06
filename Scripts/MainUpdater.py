from config import *
import os
from Scrapper import Scrapper
from Changer import Changer


def MainUpdater(subreddit_name="wallpapers"):
    dir_path = "%s/WallpaperUpdater/" % os.environ["APPDATA"]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    settings = config_loader(dir_path + "settings.toml")
    if(settings["currentimg"] == 6):
        Scrapper(dir_path, subreddit_name)
        settings["currentimg"] = 0

    files = os.listdir(dir_path + "Temp_images")
    Changer(os.path.abspath(dir_path + "Temp_images/" + files[settings["currentimg"]]).replace("\\", "/"))
    settings["currentimg"] += 1
    config_saver(settings, dir_path + "settings.toml")
