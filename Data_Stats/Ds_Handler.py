###############################################################################
# File Name  : Ds_Handler.py
# Date       : 10/27/2020
# Description: Database functions
###############################################################################

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from datetime import datetime


class Reading:
    __tablename__ = 'Readings'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    sensor = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)
    humidity = Column('Humidity', Float)


class Ds_Database_Manager:
    def __init__(self, config=None):
		self.engine = create_engine('sqlite:///db_test.db', echo=True) #db address
		self.base = declarative_base()
		self.session = sessionmaker(bind=engine)
		self.meta = MetaData()
        if config:
            if config.database_location:
                self.open(config.database_location)
        else:
            print("Config Unavailable")

    #def get_last_row

# class Ds_Sensor_Db(Ds_Database_Manager):
# 		def __init__(self, config=None, sensor_num=None):
#         	super().__init__(config)



if __name__ == '__main__':
    print("Starting File: ", __file__)

    database_manageer = Ds_Database_Manager()

 

    #if not engine.dialect.has_table(engine, Reading.__tablename__): #if table doesn't exist
    # meta.create_all(engine)

    # reading = Reading(time_stamp=datetime.now(), sensor='upper_sensor',temperature=78.5, humidity=51.2)

    # print(Reading.__table__)

    # print(reading.time_stamp)
    # print(reading.sensor)
    # print(reading.temperature)
    # print(reading.humidity)


    # session = Session()
    # session.add(reading)
    # session.commit()
    # print("query")
    # query = session.query(Reading).all()
    
    # for Reading in query:
    # 	print(Reading.time_stamp)
    # 	print(Reading.sensor)
    # 	print(Reading.temperature)
    # 	print(Reading.humidity)


    print("Later World")