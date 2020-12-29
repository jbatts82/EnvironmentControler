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
    await init_sensor_1(config)
    await init_sensor_2(config)
    await init_sensor_3(config)
    await init_sensor_4(config)
    
async def init_sensor_1(config):
    global sensor1
    sensor1 = DHT11(config)

async def init_sensor_2(config):
    global sensor2
    sensor2 = DHT11(config)

async def init_sensor_3(config):
    global sensor3
    sensor3 = DHT11(config)

async def init_sensor_4(config):
    global sensor4
    sensor4 = DHT11(config)

async def process_sensor_1():
    global sensor1
    sensor1.process_sensor()
    sensor_data = sensor1.get_current_data()
    database = Ds_App(config)
    is_good = database.verify_sensor_data(sensor_data)
    if is_good:
        database.write_sensor_data(sensor_data)
    
async def process_sensor_2():
    global sensor2
    sensor2.process_sensor()
    sensor_data = sensor2.get_current_data()
    database = Ds_App(config)
    is_good = database.verify_sensor_data(sensor_data)
    if is_good:
        database.write_sensor_data(sensor_data)

async def process_sensor_3():
    global sensor3
    sensor3.process_sensor()
    sensor_data = sensor3.get_current_data()
    database = Ds_App(config)
    is_good = database.verify_sensor_data(sensor_data)
    if is_good:
        database.write_sensor_data(sensor_data)

async def process_sensor_4():
    global sensor4
    sensor4.process_sensor()
    sensor_data = sensor4.get_current_data()
    database = Ds_App(config)
    is_good = database.verify_sensor_data(sensor_data)
    if is_good:
        database.write_sensor_data(sensor_data)

async def main_loop():
    await init_sensors()
    while True:
        await process_sensor_1()
        t.sleep(15)
        await process_sensor_2()
        t.sleep(15)
        await process_sensor_3()
        t.sleep(15)
        await process_sensor_4()
        t.sleep(15)

# if __name__ == '__main__':
#     print("Starting          :  ", __file__)
#     asyncio.run(main_loop())
    
    
    
    
    

    
    
