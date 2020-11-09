###############################################################################
# File Name  : Shared.py
# Date       : 10/31/2020
# Description: 
###############################################################################

from datetime import datetime

class DHT11_Data:
    def __init__(self, name=None, time_data=0, humidity=0, temperature_f=0):
        self.name = name
        self.time_data = time_data
        self.humidity = humidity
        self.temperature_f = temperature_f
        self.error_state = False

    def print_data(self):
        print("DHT11 Name : ",self.name)
        print("Time       : ",self.time_data)
        print("Humidity   : ",self.humidity)
        print("Temperature: ",self.temperature_f)
        print("Error State: ",self.error_state)
