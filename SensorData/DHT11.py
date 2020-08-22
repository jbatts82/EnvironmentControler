###############################################################################
# File Name  : DHT11.py
# Date       : 07/12/2020
# Description: Reads humidity sensor
###############################################################################

import sys
import time
import Adafruit_DHT

sensor1_config = {"name" : "Upper Sensor", "data_pin":17}
sensor2_config = {"name" : "Lower Sensor", "data_pin":26}

dht11_sensor_array = {}
dht11_sensor_array[0] = sensor1_config
dht11_sensor_array[1] = sensor2_config

class Sensor:
    def __init__(self, config):
        self.sensor_type = 11
        self.pin = config["data_pin"]
        self.name = config["name"]
        self.humidity = None
        self.temperature_c = None
        self.temperature_f = None
        self.previous_c = None
        self.previous_f = None
        self.previous_h = None
        self.process_sensor()
        
    def process_sensor(self):
        print("Processing        :", self.name)
        try:
            self.humidity, self.temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
            self.temperature_f = self.temperature_c * 9/5.0 + 32
        except:
            print("SIGNAL SNA        :",self.name)
            self.temperature_c = None
            self.temperature_f = None
            self.humidity = None
        else:
            print("Success Processing:", self.name)
            self.previous_c = self.temperature_c 
            self.previous_f = self.temperature_f 
            self.previous_h = self.humidity
        finally:
            pass
    
    def get_sensor_name(self):
        return self.name
    
    def get_temp_c(self):
        return self.temperature_c
        
    def get_temp_f(self):
        return self.temperature_f
        
    def get_humidity(self):
        return self.humidity
#end: class Sensor:

def get_dht11_configs():
    return dht11_sensor_array

def sensor_test():
    print("DHT11.py: Sensor Test")
    
    config_array = get_dht11_configs()
    sensor1_config = config_array[0]
    sensor2_config = config_array[1]
    sensor1 = Sensor(sensor1_config)
    sensor2 = Sensor(sensor2_config)
    
    while True:
        sensor1.process_sensor()
        sensor2.process_sensor()
        print("Sensor: " ,sensor1.get_sensor_name())
        print("tempc : " ,sensor1.get_temp_c())
        print("tempf : " ,sensor1.get_temp_f())
        print("humit : " ,sensor1.get_humidity())
        print("Sensor: " ,sensor2.get_sensor_name())
        print("tempc : " ,sensor2.get_temp_c())
        print("tempf : " ,sensor2.get_temp_f())
        print("humit : " ,sensor2.get_humidity())
        time.sleep(3)
    
    
if __name__ == '__main__':
    sensor_test() 
    
    
