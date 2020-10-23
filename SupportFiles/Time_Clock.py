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
        self.fan_on_tmr = 0
  
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

        # this_morning = datetime.datetime(2009, 12, 2, 9, 30)
        # last_night = datetime.datetime(2009, 12, 1, 20, 0)
        # this_morning.time() < last_night.time()
        # today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)