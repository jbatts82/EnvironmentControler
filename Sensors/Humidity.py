###############################################################################
# Filename    : Humidity.py
# Date        : 07/25/2020 
# Description : Processes humidity sensor data. 
###############################################################################

import DHT11
from DHT11 import Sensor
import Csv_Handler

file_name = 'humidity_log.txt'
field_names = field_names = ['date', 'time', 'avg_humidity']

class Humidity:
    def __init__(self, sensor1, sensor2):
        self.max_humidity = 0
        self.min_humidity = 99
        self.avg_humidity = 0
        self.instant_humidity1 = 0
        self.instant_humidity2 = 0
        self.sensor_cnt = 0
        self.data_log = None
        
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        
        self.process_humidity()


    def calculate_avg_humidity(self):
        return (self.instant_humidity1 + self.instant_humidity2) / 2
    
    def get_average_humidity(self):
        return self.avg_humidity
        
    def get_humidity1(self):
        return self.instant_humidity1
    
    def get_humidity2(self):
        return self.instant_humidity2
        
    def is_max(self, humidity):
        if humidity > self.max_humidity:
            self.max_humidity = humidity
            
    def is_min(self, humidity):
        if humidity < self.min_humidity:
            self.min_humidity = humidity
        
    def get_min_humidity(self):
        return self.min_humidity
        
    def get_max_humidity(self):
        return self.max_humidity
        
    def process_humidity(self):
        self.instant_humidity1 = self.sensor1.get_humidity()
        self.instant_humidity2 = self.sensor2.get_humidity()
        self.avg_humidity = self.calculate_avg_humidity()
        self.is_max(self.avg_humidity)
        self.is_min(self.avg_humidity)


        
def humidity_test():
    print("Humidity.py: Humidity Test")
    the_humidity = Humidity()
    print("Humidity 1  : ", the_humidity.get_humidity1())
    print("Humidity 2  : ", the_humidity.get_humidity2())
    print("Humidity Avg: ", the_humidity.get_average_humidity())

    


    
if __name__ == '__main__':
    humidity_test() 
    