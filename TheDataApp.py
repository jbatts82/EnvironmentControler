###############################################################################
# File Name  : TheDataApp.py
# Date       : 10/30/2020
# Description: 
###############################################################################


from Data_Stats import DataApp





if __name__ == '__main__':
	print("Starting          :  ", __file__)
	DataApp.write_sensor_data()


	# sensor_data1 = DHT11_Data()
	# sensor_data1.name = "sensor1"
	# sensor_data1.time_data = datetime.now()
	# sensor_data1.humidity = float("{0:.2f}".format(random.uniform(0, 100)))
	# sensor_data1.temperature_f = float("{0:.2f}".format(random.uniform(32, 120)))
	# sensor_data1.print_data()
