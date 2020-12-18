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
    print("Hello MMMEEE")
    print("T!!!!!!!!he Request Method: {}".format(request.method))
    
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
    last_rec = data_app.get_last_sensor_reading()
    _data = [last_rec.temperature_f, last_rec.humidity, last_rec.time_data, last_rec.name]

    name_form = forms.NameForm()
    if name_form.validate_on_submit():
        name = name_form.name.data
        print("The Name is: {}".format(name))


    readings = data_app.get_previous_readings_time(60)
    global temp_arr, time_arr
    temp_arr = []
    time_arr = []
    for reading in readings:
        temp_arr.append(reading.temperature)
        time_arr.append(reading.time_stamp)
    plot_png()

    return render_template('index.html', title=_title, user=_user, posts=_posts, data=_data, form=name_form)


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