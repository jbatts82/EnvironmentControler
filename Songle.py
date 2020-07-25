###############################################################################
# File Name  : Songle.py
# Author     : John
# Date       : 07/12/2020
# Description: Controls relay
###############################################################################

from gpiozero import LED
from time import sleep

global relay1, relay2

relay1 = LED(14)
relay2 = LED(18)

def relay1_on():
    relay1.on()
    
def relay1_off():
    relay1.off()

def relay2_on():
    relay2.on()
    
def relay2_off():
    relay2.off()