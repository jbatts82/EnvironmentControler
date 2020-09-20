###############################################################################
# Filename    : Leds.py
# Date        : 08/26/2020 
# Description : Controls LED Indicator Lights
#             : LED1->29->gpiozero_5
#               LED2->31->gpiozero_6
#               LED3->33->gpiozero_13
#               LED4->35->gpio24
###############################################################################

from gpiozero import LED
from time import sleep

led1 = LED(5)
led2 = LED(6)
led3 = LED(13)
led4 = LED(19)


def toggle_sensor_led():
    print("toggle LED")
    led1.toggle()

def toggle_control_led():
    led2.toggle()



