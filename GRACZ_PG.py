from gracz import *

player = Gracz()
global rotation_iteration


def go(player=player, wp=1, iter=1, ring=config.use_ring, amulet=config.use_amulet):  # , rotation_iteration=1
    # LOOP START #
    global rotation_iteration
    timestamp = datetime.datetime.now()
    # STATUS CHECK 1 #
    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                       manalow=config.manalow)
    # ATTACKING? #
    if player.is_bije():
        # YES #
        # PG MODE #
        if config.pg_mode:
            timestamp_3 = datetime.datetime.now()
            looptime_3 = timestamp_3 - timestamp
            print('{:<30} {:<20.2f}'.format('PG-MODE CHECK:', looptime_3.total_seconds()))
            if looptime_3.total_seconds() < 0.6:
                sleep(0.6 - looptime_3.total_seconds())
                print('Sleeping {:.3f} seconds...'.format(0.6 - looptime_3.total_seconds(), ''))
            player.pg_mode(exeta=config.exeta, rotation_spell=rotation_iteration)
            rotation_iteration += 1
    else:
        # NOT ATTACKING #
        # IS ON WP? #
        if player.cave.is_on_wp(wp):
            # YES #
            # ARE THERE MOSNTERS? #
            if player.is_co_bic():
                # YES #
                # ATTACK #
                player.do_bij()
                # PG MODE #
                if config.pg_mode:
                    timestamp_4 = datetime.datetime.now()
                    looptime_4 = timestamp_4 - timestamp
                    print('{:<30} {:<20.2f}'.format('PG-MODE CHECK:', looptime_4.total_seconds()))
                    if looptime_4.total_seconds() < 0.5:
                        sleep(0.5 - looptime_4.total_seconds())
                        print('Sleeping {:.3f} seconds...'.format(0.5 - looptime_4.total_seconds(), ''))
                    player.pg_mode(exeta=config.exeta, rotation_spell=rotation_iteration)
                    rotation_iteration += 1
            else:
                # NO MONSTERS #
                # LOOT #
                player.do_loot()
                rotation_iteration = 1
                # GO TO NEXT WP #
                if player.cave.is_wp_fancy(wp, wps):
                    player.cave.do_go_wp_plus(wp, wps)
                if wp == list(wps.keys())[-1]:
                    wp = list(wps.keys())[0]
                    if config.rush:
                        pyautogui.press(config.hotkey_haste)
                else:
                    wp += 1
                    if config.rush:
                        pyautogui.press(config.hotkey_haste)
                player.cave.do_go_wp(wp)
        else:
            # NOT ON WP #
            # GO TO WP #
            player.cave.do_go_wp(wp)
            player.eat_food(loop_count=iter)
    # MID-TIMING CHECK #
    timestamp_2 = datetime.datetime.now()
    looptime_2 = timestamp_2 - timestamp
    print('{:<30} {:<20.2f}'.format('MID-TIMING CHECK:', looptime_2.total_seconds()))
    if looptime_2.total_seconds() <= 1.2:
        sleep(1.2 - looptime_2.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(1.2 - looptime_2.total_seconds(), ''))
    # STATUS CHECK 2 #
    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                       manalow=config.manalow)
    if ring:
        player.ring_control()
        sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    if amulet:
        player.amulet_control()
        sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit

    if rotation_iteration == len(config.rotation)+1:
        print(rotation_iteration)
        rotation_iteration = 1
    # END-TIMING CHECK #
    timestamp_end = datetime.datetime.now()
    looptime_end = timestamp_end - timestamp
    print('{:<30} {:<20.2f}'.format('END-TIMING CHECK:', looptime_end.total_seconds()))
    if looptime_end.total_seconds() < 2.1:
        sleep(2.1 - looptime_end.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(2.1 - looptime_end.total_seconds()))
    print()
    return wp


def loop():
    nextwp = 1
    iteration = 1
    rot_iter = 1
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        print('{:<30} {:<20d}'.format('Going to wp:', nextwp))
        nextwp = go(wp=nextwp, iter=iteration)  # , rotation_iteration=rot_iter
        iteration += 1


rotation_iteration = 1
pyautogui.click(config.default)
loop()
