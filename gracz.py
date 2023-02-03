# global pkgs
from time import time, sleep
import pyautogui
import win32gui
import datetime
# andrew pkgs
import utils
import cave
from config_picker import *


### D2R update - nowy andrzej szuka
#     def andrzej_szuka(self,
#                       d2_wnd, --> nowe, idk jak na linuxie, na Windowsie dziala, znajduje okno gry, wtedy kazda
#                                   funkcja szuka relatywnie do poczatku okna
#                       region,  --> teraz andrzej_szuka liczy region relatywnie do okna
#                       image_path,
#                       confidence=0.75,
#                       scale=True,
#                       debug=False,
#                       debugpx=False):

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

    # @timing
    def start_game(self, d2_wnd):
        self.utils.andrzej_szuka(d2_wnd, )


    def find_item(self, d2_wnd, jakie_itemy, gdzie_szukac_itemu, czy_podniesc):
        for item in jakie_itemy:
            item_coords = self.utils.andrzej_szuka(d2_wnd, gdzie_szukac_itemu, image_path='./src/items/'+ item +'.png')
            if czy_podniesc:
                if item_coords:
                    pyautogui.rightClick(item_coords)
                    print("Kupilem koronetke!")
                else:
                    print("Nie znalazlem ", item, ", szukam dalej...")


    def kopnij_beczke(self, jak_wyglada_beczka, gdzie_szukac_beczki):
        pozycja_beczki = ()
        return pozycja_beczki
