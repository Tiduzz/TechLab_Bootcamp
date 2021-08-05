from sqlalchemy import Column, String, Integer
from data.database import Base


class Room(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True) 
    name = Column(String(255), unique=True)
    area = Column(Integer) 

    def __init__(self,name,area):
        self.name = name
        self.area = area
    
    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)

        return fields