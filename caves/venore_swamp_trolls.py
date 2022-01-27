##################
### Cavebot config
###
### Venore
### Swamp Trolls
###
### Hall of fame:
### puchal 21 - 30+

### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
total_wp = [1, 2, 3, 4, 5, 6]

# Path to cave
# from venore east bank
to_cave_wps = [16, 17, 18, 19]
to_cave_special_wps = {'17': 'shovel'}

# Path to depo
# last one is venore east bank
# from any in that cave
to_dp_wps = [16, 15, 14, 13, 12, 19, 14]
to_dp_special_wps = {'15': 'rope',
                     '14': 'rope'}

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
target_list = ["swamp_troll"]

# FACC Backapck trash
item_blacklsit = ['mouldy_chese', 'torch', 'leather_boots', 'spear', 'fish']
