from PyQt5.QtCore import QThread, pyqtSignal
import schedule
from MainUpdater import MainUpdater
import time
from config import *
import os
import logging


class ScheduleThread(QThread):
    stopSchedule = pyqtSignal()

    def __init__(self, subreddit_name):
        self.logger = logging.getLogger("WallpaperUpdater")
        self.filelogger = logging.FileHandler("WallpaperUpdater.log")
        # self.FORMAT = logging.Formatter("%(asctime)-15s %(clientip)s %(user)-8s %(message)s")
        # self.filelogger.setFormatter(self.FORMAT)
        self.logger.addHandler(self.filelogger)
        self.logger.setLevel(logging.DEBUG)
        QThread.__init__(self)
        self.subreddit_name = subreddit_name
        self.logger.debug("Thread has started")

    # def __del__(self):
    #     self.wait()

    def run(self):
        dir_path = "%s/WallpaperUpdater/" % os.environ["APPDATA"]
        self.settings = config_loader(dir_path + "settings.toml")
        ct = self.settings["date"]
        if self.subreddit_name == "":
            schedule.every().day.at(ct).do(MainUpdater)
        else:
            schedule.every().day.at(ct).do(MainUpdater, self.subreddit_name)
        self.logger.debug("While has started")
        while ct == config_loader(dir_path + "settings.toml")["date"]:
            schedule.run_pending()
            time.sleep(15)
