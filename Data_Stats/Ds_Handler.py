###############################################################################
# File Name  : Ds_Handler.py
# Date       : 10/27/2020
# Description: Database functions
###############################################################################

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from datetime import datetime



base = declarative_base()

class Reading(base):
    __tablename__ = 'Readings'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    sensor = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)
    humidity = Column('Humidity', Float)


class Ds_Manager:
    def __init__(self, config=None):
        if config:
            database_temp = config.database_loc
            database_loc = "sqlite://{}".format(database_temp)
        else:
            print("Config Unavailable")
            database_loc = None
        self.engine = create_engine(database_loc, echo=False) #db address
        base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)
        self.the_session = self.session()

        self.meta = MetaData()
        if not self.engine.dialect.has_table(self.engine, Reading.__tablename__): #if table doesn't exist
            self.meta.create_all(self.engine)


class Ds_Sensor(Ds_Manager):
    def __init__(self, config=None):
        super().__init__(config)

    def insert_record(self, reading):
        print("Writing to Database...")
        self.the_session.add(reading) #adds a model to database
        self.the_session.commit()
        
    def get_last_sensor_rec(self):
        query = self.the_session.query(Reading).first()
        print(query.time_stamp)
        return query

    def get_last_sensor_rec_from(self, time):
        pass

    def get_table(self):
        query = self.the_session.query(Reading).all()
        return query

    def dump_table(self, query):
        print("Dumping Table") 
        for each in query:
            print(each.humidity)
            print(each.time_stamp)
            print(each.sensor)
            print(each.temperature)
            print(each.humidity)

if __name__ == '__main__':
    print("Starting File: ", __file__)


    db_sensor = Ds_Sensor()






    #if not engine.dialect.has_table(engine, Reading.__tablename__): #if table doesn't exist
    # meta.create_all(engine)
    # reading = Reading(time_stamp=datetime.now(), sensor='upper_sensor',temperature=78.5, humidity=51.2)
    # print(Reading.__table__)
    # print(reading.time_stamp)
    # print(reading.sensor)
    # print(reading.temperature)
    # print(reading.humidity)
    # session = Session()
    # session.add(reading) #adds a model to database
    # session.commit()
    # print("query")
    # query = session.query(Reading).all()
    ##users = User.query.filter(username='todd').all()
    # session.close()
    # for Reading in query:
    # 	print(Reading.time_stamp)
    # 	print(Reading.sensor)
    # 	print(Reading.temperature)
    # 	print(Reading.humidity)
    print("Later World")