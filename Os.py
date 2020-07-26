# Filename: Os.py
#
#
#

import schedule
import time
import Humidity

def Task_10s():
    Humidity.process_humidity()

def Task_60s():
    Humidity.save_humidity_to_file()
    

schedule.every(10).seconds.do(Task_10s)
schedule.every(60).seconds.do(Task_60s)

Humidity.init_humidity()


try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("quitting")


