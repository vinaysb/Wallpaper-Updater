from PyQt5.QtCore import QThread, pyqtSignal
import schedule
from MainUpdater import MainUpdater
from datetime import datetime, timedelta
import time


class ScheduleThread(QThread):
    stopSchedule = pyqtSignal()

    def __init__(self, subreddit_name):
        QThread.__init__(self)
        self.subreddit_name = subreddit_name

    def __del__(self):
        self.wait()

    def run(self):
        print(1)
        if self.subreddit_name == '':
            schedule.every().day.at(str((datetime.now() + timedelta(minutes=1)).strftime('%H:%M'))).do(MainUpdater)
        else:
            schedule.every().day.at(str((datetime.now() + timedelta(minutes=1)).strftime('%H:%M'))).do(MainUpdater, self.subreddit_name)
        while True:
            schedule.run_pending()
            time.sleep(15)
