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
        self.cap = Backpack.get_avial_cap()
        if int(self.cap) > min_cap_to_cont_hunt:
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
        if xyz != wp_center and xyz != wp_center2 and xyz != wp_center3:
            # print('did not yet reach wp', wp)
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

    def go_to_cave(self, currentwp):
        timestamp = datetime.datetime.now()
        #  to_cave_wps
        # go wp
        self.do_go_wp(currentwp)
        # see if special moves
        if currentwp in to_cave_special_wps:
            print('special way point!')
            if self.is_on_wp(currentwp):
                print('standing on special way point!')
                if to_cave_special_wps[currentwp] == 'rope':
                    self.use_rope()
                    # todo
                    #currentwp = currentwp[#index +1]
                    timestamp2 = datetime.datetime.now()
                    looptime = timestamp2 - timestamp
                    print('TIME go_to_cave', looptime)
                    return currentwp
                if to_cave_special_wps[currentwp] == 'shovel':
                    self.use_shovel()
                    # todo
                    #currentwp = currentwp[##index +1]
                    timestamp2 = datetime.datetime.now()
                    looptime = timestamp2 - timestamp
                    print('TIME go_to_cave', looptime)
                    return currentwp
        else:
            # see if next wp on minimap
            # todo index +1
            #wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(currentwp[index+1]) + ".png", region=minimap, confidence=.8)
            wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(currentwp) + ".png", region=minimap, confidence=.8)
            if wp_coord is not None:
                print('next wp in area')
                #currentwp = currentwp[#index +1]
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_to_cave', looptime)
                return currentwp
            else:
                print('cant find next wp')
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_to_cave', looptime)
                return currentwp

        first_cave_wp = pyautogui.locateCenterOnScreen("src/wp/" + str(total_wp[0]) + ".png",region=minimap, confidence=.8)
        if first_cave_wp is not None:
            print('seems like reached cave')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME go_to_cave', looptime)
            return True


    def go_to_dp(self, currentwp):
        timestamp = datetime.datetime.now()
            # go wp
        self.do_go_wp(currentwp)
        # see if special moves
        if currentwp in to_dp_special_wps:
            print('special way point!')
            if self.is_on_wp(currentwp):
                print('standing on special way point!')
                if to_dp_special_wps[currentwp] == 'rope':
                    self.use_rope()
                    # todo
                    #currentwp = currentwp[#index +1]
                    timestamp2 = datetime.datetime.now()
                    looptime = timestamp2 - timestamp
                    print('TIME go_to_dp', looptime)
                    return currentwp
                if to_dp_special_wps[currentwp] == 'shovel':
                    self.use_shovel()
                    # todo
                    #currentwp = currentwp[##index +1]
                    timestamp2 = datetime.datetime.now()
                    looptime = timestamp2 - timestamp
                    print('TIME go_to_dp', looptime)
                    return currentwp
        else:
            # see if next wp on minimap
            # todo index +1
            #wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(currentwp[index+1]) + ".png", region=minimap, confidence=.8)
            wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(currentwp) + ".png", region=minimap, confidence=.8)
            if wp_coord is not None:
                print('next wp in area')
                #currentwp = currentwp[#index +1]
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_to_dp', looptime)
                return currentwp
            else:
                print('cant find next wp')
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_to_dp', looptime)
                return currentwp

        #todo fix it to print last
        bank = self.is_on_wp(to_dp_wps[-1])
        if bank:
            print('seems like reached dp')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME go_to_dp', looptime)
            return True

