###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import random
import numpy as np


from WebApp import forms
from WebApp import app
from Data_Stats.DataApp import Ds_App
from WebApp import Config


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    _user = {'username': 'John'}
    _title = 'RPiii Environment Controller'
    _posts = [
        {
            'author': {'username': 'John'},
            'body': 'Hello me, Its me again'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'A credit to dementia'
        }
    ]
    config = Config()
    data_app = Ds_App(config)


    sensor_name = "upper_sensor"
    previous_minutes_back = 60

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        sensor_name = graphConfig.sensor_name.data
        print("Sensor Choice: {}".format(sensor_name))
        print("The Minutes Back: {}".format(minutes))
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
    plot_png()

    last_rec = readings[-1]
    _data = [last_rec.temperature, last_rec.humidity, last_rec.time_stamp, last_rec.sensor]

    return render_template('index.html', title=_title, user=_user, posts=_posts, data=_data, form=graphConfig)


@app.route('/plot.png')
def plot_png():
    fig = create_figure(time_arr, temp_arr)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(x_input, y_input):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = x_input
    ys = y_input
    axis.plot(xs, ys)
    return fig