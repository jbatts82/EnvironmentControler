###############################################################################
# Filename    : Humidity.py
# Date        : 07/25/2020 
# Description :
###############################################################################

import DHT11
import File_Handler

humidity_list = []
humidity_file = 'humidity_log.txt'
current_humidity_per = 0

def init_humidity():
    get_humidity_from_file()

def process_humidity():
    global current_humidity_per
    current_humidity_per = DHT11.get_humidity_percent()
    add_humidity_data_to_list(current_humidity_per)
    print("The Humidity is: ", current_humidity_per)

def get_humidity():
    global current_humidity_per
    return current_humidity_per

def get_humidity_from_file():
    # open file and put into list
    global humidity_list, humidity_file
    humidity_list = File_Handler.get_from_file(humidity_file)
        
def save_humidity_to_file():
    global humidity_list, humidity_file
    File_Handler.save_to_file(humidity_list, humidity_file)
        
def add_humidity_data_to_list(hum_data):
    global humidity_list
    humidity_list.append(hum_data)

def print_humidity():
    # read through the list
    global humidity_list
    print("Printing Humidity: ")
    for line in humidity_list:
        print(line)
        
def erase_humidity_file():
    global humidity_file
    File_Handler.erase_file(humidity_file)
