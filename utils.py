# global pkgs
import cv2 as cv
from numpy import array
from time import time, sleep
from PIL import ImageGrab
# andrew pkgs
from config_picker import *


class Utils:

    def __init__(self):
        pass

    def timing(f):
        def wrap(*args, **kwargs):
            time1 = time()
            ret = f(*args, **kwargs)
            time2 = time()
            duration = (time2 - time1) * 1000.0
            print('DURATION {:<20s} {:.1f} ms'.format(
                f.__name__, duration))
            return ret

        return wrap

    #@timing
    def andrzej_szuka(self, d2_wnd,
                      region,
                      image_path,
                      confidence=0.75,
                      scale=True,
                      debug=False,
                      debugpx=False):
        # todo load id as global before, not every time function runs
        # print('Andrzej szuka', region)
        template_tmp = cv.imread(image_path)
        if scale and config.scale != 1:
            up_points = (template_tmp.shape[0] * config.scale,
                         template_tmp.shape[1] * config.scale)
            template = cv.resize(template_tmp, up_points, interpolation=cv.INTER_LINEAR)
        else:
            template = template_tmp
        # template = cv2.cvtColor(np.array(image))#, cv2.COLOR_RGB2BGR)
        img = ImageGrab.grab(bbox=(d2_wnd[0]+region[0], d2_wnd[1]+region[1], d2_wnd[0]+region[2], d2_wnd[1]+region[3]))
        img_cv = cv.cvtColor(array(img), cv.COLOR_RGB2BGR)
        # openCV possible methods: ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED',
        # 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED', 'cv.COLOR_RGB2BGR']
        method = eval("cv.TM_CCOEFF_NORMED")
        res = cv.matchTemplate(img_cv, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        sleep(0.05)
        if debug:
            print('{:<30}{:<20.3f}'.format('Best match:', max_val))
        if debugpx:
            cv.imshow('desc', img_cv)
            cv.waitKey(0)
            cv.destroyAllWindows()
            cv.imshow('desc', template)
            cv.waitKey(0)
            cv.destroyAllWindows()
        if max_val >= confidence:
            # print('True')
            #return True
            return d2_wnd[0]+region[0]+max_loc[0], d2_wnd[1]+region[1]+max_loc[1]
        else:
            # print('False')  # in case of manahigh this means there is no manahigh (no mana to burn)
            return False



# todo needs rework
# import pytesseract if needed to get sting from bp.png
#class Backpack:
#
#    def __init__(self):
#        pass
#
#    def get_avial_cap(self):
#        # returns amount of cap left based on what it can read from inverted.png
#        # tested - looks fine
#        Other().get_screenshoot(region=config.cap_region, filename='bp')
#        cap = pytesseract.image_to_string('inverted_bp.png',
#                                          config='--psm 13 --oem 3 -c tessedit_char_whitelest=0123456789')
#        print(cap.strip())
#        return cap

#    def get_avial_slots(self):
#        # works ok - no use yet
#        slots = list(pyautogui.locateAllOnScreen('src/status/backpack_slot.png', region=config.backpack, confidence=.8))
#        print(len(slots))
#        return slots
#

#todo if needed it needs to be redone with opencv
#from random import choice
#    def do_drop_random_item_from_blacklist(self, item_blacklist):
#        # facc feature
#        # z listy itemy w caves, wybiera losowy itemy i probuje go wywalic
#        # sprawdzanie calej listy za dlugo trwa
#        item = choice(item_blacklist)
#        print('checking for item', item)
#        item_cords = pyautogui.locateCenterOnScreen('src/items/' + str(item) + '.png', region=config.backpack,
#                                                    confidence=.94)
#        if item_cords is not None:
#            print('dropping', item)
#            # throw away
#            pyautogui.moveTo(item_cords[0] - 8, item_cords[1] + 4, duration=0.1)
#            sleep(0.1)
#            # pyautogui.dragTo(character, duration=.15)
#            #            pyautogui.click(item_cords[0]-17, item_cords[1]+6)
#            pyautogui.click()
#            pyautogui.mouseDown(button='left')
#            sleep(0.1)
#            pyautogui.move(2, 2)
#            sleep(0.1)
#            pyautogui.moveTo(config.character, duration=0.2)
#            ## sleep(0.1)
#            pyautogui.mouseUp(button='left')
#            return True
#        else:
#            return False
