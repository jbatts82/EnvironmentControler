###############################################################################
# File Name  : timeclock.py
# Date       : 08/01/2020
# Description: 
###############################################################################

from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time