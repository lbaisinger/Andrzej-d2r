import datetime

import cv2 as cv
import pyautogui
import time
import PIL.Image
from utils import *
from utils import Utils
from time import sleep
from config_picker import *


class Cave:

    def __init__(self):
        # self.current_waypoint =
        self.utils = Utils()
        pass

    def timing(f):
        def wrap(*args, **kwargs):
            time1 = time.time()
            ret = f(*args, **kwargs)
            time2 = time.time()
            print('DURATION {:<20s} {:.1f} ms'.format(
                f.__name__, (time2 - time1) * 1000.0))

            return ret

        return wrap

    def use_rope(self):
        # works ok
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.press(config.hotkey_rope)
        sleep(0.1)
        pyautogui.click(config.character)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_rope', looptime)
        return True

    def use_shovel(self):
        # works ok
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.press(config.hotkey_shovel)
        sleep(0.1)
        # pyautogui.moveTo(config.character)
        pyautogui.click(config.character)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_shovel', looptime)
        return True

    def use_ladder(self):
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.click(config.character, button='right')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_ladder', looptime)
        return True

    def is_has_cap(self):
        # todo fix it to be sure that it can always read cap
        timestamp = datetime.datetime.now()
        bp = Backpack()
        try:
            cap = bp.get_avial_cap()
            print('cap', cap)
            if int(cap) > config.min_cap_to_cont_hunt:
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_has_cap T', looptime)
                return True
            else:
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_has_cap F', looptime)
                return False
        except ValueError:
            # todo fix it to be sure that it can always read cap
            print('WARNING - couldnt read cap to int')
            return True

    def is_ready_to_go_to_dp(self):
        # todo fix it to be sure that it can always read cap
        timestamp = datetime.datetime.now()
        if self.is_has_cap():
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp F', looptime)
            return False
        elif not (self.is_has_cap()):
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp T', looptime)
            return True

    # @timing
    def is_on_wp(self, wp):
        # todo minimap center coords
        if self.utils.andrzej_szuka(region=config.minimap_center_cv, image_path='./src/wp/' + str(wp) + '.png'):
            # print('is on wp')
            return True
        else:
            # print('not on wp')
            return False

    # @timing
    def is_on_wp_legacy(self, wp):
        timestamp = datetime.datetime.now()
        # standing on wp ?
        # img = PIL.Image.open("src/wp/" + str(wp) + ".png")
        # img_size = img.size
        # wp_img = img.resize((img_size[0] * config.scale,
        #                      img_size[1] * config.scale))
        xyz = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png",#wp_img,
                                             region=config.minimap,
                                             # todo mozna by go mniejszym zrobic, ten region do jakiegos samego
                                             #  srodka minimapy
                                             confidence=.8)
        if xyz is not None:
            # debug
            # print(xyz)
            # to wide
            # if not(wp_center[0] -1 <= xyz[0] <= wp_center[0] +1) and not(wp_center[1] <= xyz[1] <= wp_center[1] +1):
            if xyz != config.wp_center and xyz != config.wp_center2 and xyz != config.wp_center3 and xyz != config.wp_center4 and xyz != config.wp_center5 and xyz != config.wp_center6 and xyz != config.wp_center7 and xyz != config.wp_center8 and xyz != config.wp_center9:
                print('not yet on wp', xyz)
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('{:<30} {:<20.2f}'.format('TIME IS_ON_WP F:', looptime.total_seconds()))
                return False
            else:
                print('>>>> reached wp', wp, 'at', xyz)
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('{:<30} {:<20.2f}'.format('TIME IS_ON_WP T:', looptime.total_seconds()))
                return True
        else:
            print('couldnt find wp', wp)
            # #try to move minimap
            # #add timestamp
            return False

    # @timing
    def do_go_wp(self, wp):

        print('going to wp', wp)
        if self.utils.andrzej_szuka(region=config.minimap_cv, image_path='./src/wp/' + str(wp) + '.png'):
            template = cv.imread('./src/wp/' + str(wp) + '.png')
            image = ImageGrab.grab(bbox=config.minimap_cv)
            img_cv = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
            # image = cv.imread('./src/wp/' + str(wp) + '.png')
            method = eval("cv.TM_CCOEFF_NORMED")
            res = cv.matchTemplate(img_cv, template, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # print(max_loc)
            pyautogui.click(config.minimap_cv[0]+max_loc[0], config.minimap_cv[1]+max_loc[1])
            pyautogui.moveTo(config.default)
        else:
            print('Couldnt find wp', wp)

    # @timing
    def do_go_wp_legacy(self, wp):
        # szuka wp na mapie i go naciska
        # dziala ok
        timestamp = datetime.datetime.now()
        img = PIL.Image.open("src/wp/" + str(wp) + ".png")
        img_size = img.size
        wp_img = img.resize((img_size[0] * config.scale,
                             img_size[1] * config.scale))
        wp_coord = pyautogui.locateCenterOnScreen(wp_img,
                                                  region=config.minimap,
                                                  confidence=.75)
        if wp_coord is not None:
            # print('going wp', str(wp), wp_coord[0], wp_coord[1])
            pyautogui.click(wp_coord[0], wp_coord[1])
            pyautogui.moveTo(
                config.default)  # Added moveto default (otherwise sometime mouse stays on wp and cannot detect)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('{:<30} {:<20.2f}'.format('TIME GO TO WP:', looptime.total_seconds()))
            return True
        else:
            print('couldnt find wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME GP_WP NOT_OK', looptime)

    def is_wp_fancy(self, wp, specials: {}):
        # todo verify if rly works
        timestamp = datetime.datetime.now()
        # sprawdz czy podany wp specjalny
        if specials[wp] in ['rope', 'shovel', 'ladder']:
            # to bedzie specjalyn wp
            print('am special')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_wp_fancy T', looptime)
            return True
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_wp_fancy F', looptime)
            return False

    def do_go_wp_plus(self, wp, specials: {}):
        # todo timestamps
        timestamp = datetime.datetime.now()
        if specials[wp] == 'rope':
            self.use_rope()
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus rope', looptime)
            return True
        if specials[wp] == 'shovel':
            self.use_shovel()
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus shovel', looptime)
            return True
        if specials[wp] == 'ladder':
            self.use_ladder()
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus use_ladder', looptime)
            return True
        #        if specials[wp] is None:
        #            timestamp2 = datetime.datetime.now()
        #            looptime = timestamp2 - timestamp
        #            print('TIME do_go_wp_plus None', looptime)
        #            return True
        # if did not catch in any of ifs above
        return False

    def is_wp_in_range(self, wp):
        wp_cords = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=config.minimap, confidence=.8)
        if wp_cords is not None:
            return True
        else:
            return False

    def go_somewhere(self, wp, specials: {}):
        nextwp = wp + 1

        # sprawdz czy nie wszedl po shcodach/wszedl w dziure
        if specials[wp] == 'lvl_changing_wp':
            print('to level changer')
            if self.is_wp_in_range(nextwp):
                return nextwp

        # sprawdz czy stoje na wp      
        if self.is_on_wp(wp=wp, wp_val=list(specials.values())):
            # sprawdz czy to nie koniec
            if specials[wp] == 'LAST':
                print('done! im there')
                return True

            # jak fancy to zrob cos 
            if self.is_wp_fancy(wp=wp, specials=specials):
                self.do_go_wp_plus(wp, specials)
            # i dawaj na next
            return nextwp

            # w kazdym innym wypadku
        self.do_go_wp(wp)
        return wp
