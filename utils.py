import datetime
import pyautogui
import pytesseract
import PIL
from PIL import Image
from random import choice
from time import sleep
# app default config
from config import *

try:
    from config_local import *
except ImportError:
    print('no local config')
    pass


class Backpack:

    def get_avial_cap(self):
        # returns amount of cap left based on what it can read from inverted.png
        # tested - looks fine
        Other().get_screenshoot(region=cap_region)
        cap = pytesseract.image_to_string('inverted.png', config='--psm 10 --oem 3 -c tessedit_char_whitelest=0123456789')
        print(cap.strip())
        return cap

    def get_avial_slots(self):
        timestamp = datetime.datetime.now()
        slots = list(pyautogui.locateAllOnScreen('src/status/backpack_slot.png', region=backpack, confidence=.8))
        print(len(slots))
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_AVIAL_SLOTS', looptime)
        return slots

    def do_drop_random_item_from_blacklist(self, item_blacklist=item_blacklsit):
        timestamp = datetime.datetime.now()
        item = choice(item_blacklist)
        print('checking for item', item)
        item_cords = pyautogui.locateCenterOnScreen('src/items/'+ str(item) + '.png', region=backpack, confidence=.94)
        if item_cords is not None:
            print('dropping', item)
            # throw away
            pyautogui.moveTo(item_cords[0] - 8, item_cords[1] + 4, duration=0.1)
            sleep(0.1)
            # pyautogui.dragTo(character, duration=.15)
            #            pyautogui.click(item_cords[0]-17, item_cords[1]+6)
            pyautogui.mouseDown(button='left')
            ## sleep(0.1)
            pyautogui.moveTo(character, duration=0.15)
            ## sleep(0.1)
            pyautogui.mouseUp(button='left')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME CHECK_BACKLISTED_ITEMS', looptime)
            return True
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME CHECK_BACKLISTED_ITEMS', looptime)
            return False

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

    def is_ring_on(self, ring_type):
        # todo add .png for more rings
        # available: axe_ring, sword_ring
        if pyautogui.locateOnScreen(ring_type + ".png", region=ring, confidence=.5) is None:
            pyautogui.press('f4')
