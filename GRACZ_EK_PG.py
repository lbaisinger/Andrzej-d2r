############################################################
# RYCERZ WPIERDALA SIE PO SAME KULE I KRECI MIECZEM MLYNKI #
############################################################

# VERSION IN PROGRESS, NOT USABLE YET #

from caves.any_9 import *
from gracz import *

player = Gracz()
pyautogui.click(config.default)


def go(player=player, wp=1):

    # LOOP START #
    timestamp = datetime.datetime.now()
    if config.use_ring:
        if player.other.is_ring_on() is False:
            player.other.put_on_ring(config.hotkey_ring)
            sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit
    # TIMING CHECK #
    timestamp_2 = datetime.datetime.now()
    looptime_1 = timestamp_2 - timestamp
    looptime_full_1 = looptime_1.total_seconds()
    print('{:<30} {:<20.2f}'.format('Timestamp ring:', looptime_full_1))

    # STATUS CHECK #
    if player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                          manalow=config.manalow):
        # TIMING CHECK #
        timestamp_2 = datetime.datetime.now()
        looptime_1 = timestamp_2 - timestamp
        looptime_full_1 = looptime_1.total_seconds()
        # todo if less then 1 s here
        print('{:<30} {:<20.2f}'.format('Timestamp ring:', looptime_full_1))
        # ATTACKING? #
        if player.is_bije():
            # YES #

            # PG MODE #
            player.pg_mode(exeta=False)
            # TIMING CHECK #
            timestamp3 = datetime.datetime.now()
            looptime_new = timestamp3 - timestamp
            looptime_f2 = looptime_new.total_seconds()
            print('{:<30} {:<20.2f}'.format('Total loop time:', looptime_f2))

            # STATUS CHECK #
            player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                               manalow=config.manalow)
            # TIMING CHECK #
            timestamp3 = datetime.datetime.now()
            looptime_new = timestamp3 - timestamp
            looptime_f2 = looptime_new.total_seconds()
            print('{:<30} {:<20.2f}'.format('Total loop time:', looptime_f2))
        else:
            # NOT ATTACKING #
            # IS ON WP? #
            if player.cave.is_on_wp(wp):
                # YES #
                # ARE THERE MOSNTERS? #
                if player.is_co_bic(target_list=target_list):
                    # YES #
                    # ATTACK #
                    player.do_bij()
                    # PG MODE #
                    player.pg_mode()
                    # STATUS CHECK #
                    player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                       manalow=config.manalow)
                else:
                    # NO MONSTERS #
                    # LOOT #
                    player.do_loot()
                    # todo is there enough time here for additional STATUS CHECK?
                    # GO TO NEXT WP #
                    if wp == list(wps.keys())[-1]:
                        wp = list(wps.keys())[0]
                    else:
                        wp += 1
                    player.cave.do_go_wp(wp)
            else:
                # NOT ON WP #
                # GO TO WP #
                player.cave.do_go_wp(wp)
                # todo is there enough time here for additional STATUS CHECK?


    timestamp3 = datetime.datetime.now()
    looptime_new = timestamp3 - timestamp
    looptime_f2 = looptime_new.total_seconds()
    print('{:<30} {:<20.2f}'.format('Total loop time:', looptime_f2))
    print()
    return wp


def loop():
    nextwp = 2
    iteration = 1
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        print('{:<30} {:<20d}'.format('Going to wp:', nextwp))
        nextwp = go(wp=nextwp)
        iteration += 1


loop()

