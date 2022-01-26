import datetime
import pyautogui
import PIL
from PIL import Image
from config import *


class Backpack:

    def get_avial_slots(self):
        timestamp = datetime.datetime.now()
        slots = list(pyautogui.locateAllOnScreen('src/status/backpack_slot.png', region=backpack, confidence=.8))
        print(len(slots))
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_AVIAL_SLOTS', looptime)
        return slots


class Other:

    def get_screenshoot(self, region=minimapplus):
        timestamp = datetime.datetime.now()
        # get screen shoot
        myscreenshot = pyautogui.screenshot(region=region)
        # save it
        myscreenshot.save('screen.png')
        # invert image
        inverted_image = PIL.ImageOps.invert(Image.open('screen.png'))
        # save it
        inverted_image.save('inverted.png')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_SCREENSHOOT', looptime)
        return True
