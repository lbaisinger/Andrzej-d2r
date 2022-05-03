import pyautogui
from time import sleep
from random import uniform, randint

# fish north

startsqm = [2107, 231]
sqmsize = 128
endsqm = [3900, 620]
tries = 6
rod_hotkey = 'F5'
newsqm = [0,0]

def do_fish(sqm=startsqm):
    randdelay = uniform(1, 2)
    randtries = randint(tries, tries+2)
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


