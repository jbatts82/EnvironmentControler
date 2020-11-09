###############################################################################
# File Name  : Humidifier.py
# Date       : 10/17/2020
# Description: Humdifier Controls. Adds humidity.
###############################################################################

from time import sleep
from Control.Songle import Relay
import Control.Songle
class Humidifier:
    def __init__(self):
        self.name = "Humidifier"
        self.state = False
        self.relay_configs = Control.Songle.get_relay_configs()
        self.relay1 = Relay(self.relay_configs[1])

    def Turn_On(self):
        self.relay1.Turn_On()
        self.state = True
    
    def Turn_Off(self):
        self.relay1.Turn_Off()
        self.state = False
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        self.relay1.Turn_Off()
        self.state = True
        print("Humidifier Off")