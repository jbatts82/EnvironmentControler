
###############################################################################
# Filename    : DataApp.py
# Date        : 10/23/2020 
# Description : Application that gets and stores sensor readings. 
#               Also provides stats. 
###############################################################################

from SupportFiles.Shared import DHT11_Data
from Data_Stats.Ds_Handler import Ds_Sensor
from Data_Stats.Ds_Handler import Reading


class Ds_App:
	def __init__(self, config=None):
		self.current_sensor_data = DHT11_Data()
		self.data_base = Ds_Sensor(config)

	# accept sensor context data and format it for database context
	def write_sensor_data(self, some_sensor_data):
		print("Writing Sensor Data")

		self.current_sensor_data = some_sensor_data

		# convert sensor data to database data
		reading = Reading()
		reading.time_stamp = self.current_sensor_data.time_data
		reading.sensor = self.current_sensor_data.name
		reading.temperature = self.current_sensor_data.temperature_f
		reading.humidity = self.current_sensor_data.humidity

		# write new database object to database
		self.data_base.insert_record(reading)

	def get_last_sensor_reading(self):
		last_rec = self.data_base.get_last_sensor_rec()

		sensor_data = DHT11_Data()
		sensor_data.name = last_rec.sensor
		sensor_data.time_data = last_rec.time_stamp
		sensor_data.temperature_f = last_rec.temperature
		sensor_data.humidity = last_rec.humidity

		return sensor_data

	def get_last_temp(self, sensor_num):
		print("Last Temperature Reading From: ", str(sensor_num))

	def get_last_humid(self, sensor_num):
		print("Last Humidity Reading From: ", str(sensor_num))

	def get_rolling_avg_temp(self, sensor_num):
		print("Rolling Avg Temperature From: ", str(sensor_num))

	def get_rolling_avg_humid(self, sensor_num):
		print("Rolling Avg Humidity From: ", str(sensor_num))



#end class Ds_App