###############################################################################
# File Name  : TheDataApp.py
# Date       : 10/30/2020
# Description: 
###############################################################################

from config import Config
from Data_Stats.DataApp import Ds_App
from SupportFiles.Shared import DHT11_Data

from datetime import datetime
import random


if __name__ == '__main__':
	print("Starting           :", __file__)

	the_config = Config()

	the_data_app = Ds_App(the_config)


	for x in range(10):
		some_sensor_data = DHT11_Data("sensor1", datetime.now(),
							float("{0:.2f}".format(random.uniform(0, 100))),
							float("{0:.2f}".format(random.uniform(32, 120))))

		the_data_app.write_sensor_data(some_sensor_data)

	query = the_data_app.read_last_sensor_record()

	for each in query:
		print("Query NUmber:", each)
		print(each.humidity)
		print(each.time_stamp)
		print(each.sensor)
		print(each.temperature)
		print(each.humidity)
