###############################################################################
# File Name  : Os.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import schedule
import time
import Songle
import Time_Clock
import Plug #import and init first
import Csv_Handler as csv_handle
from DHT11 import Sensor, get_dht11_configs
from Fan import Fan
from Fan import get_fan_configs
from Heater import Heater
from Light import Light
from Csv_Handler import CSV_Tool
import Humidity
import Temperature


def system_status():
    print("*******************************************************************************")
    print("Date              :", Time_Clock.date_now())
    print("Current Time      :", Time_Clock.time_now())
    #print("Delta Time        :", Time_Clock.get_system_start_delta())
    print("Sensor            :", sensor1.get_sensor_name())
    print("Temp F            :", sensor1.get_temp_f())
    print("Humidity          :", sensor1.get_humidity())
    
    print("Sensor            :", sensor2.get_sensor_name())
    print("Temp F            :", sensor2.get_temp_f())
    print("Humidity          :", sensor2.get_humidity())
    
    print("Avg Temperature   :", the_temperature.get_average_temperature())
    print("Max Temperature   :", the_temperature.get_max_temperature())
    print("Min Temperature   :", the_temperature.get_min_temperature())

    print("Avg Humidity      :", the_humidity.get_average_humidity())
    print("Max Humidity      :", the_humidity.get_max_humidity())
    print("Min Humidity      :", the_humidity.get_min_humidity())
    
    print("Fan Name          :", fan1.Get_Name())
    print("Fan State         :", fan1.Get_State())
    
    print("Heater Name       :", heater.Get_Name())
    print("Heater State      :", heater.Get_State())
    
    print("Light Name        :", light.Get_Name())
    print("Light State       :", light.Get_State())
    print("*******************************************************************************")

def Environment_Controller():
    print("Processing        : Environmental Controls")
    
    avg_temp = the_temperature.get_average_temperature()
    avg_humidity = the_humidity.get_average_humidity()
    
    if avg_temp < 82:
        fan1.Turn_Off()
        if avg_humidity > 59:
            heater.Turn_On()
        else:
            heater.Turn_Off()
    else:
        heater.Turn_Off()
        fan1.Turn_On()



def Task_60s():
    the_humidity.process_humidity()
    the_temperature.process_temperature()
    system_status()
    Environment_Controller()

   
#init wireless plugs
Plug.init_plug()

#init sensors
config_array = get_dht11_configs()
sensor1_config = config_array[0]
sensor2_config = config_array[1]
sensor1 = Sensor(sensor1_config)
sensor2 = Sensor(sensor2_config)

#init humidity data
the_humidity = Humidity.Humidity(sensor1, sensor2)

#init temperature data
the_temperature = Temperature.Temperature(sensor1, sensor2)

#init fans
fan_configs = get_fan_configs()
fan1 = Fan(fan_configs[0])

#init heater
heater = Heater()

#init light
light = Light()

#schedule routines
schedule.every(60).seconds.do(Task_60s)
schedule.every().minute.at(":00").do(sensor1.process_sensor)
schedule.every().minute.at(":15").do(fan1.Process_Fan)
schedule.every().minute.at(":30").do(sensor2.process_sensor)
schedule.every().minute.at(":45").do(light.Process_Light)

Time_Clock.system_start_stamp()


try:
    while True: #run forever
        schedule.run_pending()
        time.sleep(1)
except:
    print("System Error")
finally:
    heater.Kill()
    print("bye..bye")
    
    


