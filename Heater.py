###############################################################################
# File Name  : Heater.py
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
heater_on_time = 0
heater_off_time = 0

def init_heater():
    heater_off()

def process_heater():
    global heater_cooldown_period, process_period, needs_cool_down, heater_on_time, heater_off_time
    print("Process_heater")
    print("Heater On Time: ", heater_on_time, " Minutes")
    print("Heater Off Time: ", heater_off_time, " Minutes")
    humidity = get_humidity()
    print(humidity)
    temp_f = get_temperature_f()
    print(temp_f)
    
    if(heater_state):
        heater_on_time +=1
    else:
        heater_off_time +=1
   
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
        
def heater_on():
    global heater_state
    heater_state = True
    relay1_on()
    
def heater_off():
    global heater_state
    heater_state = False
    relay1_off()
    
    