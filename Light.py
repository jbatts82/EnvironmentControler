###############################################################################
# Filename    : Light.py
# Date        : 07/27/2020 
# Description : Controls TPLink Smart Plugs
###############################################################################

import Plug

def Turn_On_Light():
    Plug.plug2_on()
    
def Turn_Off_Light():
    Plug.plug2_off()
    
def Get_Light_State():
    light_state = Plug.get_plug2_state()
    return light_state

def Print_Light_State():
    if Get_Light_State():
        print("Light is On")
    else:
        print("Light is Off")