##################
### Cavebot config
###
### Rookgard
###
###
### Hall of fame:
###

### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: None,
       2: None,
       3: None}

# Path to cave
# from venore east bank
to_cave_wps = {14: None,
               15: 'LAST'}

# Path to depo
# last one is venore east bank
# from any in that cave
to_dp_wps = {11: 'lvl_changing_wp',
             12: 'lvl_changing_wp',
             13: 'LAST' }

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
target_list = ["troll"]

# FACC Backapck trash
item_blacklsit = ['mouldy_chese', 'torch', 'leather_boots', 'spear', 'fish']
