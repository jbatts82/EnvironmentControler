###############################################################################
# File Name  : TheDataApp.py
# Date       : 11/07/2020
# Description: 
###############################################################################


import Control.ControllerApp as CA
from config import Config
from Data_Stats.DataApp import Ds_App

if __name__ == '__main__':
	print("Starting           :", __file__)
	the_config = Config()
	CA.Initialize_Control(the_config)
	CA.Run_Tasks()



	# Testing ds_app interfaces

	# print("Deveeloping...")
	# a_config = Config()
	# ds_app = Ds_App(a_config)

	# last_rec = ds_app.get_last_sensor_reading()
	# print(last_rec.name)
	# print(last_rec.time_data)
	# print(last_rec.temperature_f)
	# print(last_rec.humidity)

	# sensor = "upper_sensor"
	# last_temp = ds_app.get_last_temp(sensor)
	# print("Last Temperature Reading from {}: {}".format(sensor, str(last_temp)))

	# sensor = "lower_sensor"
	# last_temp = ds_app.get_last_temp(sensor)
	# print("Last Temperature Reading from {}: {}".format(sensor, str(last_temp)))

	# sensor = "upper_sensor"
	# last_temp = ds_app.get_last_humid(sensor)
	# print("Last Humidity Reading from {}: {}".format(sensor, str(last_temp)))

	# sensor = "lower_sensor"
	# last_temp = ds_app.get_last_humid(sensor)
	# print("Last Humidity Reading from {}: {}".format(sensor, str(last_temp)))

	# last_avg_room = ds_app.get_last_avg_room_temp()
	# print("Last Avg Room Temp: {}".format(str(last_avg_room)))