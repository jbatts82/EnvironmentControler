###############################################################################
# Filename    : Humidity.py
# Date        : 07/25/2020 
# Description : Processes humidity sensor data. 
###############################################################################

import sys
sys.path.append('..')
from SupportFiles.DB_Handler import DB_Sensor
from config import Config

class Humidity:
    def __init__(self):
        self.max_humidity = 0
        self.min_humidity = 99
        self.avg_humidity = 0
        self.config = Config()
        self.sensor1_db = DB_Sensor(self.config, 0)
        self.sensor2_db = DB_Sensor(self.config, 1)
        
    def process_humidity(self):
        self.update_to_latest_record()
        self.calculate_avg_humidity()
        self.is_max(self.avg_humidity)
        self.is_min(self.avg_humidity)

    def update_to_latest_record(self):
        
        self.sensor1_db.update_to_last_record()
        self.instant_humidity1 = self.sensor1_db.get_last_humidity()
        self.sensor2_db.update_to_last_record()
        self.instant_humidity2 = self.sensor2_db.get_last_humidity()

    def calculate_avg_humidity(self):
        self.avg_humidity = (self.instant_humidity1 + self.instant_humidity2) / 2
    
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