#!/usr/bin/env python3

###############################################################################
# File Name  : Controller.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import sys
sys.path.append('..')
sys.path.append('/home/mario/EnvironmentController/')
from SupportFiles.DB_Handler import DB_Manager
from SupportFiles.Time_Clock import OS_Clock
import schedule
from time import sleep
from config import Config
from Humidity import Humidity
from Temperature import Temperature
from Heater import Heater
from Humidifier import Humidifier
from Fan import Fan
from Light import Light
import Leds

def Task_Init():
    print("*******************************************************************************")
    global the_humidity
    global the_temperature
    global the_heater
    global the_humidifier
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
    the_humidifier = Humidifier()
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
    
    # Get Configuration Parameters
    the_config.get_config_file()
    fan_override = the_config.FAN_OVERRIDE
    hum_override = the_config.HUM_OVERRIDE
    max_temp_threshold = float(the_config.MAX_TEMP_THRESH)
    min_temp_threshold = float(the_config.MIN_TEMP_THRESH)
    max_humid_threshold = float(the_config.MAX_HUMIDITY_THRESH)
    min_humid_threshold = float(the_config.MIN_HUMIDITY_THRESH)
    
    
    # Get Sensor Readings
    avg_temp = the_temperature.get_average_temperature()
    intake_temp = the_temperature.get_temperature1()
    lower_temp = the_temperature.get_temperature2()
    avg_humidity = the_humidity.get_average_humidity()
    fan_override = the_config.FAN_OVERRIDE
    fan_state = the_fan.Get_State()
    max_humidity = the_humidity.get_max_humidity()
    max_temperature = the_temperature.get_max_temperature()
    
    # Get Time
    current_time = the_time.get_current_time_stamp()
    on_time = the_time.get_time_since_start()
    #fan_alarm = the_time.fan_timer()
    
    # Set Outputs
    if avg_humidity <= min_humid_threshold:
        the_humidifier.Turn_On()
    else:
        the_humidifier.Turn_Off()

    if avg_temp <= min_temp_threshold:
        the_heater.Turn_On()
    else:
        the_heater.Turn_Off()


    # Over rides
    if fan_override == "True":
        the_fan.Turn_On()
    else:
        the_fan.Turn_Off()
        
    # if hum_override == "True":
        # the_humidifier.Turn_On()
    # else:
        # the_humidifier.Turn_Off()
        
    
    # Get Updated States
    heater_state = the_heater.Get_State()
    humidifier_state = the_humidifier.Get_State()
    fan_state = the_fan.Get_State()
    light_state = the_light.Get_State()
    


    # Output System Info
    print("*******************************************************************************")
    print("System Time")
    print("Current Time       :", current_time)
    print("System On Time     :", on_time)
    print("*******************************************************************************")
    print("System Stats")
    print("Average Temp       :", avg_temp)
    print("Average Humidity   :", avg_humidity)
    print("Intake Temp        :", intake_temp)
    print("Lower Temp         :", lower_temp) 
    print("Max Humidity Seen  :", max_humidity)
    print("Max Temp Seen      :", max_temperature)
    #print("Fan Alarm State    :", fan_alarm)
    print("*******************************************************************************")
    print("Config File")
    print("Fan OverRide State :", fan_override)
    print("Hum OverRide State :", hum_override)
    print("Fan Alarm State    :", fan_alarm)
    print("Max Temp Thresh    :", max_temp_threshold)
    print("Min Temp Thresh    :", min_temp_threshold)
    print("Max Humidity Thresh:", max_humid_threshold)
    print("Min Humidity Thresh:", min_humid_threshold)
    print("*******************************************************************************")
    print("Device States")
    print("Max Humidity       :", max_humidity)
    print("Max Temperature    :", max_temperature)
    print("Heater State       :", heater_state)
    print("Humidifier State   :", humidifier_state)
    print("Fan State          :", fan_state)
    print("LED Light State    :", light_state)

    

    if fan_alarm:
        fan_override = "True"

    if avg_temp <= max_temp_threshold:
        the_heater.Turn_On()
    else:
        the_heater.Turn_Off()




    

    

    Leds.toggle_control_led()
    print("*******************************************************************************")


def toggle_air_system():
    print("Set Exhaust on for 3 minutes")




def timer_tracker():
    print("timer tracker")
    

    
schedule.every().minute.at(":20").do(Task_Process_1)
schedule.every().minute.at(":40").do(Task_Process_2)
schedule.every().minute.at(":59").do(Task_Environment_Control)
#schedule.every(1).minutes.do(timer_tracker)
#schedule.every(2).minutes.do(toggle_air_system)

#schedule.every().day.at("12:25").do(job)


Task_Init()

try:
    while True: #run forever
        schedule.run_pending()
        Leds.toggle_1s_led()
        sleep(1)
except:
    print("System Error")
    print("Unexpected error:", sys.exc_info()[0])
finally:
    the_heater.Kill()
    print("bye..bye")
    

