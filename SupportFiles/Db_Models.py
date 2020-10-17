###############################################################################
# File Name  : Db_Models.py
# Date       : 10/11/2020
# Description: Database models which implement sql schema
###############################################################################

from datetime import datetime
#from WebApp import db






# class Sensor(db.Model):
    # __tablename__ = 'Sensors'
    # index = db.Column('id', db.Integer, primary_key=True)
    # id = db.Column('SensorID', db.Integer, unique=True)
    # type = db.Column('SensorType', db.Integer)
    # location = db.Column('Location', db.String(50))
    # readings = db.relationship('Reading',  backref='SensorID', lazy='dynamic')

# class Reading(db.Model):
    # __tablename__ = 'Readings'
    # index = db.Column('id', db.Integer, primary_key=True)
    # sensor_id = db.Column('SensorID', db.Integer, db.ForeignKey('Sensors.SensorID'))
    # sensor_type = db.Column('SensorType', db.Integer)
    # timestamp = db.Column('Timestamp', db.DateTime)
    # value_type = db.Column('ValueType', db.Integer)
    # value = db.Column('Value', db.Float)

