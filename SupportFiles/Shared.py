###############################################################################
# File Name  : Shared.py
# Date       : 10/31/2020
# Description: 
###############################################################################

from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, Float




class DHT11_Data:
    def __init__(self, name=False, time_data=0, humidity=0, temperature_f=0):
        self.name = name
        self.time_data = time_data
        self.humidity = humidity
        self.temperature_f = temperature_f

    def print_data(self):
        print(self.name)
        print(self.time_data)
        print(self.humidity)
        print(self.temperature_f)





