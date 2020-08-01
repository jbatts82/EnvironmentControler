###############################################################################
# File Name  : timeclock.py
# Date       : 08/01/2020
# Description: 
###############################################################################

from datetime import datetime

six_pm = "23:00"
seven_pm = "24:00"
eight_pm = "01:00"
nine_pm = "02:00"

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time