###############################################################################
# Filename    : Fan.py
# Date        : 07/29/2020 
# Description : Controls Exhaust Fan
###############################################################################

import Plug
import Temperature

def Turn_On_Fan():
    Plug.plug1_on()
    
def Turn_Off_Fan():
    Plug.plug1_off()
    
def Get_Fan_State():
    fan_state = Plug.get_plug1_state()
    return fan_state

def Process_Fan():
    temp_f = Temperature.get_temperature_f()
    if temp_f > 80:
        Turn_On_Fan()
    else:
        Turn_Off_Fan()

def Print_Fan_State():
    if Get_Fan_State():
        print("Fan is On")
    else:
        print("Fan is Off")