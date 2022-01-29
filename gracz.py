#from random import choice
#import PIL
from time import sleep
import pyautogui
import datetime
from utils import Backpack
from utils import Other
from cave import Cave
# todo move import cave to some param like player(cave='')
# For newer versions, see importlib.import_module for Python 2 and Python 3.
from caves.venore_swamp_trolls import *


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
        self.cave = Cave()
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

    def do_bank_deposit(self):
        pyautogui.press(hotkey_hi)
        sleep(1)
        pyautogui.press(hotkey_deposit_all)
        sleep(1)
        pyautogui.press(hotkey_yes)
        return True

    def do_ressuply(self):
        if self.do_bank_deposit():
            return True
        else:
            return False

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


    def go(self, wp=1):
        # main logic goes here
        timestamp = datetime.datetime.now()
        bije = self.is_bije()
        jestcobic = self.is_co_bic()
        # todo below to be configurable
        #if self.is_allright(hplow=False, hpmid=False, manahigh=True, manalow=False):
        if self.is_allright(hplow=False, hpmid=False, manahigh=True, manalow=False):
            if not bije:
                if jestcobic:
                    self.do_bij()
                    self.do_loot()
                if not jestcobic:
                    self.do_loot()
                    if self.cave.is_on_wp(wp):
                        if wp == list(wps.keys())[-1]:
                            wp = list(wps.keys())[0]
                        else:
                            wp += 1
                    else:
                        self.cave.do_go_wp(wp)
                        # backpack_check()
                        self.backpack.do_drop_random_item_from_blacklist()
        # check if ready go to dp and go
        if self.cave.is_ready_to_go_to_dp():
            wp = list(to_dp_wps)[0]
            while wp is not True:
                print('before', wp)
                # #todo to chyba nie powinno tak wygladac ale jest 2 w nocy wiec jebac
                # #todo zostaje na chwile
                wp = player.cave.go_somwhere(currentwp=wp, specials=to_dp_wps)
                print('after', wp)
                if wp is False:
                    print('gdzies wyjebalo falsem')
                    return False
            # todo doing resupply
            sleep(5)
            self.do_ressuply()
            # go back to cave
            wp = list(to_cave_wps)[0]
            while wp is not True:
                wp = player.cave.go_somwhere(currentwp=wp, specials=to_cave_wps)
            # reset wp for cave bot
            wp = list(wps)[0]

        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print()
        print('TIME FULLLOOP', looptime)
        print()
        return wp

    def loop(self):
        nextwp = 1
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
#sleep(2)
#player.loop()
#player.other.get_screenshoot(region=redbox)

#player.cave.use_rope()
#player.cave.use_shovel()

sleep(2)
#player.other.get_screenshoot(region=cap_region)

# tested
#print(player.cave.is_has_cap())                #ok

#print(player.backpack.get_avial_slots())       #ok

#player.cave.use_rope()                         #ok
#player.cave.use_shovel()                        #ok
#print(player.cave.is_ready_to_go_to_dp())       #ok
#player.cave.is_on_wp(wp=1)                     #ok
#player.cave.do_go_wp(wp=1)                     #ok

# temp specials

temp_specials = {
    1: 'rope',
    3: 'shovel'
}
#print(player.cave.is_wp_fancy(wp=1, specials=temp_specials))       #ok
#print(player.cave.do_go_wp_plus(wp=1, specials=temp_specials))     #Ok


wp = 1
#print(temp_specials[wp])
#print(temp_specials[wp+1])

#tm = list(temp_specials)
#print(tm[tm.index(wp) + 1])

depo_wps = {
    1: 'rope',
    2: None,
    3: 'LAST'
}
#print(player.cave.go_somwhere(currentwp=1, specials=depo_wps))
#
#while True:
#    print()
#    print('next while true dla', wp)
#    print()
#    # go to cave
#    if wp is not True:
#        wp = player.cave.go_somwhere(currentwp=wp, specials=depo_wps)
#        if wp is False:
#            print('gdzies wyjebalo falsem')
#            break
#        print('generated wp', wp)
#    else:
#        print('its done')
#        # loop will cave bot and check if need to go to dp
#        wp = 1
#        player.loop()
#

to_cave_wps = {
    1: None,
    2: 'shovel',
    3: None,
    4: None,
    5: 'LAST'
}
# load cave
#from caves.rook import *
from caves.venore_swamp_trolls import *

# go to cave first time from bank
#wp = 4
#while wp is not True:
#    wp = player.cave.go_somwhere(currentwp=wp, specials=to_cave_wps)
#    if wp is False:
#        print('in be4 go wywalil false')
#        break

#player.other.get_screenshoot(region=bw)

# back to regular routine with go to dp if no cap

player.loop()
