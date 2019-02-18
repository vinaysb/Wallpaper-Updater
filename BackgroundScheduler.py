import schedule
from Scripts.MainUpdater import MainUpdater
import win32serviceutil
import win32service
import win32event
import servicemanager
import time


class WallpaperUpdaterSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "WallpaperUpdater"
    _svc_display_name_ = "Wallpaper Updater"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        schedule.every().day.at("19:00").do(MainUpdater)
        while True:
            schedule.run_pending()
            time.sleep(15)
            if win32event.WaitForSingleObject(self.hWaitStop, 5000) == win32event.WAIT_OBJECT_0:
                break


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(WallpaperUpdaterSvc)
