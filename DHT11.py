###############################################################################
# File Name  : DHT11.py
# Date       : 07/12/2020
# Description: Reads humidity sensor
###############################################################################

#!/usr/bin/python

import sys
import Adafruit_DHT

sensor = 11
pin_1 = 17
pin_2 = 26

def process_sensor_1():
    global humidity_1, temperature_c_1, temperature_f_1
    humidity_1, temperature_c_1 = Adafruit_DHT.read_retry(sensor, pin_1)
    temperature_f_1 = temperature_c_1 * 9/5.0 + 32
    
def process_sensor_2():
    global humidity_2, temperature_c_2, temperature_f_2
    humidity_2, temperature_c_2 = Adafruit_DHT.read_retry(sensor, pin_2)
    temperature_f_2 = temperature_c_2 * 9/5.0 + 32

def get_humidity_1():
    global humidity_1
    return humidity_1
    
def get_temp_1():
    global temperature_f_1
    return temperature_f_1

def get_temp_2():
    global temperature_f_2
    return temperature_f_2
    
def get_humidity_2():
    global humidity_2
    return humidity_2