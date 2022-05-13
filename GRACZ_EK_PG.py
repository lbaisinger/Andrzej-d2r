############################################################
# RYCERZ WPIERDALA SIE PO SAME KULE I KRECI MIECZEM MLYNKI #
############################################################

# VERSION IN PROGRESS, NOT USABLE YET #

from caves.any_9 import *
from gracz import *

player = Gracz()
pyautogui.click(config.default)


def go(player=player, wp=1):
    # main logic goes here
    timestamp = datetime.datetime.now()
    if config.use_ring:
        if player.other.is_ring_on() is False:
            player.other.put_on_ring(config.hotkey_ring)
            sleep(0.1)  # bot is too fast for Frodo to put his ring on, need to sleep a bit

    # TIMING TEST #
    timestamp_2 = datetime.datetime.now()
    looptime_1 = timestamp_2 - timestamp
    looptime_full_1 = looptime_1.total_seconds()
    print('{:<30} {:<20.2f}'.format('Timestamp ring:', looptime_full_1))

    if player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                          manalow=config.manalow):
        # TIMING TEST #
        timestamp_2 = datetime.datetime.now()
        looptime_1 = timestamp_2 - timestamp
        looptime_full_1 = looptime_1.total_seconds()
        # todo if less then 1 s here
        print('{:<30} {:<20.2f}'.format('Timestamp ring:', looptime_full_1))
        if player.is_bije():
            player.pg_mode(exeta=False)
            timestamp3 = datetime.datetime.now()
            looptime_new = timestamp3 - timestamp
            looptime_f2 = looptime_new.total_seconds()
            print('{:<30} {:<20.2f}'.format('Total loop time:', looptime_f2))
            player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                               manalow=config.manalow)


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

