from sqlalchemy import Column, String, Integer, ForeignKey
from data.database import Base
from data.models.Room import Room


class Camera(Base):
    __tablename__ = 'cameras'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    RoomId = Column(Integer, ForeignKey('salas.id'), unique=False)
    #StreamUrl = Column(String(255), unique=True)

    def __init__(self, name, RoomId):
        self.name = name
        self.RoomId = RoomId
        #self.StreamUrl = StreamUr

    def set_valor(self, RoomId):
        self.RoomId = RoomId
    
    def to_json(self):# converta para json
        fields = dict()
        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)        
        return fields