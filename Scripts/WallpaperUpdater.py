from Scripts.config import *
from datetime import datetime
import os
from Scripts.Scrapper import Scrapper
from Scripts.Changer import Changer


def WallpaperUpdater():
    settings = config_loader('Scripts/settings.toml')

    if(settings['currentimg'] == 6):
        Scrapper()
        settings['currentimg'] = 0

    files = os.listdir('Temp_images')

    Changer(os.path.abspath('Temp_images/' + files[settings['currentimg']]).replace('\\', '/'))
    settings['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    settings['currentimg'] += 1
    config_saver(settings, 'settings.toml')
