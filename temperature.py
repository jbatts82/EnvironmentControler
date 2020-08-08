###############################################################################
# Filename    : Temperature.py
# Date        : 07/25/2020 
# Description :
###############################################################################

import DHT11
from DHT11 import Sensor
import Csv_Handler

file_name = 'temperature_log.txt'
field_names = field_names = ['date', 'time', 'avg_temperature']

class Temperature:
    def __init__(self, sensor1, sensor2):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.instant_temperature1 = 0
        self.instant_temperature2 = 0
        self.sensor_cnt = 0
        self.data_log = None
        
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        
        self.process_temperature()


    def calculate_avg_temperature(self):
        return (self.instant_temperature1 + self.instant_temperature2) / 2
    
    def get_average_temperature(self):
        return self.avg_temperature
        
    def get_temperature1(self):
        return self.instant_temperature1
    
    def get_temperature2(self):
        return self.instant_temperature2
        
    def is_max(self, temperature):
        if temperature > self.max_temperature:
            self.max_temperature = temperature
            
    def is_min(self, temperature):
        if temperature < self.min_temperature:
            self.min_temperature = temperature
        
    def get_min_temperature(self):
        return self.min_temperature
        
    def get_max_temperature(self):
        return self.max_temperature
        
    def process_temperature(self):
        self.instant_temperature1 = self.sensor1.get_temp_f()
        self.instant_temperature2 = self.sensor2.get_temp_f()
        self.avg_temperature = self.calculate_avg_temperature()
        self.is_max(self.avg_temperature)
        self.is_min(self.avg_temperature)


        
def temperature_test():
    print("Temperature.py: Temperature Test")
    the_temperature = Temperature()
    print("Temperature 1  : ", the_temperature.get_temperature1())
    print("Temperature 2  : ", the_temperature.get_temperature2())
    print("Temperature Avg: ", the_temperature.get_average_temperature())

    


    
if __name__ == '__main__':
    temperature_test() 