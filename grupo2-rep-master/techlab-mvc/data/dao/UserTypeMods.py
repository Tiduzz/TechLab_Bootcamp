# responsavel pela criacao de "tipos de usuarios", modificacao e exclusao/dao=data acess object
from data.database import session_factory
from data.models.UserType import UserType

def CreateUserType(name, description, autorization0, autorization1, autorization2, autorization3, autorization4, autorization5, autorization6, autorization7, autorization8, autorization9):
    session = session_factory()
    user = UserType(name, description, autorization0, autorization1, autorization2, autorization3, autorization4, autorization5, autorization6, autorization7, autorization8, autorization9)
    session.add(user)
    session.commit()
    session.close()

def GetUserTypeById(id): 
    session = session_factory()
    user = session.query(UserType).filter(UserType.id == id).first()
    session.close()
    return user

def GetUserTypeByName(name): 
    session = session_factory()
    user = session.query(UserType).filter(UserType.name == name).first()
    session.close()
    return user

def UpdateUserType(id, name, description, autorization0, autorization1, autorization2, autorization3, autorization4, autorization5, autorization6, autorization7, autorization8, autorization9):
    session = session_factory()
    user = session.query(UserType).filter(UserType.id == id).first()
    user.set_valor(name)
    user.set_valor(description)
    user.set_valor(autorization0)
    user.set_valor(autorization1)
    user.set_valor(autorization2)
    user.set_valor(autorization3)
    user.set_valor(autorization4)
    user.set_valor(autorization5)
    user.set_valor(autorization6)
    user.set_valor(autorization7)
    user.set_valor(autorization8)
    user.set_valor(autorization9)
    session.add(user)
    session.commit()
    session.close()
    return user

def DeleteUserType(Id):
    session = session_factory()
    user = session.query(UserType).filter(UserType.id == Id).first()
    session.delete(user)
    session.commit()
    session.close()
