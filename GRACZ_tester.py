from gracz import *

# - Added def szukaj_andrzeju(self, region, image_path) in utils.py
# - 6x FASTER!!! (is_allright() from 2 s to ~0.3 s)
# - GRACZ_tester.py for testing
# - update README.md, added flowchart
#
# next:
# - implement in other methods (is_bije, is_co_bic, pg_mode, is_on_wp, go_to_wp)

player = Gracz()

sleep(1)
# pyautogui.click(config.default)
sleep(1)

rotation_iteration = 1
# todo add rotation_iteration counter (reset to 1 after 3rd spell in rotation)
# rotation_iteration += 1
# if rotation_iteration == 4:
#   rotation_iteration = 1
print('openCV')
# player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
player.is_bije()
player.is_co_bic()
# player.pg_mode(exeta=config.exeta, rotation_iteration=rotation_iteration)
# while True:
# player.cave.is_on_wp(wp=1)
# player.cave.is_on_wp_legacy(wp=1)
sleep(1)
# player.cave.do_go_wp(wp=1)

print()
print('legacy/pyautogui')
# player.is_allright_legacy(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
# player.is_bije_legacy()34
# player.is_co_bic_legacy(target_list=['any'])
# player.pg_mode_legacy(exeta=config.exeta)
# player.cave.is_on_wp_legacy(wp=1)
# player.cave.do_go_wp_legacy(wp=1)
