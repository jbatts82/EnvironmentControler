###############################################################################
# File Name  : Os.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import schedule
import time

from Time_Clock import get_time

import Plug #import and init first

import DHT11
from DHT11 import Sensor

from Fan import Fan
from Fan import get_fan_configs

from Heater import Heater


def Task_60s():
    print("*******************************************************************************")
    print("Current Time      : ", get_time())
    print("Sensor            : ", sensor1.get_sensor_name())
    print("Temp              : ", sensor1.temperature_f)
    print("Humidity          : ", sensor1.humidity)
    print("Sensor            : ", sensor2.get_sensor_name())
    print("Temp              : ", sensor2.temperature_f)
    print("Humidity          : ", sensor2.humidity)
    print("Fan Name          : ", fan1.Get_Name())
    print("Fan State         : ", fan1.Get_State())
    print("Heater Name       : ", heater.Get_Name())
    print("Heater State      : ", heater.Get_State())
    print("*******************************************************************************")


#init wireless plugs
Plug.init_plug()

#init sensors
config_array = DHT11.get_dht11_configs()
sensor1_config = config_array[0]
sensor2_config = config_array[1]
sensor1 = Sensor(sensor1_config)
sensor2 = Sensor(sensor2_config)

#init fans
fan_configs = get_fan_configs()
fan1 = Fan(fan_configs[0])

#init heater
heater = Heater()

#schedule routines
schedule.every(60).seconds.do(Task_60s)
schedule.every().minute.at(":00").do(sensor1.process_sensor)
schedule.every().minute.at(":15").do(fan1.Process_Fan)
schedule.every().minute.at(":30").do(sensor2.process_sensor)


try:
    while True: #run forever
        schedule.run_pending()
        time.sleep(1)
except:
    print("System Error")
finally:
    heater.Turn_Off()
    print("bye..bye")
    
    


