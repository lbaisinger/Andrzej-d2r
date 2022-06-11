# global pkgs
from time import time, sleep
import pyautogui
# andrew pkgs
import utils
from config_picker import *


class Cave:

    def __init__(self):
        self.utils = utils.Utils()
        pass

    def timing(f):
        def wrap(*args, **kwargs):
            time1 = time()
            ret = f(*args, **kwargs)
            time2 = time()
            print('DURATION {:<20s} {:.1f} ms'.format(
                f.__name__, (time2 - time1) * 1000.0))

            return ret

        return wrap

    #@timing
    def use_rope(self):
        # works ok
        sleep(0.15)
        pyautogui.press(config.hotkey_rope)
        sleep(0.15) # otherwise its too fast
        pyautogui.click(config.character)
        return True

    #@timing
    def use_shovel(self):
        # works ok
        pyautogui.press(config.hotkey_shovel)
        sleep(0.15)
        pyautogui.click(config.character)
        sleep(0.15) # otherwise its too fast
        return True

    #@timing
    def use_ladder(self):
        sleep(0.1)
        pyautogui.click(config.character, button='right')
        return True

    #@timing
    def is_on_wp(self, wp):
        # todo minimap center coords
        if self.utils.andrzej_szuka(debug=True,
                region=config.minimap_center_cv,
                image_path='./src/wp/' + str(wp) + '.png',
                confidence=.7) is not False:
            #print('is on wp')
            return True
        else:
            #print('not on wp')
            return False

    #@timing
    def do_go_wp(self, wp):

        #print('going to wp', wp)
        try:
            x, y = self.utils.andrzej_szuka(region=config.minimap_cv,
                                           image_path='./src/wp/' + str(wp) + '.png',
                                           confidence=0.69)
            #print(x,y)
            pyautogui.click(x+3, y+3)
            pyautogui.moveTo(config.default)
        except TypeError:
            print('Couldnt find wp', wp)
            return False

    #@timing
    def is_wp_fancy(self, wp, specials: {}):
        # todo verify if rly works
        # sprawdz czy podany wp specjalny
        if specials[wp] in ['rope', 'shovel', 'ladder', 'lvl_changing_wp']:
            # to bedzie specjalyn wp
            print('am special')
            return True
        else:
            return False

    #@timing
    def do_go_wp_plus(self, wp, specials: {}):
        # todo timestamps
        if specials[wp] == 'rope':
            self.use_rope()
            return True
        if specials[wp] == 'shovel':
            self.use_shovel()
            return True
        if specials[wp] == 'ladder':
            self.use_ladder()
            return True
        if specials[wp] == 'turtle':
            pyautogui.press('s')
            return True
        if specials[wp] == 'lvl_changing_wp':
            if self.is_wp_in_range(wp+1):
                return True
        # if did not catch in any of ifs above
        return False

    #@timing
    def is_wp_in_range(self, wp):
        if self.utils.andrzej_szuka(region=config.minimap_cv,
                                    image_path='./src/wp/' + str(wp) + '.png',
                                    confidence=0.69) is not False:
            return True
        else:
            return False

#
# todo needs rework
#
#    def is_has_cap(self):
#        # todo fix it to be sure that it can always read cap
#        # todo atm it happens that it sometimes print incorret values
#        bp = utils.Backpack()
#        try:
#            cap = bp.get_avial_cap()
#            print('cap', cap)
#            if int(cap) > config.min_cap_to_cont_hunt:
#                return True
#            else:
#                return False
#        except ValueError:
#            # todo fix it to be sure that it can always read cap
#            print('WARNING - couldnt read cap to int')
#            return True
#
#    def is_ready_to_go_to_dp(self):
#        # todo fix it to be sure that it can always read cap
#        if self.is_has_cap():
#            return False
#        elif not (self.is_has_cap()):
#            return True

