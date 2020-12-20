###############################################################################
# File Name  : forms.py
# Date       : 08/24/2020
# Description: Fields are defined as class variables. 
###############################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


class GraphConfig(FlaskForm):
	sensor_name = SelectField(u'Sensor Name', choices=[('upper_sensor', 'Sensor 1'), ('lower_sensor', 'Sensor 2')])
	time = IntegerField('Begin Graph X Mins Ago')
	submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')