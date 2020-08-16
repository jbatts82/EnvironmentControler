###############################################################################
# File Name  : Config.py
# Date       : 08/15/2020
# Description: System Configuration Parameters
###############################################################################


import File_Handler as fh
import os.path
from os import path

file = 'config.txt'

default_config = {
    "fan_overide": False,
    "max_temp_thresh" : 83,
    "max_humidity_thresh" : 59
}


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