import pyautogui
from importlib import import_module
from time import sleep

confname = '4k'
modulename = ('player_configs.config_' + confname)
config = import_module('player_configs.config_' + confname)

pyautogui.PAUSE = 0.005


def do_loot():
    # naciska shift + prawym na pola obok gracza
    # 1 2 3
    # 4 C 6
    # 7 8 9
    # dziala ok, chociaz jak bot zbyt zapierdala to mamy problem
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
    return True




do_loot()
