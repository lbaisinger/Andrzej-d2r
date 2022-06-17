################################
#           REGIONS            #
################################
bw = (4572, 887, 150, 130)
bw_2nd = (4572, 928, 50, 50)
redbox = (4572, 887, 4572+75, 887+150)
minimap = (4580, 21, 225, 210)
minimapplus = (1750, 30, 110, 700) #todo ask
backpack = (4222, 40, 320, 700)
ring = (4583, 424, 60, 60)
amulet = (4598, 440, 35, 35)
default = (3000, 870)
character = (3000, 870)


mana_pool_potek = (3350, 13, 3350+32, 13+32)
hp_pool_exura = (2738, 13, 2738+32, 13+32)
hp_pool_potek = (2477, 13, 2477+32, 13+32)
burn_mana = (3016, 13, 3018+32, 13+32)
#rotation = ['3', 'r', '4', 'r']
rotation = ['r', 'f', 'r', 'g']
#rotation = ['3', '4', '3', '4']
# openCV
mana_pool_potek_cv = mana_pool_potek
hp_pool_exura_cv = hp_pool_exura
hp_pool_potek_cv = hp_pool_potek
burn_mana_cv = burn_mana
bw_cv = (4572, 887, 4572+150, 887+130)
bw_2nd_cv = (4572, 928, 4572+150, 928+130)
bw_full = (4572, 887, 4572+150, 887+130) # 130
redbox_cv = (4567, 882, 4567+50, 882+150)
# wp in minimap center +/- 2 SQM for zoom 2 (zoom 1 - max zoom in, zoom 4 - max zoom out)
#minimap_center_cv = (4675, 115, 4675+20, 120+20)
minimap_center_cv = (4675, 115, 4675+20, 120+15)
status_bar = (4580, 535, 4580+110, 535+25)
minimap_cv = (4580, 21, 4580+225, 21+210)
ring_cv = (4583, 424, 4583+70, 424+70) # 40 35
amulet_cv = (4598, 440, 4598+70, 440+70) # 40 40
rush = True

# wp in minimap center +/- 2 SQM for zoom 2 (zoom 1 - max zoom in, zoom 4 - max zoom out)
#minimap_center_cv = (2079, 82, 2094, 97)
#minimap_cv = (2020, 30, 2140, 145)

################################
#           WP CENTERS         #
################################
wp_center = (4686, 124)
wp_center2 = (4686, 125) #todo
wp_center3 = (4685, 125) #todo
wp_center4 = (4685, 126)

wp_center5 = (4686, 126)
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
bloodrage = False
exeta = True
status_check = False
paralyze_check = False
poison_check = False

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
manahigh = True

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
