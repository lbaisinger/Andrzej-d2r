### CONFIG###

################################
#           REGIONS            #
################################
# wmctrl -r Tibia -e 0,0,0,2200,1369
scale = 1
bw = (2055, 355, 50, 50)
bw_2nd = (2055, 370, 50, 50)
redbox = (2020, 340, 40, 100)
minimap = (1745, 35, 120, 120)
minimap_center = (2080, 84, 15, 15)
backpack = (1566, 26, 160, 700)
ring = (2035, 240, 25, 25)
default = (1835, 300)
character = (870, 495)
mana_pool_potek = (1200, 43)
hp_pool_exura = (870, 43)
hp_pool_potek = (475, 45)
burn_mana = (1640, 40)
# openCV
mana_pool_potek_cv = (1640, 30, 1665, 50)
hp_pool_exura_cv = (880, 30, 905, 50)
hp_pool_potek_cv = (650, 30, 675, 50)
burn_mana_cv = (1200, 30, 1225, 50)
bw_cv = (2055, 355, 2105, 365)
bw_2nd_cv = (2055, 370, 2105, 400)
bw_full = (2045, 350, 2175, 480)
redbox_cv = (2020, 340, 2060, 440)
# wp in minimap center +/- 2 SQM for zoom 2 (zoom 1 - max zoom in, zoom 4 - max zoom out)
minimap_center_cv = (2079, 82, 2094, 97)
minimap_cv = (1745, 35, 1865, 155)

################################
#           WP CENTERS         #
################################
# # WP Center at zoom 1
# wp_center = (xxxx, yy)
# # WP Center at zoom 2
# wp_center = (1805, 89)
# # WP Center at zoom 3
wp_center = (2086, 89)
# +/- 2 SQM on zoom 2
# top-left corner = (2090, 93)
# bot-right corner = (2082, 85)
# # WP Center at zoom 4
# wp_center = (xxxx, yy)

################################
#           BATTLE             #
################################
use_ring = True
use_amulet = False
pg_mode = True
exeta = True
rush = True
rotation = ['r', 'f', 'g']

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
manahigh = True

################################
#           HOTKEYS     `      #
################################
hotkey_ring = 'f3'
hotkey_amulet = 'f9'
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
