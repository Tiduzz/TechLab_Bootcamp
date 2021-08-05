from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from data.database import Base
from sqlalchemy.orm import relationship


class UserType(Base):
    __tablename__ = 'tipos de usuarios'

    id = Column(Integer, primary_key=True) #id gerado automaticamente
    name = Column(String(255), unique=True)
    description = Column(String(255))
    autorization0 = Column(Boolean())#editar as autorizacoes para as funcoes construidas no codigo
    autorization1 = Column(Boolean())
    autorization2 = Column(Boolean())
    autorization3 = Column(Boolean())
    autorization4 = Column(Boolean())
    autorization5 = Column(Boolean())
    autorization6 = Column(Boolean())
    autorization7 = Column(Boolean())
    autorization8 = Column(Boolean())
    autorization9 = Column(Boolean())

    def __init__(self, name, description, autorization0, autorization1, autorization2, autorization3, autorization4, autorization5, autorization6, autorization7, autorization8, autorization9):
        self.name = name
        self.description = description
        self.autorization0 = autorization0
        self.autorization1 = autorization1
        self.autorization2 = autorization2
        self.autorization3 = autorization3
        self.autorization4 = autorization4
        self.autorization5 = autorization5
        self.autorization6 = autorization6
        self.autorization7 = autorization7
        self.autorization8 = autorization8
        self.autorization9 = autorization9
    

    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)
        
        return fields