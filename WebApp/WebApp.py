###############################################################################
# File Name  : TheWebServer.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

import datetime
import sys
sys.path.append('/home/mario/EnvironmentController/SupportFiles/')
from DB_Handler import DB_Manager
sys.path.append('/home/mario/EnvironmentController/Sensor/')
#import DHT11
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #last_row = sensor1_db.get_last_row('*')
    timeString = 1 #last_row[0]
    temp_1 = 2 #last_row[1]
    humidity = 3 #last_row[2]
    templateData = {
      'title' : 'Temperature: ',
      'time': timeString,
      'temp_1' : temp_1,
      'hum' : humidity,
    }
      
    return render_template('index.html', **templateData)



if __name__ == '__main__':
    print("Starting File: ", __file__)
    #sensor1_name = DHT11.sensor1_config['name']
    #sensor2_name = DHT11.sensor2_config['name']
    #sensor1_db = DB_Manager(database_location, sensor1_name)
    #sensor2_db = DB_Manager(database_location, sensor2_name)
    #print(sensor1_db.get_last_row("*"))
    app.run(debug=True, host='0.0.0.0')
    
    
    
    
    