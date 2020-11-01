###############################################################################
# File Name  : Db_Models.py
# Date       : 10/11/2020
# Description: Database models which implement sql schema
###############################################################################

from datetime import datetime

from SupportFiles.Shared import Table, Column, Integer, String, DateTime, Float

class Reading:
    __tablename__ = 'Readings'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    sensor = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)
    humidity = Column('Humidity', Float)





