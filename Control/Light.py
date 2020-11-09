###############################################################################
# Filename    : Light.py
# Date        : 07/27/2020 
# Description : Controls TPLink Smart Plugs
###############################################################################


import Control.Plug as Plug
from time import sleep

class Light:
    def __init__(self):
        self.name = "Mars Hydro LED x 2"
        self.state = False
        self.previous_s = False
        self.Process_Light()
        
    def Turn_On(self):
        print("Light On")
        self.state = Plug.plug2_on()
        
    def Turn_Off(self):
        print("Light Off")
        self.state = Plug.plug2_off()
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state

    def Process_Light(self):
        print("Processing         :", self.name)
        try: 
            self.state = Plug.get_plug2_state()
            self.previous_s = self.state
        except: 
            print("SIGNAL SNA         :", self.name)
            self.state = self.previous_s
        else:
            print("Success Processing :", self.name)
            self.previous_s = self.state
        finally:
            pass