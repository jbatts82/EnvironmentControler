###############################################################################
# File Name  : Controller.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

from SupportFiles.Time_Clock import OS_Clock
from Control.Heater import Heater
from Control.Humidifier import Humidifier
from Control.Fan import Fan
from Control.Light import Light
import Control.Leds


import sys
import schedule
from time import sleep

def Initialize_Control(config):
    global the_time, the_heater, the_humidifier, the_fan, the_light, the_config
    the_config = config
    the_time = OS_Clock()
    the_heater = Heater()
    the_humidifier = Humidifier()
    the_fan = Fan()
    the_light = Light()
    print("Control Objects Initialized")

def Task_Process_1():
    print("Task1")


def Task_Process_2():
    print("Task2")

 
   
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

    # Get Sensor Readings
    # avg_humidity
    # intake_temp
    # lower_temp
    # max_humidity
    # max_temperature

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
    # print("Average Temp       :", avg_temp)
    # print("Average Humidity   :", avg_humidity)
    # print("Intake Temp        :", intake_temp)
    # print("Lower Temp         :", lower_temp) 
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

    



    # Set Outputs
    # if avg_humidity <= min_humid_threshold:
    #     the_humidifier.Turn_On()
    # else:
    #     the_humidifier.Turn_Off()

    # if avg_temp <= min_temp_threshold:
    #     the_heater.Turn_On()
    # else:
    #     the_heater.Turn_Off()


    # Over rides

    if fan_override == "True":
        if fan_override_state == "True":
            the_fan.Turn_On()
        else:
            the_fan.Turn_Off()

    
    
    Control.Leds.toggle_control_led()
    print("*******************************************************************************")


def toggle_air_system():
    print("Set Exhaust on for 3 minutes")


def timer_tracker():
    print("timer tracker")
    



#schedule.every(1).minutes.do(timer_tracker)
#schedule.every(2).minutes.do(toggle_air_system)
#schedule.every().day.at("12:25").do(job)

def Run_Tasks():


    schedule.every().minute.at(":00").do(Task_Environment_Control)
    schedule.every().minute.at(":10").do(the_fan.Process_Fan)
    schedule.every().minute.at(":40").do(the_light.Process_Light)
    schedule.every().minute.at(":15").do(Task_Environment_Control)
    schedule.every().minute.at(":30").do(Task_Environment_Control)
    schedule.every().minute.at(":45").do(Task_Environment_Control)

    try:
        while True: #run forever
            schedule.run_pending()
            Control.Leds.toggle_1s_led()
            sleep(1)
    except:
        print("System Error")
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        the_heater.Kill()
        print("bye..bye")
    

