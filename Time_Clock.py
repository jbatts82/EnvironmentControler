###############################################################################
# File Name  : timeclock.py
# Date       : 08/01/2020
# Description: 
###############################################################################

import datetime

six_pm = "23:00"
seven_pm = "24:00"
eight_pm = "01:00"
nine_pm = "02:00"

    
def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return(today)

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)