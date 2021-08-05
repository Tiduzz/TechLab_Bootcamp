from sqlalchemy import Column, String, Integer, ForeignKey
from data.database import Base
from data.models.UserType import UserType
from data.models.NotificationSetting import NotificationSetting

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True) #id gerado automaticamente
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    id_user_type = Column(Integer, ForeignKey('tipos de usuarios.id'), unique=False)
    id_notification_setting = Column(Integer, ForeignKey('configuracoes dos usuarios.id'), unique=False)#mudar para True

    def __init__(self, name, email, password, id_user_type, id_notification_setting ):
        self.name = name
        self.email = email
        self.password = password
        self.id_user_type = id_user_type
        self.id_notification_setting = id_notification_setting
    

    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)
        
        return fields