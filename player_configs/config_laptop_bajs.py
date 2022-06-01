### CONFIG###

################################
#           REGIONS            #
################################
# todo remove obsolete
scale = 1
# bw = (1747, 352, 120, 100)
# bw_2nd = (1770, 374, 15, 15)
# redbox = (1740, 350, 40, 100)
# minimap = (1745, 35, 120, 120)
# minimapplus = (1750, 30, 110, 700)
# backpack = (1566, 26, 160, 700)
ring = (1745, 230, 45, 45)
amulet = (1745, 155, 45, 45)
default = (1550, 300)
character = (870, 485)
# todo remove obsolete
# mana_pool_potek = (1100, 40)
# hp_pool_exura = (800, 43)
# hp_pool_potek = (570, 43)
# burn_mana = (900, 43)
# openCV
hp_pool_potek_cv = (570, 30, 590, 50)
hp_pool_exura_cv = (780, 30, 800, 50)
mana_pool_potek_cv = (1130, 30, 1150, 50)
burn_mana_cv = (890, 30, 915, 50)
bw_cv = (1770, 355, 1820, 365)
bw_2nd_cv = (1770, 370, 1820, 400)
bw_full = (1760, 345, 1820, 475)
redbox_cv = (1740, 350, 1780, 470)
# wp in minimap center +/- 2 SQM for zoom 2 (zoom 1 - max zoom in, zoom 4 - max zoom out)
minimap_center_cv = (1800, 83, 1812, 95)
minimap_cv = (1745, 35, 1865, 155)
ring_cv = (1745, 230, 1790, 275)
amulet_cv = (1745, 155, 1790, 200)

################################
#           WP CENTERS         #
################################
# todo delete - obsolete
# # WP Center at zoom 1
# wp_center = (1807, 88)
# # # WP Center at zoom 2
# wp_center2 = (1807, 89)
# # # WP Center at zoom 3
# wp_center3 = (1807, 90)
# # # WP Center at zoom 4
# wp_center4 = (1806, 88)

################################
#           BATTLE             #
################################
use_ring = True
use_amulet = False
pg_mode = True
# exeta any monster?
exeta = True
# rush from wp to wp
rush = True
# can have any number of spells, just like rotation, e.g. exori/exori gran/exori/exori mas
rotation = ['r', 'f', 'r', 'g']

################################
#           HEAL & MANA        #
################################
# heal if hp low with poton
hplow = True
# heal if hp moderate with exura
hpmid = True
# see if low mana and drink potion
manalow = True
# see if too much mana and burn
manahigh = False

################################
#           HOTKEYS     `      #
################################
hotkey_ring = 'f3'
hotkey_amulet = 'f5'
hotkey_shovel = 'f7'
hotkey_rope = 'f8'
hotkey_exura = '2'
hotkey_manapot = 'f2'
hotkey_manaburn = 'v'
hotkey_hppot = 'f1'
hotkey_food = 'f4'
hotkey_pg_single_spell_1 = '3'
hotkey_pg_single_spell_2 = '4'
hotkey_pg_area_spell_1 = 'r'
hotkey_pg_area_spell_2 = 'f'
hotkey_hi = 'f10'
hotkey_deposit_all = 'f11'
hotkey_yes = 'f12'
hotkey_haste = 'v'
hotkey_exeta = 'x'
is_co_bic_custom_confidence = 0.75