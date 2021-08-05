from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from data.database import Base
# from sqlalchemy.orm import relationship
# from data.models.User import User

class NotificationSetting(Base):
    __tablename__ = 'configuracoes dos usuarios'

    id = Column(Integer, primary_key=True) #id gerado automaticamente
    # User_id = Column(Integer, ForeignKey('usuarios.id'))           # daqui
    # user = relationship("User", back_populates="configurações dos usuarios")# ate aqui e a funcao one-to-one, aqui sendo filho
    # none = Column()
    confiuration0 = Column(Boolean())
    confiuration1 = Column(Boolean())
    confiuration2 = Column(Boolean())
    confiuration3 = Column(Boolean())
    confiuration4 = Column(Boolean())
    confiuration5 = Column(Boolean())
    confiuration6 = Column(Boolean())
    confiuration7 = Column(Boolean())
    confiuration8 = Column(Boolean())
    confiuration9 = Column(Boolean())

    # user_id,
    def __init__(self,  confiuration0, confiuration1, confiuration2, confiuration3, confiuration4, confiuration5, confiuration6, confiuration7, confiuration8, confiuration9):
        # self.user_id =user_id
        self.confiuration0
        self.confiuration1
        self.confiuration2
        self.confiuration3
        self.confiuration4
        self.confiuration5
        self.confiuration6
        self.confiuration7
        self.confiuration8
        self.confiuration9
          
    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)
        
        return fields