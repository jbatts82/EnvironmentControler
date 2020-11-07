###############################################################################
# Filename    : SensorApp.py
# Date        : 08/22/2020 
# Description : This app runs continuously collecting sensor data and writing 
#               to a database. 
###############################################################################
import asyncio
from datetime import datetime
from Sensors.DHT11 import DHT11
from Data_Stats.DataApp import Ds_App
from config import Config
from Control import Leds
import time as t

config = Config()

async def init_sensors():
    print("Init Sensors")
    await init_sensor_1(config)
    await init_sensor_2(config)
    
async def init_sensor_1(config):
    global sensor1
    sensor1 = DHT11(config)

async def init_sensor_2(config):
    global sensor2
    sensor2 = DHT11(config)

async def process_sensor_1():
    global sensor1
    # read sensor
    sensor1.process_sensor()
    # get new data
    sensor_data = sensor1.get_current_data()
    # write to database
    database = Ds_App(config)
    database.write_sensor_data(sensor_data)
    
async def process_sensor_2():
    global sensor2
    sensor2.process_sensor()
    # get new data
    sensor_data = sensor2.get_current_data()
    # write to database
    database = Ds_App(config)
    database.write_sensor_data(sensor_data)
    
async def process_status_led():
    Leds.toggle_sensor_led()
    t.sleep(1)

async def main_loop():
    await init_sensors()
    while True:
        await process_status_led()
        await process_sensor_1()
        t.sleep(30)
        await process_status_led()
        await process_sensor_2()
        t.sleep(30)

# if __name__ == '__main__':
#     print("Starting          :  ", __file__)
#     asyncio.run(main_loop())
    
    
    
    
    

    
    
