# global pkgs
from time import time, sleep
import pyautogui
import win32gui
import datetime
# andrew pkgs
import utils
import math
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
        hwnd = win32gui.FindWindow(None, "Diablo II: Resurrected")
        # window_rect = win32gui.GetClientRect(window_handle)
        rect = win32gui.GetWindowRect(hwnd)
        clientRect = win32gui.GetClientRect(hwnd)
        windowOffset = math.floor(((rect[2] - rect[0]) - clientRect[2]) / 2)
        titleOffset = ((rect[3] - rect[1]) - clientRect[3]) - windowOffset
        newRect = (rect[0] + windowOffset, rect[1] + titleOffset, rect[2] - windowOffset, rect[3] - windowOffset)
        return newRect

    # @timing
    def start_game(self, d2_wnd, difficulty="HELL"):
        img_coords = self.utils.andrzej_szuka(d2_wnd=d2_wnd, region=d2_wnd, image_path="./src/buttons/play.png")
        # print(img_coords)
        pyautogui.click(img_coords)
        sleep(1)
        if difficulty == "HELL":
            img_coords2 = self.utils.andrzej_szuka(d2_wnd, d2_wnd, image_path="./src/buttons/dificulty_hell.png")
            # print(img_coords2)
            pyautogui.click(img_coords2)
        elif difficulty == "NM":
            img_coords2 = self.utils.andrzej_szuka(d2_wnd, d2_wnd, image_path="./src/buttons/difficulty_nightmare.png")
            # print(img_coords2)
            pyautogui.click(img_coords2)
        if difficulty == "NORM":
            img_coords2 = self.utils.andrzej_szuka(d2_wnd, d2_wnd, image_path="./src/buttons/dificulty_normal.png")
            # print(img_coords2)
            pyautogui.click(img_coords2)

    def find_item(self, d2_wnd, jakie_itemy, gdzie_szukac_itemu, czy_podniesc):
        for item in jakie_itemy:
            item_coords = self.utils.andrzej_szuka(d2_wnd, gdzie_szukac_itemu, image_path='./src/items/'+ item +'.png')
            if czy_podniesc:
                if item_coords:
                    pyautogui.rightClick(item_coords)
                    print("Kupilem koronetke!")
                else:
                    print("Nie znalazlem ", item, ", szukam dalej...")
            else:
                print("nie chce pan podniesc to pokaze gdzie")
                #todo obrysowac item ramka
                #import math
                # from PIL import Image, ImageDraw
                #
                # w, h = 220, 190
                # shape = [(40, 40), (w - 10, h - 10)]
                #
                # # creating new Image object
                # img = Image.new("RGB", (w, h))
                #
                # # create rectangle image
                # img1 = ImageDraw.Draw(img)
                # img1.rectangle(shape, fill ="# ffff33", outline ="red")
                # img.show()


    def kopnij_beczke(self, jak_wyglada_beczka, gdzie_szukac_beczki):
        pozycja_beczki = ()
        return pozycja_beczki
