##################
### Cavebot config
###
### Rookgard
###
###
### Hall of fame:
### Cremna Nepe 2-8
### Thor Teik 2-8
### Benjamin Hatchet 2-8
###
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
wps = {1: None,
       2: None,
       3: None,
       4: None}
wp_val = list(wps.values())

# Path to cave
# from bank on the floor
to_cave_wps = {14: 'lvl_changing_wp',
               15: 'lvl_changing_wp',
               16: 'LAST'}

# Path to depo
# from dawnport surroundings
# from any in that cave
to_dp_wps = {11: 'lvl_changing_wp',
             12: 'lvl_changing_wp',
             13: 'LAST' }

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
# or just letters its faster
target_list = ["any"]

# FACC Backapck trash
item_blacklsit = ['leather_armor', 'bone_club', 'hand_axe', 'torch', 'leather_boots', 'spear', 'rope', 'meat']
