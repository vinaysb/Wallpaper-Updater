from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ScheduleThread import ScheduleThread
import os
import webbrowser
import ctypes
from config import *


class UiWallpaperUpdater(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self):
        self.setObjectName("WallpaperUpdater")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(342, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(342, 240))
        self.setMaximumSize(QtCore.QSize(342, 240))
        self.setBaseSize(QtCore.QSize(342, 240))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.Logo = self.resource_path("wallpaper_updater_2XT_icon.ico")
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setFocusPolicy(QtCore.Qt.TabFocus)
        self.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.subreddit_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.subreddit_entry.setGeometry(QtCore.QRect(20, 60, 301, 31))
        self.subreddit_entry.setMaxLength(21)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subreddit_entry.setFont(font)
        self.subreddit_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.subreddit_entry.setObjectName("subreddit_entry")
        self.subreddit_entry.returnPressed.connect(self.Ok_Pressed)
        self.subreddit_entry_label = QtWidgets.QLabel(self.centralwidget)
        self.subreddit_entry_label.setGeometry(QtCore.QRect(20, 30, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.subreddit_entry_label.setFont(font)
        self.subreddit_entry_label.setObjectName("subreddit_entry_label")
        self.subreddit_Buttonbox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.subreddit_Buttonbox.setGeometry(QtCore.QRect(135, 110, 186, 23))
        self.subreddit_Buttonbox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.subreddit_Buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
        self.subreddit_Buttonbox.setObjectName("Subreddit_Buttonbox")
        self.setCentralWidget(self.centralwidget)
        self.subreddit_Buttonbox.accepted.connect(self.Ok_Pressed)
        self.subreddit_Buttonbox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.Reset_Pressed)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 23))
        self.menubar.setObjectName("menubar")
        self.trayIcon = QtWidgets.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon(self.Logo))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.trayMenu = QtWidgets.QMenu()
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.trayIcon.setContextMenu(self.trayMenu)
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.actionREADME = QtWidgets.QAction(self)
        self.actionREADME.setObjectName("actionREADME")
        self.actionAbout_me = QtWidgets.QAction(self)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.actionShow = QtWidgets.QAction("Show", self)
        self.actionHide = QtWidgets.QAction("Hide", self)
        self.actionExit = QtWidgets.QAction("Exit", self)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionHide)
        self.menuAbout.addAction(self.actionREADME)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_me)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.trayMenu.addAction(self.actionShow)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(self.actionExit)
        self.actionClose.triggered.connect(QtWidgets.qApp.quit)
        self.actionREADME.triggered.connect(self.readme)
        self.actionShow.triggered.connect(self.show)
        self.actionHide.triggered.connect(self.hide)
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.trayIcon.show()
        self.setWindowIcon(QtGui.QIcon(self.Logo))
        dir_path = '%s/WallpaperUpdater/' % os.environ['APPDATA']
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        self.settings = config_loader(dir_path + 'settings.toml')
        if (self.settings['date'] != 0):
            self.threader(self.settings['subreddit_name'])

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, WallpaperUpdater):
        _translate = QtCore.QCoreApplication.translate
        WallpaperUpdater.setWindowTitle(_translate("WallpaperUpdater", "Reddit Wallpaper Updater"))
        self.subreddit_entry.setPlaceholderText(_translate("WallpaperUpdater", "wallpapers"))
        self.subreddit_entry_label.setText(_translate("WallpaperUpdater", "Type the name of the subreddit (Without \"/r\")"))
        self.menuFile.setTitle(_translate("WallpaperUpdater", "File"))
        self.menuAbout.setTitle(_translate("WallpaperUpdater", "About"))
        self.actionClose.setText(_translate("WallpaperUpdater", "Close"))
        self.actionREADME.setText(_translate("WallpaperUpdater", "README"))
        self.actionAbout_me.setText(_translate("WallpaperUpdater", "About me"))

    def Ok_Pressed(self):
        subreddit_name = self.subreddit_entry.text()
        self.settings['date'] = str((datetime.now() + timedelta(minutes=1)).strftime('%H:%M'))
        self.threader(subreddit_name)

    def Reset_Pressed(self):
        self.subreddit_entry.setText("")
        self.subreddit_entry.setPlaceholderText("wallpapers")

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def readme(self):
        webbrowser.open("https://github.com/vinaysb/Wallpaper-Updater/blob/master/README.md")

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def threader(self, subreddit_name):
        self.myThread = (ScheduleThread(subreddit_name))
        self.myThread.start()


if __name__ == "__main__":
    myappid = 'mycompany.Wallpaper-Updater.GUI.0.5'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiWallpaperUpdater()
    MainWindow.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
