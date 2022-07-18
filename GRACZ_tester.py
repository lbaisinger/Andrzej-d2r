from gracz import *
from utils import *

player = Gracz()
utils = Utils()
sleep(2)
pyautogui.click(config.default)
rotation_iteration = 1

iter = 1


print('openCV')
# x = utils.andrzej_szuka(region=config.bw_2nd_cv,
#                                     image_path='./src/monsters/any.png',
#                                     confidence=config.is_co_bic_custom_confidence,
#                                     scale=False)
# print(x)
# player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
# player.is_bije()
# player.do_loot()
# player.is_co_bic()
# while True:
# player.cave.is_on_wp(wp=1)
# player.cave.is_on_wp_legacy(wp=1)
# player.cave.do_go_wp(wp=1)
# player.ring_control()
# player.amulet_control()
# player.eat_food(loop_count=iter)
multiple_rotation_iteration = 0
single_rotation_iteration = 0

for iter in range(1,5):
    if multiple_rotation_iteration >= len(config.rotation_multiple):
        # print(rotation_iteration)
        multiple_rotation_iteration = 0
    if single_rotation_iteration >= len(config.rotation_single):
        # print(rotation_iteration)
        single_rotation_iteration = 0
    targets = player.pg_mode(exeta=config.exeta,
                             multiple_spell=multiple_rotation_iteration,
                             single_spell=single_rotation_iteration,
                             iteration=iter)
    if targets == 'multiple':
        multiple_rotation_iteration += 1
    elif targets == 'single':
        single_rotation_iteration += 1
    print(targets)
    sleep(2)
# print()
# print('legacy/pyautogui')
# player.is_allright_legacy(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
# player.is_bije_legacy()34
# player.is_co_bic_legacy(target_list=['any'])
# player.pg_mode_legacy(exeta=config.exeta)
# player.cave.is_on_wp_legacy(wp=1)
# player.cave.do_go_wp_legacy(wp=1)
# player.ring_control_legacy()
# player.amulet_control_legacy()
