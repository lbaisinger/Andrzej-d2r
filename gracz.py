import PIL
import pyautogui
import datetime
from time import sleep
from utils import Backpack
from utils import Other
from cave import Cave
from config_picker import *


class Gracz:

    def __init__(self):
        self.gracz = {}
        self.monsterlist = []
        self.backpack = Backpack()
        self.other = Other()
        self.cave = Cave()
        # Add pause after each pyautogui commands
        pyautogui.PAUSE = 0.05
        print('loaded with config ', confname)

    def get_avialable_slots(self):
        # podaje ile jest dostepynch slotow w regionie na bp
        # dziala ok
        return len(self.backpack.get_avial_slots())

    def is_bije(self):
        # sprawdza czy jest cos zaznaczonego czerwona ramke na redbox region
        # dziala ok
        timestamp = datetime.datetime.now()

        img = PIL.Image.open('src/status/attacking.png')
        img_size = img.size
        rescaled_img = img.resize((img_size[0] * config.scale,
                                   img_size[1] * config.scale))
        if pyautogui.locateOnScreen(rescaled_img, region=config.redbox, confidence=.3) is None:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_bije F', looptime)
            return False
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_bije T', looptime)
            return True

    def is_co_bic(self, target_list):
        # sprawdza czy jest ktorys z potworow z monsterlisty
        # dziala ok / nie dziala ok na 4k
        # mozna usprawnic szukajac a e i o u
        timestamp = datetime.datetime.now()
        # check if there is smth to figtht
        self.monsterlist = []
        for j in target_list:
            # print(pyautogui.locateOnScreen(str(j) + ".png", region=bw, confidence=.5))
            if pyautogui.locateOnScreen("src/monsters/" + str(j) + ".png", region=config.bw, confidence=.9) is not None:
                pyautogui.press('Esc')  # co by sie nie wpierdalal w 20 mobow zanim zacznie atakowac
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_co_bic T', looptime)
                return True
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME is_co_bic F', looptime)
        return False


    def is_allright(self, hplow=config.hplow,
                    hpmid=config.hpmid,
                    manalow=config.hpmid,
                    manahigh=config.hpmid):
        # sprawdza czy pixel w odpowiednim miejscu jest szary
        # jak tak to wykonuje odpowiednia akcje
        # dziala ok ale wolno
        timestamp = datetime.datetime.now()
        # print("Status check")
        # print('eatin')
        pyautogui.press(config.hotkey_food)
        # Check for serious healing (potion)
        if hplow:
            if pyautogui.pixelMatchesColor(int(config.hp_pool_potek[0]), int(config.hp_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_hppot)
                print("~~~Fully healed!~~~")
        # Check for lesser healing (exura)
        if hpmid:
            if pyautogui.pixelMatchesColor(int(config.hp_pool_exura[0]), int(config.hp_pool_exura[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_exura)
                print("~~~Healed!~~~")
        # Check for mana
        if manalow:
            if pyautogui.pixelMatchesColor(int(config.mana_pool_potek[0]), int(config.mana_pool_potek[1]),
                                           (40, 40, 40),
                                           tolerance=10):
                pyautogui.press(config.hotkey_manapot)
                print("~~~Mana restored!~~~")
        if manahigh:
            if pyautogui.pixelMatchesColor(int(config.burn_mana[0]), int(config.burn_mana[1]),
                                           (0, 52, 116),
                                           tolerance=10):
                pyautogui.press(config.hotkey_manaburn)
                print("~~~Mana Burned!~~~")
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME is_allright', looptime)
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
        print('TIME LOOTING', looptime)
        return True

    def do_bij(self):
        # naciska spacje i atakuje nast z battle window
        # dziala ok
        timestamp = datetime.datetime.now()
        # print('fight')
        pyautogui.press('space')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME do_bij', looptime)
        return True
