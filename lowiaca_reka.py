import pyautogui
from time import sleep
from random import uniform, randint

# general

sqmsize = 128
tries = 4
rod_hotkey = 'F5'

# fish north
startsqm = [2107, 231]
endsqm = [3900, 620]

# helper
newsqm = [0, 0]


def do_fish(sqm=startsqm):
    sleep(1) # time to move to game window
    randdelay = uniform(1, 1.61)
    randtries = randint(tries-1, tries+1)
    for x in range(randtries):
        pyautogui.press(rod_hotkey)
        pyautogui.click(sqm)
        sleep(randdelay)
    # next sqm x row
    if sqm[0] + sqmsize < endsqm[0]:
        newsqm[0] = sqm[0] + sqmsize
        newsqm[1] = sqm[1]
    else:
        print('hit max X')
        newsqm[0] = 2107
        #newsqm[0] = startsqm[0] # nie mam pojecia czemu to nie dziala
        # next sqm y
        newsqm[1] = sqm[1] + sqmsize
        if newsqm[1] > endsqm[1]:
            print('hit max Y')
            print('done fishin')
            return False
    return newsqm


newsqm = startsqm

while newsqm is not False:
    newsqm = do_fish(newsqm)


