###############################################################################
# Filename    : Csv_Handler.py
# Date        : 08/02/2020 
# Description : Reads and Writes data to csv file.
###############################################################################

import csv
import os.path
from os import path
import datetime
from time import sleep
import time
import random
import Time_Clock

#file_name = 'test_readings.csv'
#field_names = ['abs_time', 'temp', 'humidity']

class CSV_Tool:
    def __init__(self, file_name, field_names):
        self.file_name = file_name
        self.field_names = field_names

    def append_to_file(self, record):
        with open(self.file_name, mode='a') as sensor_readings:
            sensor_write = csv.DictWriter(sensor_readings, delimiter=',', \
            fieldnames=self.field_names, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #sensor_write.writeheader()
            write_to_log = sensor_write.writerow(record)
        return(write_to_log)

    def verify_csv(self):
        pass
    
    def create_csv(self):
        pass
        
    def get_field_names(self):
        pass

    def dump_record_values(self):
        with open(self.file_name) as sensor_file:
            sensor_read = csv.reader(sensor_file, delimiter=',')
            print(type(sensor_read))
            for row in sensor_read:
                print(row)
                
    def empty_file(self):
        with open(self.file_name, mode='w') as file:
            file.close()
            

    
    
def csv_test():
    print("Csv_Handler.py: Csv Test")
    the_tool = CSV_Tool(file_name, field_names)
    the_time = Time_Clock.OS_Clock()
    
    record = {}
    for x in range(100):
        record['abs_time'] = the_time.get_current_time_stamp()
        record['temp'] = random.uniform(32, 120)
        record['humidity'] = random.uniform(32, 120)
        the_tool.append_to_file(record)
    the_tool.dump_record_values()
    the_tool.empty_file()




    
if __name__ == "__main__":
    csv_test()
