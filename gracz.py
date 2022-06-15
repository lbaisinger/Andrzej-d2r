# global pkgs
from time import time, sleep
import pyautogui
import datetime
# andrew pkgs
import utils
import cave
from config_picker import *


class Gracz:

    def __init__(self):
        # self.backpack = utils.Backpack()
        self.cave = cave.Cave()
        self.utils = utils.Utils()
        # Add pause after each pyautogui commands
        pyautogui.PAUSE = config.pa_pause
        print('loaded with config ', confname)

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
    def is_bije(self):
        if self.utils.andrzej_szuka(region=config.redbox_cv,
                                    image_path="./src/status/attacking.png",
                                    confidence=0.3) is not False:
            # print('STATUS - Bije')
            return True
        else:
            # print('is_bije False')
            return False

    #@timing
    def pg_mode(self, exeta=config.exeta,
                bloodrage=config.bloodrage,
                rotation_spell=1,
                iteration=1):
        # exeta on turn 1 and 3 (no point exeta at start, better before exori gran, i.e. iteration == 1)
        if exeta and (rotation_spell == 1 or rotation_spell == 3):
            if self.utils.andrzej_szuka(region=config.bw_full,
                                        image_path='./src/monsters/any.png') is not False:
                pyautogui.press(config.hotkey_exeta)
                sleep(0.05)
        if self.utils.andrzej_szuka(region=config.bw_2nd_cv,
                                    image_path='./src/monsters/any.png',
                                    confidence=config.is_co_bic_custom_confidence,
                                    scale=False) is not False:
            # Case bloodrage only when multiple targets, waste to bloodrage single mob
            if bloodrage and not self.utils.andrzej_szuka(region=config.status_bar,
                                                          image_path='./src/status/boosted.png',
                                                          scale=False):
            # todo test new condition (only use bloodrage when attacking 2+ monster and NOT boosted already!
            # if bloodrage and rotation_spell == 0:
                pyautogui.press(config.hotkey_bloodrage)
                sleep(0.05)
            pyautogui.press(config.rotation[rotation_spell])
            #print('aoe' + str(rotation_spell))
        else:
            pyautogui.press(config.hotkey_pg_single_spell_1)
            #print('single spell 1')
            sleep(0.1)
            pyautogui.press(config.hotkey_pg_single_spell_2)
            #print('single spell 2')

    #@timing
    def is_co_bic(self):
        if self.utils.andrzej_szuka(region=config.bw_cv,
                                    image_path='./src/monsters/any.png',
                                    confidence=config.is_co_bic_custom_confidence,
                                    scale=False) is not False:
            #print('is_co_bic')
            return True
        else:
            #print('is_co_bic False')
            return False

    #@timing
    def is_allright(self, hplow=config.hplow,
                    hpmid=config.hpmid,
                    manalow=config.hpmid,
                    manahigh=config.hpmid):
        # pyautogui.press(config.hotkey_food)
        # Check for serious healing (potion)
        pot_used = False
        if hplow:
            if self.utils.andrzej_szuka(region=config.hp_pool_potek_cv,
                                        image_path="./src/status/empty-bar.png") is not False:
                pyautogui.press(config.hotkey_hppot)
                sleep(.15)
                # to be double sure that hp pot is used
                if self.utils.andrzej_szuka(region=config.hp_pool_potek_cv,
                                            image_path="./src/status/empty-bar.png") is not False:
                    pyautogui.press(config.hotkey_hppot)
                    sleep(.15)
                pot_used = True
                print('>>>Healed!')
            # else:
                # print('Low HP ok.')
        # Check for lesser healing (exura)
        if hpmid:
            if self.utils.andrzej_szuka(region=config.hp_pool_exura_cv,
                                        image_path="./src/status/empty-bar.png") is not False:
                pyautogui.press(config.hotkey_exura)
                print('>>>Exura')
            # else:
                # print('Mid HP ok.')
        # Check for mana
        if manalow:
            if self.utils.andrzej_szuka(region=config.mana_pool_potek_cv,
                                        image_path="./src/status/empty-bar.png") is not False and not pot_used:
                pyautogui.press(config.hotkey_manapot)
                sleep(.15)
                print('>>>Mana potion!')
            # else:
                # print('MP ok.')
        if manahigh:  # szukamy szarego paska, jesli NIE jest szary to full mana - burn it
            if not self.utils.andrzej_szuka(region=config.burn_mana_cv,
                                            image_path="./src/status/empty-bar.png") is not False:
                pyautogui.press(config.hotkey_manaburn)
                print('>>>Mana burned!')
        return True

    def status_control(self):
        if config.paralyze_check:
            if self.utils.andrzej_szuka(region=config.status_bar,
                                        image_path='./src/status/paralyze.png'):
                pyautogui.press(config.hotkey_paralyze)
        if config.poison_check:
            if self.utils.andrzej_szuka(region=config.status_bar,
                                        image_path='./src/status/paralyze.png'):
                pyautogui.press(config.hotkey_antidote)

    #@timing
    def eat_food(self, loop_count=1):
        if loop_count % 3 == 0:
            pyautogui.press(config.hotkey_food)
            print('munch')
            return True

    #@timing
    def do_bank_deposit(self):
        # naciska 3 hotkeye w celu zdeponowac zloto
        # dziala ok
        pyautogui.press(config.hotkey_hi)
        sleep(2)
        pyautogui.press(config.hotkey_deposit_all)
        sleep(2)
        pyautogui.press(config.hotkey_yes)
        return True

    #@timing
    def do_ressuply(self):
        # zagregowana funkcja ressuply
        # mozna tu dolozyc wiecej akcji jak potrzeba
        if self.do_bank_deposit():
            return True
        else:
            return False

    #@timing
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
        pyautogui.rightClick(config.character[0] - 75 * config.scale, config.character[1])  # 4
        pyautogui.rightClick(config.character[0], config.character[1])  # C
        pyautogui.rightClick(config.character[0] + 75 * config.scale, config.character[1])  # 6
        pyautogui.rightClick(config.character[0] - 75 * config.scale, config.character[1] + 75 * config.scale)  # 7
        pyautogui.rightClick(config.character[0], config.character[1] + 75 * config.scale)  # 8
        pyautogui.rightClick(config.character[0] + 75 * config.scale, config.character[1] + 75 * config.scale)  # 9
        pyautogui.keyUp('Shift')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('{:<30} {:<20.2f}'.format('TIME LOOT:', looptime.total_seconds()))
        return True

    #@timing
    def do_bij(self):
        # naciska spacje i atakuje nast z battle window
        # dziala ok
        # print('fight')
        pyautogui.press('space')
        return True

    #@timing
    def ring_control(self, ring_hotkey=config.hotkey_ring):
        if self.utils.andrzej_szuka(region=config.ring_cv,
                                    image_path='./src/items/ring_empty.png') is not False:
            print("No ring, equipping new one.")
            pyautogui.press(ring_hotkey)
            return False
        else:
            #print("Ring equipped.")
            return True

    #@timing
    def amulet_control(self, amulet_hotkey=config.hotkey_amulet):
        if self.utils.andrzej_szuka(region=config.amulet_cv,
                                    image_path='./src/items/amulet_empty.png') is not False:
            print("No Amulet, equipping new one.")
            pyautogui.press(amulet_hotkey)
            return False
        else:
            #print("Amulet equipped.")
            return True
