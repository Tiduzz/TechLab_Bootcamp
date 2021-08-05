#importacao do sqlalchemy das funcoes a serem utilizadas
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#conecta essa parte com o mysql atraves do pimysql, usa o nome, senha e endereco
engine = create_engine('mysql+pymysql://root:12345678@172.17.0.1:50050/techlab')
#para criar secoes(novas partes no mysql)
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()

# necessario chamar os modelos aqui para poder inicialos no mysql
from data.models.Camera import Camera
from data.models.Room import Room
from data.models.Report import Report
from data.models.User import User
from data.models.UserType import UserType
from data.models.FaceRecognition import Frame
from data.models.NotificationSetting import NotificationSetting

#mais coisas do sqlalchemy
Base.metadata.create_all(engine)
#usado para chamar o _SessionFactory corretamente 
def session_factory():
    return _SessionFactory()