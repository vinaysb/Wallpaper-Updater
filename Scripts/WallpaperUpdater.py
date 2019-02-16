from Scripts.config import *
from datetime import datetime
import os
from Scripts.Scrapper import Scrapper
from Scripts.Changer import Changer


def WallpaperUpdater():
    dir_path = '%s/WallpaperUpdater/' % os.environ['APPDATA']
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    settings = config_loader(dir_path + 'settings.toml')
    if(settings['currentimg'] == 6):
        Scrapper(dir_path)
        settings['currentimg'] = 0

    files = os.listdir(dir_path + 'Temp_images')
    Changer(os.path.abspath(dir_path + 'Temp_images/' + files[settings['currentimg']]).replace('\\', '/'))
    settings['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    settings['currentimg'] += 1
    config_saver(settings, dir_path + 'settings.toml')
