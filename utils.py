import datetime
import cv2
import cv2 as cv
import pyautogui
import PIL
import pytesseract
from PIL import Image, ImageGrab
import numpy as np
from random import choice
from time import sleep
from config_picker import *


class Utils:

    def __init__(self):
        pass

    def andrzej_szuka(self, region, image_path):
        # todo load id as global before, not every time function runs
        template = cv.imread(image_path)
        # template = cv2.cvtColor(np.array(image))#, cv2.COLOR_RGB2BGR)
        img = ImageGrab.grab(bbox=region)
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        # openCV possible methods: ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED',
        # 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        method = eval("cv.TM_CCOEFF_NORMED")
        res = cv.matchTemplate(img_cv, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        print('{:<30}{:<20.3f}'.format('Best match:', max_val))
        # if res.any() >= 1.0:
        sleep(0.05)
        # cv.imshow('desc', img_cv)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        # cv.imshow('desc', template)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        if max_val >= 0.8:
            print('True')
            return True
        else:
            print('False')  # in case of manahigh this means there is no manahigh (no mana to burn)
            return False



class Backpack:

    def __init__(self):
        # self.current_waypoint =
        pass

    def get_avial_cap(self):
        # returns amount of cap left based on what it can read from inverted.png
        # tested - looks fine
        Other().get_screenshoot(region=config.cap_region, filename='bp')
        cap = pytesseract.image_to_string('inverted_bp.png',
                                          config='--psm 13 --oem 3 -c tessedit_char_whitelest=0123456789')
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
        # z listy itemy w caves, wybiera losowy itemy i probuje go wywalic
        # sprawdzanie calej listy za dlugo trwa
        timestamp = datetime.datetime.now()
        item = choice(item_blacklist)
        print('checking for item', item)
        item_cords = pyautogui.locateCenterOnScreen('src/items/' + str(item) + '.png', region=config.backpack,
                                                    confidence=.94)
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
            pyautogui.move(2, 2)
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

    def __init__(self):
        # self.current_waypoint =
        pass

    def get_screenshoot(self, region=config.minimap, filename='screen'):
        # self explainatory
        timestamp = datetime.datetime.now()
        # get screen shoot
        myscreenshot = pyautogui.screenshot(region=region)
        # save it
        final_filename = str(region) + filename + '.png'
        myscreenshot.save(final_filename)
        print(final_filename)
        # invert image
        inverted_image = PIL.ImageOps.invert(Image.open(final_filename))
        # gray scale 
        inverted_image = PIL.ImageOps.grayscale(inverted_image)
        # save it
        # inverted_file_name = 'inverted' + str(region) + filename + '.png'
        inverted_file_name = 'inverted_' + filename + '.png'
        inverted_image.save(inverted_file_name)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME GET_SCREENSHOOT', looptime)
        return True

