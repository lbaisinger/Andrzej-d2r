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
# Note: ze scyzorykiem to jeden chuj czy shovel czy rope
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
to_cave_wps = {}

# Path to depo
to_dp_wps = {}

# Monster list for the hunt, must match names of the .png files LOWERCASE, prioritize
target_list = ["any"]

# FACC Backapck trash
item_blacklsit = ['torch']
