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

print('openCV')
# player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
player.is_bije()
print()
print('legacy/pyautogui')
# player.is_allright_legacy(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
#                                    manalow=config.manalow)
player.is_bije_legacy()
