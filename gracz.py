# global pkgs
from time import time, sleep
import pyautogui
import win32gui
import datetime
# andrew pkgs
import utils
import cave
from config_picker import *


class Gracz:

    def __init__(self):
        self.cave = cave.Cave()
        self.utils = utils.Utils()
        pyautogui.PAUSE = config.pa_pause
        print('loaded with config ', confname)

    def timing(f):
        def wrap(*args, **kwargs):
            time1 = time()
            ret = f(*args, **kwargs)
            time2 = time()
            print('DURATION {:<20s} {:.1f} ms'.format(
                f.__name__, (time2 - time1) * 1000.0))

            return ret

        return wrap

    # @timing
    def find_d2_window(self):
        window_handle = win32gui.FindWindow(None, "Diablo II: Resurrected")
        window_rect = win32gui.GetWindowRect(window_handle)
        return window_rect

    def kopnij_beczke(self, jak_wyglada_beczka, gdzie_szukac_beczki):
        pozycja_beczki = ()
        return pozycja_beczki
