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
from Data_Stats.Db_Models import Reading

class Ds_Manager:
    def __init__(self, config=None):
        if config:
            database_temp = config.database_loc
        else:
            print("Config Unavailable")

        self.database_loc = "sqlite://{}".format(database_temp)
        self.engine = create_engine(self.database_loc, echo=True) #db address
        self.base = declarative_base()
        self.session = sessionmaker(bind=self.engine)
        self.meta = MetaData()


class Ds_Sensor(Ds_Manager):
    def __init__(self, config=None):
        super().__init__(config)

    def write_to_sensor_table(self, reading):
        print("Writing to Database...")
        print(reading.time_stamp)
        print(reading.sensor)
        print(reading.temperature)
        print(reading.humidity)
        # now actually write to databae

if __name__ == '__main__':
    print("Starting File: ", __file__)
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