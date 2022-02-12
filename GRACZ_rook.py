from caves.rook import *
from gracz import *

# Facc rycek od one shotowania itemow do imbuli

sleep(2)
player = Gracz()
pyautogui.click(config.default)  # focus on game window


def go(player=player, wp=1):
    # main logic goes here
    timestamp = datetime.datetime.now()

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
#    while True:
    while player.cave.is_has_cap():
        print()
        print('going', nextwp)
        print()
        nextwp = go(wp=nextwp)



def go_hunt(player=player):
    wp = list(to_cave_wps.keys())[0]
    while wp is not True:
        wp = player.cave.go_somewhere(wp=wp, specials=to_cave_wps)
        sleep(3)
    print('reached hunting ground')



def go_depo(player=player):
    wp = list(to_dp_wps.keys())[0]
    while wp is not True:
        wp = player.cave.go_somewhere(wp, to_dp_wps)
        sleep(3)
    print('reached bank')
    player.do_bank_deposit()



def go_exp_yourself(player=player):
    go_hunt()
    loop()
    go_depo()



go_exp_yourself()
go_exp_yourself()
go_exp_yourself()
