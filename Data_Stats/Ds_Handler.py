

###############################################################################
# File Name  : Ds_Handler.py
# Date       : 10/27/2020
# Description: Database functions
###############################################################################


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///db_test.db', echo=True) #db address

Base = declarative_base()

Session = sessionmaker(bind=engine)

meta = MetaData()

Readings = Table(
	'Readings', meta,
    Column('TimeDate', DateTime, primary_key=True, index=True),
    Column('Sensor', String(20)),
    Column('Temperature', Float),
    Column('Humidity', Float),
)


class Reading(Base):
    __tablename__ = 'Readings'
    #index = Column('id', Integer, primary_key=True)
    #timestamp = Column('Timestamp', DateTime)
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    sensor = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)
    humidity = Column('Humidity', Float)



if __name__ == '__main__':
    print("Starting File: ", __file__)


    #if not engine.dialect.has_table(engine, Reading.__tablename__): #if table doesn't exist
    meta.create_all(engine)

    reading = Reading(time_stamp=datetime.now(), sensor='upper_sensor',temperature=78.5, humidity=51.2)

    print(Reading.__table__)

    print(reading.time_stamp)
    print(reading.sensor)
    print(reading.temperature)
    print(reading.humidity)


    session = Session()
    session.add(reading)
    session.commit()
    print("query")
    query = session.query(Reading).all()
    
    for Reading in query:
    	print(Reading.time_stamp)
    	print(Reading.sensor)
    	print(Reading.temperature)
    	print(Reading.humidity)


    print("Later World")