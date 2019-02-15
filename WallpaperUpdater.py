from config import *
from datetime import datetime
import os
from Scrapper import Scrapper
from Changer import Changer


def WallpaperUpdater():
    settings = config_loader('settings.toml')
    print(settings)

    if(settings['imgs_processed'] == 6):
        Scrapper()
        settings['imgs_processed'] = 0

    files = os.listdir('Temp_images')

    for index, img in enumerate(files):
        currentimg = index
        Changer(os.path.abspath('Temp_images/' + img).replace('\\', '/'))
        settings['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        settings['currentimg'] = currentimg
        config_saver(settings, 'settings.toml')
