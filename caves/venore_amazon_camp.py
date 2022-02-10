##################
### Cavebot config
###
### Venore
### Amazon Camp
###
### Hall of fame:
###

cave_name = "Venore amazon camp"
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: None,
       2: None,
       3: None,
       4: None,
       5: None}
wp_val = list(wps.values())

# Path to cave
# from venore east bank
# 4 na powierzchni
to_cave_wps = {4: None,
               5: 'lvl_changing_wp',
               6: 'lvl_changing_wp',
               7: 'lvl_changing_wp',
               8: 'shovel',
               9: 'lvl_changing_wp',
               10: 'rope',
               11: 'LAST'}

# Path to depo
# last one is venore east bank
# from any in that cave
to_dp_wps = {11: 'lvl_changing_wp',
             12: 'rope',
             13: 'rope',
             14: 'lvl_changing_wp',
             15: 'lvl_changing_wp',
             16: 'lvl_changing_wp',
             17: 'LAST'}

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
#target_list = ["amazon"]
target_list = ["any"]

# FACC Backapck trash
# ground level
# item_blacklsit = ['iron_dagger', 'iron_dagger', 'sabre', 'skulls', 'breads', 'torch']
# -1 level

item_blacklsit = ['iron_dagger', 'iron_dagger', 'sabre', 'skulls', 'breads', 'torch', 'meat', 'hunting_spear', 'chain_armor', 'apples','spear','cape','cookies','wolf_tooth_chain', 'plate_armor','double_axe','coat','leather_boots','gold_sickle']
