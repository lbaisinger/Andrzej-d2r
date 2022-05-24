from caves.any_8 import *
from gracz import *

player = Gracz()


def go(player=player, wp=1, ring=config.use_ring, amulet=config.use_amulet, rotation_iteration=1):
    # LOOP START #
    timestamp = datetime.datetime.now()
    if rotation_iteration == 4:
        rotation_iteration = 1
    # STATUS CHECK 1 #
    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                       manalow=config.manalow)
    # ATTACKING? #
    if player.is_bije():
        # YES #
        # PG MODE #
        if config.pg_mode:
            player.pg_mode(exeta=config.exeta, rotation_spell=rotation_iteration)
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
                    player.pg_mode(exeta=config.exeta, rotation_spell=rotation_iteration)
            else:
                # NO MONSTERS #
                # LOOT #
                player.do_loot()
                rotation_iteration = 1
                # GO TO NEXT WP #
                if wp == list(wps.keys())[-1]:
                    wp = list(wps.keys())[0]
                else:
                    wp += 1
                player.cave.do_go_wp(wp)
                if config.rush:
                    pyautogui.press(config.hotkey_haste)
        else:
            # NOT ON WP #
            # GO TO WP #
            player.cave.do_go_wp(wp)
    # MID-TIMING CHECK #
    timestamp_4 = datetime.datetime.now()
    looptime_4 = timestamp_4 - timestamp
    print('{:<30} {:<20.2f}'.format('MID-TIMING CHECK:', looptime_4.total_seconds()))
    if looptime_4.total_seconds() < 1.1:
        sleep(1.1 - looptime_4.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(1.1 - looptime_4.total_seconds(), ''))
    # STATUS CHECK 2 #
    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                       manalow=config.manalow)
    if ring:
        player.ring_control()
        sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    if amulet:
        player.amulet_control()
        sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
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
        nextwp = go(wp=nextwp, rotation_iteration=rot_iter)
        iteration += 1


pyautogui.click(config.default)
loop()
