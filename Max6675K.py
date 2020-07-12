###############################################################################
# File Name  : Max6675K.py
# Author     : John
# Date       : 05/23/20
# Description: Gets temperature from the sensor
###############################################################################

import spidev
import time

def init_tempSensor(bus, device):
    global spi
    spi = spidev.SpiDev() # create spi object
    spi.open(bus, device) # open spi port 0, device (CS) 0
    spi.max_speed_hz = 1953000
    spi.mode = 0b00 #
    spi.bits_per_word = 8
    spi.lsbfirst = False 
    return 1

def disconnect():
    spi.close() # … close the port before exit

def getTemp():
    resp = spi.readbytes(2)
    print(resp)
    frame = resp[0] << 8 | resp[1]
    print(frame)
    
    if(frame & 0x4):
        print("Error: Thermo-Couple Input Is Open")
    else:
        raw = frame>>3
        print("raw: ", raw)
        C = raw*.25
        print("C  : ", C)
        F = (C * 9 / 5) + 32
        print("F  : ", F)
    return str(F)
    



def hello():
    return "hellhhho"


