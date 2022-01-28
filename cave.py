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
        # testing
        timestamp = datetime.datetime.now()
        pyautogui.press(hotkey_rope)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_rope', looptime)
        return True

    def use_shovel(self):
        timestamp = datetime.datetime.now()
        pyautogui.press(hotkey_shovel)
        pyautogui.moveTo(character)
        pyautogui.click(character)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_shovel', looptime)
        return True

    def is_has_cap(self):
        timestamp = datetime.datetime.now()
        bp = Backpack()
        cap = bp.get_avial_cap()
        if int(cap) > min_cap_to_cont_hunt:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_has_cap T', looptime)
            return True
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_has_cap F', looptime)
            return False

    def is_ready_to_go_to_dp(self):
        timestamp = datetime.datetime.now()
        if self.is_has_cap():
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp F', looptime)
            return False
        elif not(self.is_has_cap()):
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp T', looptime)
            return True

    def is_on_wp(self, wp):
        timestamp = datetime.datetime.now()
        # standing on wp ?
        xyz = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=minimap, confidence=.9)
        if xyz is not None:
            # debug
            print(xyz)
            if not(wp_center[0] - 1 <= xyz[0] <= wp_center[0] + 1) and not(wp_center[1] - 1 <= xyz[1] <= wp_center[1] + 1):
            #if xyz != wp_center and xyz != wp_center2 and xyz != wp_center3:
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
        if specials[wp] is not None:
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

    def do_go_wp_plus(self, wp, specials:{}):
        #todo timestamps
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
        if specials[wp] == 'dosmthfancy':
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus dosmthfancy', looptime)
            return True
        if specials[wp] is None:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus None', looptime)
            return True
        # if did not catch in any of ifs above
        return False


# new one to go dp/bank in one
    def go_somwhere(self, currentwp, specials: {}):
        print(currentwp)
        print(specials[currentwp])
        timestamp = datetime.datetime.now()
        # idz do wp
        self.do_go_wp(currentwp)
        # sprawdz czy doszedles do wp
        if self.is_on_wp(wp=currentwp):
            # jest to ostatni wp
            if specials[currentwp] == 'LAST':
                # its done to ostatni
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_somwhere LAST', looptime)
                return True
            # jesli nie jest ostatni
            # czy to jest fancy wp
            if self.is_wp_fancy(wp=currentwp, specials=specials):
                # jesli tak to zrob fancy rzeczy
                self.do_go_wp_plus(wp=currentwp, specials=specials)
                # dawaj na nast wp
                nextwp = currentwp+1
                print(nextwp)
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_somwhere do_go_wp_plus', looptime)
                return nextwp
            else:
                return currentwp+1
            ## if not caught anything else
            #print('face the thing that should not be')
        elif not self.is_on_wp(wp=currentwp):
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME go_somwhere nothing fancy, reach it go next', looptime)
            return currentwp

        # #jesli nie ostatni
#        if not specials[currentwp] == 'LAST':
#            # todo przeniesc to gdzies na pewno nie tu
#            # sprawdz czy nast na horyzoncie
#            nextwp = currentwp+1
#            print('debug', nextwp)
#            print('debug', specials[currentwp])
#            nextwp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(nextwp) + ".png",
#                                                          region=minimap,
#                                                          confidence=.8)
#            # jesli jest
#            if nextwp_coord is not None:
#                # jest nast na horyzncie, znaczy sie dotarlismy
#                # zwroc nastepny
#                timestamp2 = datetime.datetime.now()
#                looptime = timestamp2 - timestamp
#                print('TIME go_somwhere next_on_horizon', looptime)
#                return nextwp
        # w inny wypadku
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME go_somwhere False', looptime)
        return currentwp




