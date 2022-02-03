from time import sleep
import pyautogui
import datetime
from utils import Backpack
from utils import Other

try:
    from config_local import *
except ImportError:
    print('no local config')
    pass

wsk = Other()
pyautogui.click(default)
if wsk.is_ring_on() is False:
    wsk.put_on_ring(hotkey_ring)
else:
    print('ring equipped')
