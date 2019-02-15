import ctypes
import os


def Changer(desktopbg):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, desktopbg, 3)
    os.remove(desktopbg)
