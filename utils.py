import datetime
import pyautogui
import PIL
import pytesseract
from PIL import Image
from random import choice
from time import sleep
from config_picker import *


class Backpack:

    def get_avial_cap(self):
        # returns amount of cap left based on what it can read from inverted.png
        # tested - looks fine
        Other().get_screenshoot(region=config.cap_region)
        cap = pytesseract.image_to_string('inverted.png', config='--psm 10 --oem 3 -c tessedit_char_whitelest=0123456789')
        print(cap.strip())
        return cap

    def get_avial_slots(self):
        # works ok - no use yet
        timestamp = datetime.datetime.now()
        slots = list(pyautogui.locateAllOnScreen('src/status/backpack_slot.png', region=config.backpack, confidence=.8))
        print(len(slots))
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_AVIAL_SLOTS', looptime)
        return slots

    def do_drop_random_item_from_blacklist(self, item_blacklist):
        # facc feature
        timestamp = datetime.datetime.now()
        item = choice(item_blacklist)
        print('checking for item', item)
        item_cords = pyautogui.locateCenterOnScreen('src/items/' + str(item) + '.png', region=config.backpack, confidence=.94)
        if item_cords is not None:
            print('dropping', item)
            # throw away
            pyautogui.moveTo(item_cords[0] - 8, item_cords[1] + 4, duration=0.1)
            sleep(0.1)
            # pyautogui.dragTo(character, duration=.15)
            #            pyautogui.click(item_cords[0]-17, item_cords[1]+6)
            pyautogui.click()
            pyautogui.mouseDown(button='left')
            sleep(0.1)
            pyautogui.move(2,2)
            sleep(0.1)
            pyautogui.moveTo(config.character, duration=0.2)
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

    def get_screenshoot(self, region=config.minimap, filename='screen'):
        timestamp = datetime.datetime.now()
        # get screen shoot
        myscreenshot = pyautogui.screenshot(region=region)
        # save it
        final_filename = str(region) + filename + '.png'
        myscreenshot.save(final_filename)
        print(final_filename)
        # invert image
        inverted_image = PIL.ImageOps.invert(Image.open(final_filename))
        # save it
        inverted_file_name = 'inverted' + str(region) + filename + '.png'
        inverted_image.save(inverted_file_name)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_SCREENSHOOT', looptime)
        return True

    def is_ring_on(self):
        # todo add .png for more rings
        ring_type = config.ring_to_equip
        # available: axe_ring, sword_ring
        if pyautogui.locateOnScreen('src/items/' + ring_type + ".png", region=config.ring, confidence=.5) is None:
            print("No ring detected")
            return False
        else:
            print("Ring equipped.")
            return True

    def put_on_ring(self, ring_hotkey):
        print("Equipping ring.")
        pyautogui.press(ring_hotkey)
        return True
