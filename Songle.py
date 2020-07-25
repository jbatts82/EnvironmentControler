###############################################################################
# File Name  : Songle.py
# Author     : John
# Date       : 07/12/2020
# Description: Controls relay
###############################################################################

from gpiozero import LED
from time import sleep

relay1 = LED(14)
relay2 = LED(18)

def init_relay():
    global relay1, relay2
    relay1.off()
    relay2.off()

def relay1_on():
    global relay1
    relay1.on()
    
def relay1_off():
    global relay1
    relay1.off()

def relay2_on():
    global relay2
    relay2.on()
    
def relay2_off():
    global relay2
    relay2.off()
    
    

relay1_on()