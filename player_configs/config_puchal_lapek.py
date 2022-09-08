################################
#           REGIONS            #
################################
# char
default = (960, 457)
character = (960, 457)
sqm_edge_length_px = 36

# ( x - 1080 ) / 2
# (y /2 ) + 24

# hp/mana bar
mana_pool_potek_cv = (1022, 30, 1022+32, 30+32)
hp_pool_exura_cv = (898, 30, 898+32, 30+32)
hp_pool_potek_cv = (699, 30, 699+32, 30+32)
burn_mana_cv = (968, 30, 968,+32, 30+32)

# battle window
#bw_cv = (4572, 887, 4572+150, 887+130)
bw_cv = (1746, 468, 1746+75, 468+65)
#bw_2nd_cv = (4572, 928, 4572+150, 928+130)
bw_2nd_cv = (1746, 488, 1746+75, 488+65)
#bw_full = (4572, 887, 4572+150, 887+130) # 130
bw_full = (1746, 468, 1746+75, 468+65) # 130
#redbox_cv = (4567, 882, 4567+50, 882+150)
redbox_cv = (1744, 465, 1744+25, 465+75)
#redbox_cv_1st = (4567, 882, 4567+50, 882+50)
redbox_cv_1st = (1744, 465, 1744+25, 465+75)

# minimap
#minimap_center_cv = (4675, 115, 4675+20, 120+15)
minimap_center_cv = (1798, 82, 1798+20, 82+20)

# char items
#status_bar = (4580, 535, 4580+110, 535+25)
status_bar = (1750, 292, 1750+110, 292+25)

#minimap_cv = (4580, 21, 4580+225, 21+210)
minimap_cv = (1750, 35, 1750+120, 35+120)

#ring_cv = (4583, 424, 4583+70, 424+70) # 40 35
ring_cv = (1752, 236, 1752+40, 236+35)
#amulet_cv = (4598, 440, 4598+70, 440+70) # 40 40
amulet_cv = (1759, 244, 1759+40, 244+40)


################################
#           WP CENTERS         #
################################
wp_center = (1803, 86)
wp_center2 = (1803, 87) #todo
wp_center3 = (1802, 86) #todo
wp_center4 = (1802, 87)

wp_center5 = wp_center
wp_center6 = wp_center
wp_center7 = wp_center
wp_center8 = wp_center
wp_center9 = wp_center


################################
#           BATTLE             #
################################
use_ring = True
use_amulet = False
pg_mode = True
skillboost = True
#exeta = False
exeta = True
status_check = False
paralyze_check = False
poison_check = False
rotation_single = ['3', '4', 'r']
rotation_multiple = ['r', 'f', 'r', 'g']
rush = True

################################
#           HEAL & MANA `      #
################################
scale = 2
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
hotkey_ring = 'f10'
hotkey_amulet = 'f9'
hotkey_shovel = 'f8'
hotkey_rope = 'f8'
hotkey_bloodrage = 't'
hotkey_antidote = ''
hotkey_exura = '2'
hotkey_manapot = 'f4'
hotkey_manaburn = 'f7'
hotkey_hppot = 'f1'
hotkey_food = 'f11'
hotkey_pg_single_spell_1 = '3'
hotkey_pg_single_spell_2 = '4'
hotkey_pg_area_spell_1 = 'r'
hotkey_pg_area_spell_2 = 'f'
hotkey_haste = 'f9'
hotkey_exeta = 'f6'

# hotkey_chase = '/'    # OBSOLETE?

################################
#           MISC        `      #
################################
min_cap_to_cont_hunt = 15
pa_pause = 0.005
filename = '124ek_arena_Yalahar_2'
ServerLog_path = r'/home/bajsi/.local/share/CipSoft GmbH/Tibia/packages/Tibia/log/Server Log.txt'
cap_region = (4737, 510, 40, 20)
hotkey_hi = 'f10'
hotkey_deposit_all = 'f11'
hotkey_yes = 'f12'
is_co_bic_custom_confidence = 0.999
is_bije_custom_confidence = 0.25

