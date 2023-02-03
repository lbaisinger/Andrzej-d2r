# global pkgs
import cv2 as cv
from numpy import array
import numpy as np
from time import time, sleep
from PIL import ImageGrab
# andrew pkgs
from config_picker import *
from PIL import Image, ImageDraw


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

    # @timing
    def andrzej_szuka(self,
                      d2_wnd,  # przekazane od GRACZA do lokalizacji okna gry
                      region,  # region w ktorym szukamy, moze byc jeden z 16 regionow, lub sklep/skrzynka/etc
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
        img = ImageGrab.grab(
            bbox=(d2_wnd[0] + region[0], d2_wnd[1] + region[1], d2_wnd[0] + region[2], d2_wnd[1] + region[3]))
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
            # return True
            return d2_wnd[0] + region[0] + max_loc[0], d2_wnd[1] + region[1] + max_loc[1]
        else:
            # print('False')  # in case of manahigh this means there is no manahigh (no mana to burn)
            return False
