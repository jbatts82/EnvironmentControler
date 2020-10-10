#!/usr/bin/env python3

###############################################################################
# File Name  : Controller.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import sys
sys.path.append('..')
sys.path.append('/home/mario/EnvironmentController/')


# with open('control_output.txt', 'w') as f:
    # sys.stdout = f # Change the standard output to the file we created.


from SupportFiles.DB_Handler import DB_Manager
from SupportFiles.Time_Clock import OS_Clock
import schedule
from time import sleep
from config import Config
from Humidity import Humidity
from Temperature import Temperature
from Heater import Heater
from Fan import Fan
from Light import Light
import Leds


def Task_Init():
    print("*******************************************************************************")
    global the_humidity
    global the_temperature
    global the_heater
    global the_fan
    global the_config
    global the_time
    global the_light
    the_time = OS_Clock()
    the_config = Config()
    the_humidity = Humidity()
    the_humidity.process_humidity()
    the_temperature = Temperature()
    the_temperature.process_temperature()
    the_heater = Heater()
    the_fan = Fan()
    the_light = Light()
    the_time = OS_Clock()
    print("Initialization     : Complete")

def Task_Process_1():
    the_humidity.process_humidity()
    the_fan.Process_Fan()

def Task_Process_2():
    the_temperature.process_temperature()
    the_light.Process_Light()
 
   
def Task_Environment_Control():
    print("*******************************************************************************")
    print("Processing         : Environmental Controls")
    the_config.get_config_file()
    avg_temp = the_temperature.get_average_temperature()
    avg_humidity = the_humidity.get_average_humidity()
    temp_threshold = float(the_config.MAX_TEMP_THRESH)
    humid_threshold = float(the_config.MAX_HUMIDITY_THRESH)
    fan_override = the_config.FAN_OVERRIDE
    fan_state = the_fan.Get_State()
    max_humidity = the_humidity.get_max_humidity()
    max_temperature = the_temperature.get_max_temperature()
    current_time = the_time.get_current_time_stamp()
    on_time = the_time.get_time_since_start()
    light_state = the_light.Get_State()
    heater_state = the_heater.Get_State()
    fan_alarm = the_time.fan_timer()
    

    print("Current Time       :", current_time)
    print("System On Time     :", on_time)
    print("Average Temp       :", avg_temp)
    print("Average Humidity   :", avg_humidity)
    print("Fan OverRide State :", fan_override)
    print("Fan Alarm State    :", fan_alarm)
    print("Max Temp Thresh    :", temp_threshold)
    print("Max Humidity Thresh:", humid_threshold)
    print("Max Humidity       :", max_humidity)
    print("Max Temperature    :", max_temperature)
    print("Heater State       :", heater_state)
    print("Fan State          :", fan_state)
    print("LED Light State    :", light_state)


    if fan_alarm:
        fan_override = "True"


    if avg_temp <= 70:
        the_heater.Turn_On()
    else:
        the_heater.Turn_Off()



    # if fan_override == "True":
        # the_fan.Turn_On()
    # else:
        # if avg_temp < temp_threshold:
            # the_fan.Turn_Off()
            # if avg_humidity > 59:
                # the_heater.Turn_On()
            # else:
                # the_heater.Turn_Off()
        # else:
            # the_heater.Turn_Off()
            # the_fan.Turn_On()
    
    


    Leds.toggle_control_led()
    print("*******************************************************************************")


def toggle_air_system():
    pass


def system_info_dump():
    pass
    
schedule.every().minute.at(":20").do(Task_Process_1)
schedule.every().minute.at(":40").do(Task_Process_2)
schedule.every().minute.at(":59").do(Task_Environment_Control)
schedule.every(1).minutes.do(toggle_air_system)


Task_Init()

try:
    while True: #run forever
        schedule.run_pending()
        sleep(1)
except:
    print("System Error")
    print("Unexpected error:", sys.exc_info()[0])
finally:
    the_heater.Kill()
    print("bye..bye")
    

