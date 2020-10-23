###############################################################################
# File Name  : myConfig.py
# Date       : 08/24/2020
# Description: configuration 
###############################################################################

import os
import os.path
from os import path
from configparser import ConfigParser
from SupportFiles import File_Handler as fh
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYT = 23
    CONFIG_FILE = '/home/mario/EnvironmentController/my_config.txt'
    db_name = 'readings.db'
    FAN_OVERRIDE = None
    MAX_TEMP_THRESH = 0
    MAX_HUMIDITY_THRESH = 0
    database_location_og = '/home/mario/EnvironmentController/readings.db'
    database_location = '/home/mario/EnvironmentController/more_readings.db'
    sensor_cnt = 2
    sensor_configs = [{"name":"upper_sensor", "data_pin":17, "assigned":False, "sensor_type":11}, {"name":"lower_sensor", "data_pin":26, "assigned":False, "sensor_type":11}]
    
    def __init__(self):
        self.init_file()

    def init_file(self):
        print("Processing         : Config file")
        if path.exists(self.CONFIG_FILE):
            self.config = fh.get_from_file(self.CONFIG_FILE)
        else:
            self.config = fh.create_file(self.CONFIG_FILE)
        print("Success Processing : Config file")
        
    def get_config_file(self):
        self.update_config()
        self.FAN_OVERRIDE = self.config[0]
        self.HUM_OVERRIDE = self.config[1]
        self.MAX_TEMP_THRESH = self.config[2]
        self.MIN_TEMP_THRESH = self.config[3]
        self.MAX_HUMIDITY_THRESH = self.config[4]
        self.MIN_HUMIDITY_THRESH = self.config[5]
        
    
    def update_config(self):
        self.config = fh.get_from_file(self.CONFIG_FILE)

    def get_from_file(self, in_file):
        # open file and put into list
        out_list = []
        with open(in_file, 'r') as filehandle:
            for line in filehandle:
                remove_new_line = line[:-1]
                out_list.append(remove_new_line)
        return out_list