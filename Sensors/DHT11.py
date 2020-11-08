###############################################################################
# File Name  : DHT11.py
# Date       : 07/12/2020
# Description: Reads humidity sensor
###############################################################################

import sys
import time
from datetime import datetime
import Adafruit_DHT
from SupportFiles.Shared import DHT11_Data

class DHT11:
    sensor_index = 0
    def __init__(self, config):
        if config.sensor_cnt > self.sensor_index:
            config.sensor_configs[self.sensor_index]["assigned"] =  True
            self.pin = config.sensor_configs[self.sensor_index]["data_pin"]
            self.name = config.sensor_configs[self.sensor_index]["name"]
            self.sensor_type = config.sensor_configs[self.sensor_index]["sensor_type"]
            self.current_data = DHT11_Data()
            self.previous_data = DHT11_Data() #ie:previous good data
            self.current_data.name = config.sensor_configs[self.sensor_index]["name"]
            DHT11.sensor_index += 1
            self.process_sensor()
            print("Sensor Started")
        else:
            print("Error: All Sensors Used or some other error")
        
    def __del__(self): 
        pass
        
    def process_sensor(self):
        print("Processing        :", self.name)
        try:
            humidity, temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
            temperature_f = temperature_c * 9/5.0 + 32
            print("Sensor         : {}".format(self.name))
            print("The Temperature: {}".format(str(temperature_f)))
            print("The Humidity   : {}".format(str(humidity)))

            self.current_data.time_data = datetime.now()
            self.current_data.temperature_f = temperature_f
            self.current_data.humidity = humidity
            self.current_data.error_state = False
        except:
            print("!!!SIGNAL SNA!!!  :",self.name)
            self.current_data = self.previous_data
        else:
            print("Success Processing:", self.name)
            print("Time              :", self.current_data.time_data)
            print("Temp              :", self.current_data.temperature_f)
            print("Humidity          :", self.current_data.humidity)
            print("Time              :", self.current_data.error_state)
            self.previous_data = self.current_data
        finally:
            pass
    
    def get_current_data(self):
        return self.current_data

#end: class Sensor: