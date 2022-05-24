import PIL
from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv
import time
import pyautogui
import datetime
from time import sleep
from utils import Backpack
from utils import Other
from utils import Utils
from cave import Cave
from config_picker import *


class Gracz:

    def __init__(self):
        self.gracz = {}
        self.monsterlist = []
        self.backpack = Backpack()
        self.other = Other()
        self.cave = Cave()
        self.utils = Utils()
        # Add pause after each pyautogui commands
        pyautogui.PAUSE = 0.05
        print('loaded with config ', confname)

    def timing(f):
        def wrap(*args, **kwargs):
            time1 = time.time()
            ret = f(*args, **kwargs)
            time2 = time.time()
            print('DURATION {:<20s} {:.1f} ms'.format(
                f.__name__, (time2 - time1) * 1000.0))

            return ret

        return wrap

    def get_avialable_slots(self):
        # podaje ile jest dostepynch slotow w regionie na bp
        # dziala ok
        return len(self.backpack.get_avial_slots())

    @timing
    def is_bije(self):
        timestamp = datetime.datetime.now()
        if self.utils.andrzej_szuka(region=config.redbox_cv, image_path="./src/status/attacking.png"):
            print('is_bije True')
            # timestamp2 = datetime.datetime.now()
            # looptime = timestamp2 - timestamp
            # print('{:<30} {:<20.2f}'.format('DURATION is_bije T:', looptime.total_seconds()))
            return True
        else:
            print('is_bije False')
            # timestamp2 = datetime.datetime.now()
            # looptime = timestamp2 - timestamp
            # print('{:<30} {:<20.2f}'.format('DURATION is_bije F:', looptime.total_seconds()))
            return False

    @timing
    def is_bije_legacy(self):
        # sprawdza czy jest cos zaznaczonego czerwona ramke na redbox region
        # dziala ok
        # timestamp = datetime.datetime.now()
        img = PIL.Image.open('src/status/attacking.png')
        img_size = img.size
        rescaled_img = img.resize((img_size[0] * config.scale,
                                   img_size[1] * config.scale))
        if pyautogui.locateOnScreen(rescaled_img, region=config.redbox, confidence=.5) is None:
            print('is_bije False')
            # timestamp2 = datetime.datetime.now()
            # looptime = timestamp2 - timestamp
            # print('{:<30} {:<20.2f}'.format('DURATION is_bije F:', looptime.total_seconds()))
            return False
        else:
            print('is_bije True')
            # timestamp2 = datetime.datetime.now()
            # looptime = timestamp2 - timestamp
            # print('{:<30} {:<20.2f}'.format('DURATION is_bije T:', looptime.total_seconds()))
            return True

    # todo wrzucic tablce 'hotkeys' z wybranymi skillami do rotacji (e.g. exori hur/ exori min)
    def pg_mode(self, exeta=False):
        timestamp = datetime.datetime.now()
        # check if there's monster to exeta res
        # todo monsters_to_exeta[] as argument
        if exeta:
            if pyautogui.locateOnScreen("src/monsters/young_sea_serpent.png", region=config.bw,
                                        confidence=.8) is not None:
                pyautogui.press('x')
                print('exeta!')
                sleep(0.1)
        if pyautogui.locateOnScreen("src/monsters/any.png", region=config.bw_2nd, confidence=.6) is not None:
            pyautogui.press(config.hotkey_pg_area_spell_1)
            sleep(0.1)
            pyautogui.press(config.hotkey_pg_area_spell_2)
        else:
            pyautogui.press(config.hotkey_pg_single_spell_1)
            sleep(0.1)
            pyautogui.press(config.hotkey_pg_single_spell_2)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('{:<30} {:<20.2f}'.format('Duration PG_MODE:', looptime.total_seconds()))

    def is_co_bic(self, target_list):
        timestamp = datetime.datetime.now()
        # check if there is smth to figtht
        # self.monsterlist = []
        # if self.other.szukaj_andrzeju(region=config.bw, )
        for j in target_list:
            # print(pyautogui.locateOnScreen(str(j) + ".png", region=bw, confidence=.5))
            if pyautogui.locateOnScreen("src/monsters/" + str(j) + ".png", region=config.bw, confidence=.9) is not None:
                # pyautogui.press('Esc')  # safety net
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('{:<30} {:<20.2f}'.format('Duration IS_CO_BIC T:', looptime.total_seconds()))
                return True
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('{:<30} {:<20.2f}'.format('Duration IS_CO_BIC F:', looptime.total_seconds()))
        return False

    @timing
    def is_allright(self, hplow=config.hplow,
                    hpmid=config.hpmid,
                    manalow=config.hpmid,
                    manahigh=config.hpmid):
        timestamp = datetime.datetime.now()
        pyautogui.press(config.hotkey_food)
        # Check for serious healing (potion)
        if hplow:
            if self.utils.andrzej_szuka(region=config.hp_pool_potek_cv, image_path="./src/status/empty-bar.png"):
                pyautogui.press(config.hotkey_hppot)
            timestamp_1 = datetime.datetime.now()
            looptime_1 = timestamp_1 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-hplow:', looptime_1.total_seconds()))
        # Check for lesser healing (exura)
        if hpmid:
            if self.utils.andrzej_szuka(region=config.hp_pool_exura_cv, image_path="./src/status/empty-bar.png"):
                pyautogui.press(config.hotkey_exura)
            timestamp_2 = datetime.datetime.now()
            looptime_2 = timestamp_2 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-hpmid:', looptime_2.total_seconds()))
        # Check for mana
        if manalow:
            if self.utils.andrzej_szuka(region=config.mana_pool_potek_cv, image_path="./src/status/empty-bar.png"):
                pyautogui.press(config.hotkey_manapot)
            timestamp_3 = datetime.datetime.now()
            looptime_3 = timestamp_3 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-manalow:', looptime_3.total_seconds()))
        if manahigh:  # szukamy szarego paska, jesli NIE jest szary to full mana - burn it
            if not self.utils.andrzej_szuka(region=config.burn_mana_cv, image_path="./src/status/empty-bar.png"):
                pyautogui.press(config.hotkey_manaburn)
            timestamp_4 = datetime.datetime.now()
            looptime_4 = timestamp_4 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-manahigh:', looptime_4.total_seconds()))
        timestamp_5 = datetime.datetime.now()
        looptime = timestamp_5 - timestamp
        print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT:', looptime.total_seconds()))
        return True

    def is_allright_legacy(self, hplow=config.hplow,
                           hpmid=config.hpmid,
                           manalow=config.hpmid,
                           manahigh=config.hpmid):
        timestamp = datetime.datetime.now()
        pyautogui.press(config.hotkey_food)
        # Check for serious healing (potion)
        if hplow:
            if pyautogui.pixelMatchesColor(int(config.hp_pool_potek[0]), int(config.hp_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_hppot)
            timestamp_1 = datetime.datetime.now()
            looptime_1 = timestamp_1 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-hplow:', looptime_1.total_seconds()))
        # Check for lesser healing (exura)
        if hpmid:
            if pyautogui.pixelMatchesColor(int(config.hp_pool_exura[0]), int(config.hp_pool_exura[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_exura)
            timestamp_2 = datetime.datetime.now()
            looptime_2 = timestamp_2 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-hpmid:', looptime_2.total_seconds()))
        # Check for mana
        if manalow:
            if pyautogui.pixelMatchesColor(int(config.mana_pool_potek[0]), int(config.mana_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_manapot)
            timestamp_3 = datetime.datetime.now()
            looptime_3 = timestamp_3 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-manalow:', looptime_3.total_seconds()))
        if manahigh:
            if pyautogui.pixelMatchesColor(int(config.burn_mana[0]), int(config.burn_mana[1]),
                                           (0, 52, 116),
                                           tolerance=10):
                pyautogui.press(config.hotkey_manaburn)
            timestamp_4 = datetime.datetime.now()
            looptime_4 = timestamp_4 - timestamp
            print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT-manahigh:', looptime_4.total_seconds()))
        timestamp_5 = datetime.datetime.now()
        looptime = timestamp_5 - timestamp
        print('{:<30} {:<20.2f}'.format('Duration IS_ALLRIGHT:', looptime.total_seconds()))
        return True

    def do_bank_deposit(self):
        # naciska 3 hotkeye w celu zdeponowac zloto
        # dziala ok
        pyautogui.press(config.hotkey_hi)
        sleep(2)
        pyautogui.press(config.hotkey_deposit_all)
        sleep(2)
        pyautogui.press(config.hotkey_yes)
        return True

    def do_ressuply(self):
        # zagregowana funkcja ressuply
        # mozna tu dolozyc wiecej akcji jak potrzeba
        if self.do_bank_deposit():
            return True
        else:
            return False

    def do_loot(self):
        # naciska shift + prawym na pola obok gracza
        # 1 2 3
        # 4 C 6
        # 7 8 9
        # dziala ok, chociaz jak bot zbyt zapierdala to mamy problem
        timestamp = datetime.datetime.now()
        # print('looting')
        pyautogui.keyDown('Shift')
        pyautogui.rightClick(config.character[0] - 75 * config.scale, config.character[1] - 75 * config.scale)  # 1
        pyautogui.rightClick(config.character[0], config.character[1] - 75 * config.scale)  # 2
        pyautogui.rightClick(config.character[0] + 75 * config.scale, config.character[1] - 75 * config.scale)  # 3
        pyautogui.rightClick(config.character[0] - 60 * config.scale, config.character[1])  # 4
        pyautogui.rightClick(config.character[0], config.character[1])  # C
        pyautogui.rightClick(config.character[0] + 60 * config.scale, config.character[1])  # 6
        pyautogui.rightClick(config.character[0] - 75 * config.scale, config.character[1] + 75 * config.scale)  # 7
        pyautogui.rightClick(config.character[0], config.character[1] + 75 * config.scale)  # 8
        pyautogui.rightClick(config.character[0] + 75 * config.scale, config.character[1] + 75 * config.scale)  # 9
        pyautogui.keyUp('Shift')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('{:<30} {:<20.2f}'.format('TIME LOOT:', looptime.total_seconds()))
        return True

    def do_bij(self):
        # naciska spacje i atakuje nast z battle window
        # dziala ok
        timestamp = datetime.datetime.now()
        # print('fight')
        pyautogui.press('space')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('{:<30} {:<20.2f}'.format('TIME BIJ:', looptime.total_seconds()))
        return True

    def ring_control(self, ring_hotkey=config.hotkey_ring):
        if pyautogui.locateOnScreen('src/items/ring_empty.png', region=config.ring, confidence=.5) is not None:
            print("No ring, equipping new one.")
            pyautogui.press(ring_hotkey)
            return False
        else:
            print("Ring equipped.")
            return True

    def amulet_control(self, amulet_hotkey=config.hotkey_amulet):
        if pyautogui.locateOnScreen('src/items/amulet_empty.png', region=config.amulet, confidence=.5) is not None:
            print("No Amulet, equipping new one.")
            pyautogui.press(amulet_hotkey)
            return False
        else:
            print("Amulet equipped.")
            return True
