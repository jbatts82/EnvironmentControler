###############################################################################
# File Name  : myConfig.py
# Date       : 08/24/2020
# Description: configuration 
###############################################################################

import os
import os.path
from os import path
from configparser import ConfigParser

file = 'config.txt'

default_config = {
    "fan_overide": False,
    "max_temp_thresh" : 83,
    "max_humidity_thresh" : 59
}

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    
# Example .ini file layout
# [main]
# key1 = value1
# key2 = value2
# key3 = value3
def create_config_file():
    config = ConfigParser()
    config.read('config.ini')
    config.add_section('main')
    config.set('main', 'key1', 'value1')
    config.set('main', 'key2', 'value2')
    config.set('main', 'key3', 'value3')
    with open('config.ini', 'w') as f:
        config.write(f)


def read_config_file():
    config = ConfigParser()
    config.read('config.ini')
    print(config.get('main', 'key1')) # -> "value1"
    print(config.get('main', 'key2')) # -> "value2"
    print(config.get('main', 'key3')) # -> "value3"
    # getfloat() raises an exception if the value is not a float
    a_float = config.getfloat('main', 'a_float')

    # getint() and getboolean() also do this for their respective types
    an_int = config.getint('main', 'an_int')


def init_config():
    global config, file
    print("Processing        : Config file")
    if path.exists(file):
        config = fh.get_from_file(file)
    else:
        config = fh.create_file(file)
        config_vals = default_config.values()
        fh.save_to_file(config_vals, file)
    print("Success Processing: Config file")
    
def get_config_dict():
    global config
    update_config()
    config_dict = {}
    config_dict["fan_overide"] = config[0]
    config_dict["max_temp_thresh"] = config[1]
    config_dict["max_humidity_thresh"] = config[2]
    return config_dict
    
def update_config():
    global config
    config = fh.get_from_file(file)

def config_test():
    print(__file__, "config test")
    init_config()
    print("The Config: ", config)
    adict = get_config_dict()
    print("a dictionary 1: ", adict)
    input("Change Config")
    adict = get_config_dict()
    print("a dictionary 2: ", adict)

if __name__ == "__main__":
    config_test()