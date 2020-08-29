###############################################################################
# File Name  : DB_Handler.py
# Date       : 08/14/2020
# Description: Database functions
###############################################################################


#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import random

class DB_Manager:
    def __init__(self, config, sensor_num):
        self.connection   = None
        self.cursor       = None
        self.sensor_table = None
        if config.database_location:
            self.open(config.database_location)
            if config.sensor_configs[sensor_num]["name"]:
                self.sensor_table = config.sensor_configs[sensor_num]["name"] + "_table"
                self.create_table(self.sensor_table)
    
    def print_table(self):
        try:
            cmd = '''SELECT * FROM {}'''.format(self.sensor_table)
            result = self.cursor.execute(cmd)
        except sqlite3.Error as e:
            print('Error Printing Table')
        else:
            all_rows = result.fetchall()
            for row in all_rows:
                print(row)
    
    def write_sensor_data(self, time_stamp, temp_f, humidity):
        try:
            cmd = '''INSERT INTO {}(time_stamp, temp_f, humidity) VALUES (:time_stamp_t, :temp_f_r, :humidity_r)'''.format(self.sensor_table)
            val_dic = {'time_stamp_t':time_stamp, 'temp_f_r':temp_f, 'humidity_r':humidity}
            self.cursor.execute(cmd, val_dic)
            self.connection.commit()
        except sqlite3.Error as e:
            print('Error writing sensor data.')
        else:
            print('Data Wrote to Table')
    
    def create_table(self, table_name):
        try:
            cmd = "CREATE TABLE IF NOT EXISTS {}(time_stamp DATETIME PRIMARY KEY, temp_f NUMERIC, humidity NUMERIC);".format(table_name)
            self.cursor.execute(cmd)
        except sqlite3.Error as e:
            print('Error creating table.')
        else:
            print(table_name, 'table available.')
    
    def open(self, database):
        try:
            self.connection = sqlite3.connect(database, check_same_thread=False)
            self.cursor = self.connection.cursor()
            print(database, " Opened")
        except sqlite3.Error as e:
            print("Error connecting to database!")
    
    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            print("Database Closed")
    
    def get_row(self, table, columns, limit=None):
        cmd = "SELECT {0} FROM {1};".format(columns, table)
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        return rows[len(rows) - limit if limit else 0:]
    
    def get_last_row(self, columns):
        return self.get_row(self.sensor_table, columns, limit = 1)[0]
           
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

    
def db_test():
    print(__file__, ": Testing")

    sensor1_db = DB_Manager(database_location, sensor1_name)
    sensor2_db = DB_Manager(database_location, sensor2_name)
    print("print table 1")
    sensor1_db.print_table()
    print("print table 2")
    sensor2_db.print_table()
    print(sensor1_db.get_last_row("*"))
    
if __name__ == '__main__':
    db_test() 
    
    
    
    
    
