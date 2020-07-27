###############################################################################
# File Name  : Os.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import schedule
import time
import Humidity
import Temperature
import Heater
import Songle

def Task_10s():
    Humidity.process_humidity()
    time.sleep(1)
    Temperature.process_temperature()
    time.sleep(1)

def Task_30s():
    Humidity.save_humidity_to_file()
    time.sleep(1)
    Temperature.save_temperature_to_file()
    time.sleep(1)

def Task_60s():
    Heater.process_heater()
    time.sleep(1)

schedule.every(10).seconds.do(Task_10s)
schedule.every(30).seconds.do(Task_30s)
schedule.every(60).seconds.do(Task_60s)

Humidity.init_humidity()
Temperature.init_temperature()


try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("quitting by keyboard")
finally:
    print("bye..bye")
    Humidity.save_humidity_to_file()
    Temperature.save_temperature_to_file()
    Songle.shut_down()
    
    


