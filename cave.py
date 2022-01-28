import datetime
import pyautogui
from utils import Backpack

try:
    from config_local import *
except ImportError:
    print('no local config')
    pass

try:
    from caves.venore_swamp_trolls import *
except ImportError:
    print('no cave config')
    pass


class Cave:

    def __init__(self):
        #self.current_waypoint =
        pass

    def use_rope(self):
        pyautogui.press(hotkey_rope)
        return True

    def use_shovel(self):
        pyautogui.press(hotkey_shovel)
        pyautogui.moveTo(character)
        pyautogui.click(character)
        return True

    def is_has_cap(self):
        bp = Backpack()
        cap = bp.get_avial_cap()
        if int(cap) > min_cap_to_cont_hunt:
            return True
        else:
            return False

    def is_ready_to_go_to_dp(self):
        if self.is_has_cap():
            return False
        elif not(self.is_has_cap()):
            return True

    def is_on_wp(self, wp):
        timestamp = datetime.datetime.now()
        # standing on wp ?
        xyz = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=minimap, confidence=.8)
        print(xyz)
        # todo not in range
        if xyz != wp_center and xyz != wp_center2 and xyz != wp_center3:
            print('did not yet reach wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_on_wp F', looptime)
            return False
        else:
            print('>>>> reached wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_on_wp T', looptime)
            return True

    def do_go_wp(self, wp):
        timestamp = datetime.datetime.now()
        wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=minimap, confidence=.8)
        if wp_coord is not None:
            # print('going wp', str(wp), wp_coord[0], wp_coord[1])
            pyautogui.click(wp_coord[0], wp_coord[1])
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp T', looptime)
            return True
        else:
            print('couldnt find wp')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp F', looptime)
            return False

    def is_wp_fancy(self, wp, specials: {}):
        timestamp = datetime.datetime.now()
        # sprawdz czy podany wp specjalny
        if wp in specials.keys():
            # to bedzie specjalyn wp
            print('am special')
            return True
        else:
            return False

    def do_go_wp_plus(self, wp, specials:{}):
        #todo timestamps
        if specials[wp] == 'rope':
            self.use_rope()
            return True
        if specials[wp] == 'shovel':
            self.use_shovel()
            return True
        if specials[wp] == 'dosmthfancy':
            return True
        # if did not catch in any of ifs above
        return False


# new one to go dp/bank in one
    def go_somwhere(self, currentwp, specials: {}):
        # todo timestamp
        # todo krecenie sie w kolko na hunty
#        timestamp = datetime.datetime.now()
        # idz do wp
        self.do_go_wp(currentwp)
        # sprawdz czy doszedles do wp
        if self.is_on_wp(wp=currentwp):
            # jest to ostatni wp
            if currentwp == specials.keys()[-1]:
                # its done to ostatni
                return True
            # jesli nie jest ostatni
            # czy to jest fancy wp
            if self.is_wp_fancy(wp=currentwp, specials=specials):
                # jesli tak to zrob fancy rzeczy
                self.do_go_wp_plus(wp=currentwp, specials=specials)
                # dawaj na nast wp
                nextwp = list(specials)[specials.index(currentwp) + 1]
                print(nextwp)
                return nextwp
        # #jesli nie ostatni
        if not specials[currentwp] == 'LAST':
            # sprawdz czy nast na horyzoncie
            nextwp = list(specials[specials.index(currentwp) + 1])
            nextwp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(nextwp) + ".png",
                                                          region=minimap,
                                                          confidence=.8)
            # jesli jest
            if nextwp_coord is not None:
                # jest nast na horyzncie, znaczy sie dotarlismy
                # zwroc nastepny
                return nextwp
        # w inny wypadku
        return False




