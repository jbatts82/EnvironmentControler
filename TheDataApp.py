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
import numpy as np
import pandas as pd


def insert_some_rando_data(record_num):
	for x in range(record_num):
		some_sensor_data = DHT11_Data("sensor1", datetime.now(),
							float("{0:.2f}".format(random.uniform(0, 100))),
							float("{0:.2f}".format(random.uniform(32, 120))))
		the_data_app.write_sensor_data(some_sensor_data)



def date_time_practice():
	print("datetime_practice...")

	date_time_now = datetime.now()

	print("the datetime now: {}".format(date_time_now))
	print("the current year: {}".format(date_time_now.year))
	print("the current day : {}".format(date_time_now.strftime("%A"))) 
	my_speced_date = datetime(1982, 3, 22)
	print("my birthday     : {}".format(my_speced_date))


def pandas_numpy_practice():
	print("Number Practice!")
	the_config = Config()
	the_data_app = Ds_App(the_config)
	sensor_name = "upper_sensor"
	the_average = the_data_app.get_rolling_avg_temp(sensor_name)
	print("The rolling average is: {}".format(the_average))





if __name__ == '__main__':
	print("Starting           :", __file__)
	time_of_day()
