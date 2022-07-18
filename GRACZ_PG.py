from gracz import *

player = Gracz()
global multiple_rotation_iteration
global single_rotation_iteration


def go(player=player,
       wp=1,
       iter=1,
       ring=config.use_ring,
       amulet=config.use_amulet):  # , rotation_iteration=1

    # LOOP START #
    timestamp = datetime.datetime.now()

    global multiple_rotation_iteration
    global single_rotation_iteration
    if multiple_rotation_iteration >= len(config.rotation_multiple):
        # print(rotation_iteration)
        multiple_rotation_iteration = 0
    if single_rotation_iteration >= len(config.rotation_single):
        # print(rotation_iteration)
        single_rotation_iteration = 0

    # STATUS CHECK 1 #
    player.is_allright(hplow=config.hplow,
                       hpmid=config.hpmid,
                       manahigh=config.manahigh,
                       manalow=config.manalow)
    # ATTACK OR WP ? #
    if not player.is_bije():
        # NOT ATTACKING #
        print('nie bije')
        # IF NOT ON2 WP CUZ ITS LVL CHANGER
        if wps[wp] == 'lvl_changing_wp':
            # CHEK IF NEXT ONE IS IN RANGE
            if player.cave.is_wp_in_range(wp + 1):
                # INCREMENT
                wp += 1
        # IS ON WP? #
        if player.cave.is_on_wp(wp):
            # YES #
            # print('is on wp')
            # ARE THERE MOSNTERS? #
            if player.is_co_bic():
                # YES #
                # ATTACK #
                player.do_bij()
            else:
                # NO MONSTERS #
                # LOOT #
                player.do_loot()
                multiple_rotation_iteration = 0
                single_rotation_iteration = 0
                # IS ON WP? #
                if player.cave.is_on_wp(wp):
                    # DOES WP NEEDS EXTRA ACTION?
                    if wps[wp] in ['rope', 'shovel', 'ladder']:
                        # IF SO GO WP TO BE EXTRA SURE
                        player.cave.do_go_wp(wp)  # to be extra sure
                        sleep(0.5)  # give some time to go
                        # DO CUSTOM ACTION
                        player.cave.do_go_wp_plus(wp, wps)
                    # YES #
                    # GO TO NEXT WP #
                    if wp == list(wps.keys())[-1]:
                        wp = list(wps.keys())[0]
                        if config.rush and not player.utils.andrzej_szuka(region=config.status_bar,
                                                                          image_path='./src/status/hasted.png',
                                                                          scale=True):
                            sleep(1)
                            pyautogui.press(config.hotkey_haste)
                    else:
                        wp += 1
                        if config.rush and not player.utils.andrzej_szuka(region=config.status_bar,
                                                                          image_path='./src/status/hasted.png',
                                                                          scale=True):
                            sleep(1)
                            pyautogui.press(config.hotkey_haste)
                # GO TO NEXT WP #
                player.cave.do_go_wp(wp)
        else:
            # NOT ON WP #
            # GO TO WP #
            if config.status_check:
                player.status_control()
            player.cave.do_go_wp(wp)
            player.eat_food(loop_count=iter)

    # MID-TIMING CHECK #
    timestamp_2 = datetime.datetime.now()
    looptime_2 = timestamp_2 - timestamp
    print('{:<30} {:<20.2f}'.format('MID-TIMING CHECK:', looptime_2.total_seconds()))
    if looptime_2.total_seconds() <= 1.16:
        sleep(1.16 - looptime_2.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(1.16 - looptime_2.total_seconds(), ''))
    # STATUS CHECK 2 #
    player.is_allright(hplow=config.hplow,
                       hpmid=config.hpmid,
                       manahigh=config.manahigh,
                       manalow=config.manalow)

    # ATTACKING? #
    if player.is_bije():
        # YES #
        # PG MODE #
        if config.pg_mode:
            timestamp_3 = datetime.datetime.now()
            looptime_3 = timestamp_3 - timestamp
            print('{:<30} {:<20.2f}'.format('PG-MODE CHECK:', looptime_3.total_seconds()))
            if looptime_3.total_seconds() < 1.56:
                sleep(1.56 - looptime_3.total_seconds())
                print('Sleeping {:.3f} seconds...'.format(1.56 - looptime_3.total_seconds(), ''))
            targets = player.pg_mode(exeta=config.exeta,
                                     multiple_spell=multiple_rotation_iteration,
                                     single_spell=single_rotation_iteration,
                                     iteration=iter)
            if targets == 'multiple':
                multiple_rotation_iteration += 1
            elif targets == 'single':
                single_rotation_iteration += 1

    # UTILS CHECK
    if ring:
        player.ring_control()
        sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit2
    if amulet:
        player.amulet_control()
        sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit

    # END-TIMING CHECK #
    timestamp_end = datetime.datetime.now()
    looptime_end = timestamp_end - timestamp
    print('{:<30} {:<20.2f}'.format('END-TIMING CHECK:', looptime_end.total_seconds()))
    if looptime_end.total_seconds() < 2.2:
        sleep(2.2 - looptime_end.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(2.2 - looptime_end.total_seconds()))
    print()
    return wp


def loop():
    nextwp = 1
    iteration = 1
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        print('{:<30} {:<20d}'.format('Going to wp:', nextwp))
        nextwp = go(wp=nextwp, iter=iteration)  # , rotation_iteration=rot_iter
        iteration += 1


multiple_rotation_iteration = 0
single_rotation_iteration = 0
pyautogui.click(config.default)
loop()
