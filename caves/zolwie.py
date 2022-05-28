##################
### Cavebot config
###
### Zolwie na laguna island
### -3 i -4
###
### Hall of fame:
### Worril

cave_name = "zolwie"
### Waypoints

# start waypoint
wp_index = 1

# All waypoints to loop in that cave
# ustawilem sobie rope/shovel na 2 wp bo trudna mapa, jaskinia do ew. optymalizacji
wps = {1: 'shovel',
       2: 'shovel',
       3: 'shovel',
       4: 'shovel',
       5: 'shovel',
       6: 'shovel',
       7: 'shovel',
       8: None,
       9: 'shovel'}

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
