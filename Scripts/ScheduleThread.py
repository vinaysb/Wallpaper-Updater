from PyQt5.QtCore import QThread, pyqtSignal
import schedule
from MainUpdater import MainUpdater
import time
from config import *


class ScheduleThread(QThread):
    stopSchedule = pyqtSignal()

    def __init__(self, subreddit_name):
        QThread.__init__(self)
        self.subreddit_name = subreddit_name

    def __del__(self):
        self.wait()

    def run(self):
        print(1)
        self.settings = config_loader(dir_path + 'settings.toml')
        ct = self.settings['date']
        if self.subreddit_name == '':
            schedule.every().day.at(ct).do(MainUpdater)
        else:
            schedule.every().day.at(ct).do(MainUpdater, self.subreddit_name)
        while ct == config_loader(dir_path + 'settings.toml')['date']:
            schedule.run_pending()
            time.sleep(15)
