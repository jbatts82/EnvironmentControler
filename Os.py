###############################################################################
# File Name  : Os.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import schedule
import time
import Songle
from Time_Clock import get_time
import Plug #import and init first
import DHT11
from DHT11 import Sensor
from Fan import Fan
from Fan import get_fan_configs
from Heater import Heater
from Light import Light


def system_status():
    print("*******************************************************************************")
    print("Current Time      :", get_time())
    print("Sensor            :", sensor1.get_sensor_name())
    print("Temp F            :", sensor1.get_temp_f())
    print("Humidity          :", sensor1.get_humidity())
    print("Sensor            :", sensor2.get_sensor_name())
    print("Temp F            :", sensor2.get_temp_f())
    print("Humidity          :", sensor2.get_humidity())
    print("Fan Name          :", fan1.Get_Name())
    print("Fan State         :", fan1.Get_State())
    print("Heater Name       :", heater.Get_Name())
    print("Heater State      :", heater.Get_State())
    print("Light Name        :", light.Get_Name())
    print("Light State       :", light.Get_State())
    print("*******************************************************************************")

def Environment_Controller():
    print("Processing        : Environmental Variables")
    avg_humidity = (sensor1.get_humidity() + sensor2.get_humidity()) / 2
    print("Avg Humidity      :", avg_humidity)
    avg_temp = (sensor1.get_temp_f() + sensor2.get_temp_f()) / 2
    print("Avg Temp F        :", avg_temp)
    
    if avg_temp < 83:
        fan1.Turn_Off()
        if avg_humidity > 59:
            heater.Turn_On()
        else:
            heater.Turn_Off()
    else:
        heater.Turn_Off()
        fan1.Turn_On()
    
    
def Task_60s():
    system_status()
    Environment_Controller()
    
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

#init light
light = Light()

#schedule routines
schedule.every(60).seconds.do(Task_60s)
schedule.every().minute.at(":00").do(sensor1.process_sensor)
schedule.every().minute.at(":15").do(fan1.Process_Fan)
schedule.every().minute.at(":30").do(sensor2.process_sensor)
schedule.every().minute.at(":45").do(light.Process_Light)

try:
    while True: #run forever
        schedule.run_pending()
        time.sleep(1)
except:
    print("System Error")
finally:
    heater.Kill()
    print("bye..bye")
    
    


