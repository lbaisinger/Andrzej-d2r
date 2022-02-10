from time import sleep
import pyautogui
import datetime
from utils import Backpack
from utils import Other
from cave import Cave
from config_picker import *
from caves.any_5 import *
from gracz import *

wp = list(wps.keys())
print('wps key:', wp)

wp_val = list(wps.values())
print('wp values:', wp_val)

wp_items = list(wps.items())
print(wp_items)

for x in wps:
    if wp_val[x-1] == 'special':
        print('wp', wp, ': lopata & lina')
        pyautogui.press(config.hotkey_shovel)
        pyautogui.click(config.character)
        sleep(0.1)
        pyautogui.press(config.hotkey_rope)
        pyautogui.click(config.character)
    else:
        print('wp pospolity')