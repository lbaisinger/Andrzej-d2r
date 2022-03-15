from caves.any_5 import *
from gracz import *


player = Gracz()
pyautogui.click(config.default)


def go(player=player, wp=1, ring=True):
    # main logic goes here
    timestamp = datetime.datetime.now()
    if ring:
        if player.other.is_ring_on() is False:
            player.other.put_on_ring(config.hotkey_ring)
            sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit

    bije = player.is_bije()
    if not bije:
        jestcobic = player.is_co_bic(target_list=target_list)
    else:
        pgmode = player.pg_mode()
    jest_ok = player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                 manalow=config.manalow)
    if jest_ok:
        if not bije:
            if jestcobic:
                player.do_loot()
                player.do_bij()
            if not jestcobic:
                player.do_loot()
                if player.cave.is_on_wp(wp):
                    if wp == list(wps.keys())[-1]:
                        wp = list(wps.keys())[0]
                    else:
                        wp += 1
                else:
                    walk = player.cave.do_go_wp(wp)
                    if not walk:
                        if wp == list(wps.keys())[-1]:
                            wp = list(wps.keys())[0]
                        else:
                            wp += 1
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp

    print()
    print('TIME FULLLOOP', looptime)
    print()
    return wp


def loop():
    nextwp = 2
    iteration = 1
    while True:
        print()
        print('Starting loop:', iteration)
        print('going', nextwp)
        print()
        nextwp = go(wp=nextwp)


loop()
