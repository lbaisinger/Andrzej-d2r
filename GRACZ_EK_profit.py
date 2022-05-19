from caves.any_9 import *
from gracz import *

player = Gracz()
pyautogui.click(config.default)


def go(player=player, wp=1, ring=config.use_ring, amulet=config.use_amulet):
    # main logic goes here
    timestamp = datetime.datetime.now()
    if ring:
        player.ring_control()
        # sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    if amulet:
        player.amulet_control()
        # sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    bije = player.is_bije()
    if not bije:
        jestcobic = player.is_co_bic(target_list=target_list)
    elif config.pg_mode:
        pgmode = player.pg_mode(exeta=False)
    jest_ok = player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                 manalow=config.manalow)
    if jest_ok:
        if not bije:
            if jestcobic:  # is there an issue here? in the time between is_co_bic() check (line 19) until now (line
                # 26) some monsters could already apper on the screen, but maybe for this EXP mode it's no problem
                player.do_loot()
                player.do_bij()
            if not jestcobic:
                player.do_loot()
                if player.cave.is_on_wp(wp):
                    player.cave.use_rope()
                    sleep(0.5)
                    player.cave.use_shovel()
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
    print('{:<30} {:<20.2f}'.format('Total loop time:', looptime.total_seconds()))
    print()
    return wp


def loop():
    nextwp = 5
    iteration = 1
    while True:
        print()
        print('Starting loop:', iteration)
        print('going', nextwp)
        print()
        nextwp = go(wp=nextwp)
        iteration += 1


loop()
