###############################################################################
# File Name  : TheSensorApp.py
# Date       : 11/07/2020
# Description: 
###############################################################################


import asyncio
import Sensors.SensorApp as sa


if __name__ == '__main__':
	print("Starting           :", __file__)
	asyncio.run(sa.main_loop())



