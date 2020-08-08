###############################################################################
# File Name  : TheWebServer.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################


from flask import Flask, render_template
import datetime

app = Flask(__name__)
app.run(debug=True, host='0.0.0.0')

@app.route('/')
def index():
    timeString = 0
    temp_1 = 0
    humidity = 0
    templateData = {
      'title' : 'Temperature: ',
      'time': timeString,
      'temp_1' : temp_1,
      'hum' : humidity,
      }
      
    return render_template('index.html', **templateData)


