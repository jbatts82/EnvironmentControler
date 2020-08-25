###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for
from WebApp import app
from WebApp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'John'}
    _title = '**RPi Environment Controller!***'
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Hello me, Its me again'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'A credit to dementia'
        }
    ]
    return render_template('index.html', title=_title, user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)