import keyboard
import pyautogui
from pyautogui import *

# Add pause after each pyautgui command
pyautogui.PAUSE = 0.1
# Regions for battle window (bw), default mouse position (default), minimap,
# center of the minimap for reached wp (wp_center), ring slot
bw = (1745, 490, 155, 150)
default = (1500, 300)
minimap = (1750, 30, 100, 100)
wp_center = (1806, 83)
ring = (1755, 230, 25, 25)
# Healing and mana burn
hp_bar = (1830, 190, (192, 192, 192))
mana_bar = (1830, 200, (114, 96, 255))
# Waypoints
wp_index = 1
total_wp = 6  # total waypoints used in the hunt
# Monster list for the hunt, must match names of the .png files
target_list = ["crocodile", "crab"]


def attack(name):
    # Find monster (name) on bw
    monster_coord = pyautogui.locateOnScreen(name + ".png", region=bw, confidence=.8)
    if monster_coord is not None:
        monster = pyautogui.center(monster_coord)
    else:
        return
    # Attack
    if pyautogui.locateOnScreen("attacking.png", region=bw, confidence=.4) is not None:
        while pyautogui.locateOnScreen("attacking.png", region=bw, confidence=.4):
            # # Check for serious healing (potion)
            if pyautogui.pixelMatchesColor(450, 35, (40, 40, 40), tolerance=10):
                pyautogui.press('f1')
                print("Fully healed!")
                pyautogui.press('f3')
            # Check for lesser healing (exura)
            if pyautogui.pixelMatchesColor(595, 35, (40, 40, 40), tolerance=10):
                pyautogui.press('2')
                print("Healed!")
                pyautogui.press('f3')
            # Check for mana
            if pyautogui.pixelMatchesColor(1150, 35, (40, 40, 40), tolerance=10):
                pyautogui.press('f2')
                print("mana restored")
                pyautogui.press('f3')
            # Burn mana
            if pyautogui.pixelMatchesColor(880, 35, (0, 55, 120), tolerance=10):
                pyautogui.press('2')
                print("mana burned")
                pyautogui.press('f3')
        else:
            loot()
            # Burn mana
            if pyautogui.pixelMatchesColor(880, 35, (0, 55, 120), tolerance=10):
                pyautogui.press('2')
                print("mana burned")
                pyautogui.press('f3')
    elif pyautogui.locateOnScreen(name + ".png", region=bw, confidence=.8) is not None:
        pyautogui.click(monster[0], monster[1])
        pyautogui.moveTo(default)
        # Burn mana
        if pyautogui.pixelMatchesColor(880, 35, (0, 55, 120), tolerance=10):
            pyautogui.press('2')
            print("mana burned")
            pyautogui.press('f3')
    else:
        loot()


def waypoints(wp):
    wp_coord = pyautogui.locateOnScreen(str(wp) + ".png", region=minimap, confidence=.7)
    marker = pyautogui.center(wp_coord)
    print("going to marker", wp)
    pyautogui.click(marker[0], marker[1])
    pyautogui.moveTo(default)
    sleep(0.5)


def loot():
    pyautogui.moveTo(800, 400)
    pyautogui.click(button='right')
    pyautogui.moveTo(860, 400)
    pyautogui.click(button='right')
    pyautogui.moveTo(920, 400)
    pyautogui.click(button='right')
    pyautogui.moveTo(920, 470)
    pyautogui.click(button='right')
    pyautogui.moveTo(920, 540)
    pyautogui.click(button='right')
    pyautogui.moveTo(860, 540)
    pyautogui.click(button='right')
    pyautogui.moveTo(800, 540)
    pyautogui.click(button='right')
    pyautogui.moveTo(800, 470)
    pyautogui.click(button='right')


def bw_check():
    list1 = []
    for i in target_list:
        if pyautogui.locateOnScreen(str(i) + ".png", region=bw, confidence=.8) is not None:
            list1.append(True)
        else:
            list1.append(False)
    return list1


a = any(bw_check())
print(a)
