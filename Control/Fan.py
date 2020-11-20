###############################################################################
# Filename    : Fan.py
# Date        : 07/29/2020 
# Description : Controls Exhaust Fan
###############################################################################

from time import sleep
import Control.Plug as Plug
from SupportFiles.Time_Clock import Device_Clock

class Fan:
    def __init__(self):
        self.name = "Exhaust Fan"
        self.state = False
        self.previous_state = False
        self.device_clock = Device_Clock()
        self.Process_Fan()
        
    def Turn_On(self):
        Plug.plug1_on()
    
    def Turn_Off(self):
        Plug.plug1_off()
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state

    def Set_Fan_Timer(self, time_min):
        self.device_clock.set_on_timer(time_min)
        self.Turn_On()
        
    def Process_Fan(self):
        print("Processing         :", self.name)
        try: 
            timer_state = self.device_clock.process_clock()
            if timer_state == False:
                self.Turn_Off()

            self.state = Plug.get_plug1_state()
        except: 
            print("SIGNAL SNA         :", self.name)
            self.state = self.previous_state
        else:
            print("Success Processing :", self.name)
            self.previous_state = self.state
        finally:
            pass
            

    
    
    
    