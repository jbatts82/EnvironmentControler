# Filename: Os.py
#
#
#

import schedule
import time
import Songle


def read_temp():
    print("reading temp")
    
def read_humidity():
    print("reading hum")
    
schedule.every(10).seconds.do(read_temp)
schedule.every(25).seconds.do(read_humidity)

Songle.init_relay()
Songle.relay1_on()


try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


