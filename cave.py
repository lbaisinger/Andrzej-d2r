import datetime
import pyautogui
import PIL.Image
from utils import Backpack
from time import sleep
from config_picker import *



class Cave:

    def __init__(self):
        #self.current_waypoint =
        pass

    def use_rope(self):
        # works ok
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.press(config.hotkey_rope)
        sleep(0.1)
        pyautogui.click(config.character)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_rope', looptime)
        return True

    def use_shovel(self):
        # works ok
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.press(config.hotkey_shovel)
        sleep(0.1)
        # pyautogui.moveTo(config.character)
        pyautogui.click(config.character)
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_shovel', looptime)
        return True

    def use_ladder(self):
        timestamp = datetime.datetime.now()
        sleep(0.1)
        pyautogui.click(config.character, button='right')
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME use_ladder', looptime)
        return True

    def is_has_cap(self):
        # todo fix it to be sure that it can always read cap
        timestamp = datetime.datetime.now()
        bp = Backpack()
        try:
            cap = bp.get_avial_cap()
            if int(cap) > config.min_cap_to_cont_hunt:
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_has_cap T', looptime)
                return True
            else:
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_has_cap F', looptime)
                return False
        except ValueError:
            # todo fix it to be sure that it can always read cap
            print('WARNING - couldnt read cap to int')
            return True

    def is_ready_to_go_to_dp(self):
        # todo fix it to be sure that it can always read cap
        timestamp = datetime.datetime.now()
        if self.is_has_cap():
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp F', looptime)
            return False
        elif not(self.is_has_cap()):
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_ready_to_go_dp T', looptime)
            return True

    def is_on_wp(self, wp, wp_val):
        timestamp = datetime.datetime.now()
        # standing on wp ?
        img = PIL.Image.open("src/wp/" + str(wp) + ".png")
        img_size = img.size
        wp_img = img.resize((img_size[0] * config.scale,
                             img_size[1] * config.scale))
        xyz = pyautogui.locateCenterOnScreen(wp_img,
                                             region=config.minimap, #todo mozna by go mniejszym zrobic, ten region do jakiegos samego srodka minimapy
                                             confidence=.8)
        if xyz is not None:
            # debug
            print(xyz)
            # to wide
            #if not(wp_center[0] -1 <= xyz[0] <= wp_center[0] +1) and not(wp_center[1] <= xyz[1] <= wp_center[1] +1):
            if xyz != config.wp_center and xyz != config.wp_center2 and xyz != config.wp_center3:
                print('did not yet reach wp', wp, 'coords:', str(xyz))
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_on_wp F', looptime)
                return False
            else:
                print('>>>> reached wp', wp, 'coords:', str(xyz))
                if wp_val[wp-1] == 'special':
                    print('wp: lopata & lina')
                    self.use_rope()
                    sleep(0.2)
                    self.use_shovel()
                else:
                    print('wp pospolity')
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME is_on_wp T', looptime)
                return True
        else:
            print('couldnt find wp', wp)
            # #try to move minimap
            # #add timestamp
            return False

    def do_go_wp(self, wp):
        # szuka wp na mapie i go naciska
        # dziala ok
        timestamp = datetime.datetime.now()
        img = PIL.Image.open("src/wp/" + str(wp) + ".png")
        img_size = img.size
        wp_img = img.resize((img_size[0] * config.scale,
                             img_size[1] * config.scale))
        wp_coord = pyautogui.locateCenterOnScreen(wp_img,
                                                  region=config.minimap,
                                                  confidence=.75)
        if wp_coord is not None:
            # print('going wp', str(wp), wp_coord[0], wp_coord[1])
            pyautogui.click(wp_coord[0], wp_coord[1])
            pyautogui.moveTo(config.default)  # Added moveto default (otherwise sometime mouse stays on wp and cannot detect)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME GO_WP OK', looptime)
            return True
        else:
            print('couldnt find wp', wp)
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME GP_WP NOK', looptime)

    def is_wp_fancy(self, wp, specials: {}):
        # todo verify if rly works
        timestamp = datetime.datetime.now()
        # sprawdz czy podany wp specjalny
        if specials[wp] in ['rope','shovel']:
            # to bedzie specjalyn wp
            print('am special')
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_wp_fancy T', looptime)
            return True
        else:
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME is_wp_fancy F', looptime)
            return False

    def do_go_wp_plus(self, wp, specials:{}):
        #todo timestamps
        timestamp = datetime.datetime.now()
        if specials[wp] == 'rope':
            self.use_rope()
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus rope', looptime)
            return True
        if specials[wp] == 'shovel':
            self.use_shovel()
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus shovel', looptime)
            return True
        if specials[wp] == 'LAST':
            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print('TIME do_go_wp_plus LAST', looptime)
            return True
#        if specials[wp] == 'lvl_changing_wp':
#            # see if next in horizon
#            nextwp = wp + 1
#            print('debug', nextwp)
#            print('debug', specials[wp])
#            nextwp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(nextwp) + ".png",
#                                                          region=config.minimap,
#                                                          confidence=.8)
#            while nextwp_coord is None:
#                nextwp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(nextwp) + ".png",
#                                                              region=config.minimap,
#                                                              confidence=.8)
#                self.do_go_wp(wp)
#                sleep(.5)
#                print('looking for next wp')
#
#            # jesli jest juz znajdzie
#            timestamp2 = datetime.datetime.now()
#            looptime = timestamp2 - timestamp
#            print('TIME do_go_wp_plus lvl_changer', looptime)
#            return True
#        if specials[wp] == 'dosmthfancy':
#            timestamp2 = datetime.datetime.now()
#            looptime = timestamp2 - timestamp
#            print('TIME do_go_wp_plus dosmthfancy', looptime)
#            return True
#        if specials[wp] is None:
#            timestamp2 = datetime.datetime.now()
#            looptime = timestamp2 - timestamp
#            print('TIME do_go_wp_plus None', looptime)
#            return True
        # if did not catch in any of ifs above
        return False
    
    def is_wp_in_range(self, wp):
        wp_cords = pyautogui.locateCenterOnScreen("src/wp/" + str(wp) + ".png", region=config.minimap, confidence=.8)
        if wp_cords is not None:
            return True
        else:
            return False


    def go_somewhere(self, wp, specials: {}):
        nextwp = wp+1

        # sprawdz czy nie wszedl po shcodach/wszedl w dziure
        if specials[wp] == 'lvl_changing_wp':
            print('to level changer')
            if self.is_wp_in_range(nextwp):
                return nextwp

        # sprawdz czy stoje na wp      
        if self.is_on_wp(wp=wp, wp_val=list(specials.values())):
            # sprawdz czy to nie koniec
            if specials[wp] == 'LAST':
                print('done! im there')
                return True

            # jak fancy to zrob cos 
            if self.is_wp_fancy(wp=wp, specials=specials):
                self.do_go_wp_plus(wp, specials)
            # i dawaj na next
            return nextwp    
        
        # w kazdym innym wypadku
        self.do_go_wp(wp)
        return wp



# new one to go dp/bank in one
    def go_somwhere(self, currentwp, specials: {}):
        # todo need some work
        #print(currentwp)
        #print(specials[currentwp])
        timestamp = datetime.datetime.now()
        # idz do wp
        self.do_go_wp(currentwp)
        # sprawdz czy doszedles do wp
        if self.is_on_wp(wp=currentwp, wp_val=list(specials.values())):
            print('jestem na wp!!')
            # jest to ostatni wp
            if str(specials[currentwp]) == "LAST":
                # its done to ostatni
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_somwhere LAST', looptime)
                return True
            # jesli nie jest ostatni
            # czy stoisz na fancy wp
            if self.is_wp_fancy(wp=currentwp, specials=specials):
                # jesli tak to zrob fancy rzeczy
                if self.do_go_wp_plus(wp=currentwp, specials=specials):
                    # dawaj na nast wp
                    nextwp = currentwp+1
                    print(nextwp)
                    return nextwp
                timestamp2 = datetime.datetime.now()
                looptime = timestamp2 - timestamp
                print('TIME go_somwhere do_go_wp_plus', looptime)
                return currentwp
            ## if not caught anything else
            print('face the thing that should not be')
            print('currentwp', currentwp)
            nextwp = currentwp+1
            print('nextwp', nextwp)
            return nextwp
        elif not self.is_on_wp(wp=currentwp, wp_val=list(specials.values())):
            # sprawdz czy to nie fancy lvl chaning wp
            if specials[currentwp] == 'lvl_changing_wp':
                self.do_go_wp_plus(wp=currentwp, specials=specials)
                nextwp = currentwp+1
                return nextwp

            timestamp2 = datetime.datetime.now()
            looptime = timestamp2 - timestamp
            print(self.is_on_wp(wp=currentwp, wp_val=list(specials.values())))
            print(currentwp)
            print('TIME go_somwhere not standing on wp', looptime)
            return currentwp

        # #jesli nie ostatni
#        if not specials[currentwp] == 'LAST':
#            # todo przeniesc to gdzies na pewno nie tu
#            # sprawdz czy nast na horyzoncie
#            nextwp = currentwp+1
#            print('debug', nextwp)
#            print('debug', specials[currentwp])
#            nextwp_coord = pyautogui.locateCenterOnScreen("src/wp/" + str(nextwp) + ".png",
#                                                          region=minimap,
#                                                          confidence=.8)
#            # jesli jest
#            if nextwp_coord is not None:
#                # jest nast na horyzncie, znaczy sie dotarlismy
#                # zwroc nastepny
#                timestamp2 = datetime.datetime.now()
#                looptime = timestamp2 - timestamp
#                print('TIME go_somwhere next_on_horizon', looptime)
#                return nextwp
        # w inny wypadku
        timestamp2 = datetime.datetime.now()
        looptime = timestamp2 - timestamp
        print('TIME go_somwhere False', looptime)
        return currentwp



