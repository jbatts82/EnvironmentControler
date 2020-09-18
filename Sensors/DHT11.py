###############################################################################
# File Name  : DHT11.py
# Date       : 07/12/2020
# Description: Reads humidity sensor
###############################################################################

#!/bin/bash

import sys
import time
import Adafruit_DHT

class Sensor:
    sensor_index = 0
    def __init__(self, config):
        if config.sensor_cnt > self.sensor_index:
            config.sensor_configs[self.sensor_index]["assigned"] =  True
            self.pin = config.sensor_configs[self.sensor_index]["data_pin"]
            self.name = config.sensor_configs[self.sensor_index]["name"]
            self.sensor_type = config.sensor_configs[self.sensor_index]["sensor_type"]
            self.humidity = 999
            self.temperature_c = 999
            self.temperature_f = 999
            self.previous_c = 999
            self.previous_f = 999
            self.previous_h = 999
            self.sensor_error = False
            Sensor.sensor_index += 1
            self.process_sensor()
            print("Sensor Started")
        else:
            print("Error: All Sensors Used")
        
    def __del__(self): 
        pass
        
    def process_sensor(self):
        print("Processing        :", self.name)
        try:
            self.humidity, self.temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
            self.temperature_f = self.temperature_c * 9/5.0 + 32
        except:
            print("SIGNAL SNA        :",self.name)
            self.temperature_c = self.previous_c
            self.temperature_f = self.previous_f
            self.humidity = self.previous_h
            self.sensor_error = True
        else:
            print("Success Processing:", self.name)
            self.previous_c = self.temperature_c 
            self.previous_f = self.temperature_f 
            self.previous_h = self.humidity
            self.sensor_error = False
        finally:
            pass
    
    def get_error_state(self):
        return self.sensor_error
    
    def get_sensor_name(self):
        return self.name
    
    def get_temp_c(self):
        return self.temperature_c
        
    def get_temp_f(self):
        return self.temperature_f
        
    def get_humidity(self):
        return self.humidity
#end: class Sensor: