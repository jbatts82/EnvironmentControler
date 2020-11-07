###############################################################################
# File Name  : TheDataApp.py
# Date       : 11/07/2020
# Description: 
###############################################################################


import Control.ControllerApp as CA
from config import Config

if __name__ == '__main__':
	print("Starting           :", __file__)
	the_config = Config()
	CA.Initialize_Control(the_config)
	CA.Run_Tasks()