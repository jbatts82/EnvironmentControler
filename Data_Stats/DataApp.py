
###############################################################################
# Filename    : DataApp.py
# Date        : 10/23/2020 
# Description : Application that gets and stores sensor readings. 
#               Also provides stats. 
###############################################################################


from SupportFiles.Shared import DHT11_Data
from Data_Stats.Ds_Handler import Ds_Sensor, Ds_Control
from Data_Stats.Ds_Handler import Reading, ControlStatus


class Ds_App:
	def __init__(self, config=None):
		self.current_sensor_data = DHT11_Data()
		self.data_base = Ds_Sensor(config)
		self.control_base = Ds_Control(config)
	
	def write_sensor_data(self, some_sensor_data):
		# accept sensor context data and format it for database context
		self.current_sensor_data = some_sensor_data
		# convert sensor data to database data
		reading = Reading()
		reading.time_stamp = self.current_sensor_data.time_data
		reading.sensor = self.current_sensor_data.name
		reading.temperature = self.current_sensor_data.temperature_f
		reading.humidity = self.current_sensor_data.humidity
		# write new database object to database
		self.data_base.insert_record(reading)

	def write_control_data(self, time_stamp, heater_state, humidifer_state, fan_state, light_state):
		control_stats = ControlStatus()
		control_stats.time_stamp = time_stamp
		control_stats.heater_state = heater_state
		control_stats.humidifer_state = humidifer_state
		control_stats.fan_state = fan_state
		control_stats.light_state = light_state
		self.control_base.insert_record(control_stats)

	def get_last_sensor_reading(self):
		last_rec = self.data_base.get_last_sensor_rec()
		sensor_data = DHT11_Data()
		sensor_data.name = last_rec.sensor
		sensor_data.time_data = last_rec.time_stamp
		sensor_data.temperature_f = last_rec.temperature
		sensor_data.humidity = last_rec.humidity
		return sensor_data

	def get_last_temp(self, sensor_name):
		record = self.data_base.get_last_sensor_rec_from(sensor_name)
		last_temperature = record.temperature
		return last_temperature

	def get_last_humid(self, sensor_name):
		record = self.data_base.get_last_sensor_rec_from(sensor_name)
		last_humid = record.humidity
		return last_humid

	def get_last_avg_room_temp(self):
		sensor1_temp = self.get_last_temp("upper_sensor")
		sensor2_temp = self.get_last_temp("lower_sensor")
		avg_temp = (sensor1_temp + sensor2_temp) / 2
		return avg_temp

	def get_last_avg_room_humid(self):
		sensor1_temp = self.get_last_humid("upper_sensor")
		sensor2_temp = self.get_last_humid("lower_sensor")
		avg_humid = (sensor1_temp + sensor2_temp) / 2
		return avg_humid

	def dump_sensor_records(self):
		self.data_base.dump_table()

	def print_record(self, record):
		print("Sensor Name: {}".format(record.sensor))
		print("Time       : {}".format(record.time_stamp))
		print("Temperature: {}".format(record.temperature))
		print("Humidity   : {}".format(record.humidity))
		print("")

	def get_previous_readings_time(self, mins_previous, sensor_name):
		data = self.data_base.get_last_recs_time(mins_previous, sensor_name)
		return data

	def get_previous_control_stats(self, mins_previous):
		data = self.control_base.get_last_records(mins_previous)
		return data

	def verify_sensor_data(self, sensor_data):
		sensor_name = sensor_data.name
		sensor_temp = sensor_data.temperature_f
		rolling_average_temp = self.get_rolling_avg_temp(sensor_name)
		print("Processing         : Writing Record to Database...")
		print("The Rolling Average: {}".format(rolling_average_temp))
		print("The Sensor Temp    : {}".format(sensor_temp))

		if rolling_average_temp == False:
			return True

		difference = abs((sensor_temp - rolling_average_temp))
		print("The Difference     : {}".format(difference))
		if difference > 10:
			return False
		else:
			return True

	def get_rolling_avg_temp(self, sensor_name):
		print("Rolling Avg Temperature From: ", sensor_name)

		data = self.data_base.get_last_recs_time(5, sensor_name)
		
		count = 0
		t_sum = 0

		for record in data:
			if record.sensor == sensor_name:
				count = count + 1
				t_sum = t_sum + record.temperature

		if count == 0:
			return False
		else:
			rolling_average = t_sum / count
			return rolling_average



    # Untested
    
	def get_rolling_avg_humid(self, sensor_name):
		print("Rolling Avg Humidity From: ", sensor_name)

#end class Ds_App

