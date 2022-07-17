from gracz import *

player = Gracz()

# sleep(2)
pyautogui.click(config.default)
rotation_iteration = 1


print('openCV')
# player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
# player.is_bije()
player.do_loot()
# player.is_co_bic()
# player.pg_mode(exeta=config.exeta, rotation_spell=rotation_iteration)
# while True:
# player.cave.is_on_wp(wp=1)
# player.cave.is_on_wp_legacy(wp=1)
# player.cave.do_go_wp(wp=1)
# player.ring_control()
# player.amulet_control()
iter = 1
# player.eat_food(loop_count=iter)

# sleep(1)


print()
print('legacy/pyautogui')
# player.is_allright_legacy(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
# player.is_bije_legacy()34
# player.is_co_bic_legacy(target_list=['any'])
# player.pg_mode_legacy(exeta=config.exeta)
# player.cave.is_on_wp_legacy(wp=1)
# player.cave.do_go_wp_legacy(wp=1)
# player.ring_control_legacy()
# player.amulet_control_legacy()
