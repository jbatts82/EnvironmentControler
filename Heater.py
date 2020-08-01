###############################################################################
# File Name  : Heater.py
# Date       : 07/12/2020
# Description: Heater Controls
###############################################################################

import Songle
from time import sleep
from Songle import Relay

class Heater:
    def __init__(self):
        self.name = "Space Heater"
        self.state = False
        self.relay_configs = Songle.get_relay_configs()
        self.relay1 = Relay(self.relay_configs[0])

    def Turn_On(self):
        self.relay1.Turn_On()
        self.state = False
    
    def Turn_Off(self):
        self.relay1.Turn_Off()
        self.state = True
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        self.relay1.Turn_Off()
        self.state = True
        print("Heater Off")
        
def heater_test():
    print("Heater.py: Heater Test")   
    num = 0
    while True:
        num = not num
        print("Heater Name : ", heater.Get_Name())
        if num:
            heater.Turn_On()
        else:
            heater.Turn_Off()
        print("Heater State: ", heater.Get_State())
        sleep(5)



if __name__ == '__main__':
    try:
        heater = Heater()
        heater_test()
    except:
        heater.Turn_Off()
        print("Heater Off")
    finally:
        pass

    