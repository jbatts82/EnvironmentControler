###############################################################################
# File Name  : TheWebServer.py
# Author     : John
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################


#!/usr/local/bin/python3


from flask import Flask, render_template
import datetime
import Max6675K
import DHT11
import Songle

app = Flask(__name__)

max_temp = 0
max_hum = 0



@app.route("/hello")
def hello():
    return "Hello, World!"
 
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/relay1on')
def relay1on():
    print("relay1on")
    Songle.relay1_on()
    return render_template('index.html')

@app.route('/')
def index():

    Max6675K.init_tempSensor(0,0)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    temp_1 = Max6675K.getTemp()
    humidity = DHT11.get_humidity(11, 17)
    
    update_max_temp(temp_1)
    update_max_hum(humidity)
    
    templateData = {
      'title' : 'Temperature: ',
      'time': timeString,
      'temp_1' : temp_1,
      'hum' : humidity,
      'temp_max' : max_temp,
      'hum_max' : max_hum
      }
      
    return render_template('index.html', **templateData)

def update_max_temp(temp):
    global max_temp
    print(max_temp)
    if float(temp) > float(max_temp):
        max_temp = temp

def update_max_hum(hum):
    global max_hum
    print(max_hum)
    if float(hum) > max_hum:
        max_hum = hum   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
