###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for
from WebApp import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'John'}
    _title = '**RPiii Environment Controller!***'
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