###############################################################################
# Filename    : Humidity.py
# Date        : 07/25/2020 
# Description :
###############################################################################

temperature_c_list = []
temperature_c_file = 'temperature_log.txt'


def get_humidity_from_file():
    # open file and put into list
    global temperature_c_list, temperature_c_file
    with open(temperature_c_file, 'r') as filehandle:
        for line in filehandle:
            remove_new_line = line[:-1]
            temperature_c_list.append(remove_new_line)
        
def save_humidity_to_file():
    global temperature_c_list, temperature_c_file
    with open(temperature_c_file, 'w') as filehandle:
        filehandle.writelines("%s\n" % temp for temp in temperature_c_list)
        
def add_humidity_data_to_list(hum_data):
    global temperature_c_list
    temperature_c_list.append(hum_data)

def print_humidity():
    # read through the list
    global temperature_c_list
    print("Printing Humidity: ")
    for line in temperature_c_list:
        print(line)
        
def erase_humidity_file():
    global temperature_c_file
    file = open(temperature_c_file, 'w')
    file.close()
