###############################################################################
# File Name  : Shared.py
# Date       : 10/31/2020
# Description: 
###############################################################################

from datetime import datetime

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



# def print_this(input1, input2):
#     output_string = '''{}{:<20}{}'''.format(input1, input2)
#     print(output_string)

#     #print("Starting File: ", __file__)

# print_this("Stadfrting", "File")