##################
### Cavebot config
###
### Venore
### Swamp Trolls
###
### Hall of fame:
### puchal 21 - 31+

### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: None,
       2: None,
       3: None,
       4: None,
       5: None,
       6: None}

# Path to cave
# from venore east bank
to_cave_wps = {16: None,
               17: 'shovel',
               18: None,
               19: 'LAST'}

# Path to depo
# last one is venore east bank
# from any in that cave
to_dp_wps = {16: None,
             15: 'rope',
             14: 'rope',
             13: None,
             12: None,
             19: None,
             20: 'LAST'}
to_dp_special_wps = {15: 'rope',
                     14: 'rope'}

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
target_list = ["swamp_troll"]

# FACC Backapck trash
item_blacklsit = ['mouldy_chese', 'torch', 'leather_boots', 'spear', 'fish']
