###############################################################################
# File Name  : DHT11.py
# Author     : John
# Date       : 07/12/2020
# Description: Reads humidity sensor
###############################################################################

#!/usr/bin/python

import sys
import Adafruit_DHT

sensor = 11
pin = 17

def print_instant_humidity():
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    global sensor, pin
    humidity, temperature_c = Adafruit_DHT.read_retry(sensor, pin)    
    # Un-comment the line below to convert the temperature to Fahrenheit.
    #temperature_f = temperature_c * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature_c is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature_c, humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    
def get_humidity_percent():
    global sensor, pin
    humidity, temperature_c = Adafruit_DHT.read_retry(sensor, pin)
    return humidity
    
def get_temperature_degree_c():
    global sensor, pin
    humidity, temperature_c = Adafruit_DHT.read_retry(sensor, pin)
    return temperature_c
    