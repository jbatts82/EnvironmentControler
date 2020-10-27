

###############################################################################
# File Name  : Ds_Handler.py
# Date       : 10/27/2020
# Description: Database functions
###############################################################################


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///memory:', echo=True) #db address

Base = declarative_base()

Session = sessionmaker(bind=engine)




class Reading(Base):
    __tablename__ = 'Readings'
    #index = Column('id', Integer, primary_key=True)
    #timestamp = Column('Timestamp', DateTime)
    time_stamp = Column(DateTime, primary_key=True, index=True, default=datetime.utcnow)
    value = Column('Value', Float)


if __name__ == '__main__':
    print("Starting File: ", __file__)
    reading = Reading(time_stamp=datetime.now(), value=3)
    print(datetime.now())
    print(reading.time_stamp)