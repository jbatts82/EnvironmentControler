###############################################################################
# Filename    : Temperature.py
# Date        : 07/25/2020 
# Description :
###############################################################################


import sys
sys.path.append('..')
from SupportFiles.DB_Handler import DB_Sensor
from config import Config

class Temperature:
    def __init__(self):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.config = Config()
        self.sensor1_db = DB_Sensor(self.config, 0)
        self.sensor2_db = DB_Sensor(self.config, 1)
        
    def process_temperature(self):
        self.update_to_latest_record()
        self.calculate_avg_temperature()
        self.is_max(self.avg_temperature)
        self.is_min(self.avg_temperature)

    def update_to_latest_record(self):
        self.sensor1_db.update_to_last_record()
        self.instant_temperature1 = self.sensor1_db.get_last_temperature()
        self.sensor2_db.update_to_last_record()
        self.instant_temperature2 = self.sensor2_db.get_last_temperature()

    def calculate_avg_temperature(self):
        self.avg_temperature = (self.instant_temperature1 + self.instant_temperature2) / 2
    
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