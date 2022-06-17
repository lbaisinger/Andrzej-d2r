##################
### Cavebot config
###
### Svargrond
### Okolnir, west part
###
### Hall of fame:
###

cave_name = "Svargrond okolnir west"
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: 'lvl_changing_wp',
       2: None,
       3: 'lvl_changing_wp',
       4: None,
       5: 'lvl_changing_wp',
       6: 'lvl_changing_wp',
       7: 'lvl_changing_wp',
       8: None,
       9: None,
       10: None,
       11: None,
       12: 'lvl_changing_wp',
       13: None}
wp_val = list(wps.values())

# Path to cave
# from venore east bank
# 4 na powierzchni
to_cave_wps = {}

# Path to depo
# last one is venore east bank
# from any in that cave
to_dp_wps = {}

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
target_list = ["any"]

# FACC Backapck trash
# ground level
# item_blacklsit = ['iron_dagger', 'iron_dagger', 'sabre', 'skulls', 'breads', 'torch']
# -1 level

item_blacklsit = ['iron_dagger', 'iron_dagger', 'sabre', 'skulls', 'breads', 'torch', 'meat', 'hunting_spear', 'chain_armor', 'apples','spear','cape','cookies','wolf_tooth_chain', 'plate_armor','double_axe','coat','leather_boots','gold_sickle']
