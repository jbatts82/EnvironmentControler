###############################################################################
# File Name  : TheDataApp.py
# Date       : 10/30/2020
# Description: 
###############################################################################

from config import Config
from Data_Stats.DataApp import Ds_App
from SupportFiles.Shared import DHT11_Data

from datetime import datetime



if __name__ == '__main__':
	print("Starting           :", __file__)

	the_config = Config()

	the_data_app = Ds_App(the_config)

	some_sensor_data = DHT11_Data("sensor1", datetime.now(), 32.2, 66.6)

	the_data_app.write_sensor_data(some_sensor_data)


	# sensor_data1 = DHT11_Data()
	# sensor_data1.name = "sensor1"
	# sensor_data1.time_data = datetime.now()
	# sensor_data1.humidity = float("{0:.2f}".format(random.uniform(0, 100)))
	# sensor_data1.temperature_f = float("{0:.2f}".format(random.uniform(32, 120)))
	# sensor_data1.print_data()
