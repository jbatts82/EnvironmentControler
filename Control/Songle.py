###############################################################################
# File Name  : Songle.py
# Date       : 07/12/2020
# Description: Controls relay
###############################################################################

from gpiozero import LED
from time import sleep

relay1_config = {"name" : "Heater Switch", "gpio_zero_pin" : 14} #physical pin 8
relay2_config = {"name" : "Unassigned Switch", "gpio_zero_pin" : 18} #physical pin 12

relay_array = {}
relay_array[0] = relay1_config
relay_array[1] = relay2_config

class Relay:
    def __init__(self, config):
        self.name = config["name"]
        self.relay = LED(config["gpio_zero_pin"])
        self.relay.off()
        self.state = False

    def Get_Name(self):
        return self.name
        
    def Turn_Off(self):
        self.relay.off()
        self.state = False
    
    def Turn_On(self):
        self.relay.on()
        self.state = True
        
    def Get_State(self):
        return self.state
        
def get_relay_configs():
    return relay_array

def relay_test():
    print("Songle.py: Relay Test")
    
    relay_configs = get_relay_configs()
    
    relay1 = Relay(relay_configs[0])
    relay2 = Relay(relay_configs[1])
    
    num = 0
    
    while True:
        num = not num
        print("Relay1 Name : ", relay1.Get_Name())
        print("Relay2 Name : ", relay2.Get_Name())
        if num:
            relay1.Turn_On()
            relay2.Turn_Off()
        else:
            relay1.Turn_Off()
            relay2.Turn_On()
        print("Relay1 State: ", relay1.Get_State())
        print("Relay2 State: ", relay2.Get_State())
        sleep(5)
            
if __name__ == '__main__':
    relay_test()       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        
        
        
        
        