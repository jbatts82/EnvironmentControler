###############################################################################
# Filename    : Temperature.py
# Date        : 07/25/2020 
# Description : 
###############################################################################

import Time_Clock



class Temperature:
    def __init__(self, sensor1, sensor2):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.instant_temperature1 = 0
        self.instant_temperature2 = 0
        self.sensor_cnt = 0
        self.data_logger = CSV_Tool(file_name, field_names)
        
        self.sensor1 = Sensor
        self.sensor2 = sensor2
        print("about to profeess")
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
        
    def write_temp_to_file(self):
        the_time = Time_Clock.OS_Clock()
        record = {}
        record['abs_time'] = the_time.get_current_time_stamp()
        record['avg_temperature'] = self.avg_temperature
        self.data_logger.append_to_file(record)
            
    def process_temperature(self):
        self.instant_temperature1 = self.sensor1.get_temp_f()
        print("mytemperature1: {}").format(self.instant_temperature1)
        self.instant_temperature2 = self.sensor2.get_temp_f()
        self.avg_temperature = self.calculate_avg_temperature()
        self.is_max(self.avg_temperature)
        self.is_min(self.avg_temperature)
        self.write_temp_to_file()

        
def temperature_test():
    print("Temperature.py: Temperature Test")
    the_temperature = Temperature()
    print("Temperature 1  : ", the_temperature.get_temperature1())
    print("Temperature 2  : ", the_temperature.get_temperature2())
    print("Temperature Avg: ", the_temperature.get_average_temperature())

    


    
if __name__ == '__main__':
    temperature_test() 