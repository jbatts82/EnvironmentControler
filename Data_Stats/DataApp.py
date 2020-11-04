
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
		reading = Reading()
		reading.time_stamp = self.current_sensor_data.time_data
		reading.sensor = self.current_sensor_data.name
		reading.temperature = self.current_sensor_data.temperature_f
		reading.humidity = self.current_sensor_data.humidity
		self.data_base.write_to_sensor_table(reading)

	def read_last_sensor_record(self):
		return self.data_base.get_table()

#end class Ds_App