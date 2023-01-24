### CONFIG###
################################
#            REGIONS           #
#  RESOLUTION = 1280x800       #
# this time regions are added  #
# to d2 window coords          #
# regions=offsets from d2_wnd  #
################################
single_slot = (36, 36)
shop = (130, 195, 130+10*single_slot[0], 195+10*single_slot[1])
gamble_refresh = (410, 580, 480, 660)


################################
#           BATTLE             #
################################


################################
#           HEAL & MANA        #
################################
# Use rejuvenation potion on low HP
hplow = True
# Use healing potion on mid HP
hpmid = True
# use mana potion on low MP
manalow = False

################################
#           HOTKEYS            #
################################
attack_skill_1 = 'r'
attack_skill_2 = 'e'
teleport = 'f'
static_field = 'c'
support_skill_1 = 'f1'
support_skill_2 = 'f2'
support_skill_3 = 'f3'
# todo zrobic jakos dynamicznie przypisywanie potionow do hotkei,np zeby potion_rv byl jednoczesnie jako 3 i 4 - o
#  ile sie da
potion_hp = '1'
potion_mp = '2'
potion_rv = '3'
potion_rv2 = '4'

################################
#           MISC        `      #
################################
scale = 1
pa_pause = 0.02
