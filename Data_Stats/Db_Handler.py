###############################################################################
# File Name  : Db_Handler.py
# Date       : 08/14/2020
# Description: Database functions
###############################################################################

import sqlite3
from sqlite3 import Error
import random
from config import Config

class DB_Manager:
    def __init__(self, config=None):
        self.connection   = None
        self.cursor       = None
        if config:
            if config.database_location_og:
                self.open(config.database_location_og)
        else:
            print("Config Unavailable")
                
    def open(self, database):
        try:
            self.connection = sqlite3.connect(database, check_same_thread=False)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database!")
    
    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def print_table(self, table):
        try:
            cmd = '''SELECT * FROM {}'''.format(table)
            result = self.cursor.execute(cmd)
        except sqlite3.Error as e:
            print('Error Printing Table')
        else:
            all_rows = result.fetchall()
            for row in all_rows:
                print(row)
    
    def create_table(self, table_name):
        try:
            cmd = "CREATE TABLE IF NOT EXISTS {}(time_stamp DATETIME PRIMARY KEY, temp_f NUMERIC, humidity NUMERIC);".format(table_name)
            self.cursor.execute(cmd)
        except sqlite3.Error as e:
            print('Error creating table.')
    
    def get_row(self, table, columns, limit=None):
        cmd = "SELECT {0} FROM {1};".format(columns, table)
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        return rows[len(rows) - limit if limit else 0:]
    
    def get_last_row(self, table, columns):
        return self.get_row(table, columns, limit = 1)[0]
           
    def write(self, table, columns, data):
        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table, columns, data)
        self.cursor.execute(query)

    def query(self,sql):
        self.cursor.execute(sql)

    @staticmethod
    def toCSV(data,fname="output.csv"):
        with open(fname,'a') as file:
            file.write(",".join([str(j) for i in data for j in i]))
            
    def __del__(self): 
        self.close()

class DB_Sensor(DB_Manager):
    def __init__(self, config=None, sensor_num=None):
        super().__init__(config)
        self.sensor_table = config.sensor_configs[sensor_num]["name"] + "_table"
        self.create_table(self.sensor_table)
        self.humidity = 0
        self.temperature = 0
        self.time = 0
        
    def write_sensor_data(self, time_stamp, temp_f, humidity):
        try:
            cmd = '''INSERT INTO {}(time_stamp, temp_f, humidity) VALUES (:time_stamp_t, :temp_f_r, :humidity_r)'''.format(self.sensor_table)
            val_dic = {'time_stamp_t':time_stamp, 'temp_f_r':temp_f, 'humidity_r':humidity}
            self.cursor.execute(cmd, val_dic)
            self.connection.commit()
        except sqlite3.Error as e:
            print('Error writing sensor data.')
        else:
            print('Data Wrote to Table {}'.format(time_stamp))
            
    def get_last_humidity(self):
        return self.humidity 
        
    def get_last_time(self):
        return self.time
        
    def get_last_temperature(self):
        return self.temperature
        
    def update_to_last_record(self):
        row = self.get_last_row(self.sensor_table, "*")
        self.time = row[0]
        self.temperature = row[1]
        self.humidity = row[2]
     