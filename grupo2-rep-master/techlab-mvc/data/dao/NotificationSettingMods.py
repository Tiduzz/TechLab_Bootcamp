# responsavel pela criacao de "tipos de usuarios", modificacao e exclusao/dao=data acess object
from data.database import session_factory
from data.models.NotificationSetting import NotificationSetting

def CreateNotificationsSetting(confiuration0, confiuration1, confiuration2, confiuration3, confiuration4, confiuration5, confiuration6, confiuration7, confiuration8, confiuration9):
    session = session_factory()
    notification = NotificationSetting(confiuration0, confiuration1, confiuration2, confiuration3, confiuration4, confiuration5, confiuration6, confiuration7, confiuration8, confiuration9)
    session.add(notification)
    session.commit()
    session.close()

def GetNotificationsSetting(id): 
    session = session_factory()
    notification = session.query(NotificationSetting).filter(NotificationSetting.id == id).first()
    session.close()
    return notification


def UpdateNotificationsSetting(id, confiuration0, confiuration1, confiuration2, confiuration3, confiuration4, confiuration5, confiuration6, confiuration7, confiuration8, confiuration9):
    session = session_factory()
    notification = session.query(NotificationSetting).filter(NotificationSetting.id == id).first()
    notification.set_valor(confiuration0)    
    notification.set_valor(confiuration1)    
    notification.set_valor(confiuration2)    
    notification.set_valor(confiuration3)    
    notification.set_valor(confiuration4)    
    notification.set_valor(confiuration5)    
    notification.set_valor(confiuration6)    
    notification.set_valor(confiuration7)    
    notification.set_valor(confiuration8)
    notification.set_valor(confiuration9)        
    session.add(notification)
    session.commit()
    session.close()
    return user

def DeleteNotificationsSetting(Id):
    session = session_factory()
    notification = session.query(NotificationSetting).filter(NotificationSetting.id == Id).first()
    session.delete(notification)
    session.commit()
    session.close()
