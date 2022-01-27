#from random import choice
#import PIL
from time import sleep
import pyautogui
import datetime
from utils import Backpack
from utils import Other
# todo status check hotkeys config
# todo params in config
# todo load custom config for hunting grounds ( new class hunting grounds)
# todo fast working monsterlirst
# todo rings -> class utils.py

try:
    from config_local import *
except ImportError:
    print('no local config')
    pass

class Gracz:

    def __init__(self):
        self.gracz = {}
        self.monsterlist = []
        self.backpack = Backpack()
        self.other = Other()
        # Add pause after each pyautogui commands
        pyautogui.PAUSE = 0.05

    def get_avialable_slots(self):
        return len(self.backpack.get_avial_slots())

    def is_bije(self):
        timestamp = datetime.datetime.now()
        if pyautogui.locateOnScreen('src/status/attacking.png', region=redbox, confidence=.5) is None:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_bije F', looptime)
            return False
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_bije T', looptime)
            return True

    def is_co_bic(self):
        timestamp = datetime.datetime.now()
        # check if there is smth to figtht
        self.monsterlist = []
        for j in target_list:
            # print(pyautogui.locateOnScreen(str(j) + ".png", region=bw, confidence=.5))
            if pyautogui.locateOnScreen("src/monsters/" + str(j) + ".png", region=bw, confidence=.8) is not None:
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_co_bic T', looptime)
                return True
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME is_co_bic F', looptime)
        return False

    # todo status check hotkeys config
    # todo params in config
    def is_allright(self, hplow=True, hpmid=True, manalow=True, manahigh=True):
        timestamp = datetime.datetime.now()
        #print("Status check")
        #print('eatin')
        pyautogui.press('f4')
        # Check for serious healing (potion)
        if hplow:
            if pyautogui.pixelMatchesColor(int(hp_pool_potek[0]), int(hp_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press('f1')
                print("~~~Fully healed!~~~")
        # Check for lesser healing (exura)
        if hpmid:
            if pyautogui.pixelMatchesColor(int(hp_pool_exura[0]), int(hp_pool_exura[1]),
                                        (40, 40, 40),
                                        tolerance=10):
                pyautogui.press('f3')
                print("~~~Healed!~~~")
        # Check for mana
        if manalow:
            if pyautogui.pixelMatchesColor(int(mana_pool_potek[0]), int(mana_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press('f2')
                print("~~~Mana restored!~~~")
        if manahigh:
            if pyautogui.pixelMatchesColor(int(burn_mana[0]), int(burn_mana[1]),
                                          (0, 52, 116),
                                          tolerance=10):
                pyautogui.press('f3')
                print("~~~Mana Burned!~~~")
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME is_allright', looptime)
        return True

    def is_on_wp(self, wp):
        timestamp = datetime.datetime.now()
        # standing on wp ?
        xyz = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=minimap, confidence=.8)
        print(xyz)
        if xyz != wp_center and xyz != wp_center2 and xyz != wp_center3:
            #print('did not yet reach wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME HAS_REACHED_WP NOK', looptime)
            return False
        else:
            print('>>>> reached wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME HAS_REACHED_WP OK', looptime)
            return True

    def do_loot(self):
        timestamp = datetime.datetime.now()
        #print('looting')
        pyautogui.keyDown('Shift')
        # 1 2 3
        # 4 C 6
        # 7 8 9
        pyautogui.rightClick(character[0] - 75, character[1] - 75 ) # 1
        pyautogui.rightClick(character[0], character[1] - 75)        # 2
        pyautogui.rightClick(character[0] + 75, character[1] - 75)  # 3
        pyautogui.rightClick(character[0] - 60, character[1])        # 4
        #                                                                       # C
        pyautogui.rightClick(character[0] + 60, character[1])        # 6
        pyautogui.rightClick(character[0] - 75, character[1] + 75)  # 7
        pyautogui.rightClick(character[0], character[1] + 75)        # 8
        pyautogui.rightClick(character[0] + 75, character[1] + 75)  # 9
        pyautogui.keyUp('Shift')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME LOOTING', looptime)
        return True

    def do_bij(self):
        timestamp = datetime.datetime.now()
        #print('fight')
        pyautogui.press('space')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME do_bij', looptime)
        return True

    def do_go_wp(self, wp):
        timestamp = datetime.datetime.now()
        wp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=minimap, confidence=.8)
        if wp_coord is not None:
            #print('going wp', str(wp), wp_coord[0], wp_coord[1])
            pyautogui.click(wp_coord[0], wp_coord[1])
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME GO_WP OK', looptime)
            return True
        else:
            print('couldnt find wp')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME GP_WP NOK', looptime)

    def go(self, wp=1):
        # main logic goes here
        timestamp = datetime.datetime.now()
        bije = self.is_bije()
        jestcobic = self.is_co_bic()
        # todo below to be configurable
        if self.is_allright(hplow=False, hpmid=False, manahigh=True, manalow=False):
            if not bije:
                if jestcobic:
                    self.do_bij()
                    self.do_loot()
                if not jestcobic:
                    self.do_loot()
                    if self.is_on_wp(wp):
                        if wp == total_wp:
                            wp = 1
                        else:
                            wp += 1
                    else:
                        self.do_go_wp(wp)
                        # backpack_check()
                        self.backpack.do_drop_random_item_from_blacklist()
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print()
        print('TIME FULLLOOP', looptime)
        print()
        return wp

    def loop(self):
        nextwp = 6
        while True:
#            print()
#            print('going', nextwp)
#            print()
            nextwp = self.go(wp=nextwp)




###
# init gracza
###
player = Gracz()



## true false czy bije
#print(player.is_bije())

## true false czy jest co bic
#print(player.is_co_bic())

## todo fast working monsterlirst
##print(player.monsterlist)

## walnij spacje
#player.do_bij()

## shift click do okola
#player.do_loot()

## previously status check
#player.is_allright(hplow=False, hpmid=False, manahigh=True, manalow=False)

#player.get_avialable_slots()
#player.other.get_screenshoot(region=bw)

##
## new init
##
#
#pyautogui.mouseInfo()
#
#player.do_loot()
sleep(2)
player.loop()
#player.other.get_screenshoot(region=redbox)