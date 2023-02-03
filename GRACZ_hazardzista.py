import pyautogui

from gracz import *

player = Gracz()
d2_window = player.find_d2_window()
looptime = 0.5

def go(d2_wnd=d2_window,
       player=player,
       desired_looptime=looptime,
       iter=1):  # , rotation_iteration=1

    # LOOP START #
    timestamp = datetime.datetime.now()

    koronetka = player.utils.andrzej_szuka(d2_wnd, config.shop, image_path='./src/items/coronet.png')
    refresh = player.utils.andrzej_szuka(d2_wnd, config.gamble_refresh, image_path='./src/items/gamble_refresh.png')
    # print(refresh)
    # pyautogui.moveTo(refresh)
    print(koronetka)
    if koronetka:
        pyautogui.rightClick(koronetka)
        print("Kupilem koronetke!")
    else:
        pyautogui.click(refresh)
        print("Szukam dalej...")

    # END-TIMING CHECK #
    timestamp_end = datetime.datetime.now()
    looptime_end = timestamp_end - timestamp
    print('{:<30} {:<20.2f}'.format('END-TIMING CHECK:', looptime_end.total_seconds()))
    if looptime_end.total_seconds() < desired_looptime:
        sleep(desired_looptime - looptime_end.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(desired_looptime - looptime_end.total_seconds()))
    print()
    return 0


def loop():
    iteration = 1
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))

        # find_wnd()

        # sleep(2)
        nextwp = go(iter=iteration)  # , rotation_iteration=rot_iter
        iteration += 1

sleep(2)
# pyautogui.click(config.default)
loop()
