import datetime
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Boolean
from data.models.Camera import Camera
# from data.models.Room import Room
from data.database import Base

class Report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=False)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    people_quantity = Column(Integer)
    distance_quantity = Column(Integer)
    no_mask_quantity = Column(Integer)
    id_cameras = Column(Integer, ForeignKey('cameras.id'))
    
    def __init__(self, name, send_date, people_quantity, distance_quantity, no_mask_quantity, id_cameras): # trecho de codigo a adicionar junto do restante da aplicacao: ,people_quantity, distance_quantity, no_mask_quantity 
        self.name = name
        self.send_date = send_date
        self.people_quantity = people_quantity
        self.distance_quantity = distance_quantity
        self.no_mask_quantity = no_mask_quantity
        self.id_cameras = id_cameras
    
    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)

        return fields