###############################################################################
# File Name  : Controller.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

from SupportFiles.Time_Clock import OS_Clock, Device_Clock
from Control.Heater import Heater
from Control.Humidifier import Humidifier
from Control.Fan import Fan
from Control.Light import Light
import Control.Leds
from Data_Stats.DataApp import Ds_App
import numpy as np
import pandas as pd 

import sys
import schedule
from time import sleep

from datetime import datetime

def Initialize_Control(config):
    print("Processing         : Initializing Control Objects")
    global the_time, the_heater, the_humidifier, the_fan, the_light, the_config, data_app
    the_config = config
    the_time = OS_Clock()
    the_heater = Heater()
    the_humidifier = Humidifier()
    the_fan = Fan()
    the_light = Light()
    data_app = Ds_App(config)
    print("Processing         : Control Objects Initialized")

def Task_Environment_Control():
    print("*******************************************************************************")
    print("Processing         : Environmental Controls")
    
    # Get Configuration Parameters
    the_config.get_config_file()
    fan_override = the_config.FAN_OVERRIDE
    fan_override_state = the_config.FAN_OVER_STATE
    hum_override = the_config.HUM_OVERRIDE
    max_temp_threshold = float(the_config.MAX_TEMP_THRESH)
    min_temp_threshold = float(the_config.MIN_TEMP_THRESH)
    max_humid_threshold = float(the_config.MAX_HUMIDITY_THRESH)
    min_humid_threshold = float(the_config.MIN_HUMIDITY_THRESH)
    
    # Get Time
    current_time = the_time.get_current_time_stamp()
    on_time = the_time.get_time_since_start()

    temp_setting = get_temp_setting()
    min_temp_threshold = temp_setting['temp']

    # Get Sensor Readings
    avg_temp = data_app.get_last_avg_room_temp()
    avg_humidity = data_app.get_last_avg_room_humid()
    intake_temp = data_app.get_last_temp("upper_sensor")
    lower_temp = data_app.get_last_temp("lower_sensor")

    # Set Outputs
    fan_state = the_fan.Get_State()

    if fan_state == False:
        if avg_humidity <= min_humid_threshold:
            the_humidifier.Turn_On()
        else:
            the_humidifier.Turn_Off()

        if avg_temp <= min_temp_threshold:
            the_heater.Turn_On()
        else:
            the_heater.Turn_Off()
    else:
        the_humidifier.Turn_Off()
        the_heater.Turn_Off()


    # Over-rides
    if fan_override == "True":
        if fan_override_state == "True":
            the_fan.Turn_On()
        else:
            the_fan.Turn_Off()


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
    # print("Max Humidity Seen  :", max_humidity)
    # print("Max Temp Seen      :", max_temperature)
    print("*******************************************************************************")
    print("Config File")
    print("Fan OverRide State :", fan_override)
    print("Hum OverRide State :", hum_override)
    print("Max Temp Thresh    :", max_temp_threshold)
    print("Min Temp Thresh    :", min_temp_threshold)
    print("Max Humidity Thresh:", max_humid_threshold)
    print("Min Humidity Thresh:", min_humid_threshold)
    print("*******************************************************************************")
    print("Device States")
    print("Heater State       :", heater_state)
    print("Humidifier State   :", humidifier_state)
    print("Fan State          :", fan_state)
    print("LED Light State    :", light_state)


    data_app.write_control_data(current_time, heater_state, humidifier_state, fan_state, light_state)

    print("Processing         : Environmental Controls Processed")
    print("*******************************************************************************")

def toggle_air_system():
    print("Processing         : Set Exhaust on for 7 minutes")
    the_fan.Set_Fan_Timer(7)

def get_temp_setting():
    time_table = the_config.time_table
    date_time_now = datetime.now()
    hour_now = date_time_now.hour
    
    for hour in time_table[::-1]:
        if hour_now >= hour["hour"]:
            break

    temp_setting = hour

    return temp_setting



def Run_Tasks():
    schedule.every().minute.at(":00").do(Task_Environment_Control)
    schedule.every().minute.at(":15").do(Task_Environment_Control)
    schedule.every().minute.at(":30").do(Task_Environment_Control)
    schedule.every().minute.at(":45").do(Task_Environment_Control)

    schedule.every().minute.at(":10").do(the_fan.Process_Fan)
    schedule.every().minute.at(":40").do(the_light.Process_Light)

    schedule.every().hour.at(":23").do(toggle_air_system)


    try:
        while True: #run forever
            schedule.run_pending()
            sleep(1)
    except:
        print("System Error")
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        the_heater.Kill()
        print("bye..bye")
    

