from sqlalchemy import create_engine
import os
from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, Text, Float
import datetime

engine = create_engine('mysql+pymysql://root:12345678@172.17.0.1:50050/techlab') 

def add_column(engine, frames, camera_id):
  column_name = column.compile(dialect=engine.dialect)
  column_type = column.type.compile(engine.dialect)
  engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (frames, column_name, column_type))
  
column = Column('send_date', DateTime)
send_date = Column(DateTime, default=datetime.datetime.utcnow)
add_column(engine, 'frames', send_date)

#column = Column('camera_id', Integer)
#camera_id = Column(Integer, default=None)
#add_column(engine, 'frames', camera_id)