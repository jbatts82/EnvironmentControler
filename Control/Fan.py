###############################################################################
# Filename    : Fan.py
# Date        : 07/29/2020 
# Description : Controls Exhaust Fan
###############################################################################

from time import sleep
import Plug

fan1_config = {"name" : "Exhaust Fan"}

fan_array = {}
fan_array[0] = fan1_config

class Fan:
    def __init__(self, config):
        self.name = config["name"]
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
        print("Processing        :", self.name)
        try: 
            self.state = Plug.get_plug1_state()
        except: 
            print("SIGNAL SNA        :", self.name)
            self.state = self.previous_s
        else:
            print("Success Processing:", self.name)
            self.previous_s = self.state
        finally:
            pass
            
    
def get_fan_configs():
    return fan_array
    
def fan_test():   
    print("Fan.py: Fan Test")
    fan_configs = get_fan_configs()
    fan1 = Fan(fan_configs[0])
    
    while True:
        fan1.Process_Fan()
        print("Fan Name : ", fan1.Get_Name())
        print("Fan State: ", fan1.Get_State())
        fan1.Turn_On()
        sleep(3)
        fan1.Process_Fan()
        print("Fan Name : ", fan1.Get_Name())
        print("Fan State: ", fan1.Get_State())
        fan1.Turn_Off()
        sleep(3)
        fan1.Process_Fan()
        print("Fan Name : ", fan1.Get_Name())
        print("Fan State: ", fan1.Get_State())
        sleep(3)
      
if __name__ == '__main__':
    Plug.init_plug()
    fan_test()   
    
    
    
    