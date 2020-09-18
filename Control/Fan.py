###############################################################################
# Filename    : Fan.py
# Date        : 07/29/2020 
# Description : Controls Exhaust Fan
###############################################################################

from time import sleep
import Plug

class Fan:
    def __init__(self):
        self.name = "Exhaust Fan"
        self.state = False
        self.previous_s = False
        self.Process_Fan()
        
    def Turn_On(self):
        Plug.plug1_on()
    
    def Turn_Off(self):
        Plug.plug1_off()
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state

    def Process_Fan(self):
        print("Processing         :", self.name)
        try: 
            self.state = Plug.get_plug1_state()
        except: 
            print("SIGNAL SNA         :", self.name)
            self.state = self.previous_s
        else:
            print("Success Processing :", self.name)
            self.previous_s = self.state
        finally:
            pass
            

    
    
    
    