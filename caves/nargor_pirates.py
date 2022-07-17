##################
### Cavebot config
###
### Any 5 wp
###
###
### Hall of fame:
###

cave_name = "Any 5"
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: 'lvl_changing_wp',
       2: 'lvl_changing_wp',
       3: None,
       4: 'lvl_changing_wp',
       5: None,
       6: None,
       7: 'lvl_changing_wp',
       8: 'lvl_changing_wp',
       9: 'lvl_changing_wp',
       10: None}
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
item_blacklsit = ['torch']
