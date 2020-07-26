###############################################################################
# File Name  : Heater.py
# Author     : John
# Date       : 07/12/2020
# Description: Heater Controls
###############################################################################

from Humidity import get_humidity
from Temperature import get_temperature_f
from Songle import relay1_on, relay1_off

heater_cooldown_period = 10 #minutes
process_period = 1 #minute
needs_cool_down = False
heater_state = False

def init_heater():
    heater_off()

def process_heater():
    global heater_cooldown_period, process_period, needs_cool_down
    print("Process_heater")
    humidity = get_humidity()
    print(humidity)
    temp_f = get_temperature_f()
    print(temp_f)
    if(temp_f < 83):
        if(humidity > 60):
            heater_on()
            print("Heater On")
        else:
            heater_off()
            print("Heater Off")
    else:
        heater_off()
        print("Heater Off")

def check_if_cool_down_needed(new_heater_state):
    global heater_state
    if heater_state != new_heater_state
        if heater_state == True
            needs_cool_down = True
        
def heater_on():
    global heater_state
    heater_state = True
    relay1_on()
    
def heater_off():
    global heater_state
    heater_state = False
    relay1_off()
    
    