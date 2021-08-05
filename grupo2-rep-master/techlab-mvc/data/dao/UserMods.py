# responsavel pela criacao de "usuarios", modificacao e exclusao/dao=data acess object
from data.database import session_factory
from data.models.User import User

def CreateUser(name, email, password, id_user_type, id_notification_setting):#criar a parte de usuarios  /user_type_id
    session = session_factory()
    user = User(name, email, password, id_user_type, id_notification_setting)
    session.add(user)
    session.commit()
    session.close()

def GetUser(id): 
    session = session_factory()
    user = session.query(User).filter(User.id == id).first()
    session.close()
    return user

def UpdateUser(id, name, email, password, id_user_type):
    session = session_factory()
    user = session.query(User).filter(User.id == id).first()
    user.set_valor(name)
    user.set_valor(email)
    user.set_valor(password)
    user.set_valor(id_user_type)
    session.add(user)
    session.commit()
    session.close()
    return user

def DeleteUser(Id):
    session = session_factory()
    user = session.query(User).filter(User.id == Id).first()
    session.delete(user)
    session.commit()
    session.close()
