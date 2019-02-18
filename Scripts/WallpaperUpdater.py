from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ScheduleThread import ScheduleThread


class UiWallpaperUpdater(object):
    def setupUi(self, WallpaperUpdater):
        WallpaperUpdater.setObjectName("WallpaperUpdater")
        WallpaperUpdater.setWindowModality(QtCore.Qt.WindowModal)
        WallpaperUpdater.resize(342, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WallpaperUpdater.sizePolicy().hasHeightForWidth())
        WallpaperUpdater.setSizePolicy(sizePolicy)
        WallpaperUpdater.setMinimumSize(QtCore.QSize(342, 240))
        WallpaperUpdater.setMaximumSize(QtCore.QSize(342, 240))
        WallpaperUpdater.setBaseSize(QtCore.QSize(342, 240))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        WallpaperUpdater.setFont(font)
        WallpaperUpdater.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        WallpaperUpdater.setFocusPolicy(QtCore.Qt.TabFocus)
        WallpaperUpdater.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(WallpaperUpdater)
        self.centralwidget.setObjectName("centralwidget")
        self.subreddit_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.subreddit_entry.setGeometry(QtCore.QRect(20, 60, 301, 31))
        self.subreddit_entry.setMaxLength(21)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subreddit_entry.setFont(font)
        self.subreddit_entry.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.subreddit_entry.setObjectName("subreddit_entry")
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
        WallpaperUpdater.setCentralWidget(self.centralwidget)
        self.subreddit_Buttonbox.accepted.connect(self.Ok_Pressed)
        self.subreddit_Buttonbox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.Reset_Pressed)
        self.menubar = QtWidgets.QMenuBar(WallpaperUpdater)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        WallpaperUpdater.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WallpaperUpdater)
        self.statusbar.setObjectName("statusbar")
        WallpaperUpdater.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(WallpaperUpdater)
        self.actionClose.setObjectName("actionClose")
        self.actionREADME = QtWidgets.QAction(WallpaperUpdater)
        self.actionREADME.setObjectName("actionREADME")
        self.actionAbout_me = QtWidgets.QAction(WallpaperUpdater)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionREADME)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_me)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(WallpaperUpdater)
        QtCore.QMetaObject.connectSlotsByName(WallpaperUpdater)

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
        self.myThread = (ScheduleThread(subreddit_name))
        self.myThread.start()

    def Reset_Pressed(self):
        self.subreddit_entry.setText("")
        self.subreddit_entry.setPlaceholderText("wallpapers")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiWallpaperUpdater()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
