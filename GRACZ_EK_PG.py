############################################################
# RYCERZ WPIERDALA SIE PO SAME KULE I KRECI MIECZEM MLYNKI #
# WORK STILL IN PROGRESS!                                  #
# USE AT OWN RISK!!!                                       #
############################################################


from caves.any_8 import *
from gracz import *

player = Gracz()
pyautogui.click(config.default)


def go(player=player, wp=1, ring=config.use_ring, amulet=config.use_amulet):
    # LOOP START #
    timestamp = datetime.datetime.now()
    if ring:
        player.ring_control()
        # sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    if amulet:
        player.amulet_control()
        # sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    # TIMING CHECK 1 #
    timestamp_1 = datetime.datetime.now()
    looptime_1 = timestamp_1 - timestamp
    print('{:<30} {:<20.2f}'.format('Timestamp ring:', looptime_1.total_seconds()))
    # STATUS CHECK 1 #
    if player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                          manalow=config.manalow):
        # TIMING CHECK 2 #
        timestamp_2 = datetime.datetime.now()
        looptime_2 = timestamp_2 - timestamp
        print('{:<30} {:<20.2f}'.format('Timestamp STATUS CHECK 1:', looptime_2.total_seconds()))
        # todo if less then 1 s here
        # ATTACKING? #
        if player.is_bije():
            # YES #
            # TIMING CHECK 3 #
            timestamp_3 = datetime.datetime.now()
            looptime_3 = timestamp_3 - timestamp
            print('{:<30} {:<20.2f}'.format('Timestamp ATTACKING True:', looptime_3.total_seconds()))
            # PG MODE #
            if config.pg_mode:
                player.pg_mode(exeta=False)
            # TIMING CHECK 4 #
            timestamp_4 = datetime.datetime.now()
            looptime_4 = timestamp_4 - timestamp
            print('{:<30} {:<20.2f}'.format('Timestamp ATTACKING-PG MODE:', looptime_4.total_seconds()))
            # STATUS CHECK #
            player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                               manalow=config.manalow)
            # TIMING CHECK 5 #
            timestamp_5 = datetime.datetime.now()
            looptime_5 = timestamp_5 - timestamp
            print('{:<30} {:<20.2f}'.format('Timestamp ATTACKING-PG MODE:', looptime_5.total_seconds()))
        else:
            # NOT ATTACKING #
            # TIMING CHECK 6 #
            timestamp_6 = datetime.datetime.now()
            looptime_6 = timestamp_6 - timestamp
            print('{:<30} {:<20.2f}'.format('Timestamp NOT ATTACKING:', looptime_6.total_seconds()))
            # IS ON WP? #
            if player.cave.is_on_wp(wp):
                # YES #
                # TIMING CHECK 7 #
                timestamp_7 = datetime.datetime.now()
                looptime_7 = timestamp_7 - timestamp
                print('{:<30} {:<20.2f}'.format('Timestamp IS ON WP?:', looptime_7.total_seconds()))
                # ARE THERE MOSNTERS? #
                if player.is_co_bic(target_list=target_list):
                    # YES #
                    # TIMING CHECK 8 #
                    timestamp_8 = datetime.datetime.now()
                    looptime_8 = timestamp_8 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-MONSTERS:', looptime_8.total_seconds()))
                    # ATTACK #
                    player.do_bij()
                    # TIMING CHECK 9 #
                    timestamp_9 = datetime.datetime.now()
                    looptime_9 = timestamp_9 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-ATTACK:', looptime_9.total_seconds()))
                    # PG MODE #
                    if config.pg_mode:
                        player.pg_mode(exeta=False)
                    # TIMING CHECK 10 #
                    timestamp_10 = datetime.datetime.now()
                    looptime_10 = timestamp_10 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-PG MODE:', looptime_10.total_seconds()))
                    # STATUS CHECK #
                    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                       manalow=config.manalow)
                    # TIMING CHECK 11 #
                    timestamp_11 = datetime.datetime.now()
                    looptime_11 = timestamp_11 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-STATUS CHECK:', looptime_11.total_seconds()))
                else:
                    # NO MONSTERS #
                    # TIMING CHECK 12 #
                    timestamp_12 = datetime.datetime.now()
                    looptime_12 = timestamp_12 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-NO MONSTERS:', looptime_12.total_seconds()))
                    # LOOT #
                    player.do_loot()
                    # TIMING CHECK 13 #
                    timestamp_13 = datetime.datetime.now()
                    looptime_13 = timestamp_13 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-LOOT:', looptime_13.total_seconds()))
                    # todo is there enough time here for additional STATUS CHECK?
                    # GO TO NEXT WP #
                    if wp == list(wps.keys())[-1]:
                        wp = list(wps.keys())[0]
                    else:
                        wp += 1
                    player.cave.do_go_wp(wp)
                    # TIMING CHECK 14 #
                    timestamp_14 = datetime.datetime.now()
                    looptime_14 = timestamp_14 - timestamp
                    print('{:<30} {:<20.2f}'.format('Timestamp WP-GO TO NEXT WP:', looptime_14.total_seconds()))
            else:
                # NOT ON WP #
                # TIMING CHECK 15 #
                timestamp_15 = datetime.datetime.now()
                looptime_15 = timestamp_15 - timestamp
                print('{:<30} {:<20.2f}'.format('Timestamp NOT ON WP:', looptime_15.total_seconds()))
                # GO TO WP #
                player.cave.do_go_wp(wp)
                # TIMING CHECK 16 #
                timestamp_16 = datetime.datetime.now()
                looptime_16 = timestamp_16 - timestamp
                print('{:<30} {:<20.2f}'.format('Timestamp GO TO WP:', looptime_16.total_seconds()))
                # todo is there enough time here for additional STATUS CHECK?
    timestamp_end = datetime.datetime.now()
    looptime_end = timestamp_end - timestamp
    print('{:<30} {:<20.2f}'.format('Total loop time:', looptime_end.total_seconds()))
    print()
    return wp


def loop():
    nextwp = 1
    iteration = 1
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        print('{:<30} {:<20d}'.format('Going to wp:', nextwp))
        nextwp = go(wp=nextwp)
        iteration += 1


loop()
