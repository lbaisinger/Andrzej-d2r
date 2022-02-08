##################
### Cavebot config
###
### Venore
### Swamp Trolls
###
### Hall of fame:
### puchal 21 - 31+
### Cremna Nepe 8+

cave_name = "Venore Swap Trolls"
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: None,
       2: None,
       3: None,
       4: None,
       5: None,
       6: None,
       7: None}

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
target_list = ["swamp_troll"]

# FACC Backapck trash
item_blacklsit = ['mouldy_chese', 'torch', 'leather_boots', 'spear', 'fish']
