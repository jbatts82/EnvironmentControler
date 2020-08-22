###############################################################################
# File Name  : timeclock.py
# Date       : 08/01/2020
# Description: 
###############################################################################

import datetime
import time

class OS_Clock:
    def __init__(self):
        self.system_start_time = datetime.datetime.now()
  
    def get_time_since_start(self):
        delta_time = datetime.datetime.now() - self.system_start_time
        return delta_time
  
    def get_current_time_stamp(self):
        now = datetime.datetime.now()
        return now
  
    def date_now(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        today = str(today)
        return(today)

    def time_now(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        now = str(now)
        return(now)
    
    
def time_clock_test():
    print("Time_Clock.py: time_clock_test Test")
    the_clock = OS_Clock()
    
    for x in range(9):
        print("OS Delta Time: ", the_clock.get_time_since_start())
        print("OS Time      : ", the_clock.get_current_time_stamp())
        time.sleep(1)
         
if __name__ == '__main__':
    time_clock_test() 