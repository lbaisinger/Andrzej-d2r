from gracz import *

player = Gracz()


def go(player=player,
       iter=1,
       ring=config.use_ring,
       amulet=config.use_amulet,
       rotation_iteration=0):  #
    # LOOP START #
    timestamp = datetime.datetime.now()

    # checking if rotation_iteration is not out of range
    if rotation_iteration >= len(config.rotation):
        #print(rotation_iteration)
        rotation_iteration = 0

    # STATUS CHECK 1 #
    player.is_allright(hplow=config.hplow,
                       hpmid=config.hpmid,
                       manahigh=config.manahigh,
                       manalow=config.manalow)

    # ATTACKING? #
    if player.is_bije():
        # YES #
        # PG MODE #
        if config.pg_mode:
            player.pg_mode(exeta=config.exeta,
                           rotation_spell=rotation_iteration,
                           iteration=iter)
            rotation_iteration += 1
    else:
        # NOT ATTACKING #
        #player.do_loot()
        rotation_iteration = 0
            # IS ON WP? #
        if config.status_check:
            player.status_control()
        #player.eat_food(loop_count=iter)
    # MID-TIMING CHECK #

    timestamp_2 = datetime.datetime.now()
    looptime_2 = timestamp_2 - timestamp
    print('{:<30} {:<20.2f}'.format('MID-TIMING CHECK:', looptime_2.total_seconds()))
    if looptime_2.total_seconds() <= 1.1:
        sleep(1.1 - looptime_2.total_seconds())
        print('Sleeping {:.3f} seconds...'.format(1.1 - looptime_2.total_seconds(), ''))

    # STATUS CHECK 2 #
    player.is_allright(hplow=config.hplow,
                       hpmid=config.hpmid,
                       manahigh=config.manahigh,
                       manalow=config.manalow)

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
    return rotation_iteration


def loop():
    iteration = 1
    rotation_iteration = 0
    while True:
        print()
        print('{:<30} {:<20d}'.format('Starting loop', iteration))
        rotation_iteration = go(iter=iteration, rotation_iteration=rotation_iteration)
        iteration += 1


loop()
