from gracz import *

player = Gracz()


def go(player=player,
       wp=1,
       ring=config.use_ring,
       amulet=config.use_amulet,
       iter=1):
    # LOOP START #
    global tryb_walki
    global multiple_rotation_iteration
    global single_rotation_iteration
    timestamp = datetime.datetime.now()

    if multiple_rotation_iteration >= len(config.rotation_multiple):
        #print(rotation_iteration)
        multiple_rotation_iteration = 0
    if single_rotation_iteration >= len(config.rotation_single):
        #print(rotation_iteration)
        single_rotation_iteration = 0

    # STATUS CHECK 1 #
    player.is_allright(hplow=config.hplow,
                       hpmid=config.hpmid,
                       manahigh=config.manahigh,
                       manalow=config.manalow)
    global tryb_walki

    if config.status_check:
        player.status_control()
    # check if next wp even exists
    if wp + 1 in wps.keys():
        # if so check if next wp is turtle one and if standing on it
        if (wps[wp + 1] == 'turtle' and player.cave.is_on_wp(wp + 1)) or \
                (wps[wp] == 'turtle' and player.cave.is_on_wp(wp)):
            # print('looks like it was turtle ride')
            # if so wait a moment to avoid coming back
            sleep(1)
            # increment wp
            wp += 1
            # handle leaving turtle raft
            player.cave.do_go_wp_plus(wp, wps)
            # give andrew some time to do that
            sleep(1)
            # increment wp
            wp += 1

    # ATTACKING? #
    if player.is_bije(region_bije=config.redbox_cv):
        # YES #
        if not tryb_walki:
            tryb_walki = True
    else:
        # NOT ATTACKING #
        # JUST FINISED ATTACKING?
        # global tryb_walki
        if tryb_walki:
            # YES - LOOT #
            player.do_loot()
        # JEST CO BIĆ?
        if player.is_co_bic():
            # YES #
            player.do_bij()
            if not tryb_walki:
                tryb_walki = True
        else:
            # NO MONSTERS #
            # global tryb_walki
            tryb_walki = False
            multiple_rotation_iteration = 0
            single_rotation_iteration = 0

            # IF NOT ON2 WP CUZ ITS LVL CHANGER
            if wps[wp] == 'lvl_changing_wp':
                # CHEK IF NEXT ONE IS IN RANGE
                if player.cave.is_wp_in_range(wp + 1):
                    # INCREMENT
                    wp += 1
            # IS ON WP? #
            if player.cave.is_on_wp(wp):
                # DOES WP NEEDS EXTRA ACTION?
                if wps[wp] in ['rope', 'shovel', 'ladder']:
                    # IF SO GO WP TO BE EXTRA SURE
                    player.cave.do_go_wp(wp)  # to be extra sure
                    #sleep(1)  # give some time to go
                    # DO CUSTOM ACTION
                    player.cave.do_go_wp_plus(wp, wps)
                # YES #
                # GO TO NEXT WP #
                if wp == list(wps.keys())[-1]:
                    wp = list(wps.keys())[0]
                    if config.rush:
                        pyautogui.press(config.hotkey_haste)
                else:
                    # INCREMENT
                    # But only if next is in range - why incerement otherwise?
                    if player.cave.is_wp_in_range(wp + 1):
                        wp += 1
                        if config.rush:
                            pyautogui.press(config.hotkey_haste)
            else:
                # NOT ON WP, CHECK IF SPECIAL, MAYBE ROPED AND NEED TO FIND NEXT WP?
                if wps[wp] in ['rope', 'shovel', 'ladder']:
                    if player.cave.is_wp_in_range(wp + 1):  # MANDATORY! otherwise will only try once to e.g. rope (even
                        # if wait 1 sec, for 8lvl Andrew this is not enough,
                        # better to increment only when see next wp!!!
                        wp += 1
            # GO TO WP #
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
    if player.is_bije(region_bije=config.redbox_cv):
        # YES #
        if not tryb_walki:
            tryb_walki = True
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

    if ring:
        player.ring_control()
        sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
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
    # LOOP END #
    return wp


def loop():
    nextwp = 1
    iteration = 1
    while True:
        print()

        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        print('{:<30} {:<20d}'.format('Going to wp:', nextwp))
        nextwp = go(wp=nextwp,
                    iter=iteration)
        iteration += 1


single_rotation_iteration = 0
multiple_rotation_iteration = 0
tryb_walki = False
pyautogui.click(config.default)
loop()
