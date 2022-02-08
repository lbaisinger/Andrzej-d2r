##################
### Cavebot config
###
### Darashia
### Dragon lair
###
### Hall of fame:
### Worril 77+
###

cave_name = "Darashia Dragon Lair"
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
       7: None,
       8: None,
       9: None,
       10: None,
       11: None,
       12: None,
       13: None,
       14: None,
       15: None,
       16: None,
       17: None}

# Path to cave
to_cave_wps = {}

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
target_list = ["dragon"]

# FACC Backapck trash
#item_blacklsit = ['mouldy_chese', 'torch', 'leather_boots', 'spear', 'fish']

