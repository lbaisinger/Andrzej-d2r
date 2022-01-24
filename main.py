# Tibia cavebot (attack + loot + waypoint)
################################################################
# Required files
#   - names of the monsters on battle window (BW)
#   - waypoint images (markers on minimap, should be already included)
#
################################################################
# Available monsters (if not then put .png of the monster name from battle window (try to crop only the name)
# - pirate (works for all pirates)
# - crocodile
# - crab
# - tarantula
# - giant_spider
################################################################
# Version 1.2.
# New script for gold making - Tortoises & blood crabs in Laguna islands
# resp characterized by a lot of rope/shovel spots
# need to make WP adjustion for rope/shovel
# set rope and shovel to hotkey "use with crosshair" and move to mouse to character position in the game window
# rather big spawn, one circle with 2 levels, 4 caves on each (4 shovel + 4 rope WP)
# WP directly on stone pile/rope spot
# only 3 WP required: shovel -> WP -> rope -> repeat
################################################################
# Version 1.1.
# New main loop (more emphasis on detecting monsters)
# Added bw check instead of going through whole loop
#
# Version kingdom-swap
# no classic controls, gold stacks (!), 
# ctrl+LMB to loot
#
################################################################

import keyboard
import pyautogui
from pyautogui import *

__author__ = "bajsi"
__license__ = "GPL"
__version__ = "1.1."
__email__ = "bajs00@gmail.com"
__status__ = "Working"

# Add pause after each pyautogui command
pyautogui.PAUSE = 0.05
# Regions for battle window (bw), default mouse position (default), minimap,
# center of the minimap for reached wp (wp_center), ring slot
### REGIONS (1920 x 1080) ###
bw = (1550, 740, 150, 130)
redbox = (1740, 490, 30, 90)
minimap = (1750, 30, 110, 110)
ring = (1755, 230, 25, 25)
default = (1550, 300)
character = (950, 490)
wp_center = (1806, 83)


# Waypoints
wp_index = 2
total_wp = 3  # total waypoints used in the hunt; MAKE SURE all waypoints .png are available!

# Monster list for the hunt, must match names of the .png files
# LOWERCASE, prioritize
target_list = ["bloodcrab", "tortoise"]


def status_check():
    print("Status check")
    # Check for serious healing (potion)
    if pyautogui.pixelMatchesColor(570, 35, (40, 40, 40), tolerance=10):
        pyautogui.press('f1')
        sleep(0.1)
        pyautogui.press('r')
        print("~~~Fully healed!~~~")
    # Check for lesser healing (exura)
    elif pyautogui.pixelMatchesColor(800, 35, (40, 40, 40), tolerance=10):
        pyautogui.press('2')
        print("~~~Healed!~~~")
    # Check for mana
    if pyautogui.pixelMatchesColor(1160, 35, (40, 40, 40), tolerance=10):
        sleep(0.1)
        pyautogui.press('f2')
        print("~~~Mana restored!~~~")
    # # # Burn mana
    # if pyautogui.pixelMatchesColor(880, 35, (0, 55, 120), tolerance=10):
    #     pyautogui.press('2')
    #     # print("~~~Mana burned!~~~")
    #     pyautogui.press('f3')


def loot():
    pyautogui.keyDown('Shift')
    pyautogui.rightClick(800, 400)
    pyautogui.rightClick(860, 400)
    pyautogui.rightClick(920, 400)
    pyautogui.rightClick(920, 470)
    pyautogui.rightClick(920, 540)
    pyautogui.rightClick(860, 540)
    pyautogui.rightClick(800, 540)
    pyautogui.rightClick(800, 470)
    pyautogui.keyUp('Shift')


def attack(name):
    # Check if currently attacking
    if pyautogui.locateOnScreen("attacking.png", region=redbox, confidence=.4) is not None:
        while pyautogui.locateOnScreen("attacking.png", region=redbox, confidence=.4):
            status_check()
            sleep(0.2)
            pyautogui.press('3')
            pyautogui.press('4')
            print("Currently attacking", name)
    elif pyautogui.locateOnScreen(name + ".png", region=bw, confidence=.7) is not None:
        # Find monster (name) on bw
        monster_coord = pyautogui.locateOnScreen(name + ".png", region=bw, confidence=.7)
        if monster_coord is not None:
            print("Locating monster coordinates")
            monster = pyautogui.center(monster_coord)
        else:
            return
        pyautogui.click(monster[0], monster[1])
        print("Attacking new", name)
        status_check()
        loot()
        pyautogui.moveTo(default)
        # sleep(0.2)
        # pyautogui.press('3')
        # pyautogui.press('4')


def waypoints(wp):
    wp_coord = pyautogui.locateOnScreen(str(wp) + ".png", region=minimap, confidence=.7)
    marker = pyautogui.center(wp_coord)
    print("Going to WP", wp)
    pyautogui.click(marker[0], marker[1])
    pyautogui.moveTo(default)
    status_check()
    # sleep(1)


def bw_check():
    list1 = []
    for j in target_list:
        if pyautogui.locateOnScreen(str(j) + ".png", region=bw, confidence=.8) is not None:
            list1.append(True)
        else:
            list1.append(False)
    return list1


### NEW MAIN CAVEBOT LOOP ###
while not keyboard.is_pressed('0'):
    try:
        if pyautogui.locateOnScreen("sword_ring.png", region=ring, confidence=.5) is None:
            pyautogui.press('f4')
        while any(bw_check()):
            # Check for monsters on BW
            for i in target_list:
                print("Searching bw for", i)
                pyautogui.press('esc')
                while pyautogui.locateOnScreen(i + ".png", region=bw, confidence=.7) is not None:
                    attack(i)
            loot()
        else:
            print("bw clear")
        # If no monster then check if reached last WP
        if wp_index <= total_wp:
            # No - go to next WP
            try:
                # Standing on WP?
                if pyautogui.locateCenterOnScreen(str(wp_index) + ".png", region=minimap, confidence=.8) != wp_center:
                    # No - go to WP
                    waypoints(wp_index)
                    continue
                else:
                    # Yes - wp++, go to next WP
                    pyautogui.press('f5')
                    pyautogui.click(character)
                    pyautogui.press('f6')
                    pyautogui.click(character)
                    wp_index = wp_index + 1
                    waypoints(wp_index)
            except:
                print("Nie umiem chodzic - cos poszlo nie tak przy WP")
        else:
            # Yes - go to WP1
            wp_index = 1
            waypoints(wp_index)
            # print("Last WP")
        pyautogui.press('f3')
    except:
        Exception("CaveBot")
        print("Exception cavebot, cos poszlo nie tak")
#


# OLD MAIN LOOP
# while not keyboard.is_pressed('0'):
#     try:
#         # if pyautogui.locateOnScreen("sword_ring.png", region=ring, confidence=.5) is None:
#         #     print("Put on the ring Frodo")
#         #     pyautogui.press('f4')
#
#         for i in target_list:
#             while pyautogui.locateOnScreen(i + ".png", region=bw, confidence=.8) is not None:
#                 # while pyautogui.locateOnScreen(i + ".png", region=bw, confidence=.8) is not None:
#                 attack(i)
#                 print("attacking")
#
#         if wp_index <= total_wp:
#             try:
#                 if pyautogui.locateCenterOnScreen(str(wp_index) + ".png", region=minimap, confidence=.8) != wp_center:
#                     waypoints(wp_index)
#                 else:
#                     wp_index = wp_index + 1
#                     print("increment wp_index")
#             except:
#                 print("Nie umiem chodzic")
#         else:
#             wp_index = 1
#             print("reached last WP, going to first")
#
#     except:
#         Exception("CaveBot")
#         print("exception cavebot, cos poszlo nie tak")
