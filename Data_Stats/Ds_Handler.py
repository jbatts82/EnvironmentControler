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




###############################################################################
class Ds_Manager:
    def __init__(self, config=None):
        if config:
            database_temp = config.database_loc
            database_loc = "sqlite://{}".format(database_temp)
        else:
            print("Config Unavailable")
            database_loc = None
        self.engine = create_engine(database_loc, echo=False) #db address
        print("Connected to       :", database_loc)
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
        print("Processing         : Writing Record to Database...")
        self.the_session.add(reading)
        self.the_session.commit()
        print("Success            : Write Complete")
        
    def get_last_sensor_rec(self):
        query = self.the_session.query(Reading).order_by(Reading.time_stamp.desc())
        last_record = query.first()
        return last_record

    def get_last_sensor_rec_from(self, sensor_name):
        query = self.the_session.query(Reading).filter(Reading.sensor == sensor_name).order_by(Reading.time_stamp.desc()).all()
        last_record = query[0]
        return last_record

    def get_table(self):
        query = self.the_session.query(Reading).all()
        return query

    def view_query_dict(self, a_query):
        print("Printing Each Record Dictionary")
        for each_record in a_query:
            print(each_record.__dict__)

    def dump_table(self, query):
        print("Dumping Table") 
        for each in query:
            print("Humidity:", each.humidity)
            print("Time: ", each.time_stamp)
            print("Sensor: ", each.sensor)
            print("Temperature: ", each.temperature)
            print("Humidity: ", each.humidity)

    def get_recs_from_time(mins):
        query = self.the_session.query(Reading)
        

    # Untested

# end class Ds_Sensor(Ds_Manager):
###############################################################################




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

'''
Example SQL ALchemy

# sql where equilavent example
# in Customer where first name == Carl
records = session.query(Customer).filter(Customer.first_name == 'Carl').all()

# gets all records with first name starting with J
records = session.query(Customer).filter(Customer.first_name.like('J%')).all()







'''