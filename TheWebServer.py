###############################################################################
# File Name  : TheWebServer.py
# Author     : John
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import Flask, render_template
import datetime
import Max6675K
import DHT11
import Songle

app = Flask(__name__)

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
def getTemperature():

    Max6675K.init_tempSensor(0,0)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    #timeString = Max6675K.hello()
    temp = Max6675K.getTemp()
    humidity = DHT11.get_humidity(11, 17)
    
    
    templateData = {
      'title' : 'Temperature: ',
      'time': timeString,
      'temp' : temp,
      'hum' : humidity
      }
      
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')