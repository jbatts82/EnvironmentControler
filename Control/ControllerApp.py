###############################################################################
# File Name  : Controller.py
# Date       : 07/25/2020
# Description: Main controller of system
###############################################################################

import sys
sys.path.append("..")
from SupportFiles.DB_Handler import DB_Manager
from SupportFiles.Time_Clock import OS_Clock
import schedule
from time import sleep
from config import Config


def Task_Get_Data():
    system_config = Config()
    db = DB_Manager(system_config)




schedule.every(1).seconds.do(Task_Get_Data)

try:
    while True: #run forever
        schedule.run_pending()
        sleep(1)
except:
    print("System Error")
finally:
    #heater.Kill()
    print("bye..bye")
