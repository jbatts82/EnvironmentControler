###############################################################################
# File Name  : Os.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import schedule
import time
from datetime import datetime
import Humidity
import Temperature
import Heater
import Songle
import Plug
import Fan
import Light
import DHT11

six_pm = "23:00"
seven_pm = "24:00"
eight_pm = "01:00"
nine_pm = "02:00"


    
def Task_60s():
    get_time()
    Fan.Process_Fan()
    Fan.Print_Fan_State()
    Heater.process_heater()
    
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    return current_time

def sensor1():
    try:
        DHT11.process_sensor_1()
    except:
        print("Sensor1 ERROR")
    finally:
        print("Sensor1 Humidity: ", DHT11.get_humidity_1())
        print("Sensor1 Temp_F: ", DHT11.get_temp_1())
    
def sensor2():
    try:
        DHT11.process_sensor_2()
    except:
        print("Sensor2 ERROR")
    finally:
        print("Sensor2 Humidity: ", DHT11.get_humidity_2())
        print("Sensor2 Temp_F: ", DHT11.get_temp_2())
    
    
schedule.every(60).seconds.do(Task_60s)
schedule.every().minute.at(":00").do(sensor1)
#schedule.every().minute.at(":30").do(sensor2)

Humidity.init_humidity()
Temperature.init_temperature()
Plug.init_plug()

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
    
    


