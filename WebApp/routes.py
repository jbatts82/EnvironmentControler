###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

import io
import random

from WebApp import forms
from WebApp import app
from Data_Stats.DataApp import Ds_App
from WebApp import Config


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():

    config = Config()
    data_app = Ds_App(config)
    _title = 'RPiii Environment Controller'
    sensor_name = "plant1"
    previous_minutes_back = 60

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        sensor_name = graphConfig.sensor_name.data
        previous_minutes_back = minutes

    readings = data_app.get_previous_readings_time(previous_minutes_back, sensor_name)
    global temp_arr, time_arr, hum_arr
    temp_arr = []
    time_arr = []
    hum_arr = []
    for reading in readings:
        temp_arr.append(reading.temperature)
        hum_arr.append(reading.humidity)
        time_arr.append(reading.time_stamp)

    control_stats = data_app.get_previous_control_stats(previous_minutes_back)
    global control_time, heater_state, humidifier_state, fan_state, light_state
    control_time = []
    heater_state = []
    humidifier_state = []
    fan_state  = []
    light_state = []
    for control_stat in control_stats:
        control_time.append(control_stat.time_stamp)
        heater_state.append(control_stat.heater_state)
        humidifier_state.append(control_stat.humidifier_state)
        fan_state.append(control_stat.fan_state)
        light_state.append(control_stat.light_state)


    last_rec = readings[-1]
    _data = [last_rec.temperature, last_rec.humidity, last_rec.time_stamp, last_rec.sensor]

    return render_template('index.html', title=_title, data=_data, form=graphConfig)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure(figsize=(10,15))

    xs = time_arr
    ys = temp_arr
    axis = fig.add_subplot(6, 1, 1, xlabel='Time', ylabel='Temperature')
    axis.plot(xs, ys)

    ys = hum_arr
    axis = fig.add_subplot(6, 1, 2, xlabel='Time', ylabel='Humidity')
    axis.plot(xs, ys)

    xs = control_time
    ys = heater_state
    axis = fig.add_subplot(6, 1, 3, xlabel='Control Time', ylabel='Heater State', yticks=(0,1))
    axis.plot(xs, ys)

    ys = humidifier_state
    axis = fig.add_subplot(6, 1, 4, xlabel='Control Time', ylabel='Humidifier State', yticks=(0,1))
    axis.plot(xs, ys)

    ys = fan_state
    axis = fig.add_subplot(6, 1, 5, xlabel='Control Time', ylabel='Fan State', yticks=(0,1))
    axis.plot(xs, ys)
    
    ys = light_state
    axis = fig.add_subplot(6, 1, 6, xlabel='Control Time', ylabel='Light State', yticks=(0,1))
    axis.plot(xs, ys)

    return fig