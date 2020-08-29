###############################################################################
# Filename    : SensorApp.py
# Date        : 08/22/2020 
# Description : This app runs continuously collecting sensor data and writing 
#               to a database. 
###############################################################################

#!/usr/bin/python

import os
import sys
sys.path.append(os.path.abspath("/home/mario/EnvironmentController/"))
sys.path.append(os.path.abspath("/home/mario/EnvironmentController/SupportFiles"))
from DB_Handler import DB_Manager
import DHT11
import Max6675K
import asyncio
from datetime import datetime
import time as t
from config import Config

async def init_sensors():
    global sensor1_db, sensor2_db
    config = Config()
    await init_sensor_1(config)
    await init_sensor_2(config)
    sensor1_db = DB_Manager(config, 0)
    sensor2_db = DB_Manager(config, 1)
    
async def init_sensor_1(config):
    global sensor1
    sensor1 = DHT11.Sensor(config)

async def init_sensor_2(config):
    global sensor2
    sensor2 = DHT11.Sensor(config)

async def process_sensor_1():
    global sensor_1
    sensor1.process_sensor()
    error_state = sensor1.get_error_state()
    time = datetime.now()
    temp = sensor1.get_temp_f()
    humidity = sensor1.get_humidity()
    sensor1_db.write_sensor_data(time, temp, humidity)
    t.sleep(30)
    
async def process_sensor_2():
    global sensor_2
    sensor2.process_sensor()
    error_state = sensor2.get_error_state()
    time = datetime.now()
    temp = sensor2.get_temp_f()
    humidity = sensor2.get_humidity()
    sensor2_db.write_sensor_data(time, temp, humidity)
    t.sleep(30)

async def main_loop():
    await init_sensors()
    while True:
        await process_sensor_1()
        print("Sensor            : " ,sensor1.get_sensor_name())
        print("Error             : " ,str(sensor1.get_error_state()))
        print("tempc             : " ,sensor1.get_temp_c())
        print("tempf             : " ,sensor1.get_temp_f())
        print("humity            : " ,sensor1.get_humidity())
        await process_sensor_2()
        print("Sensor            : " ,sensor2.get_sensor_name())
        print("Error             : " ,str(sensor2.get_error_state()))
        print("tempc             : " ,sensor2.get_temp_c())
        print("tempf             : " ,sensor2.get_temp_f())
        print("humity            : " ,sensor2.get_humidity())

if __name__ == '__main__':
    print("Starting          :  ", __file__)
    asyncio.run(main_loop())
    
    
    
    
    

    
    
