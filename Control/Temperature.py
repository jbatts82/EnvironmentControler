###############################################################################
# Filename    : Temperature.py
# Date        : 07/25/2020 
# Description :
###############################################################################


import sys
sys.path.append('/home/mario/EnvironmentController/SupportFiles/')
import Time_Clock
import DB_Handler

database_location = '/home/mario/EnvironmentController/readings.db'

class Temperature:
    def __init__(self):
        self.start_time              = 0
        self.max_temperature         = 0
        self.min_temperature         = 99
        self.rolling_avg_temperature = 0
        self.rolling_avg_time        = 0
        self.instant_temperature1    = 0
        self.instant_temperature2    = 0
        self.instant_avg_temperature = 0
        self.temp1_data              = None
        self.temp2_data              = None
        init_data_stream(self)
        self.process_temperature()

    def process_temperature(self):
        #get last database entry
        self.get_temp1()
        self.get_temp2()
        self.calculate_instant_avg_temperature()
        self.is_max(self.instant_avg_temperature)
        self.is_min(self.instant_avg_temperature)
        
    def init_data_stream(self):
        #connect to database
        self.temp1_data = DB_Manager(database_location, sensor1_name)
        self.temp2_data = DB_Manager(database_location, sensor1_name)

    def get_temp1(self):
        row = self.temp1_data.get_last_row('*')
        self.instant_temperature1 = row[1]
        
    def get_temp2(self):
        row = self.temp2_data.get_last_row('*')
        self.instant_temperature2 = row[1]
        
    def calculate_instant_avg_temperature(self):
        self.instant_avg_temperature = (self.instant_temperature1 + self.instant_temperature2) / 2
    
    def get_instant_avg_temperature(self):
        return self.instant_avg_temperature
        
    def get_instant_temp1(self):
        return self.instant_temperature1
    
    def get_instant_temp2(self):
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
       


        
def temperature_test():
    print("Temperature.py: Temperature Test")
    the_temperature = Temperature()
    print("Temperature 1  : ", the_temperature.get_temperature1())
    print("Temperature 2  : ", the_temperature.get_temperature2())
    print("Temperature Avg: ", the_temperature.get_average_temperature())

    


    
if __name__ == '__main__':
    temperature_test() 