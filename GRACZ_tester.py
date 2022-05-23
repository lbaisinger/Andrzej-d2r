from gracz import *

player = Gracz()

sleep(1)
# pyautogui.click(config.default)
sleep(1)

player.is_allright(hplow=config.hplow, hpmid=config.hpmid, manahigh=config.manahigh,
                                   manalow=config.manalow)

