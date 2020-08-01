###############################################################################
# Filename    : Temperature.py
# Date        : 07/25/2020 
# Description :
###############################################################################

import DHT11
import File_Handler
import Max6675K

temperature_list = []
temperature_file = 'temperature_log.txt'
last_temp_c = 0
last_temp_f = 0
avg_10min_temp_c = 0
avg_10min_temp_f = 0

def init_temperature():
    get_temperature_from_file()
    Max6675K.init_tempSensor()

def process_temperature():
    global last_temp_c, last_temp_f
    last_temp_c = DHT11.get_temperature1_degree_c()
    last_temp_f = last_temp_c * 9/5.0 + 32
    add_temperature_data_to_list(last_temp_f)
    print("The Temperature is: ", last_temp_f)

def get_temperature_f():
    global last_temp_f
    return last_temp_f
    
def get_temperature_c():
    global last_temp_c
    return last_temp_c

def get_box_temperature_f():
    return Max6675K.getTemp()

def get_temperature_from_file():
    # open file and put into list
    global temperature_list, temperature_file
    temperature_list = File_Handler.get_from_file(temperature_file)
        
def save_temperature_to_file():
    global temperature_list, temperature_file
    File_Handler.save_to_file(temperature_list, temperature_file)
        
def add_temperature_data_to_list(hum_data):
    global temperature_list
    temperature_list.append(hum_data)

def print_temperature():
    # read through the list
    global temperature_list
    print("Printing temperature: ")
    for line in temperature_list:
        print(line)
        
def erase_temperature_file():
    global temperature_file
    File_Handler.erase_file(temperature_file)