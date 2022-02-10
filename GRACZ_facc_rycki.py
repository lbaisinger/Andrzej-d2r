from caves.venore_amazon_camp import *
from gracz import *

# Facc rycek od one shotowania itemow do imbuli

sleep(2)
player = Gracz()
pyautogui.click(config.default)  # focus on game window


def go(player=player, wp=1, ring=False):
    # main logic goes here
    timestamp = datetime.datetime.now()
    if ring:
        if player.other.is_ring_on() is False:
            player.other.put_on_ring(config.hotkey_ring)
            sleep(0.2)  # bot is too fast for Frodo to put his ring on, need to sleep a bit

    bije = player.is_bije()
    if not bije:  # check only if not attacking, otherwise waste of time
        jestcobic = player.is_co_bic(target_list=target_list)
    jest_ok = player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                 manalow=config.manalow)
    if jest_ok:
        if not bije:
            if jestcobic:
                player.do_loot()
                player.do_bij()
                player.backpack.do_drop_random_item_from_blacklist(item_blacklist=item_blacklsit)
            if not jestcobic:
                player.do_loot()
                player.backpack.do_drop_random_item_from_blacklist(item_blacklist=item_blacklsit)
                if player.cave.is_on_wp(wp, wp_val):
                    if wp == list(wps.keys())[-1]:
                        wp = list(wps.keys())[0]
                    else:
                        wp += 1
                else:
                    player.cave.do_go_wp(wp)
                    player.backpack.do_drop_random_item_from_blacklist(item_blacklist=item_blacklsit)
#  czyli jesli bije //   if bije
        else:
            player.backpack.do_drop_random_item_from_blacklist(item_blacklist=item_blacklsit)

    timestamp2 = datetime.datetime.now()
    looptime = timestamp2 - timestamp
    print()
    print('TIME FULLLOOP', looptime)
    print()
    return wp


def loop():
    nextwp = 1
    while True:
        print()
        print('going', nextwp)
        print()
        nextwp = go(wp=nextwp)


loop()
