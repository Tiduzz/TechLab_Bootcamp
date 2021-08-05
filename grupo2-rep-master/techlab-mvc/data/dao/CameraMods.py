# responsavel pela criacao de "cameras", modificacao e exclusao/dao=data acess object
from data.database import session_factory
from data.models.Camera import Camera

def CreateCamera(name, idRoom):#criar a parte de cameras
    session = session_factory()
    camera = Camera(name, idRoom)
    session.add(camera)
    session.commit()
    session.close()

def GetCamera(id=None):#editar 
    session = session_factory()
    if id is not None:
        camera = session.query(Camera).filter(Camera.id == id).first()
    else:
        cameras = list()
        camera = session.query(Camera).all()
        for c in camera:
            cameras.append(c.to_json())
        camera = cameras 
    
    session.close()
    return camera

def UpdateCamera(id, name, idRoom):
    session = session_factory()
    camera = session.query(Camera).filter(Camera.id == id).first()
    camera.set_valor(name)
    camera.set_valor(idRoom)
    session.add(camera)
    session.commit()
    session.close()
    return camera

def DeleteCamera(id):
    session = session_factory()
    camera = session.query(Camera).filter(Camera.id == id).first()
    session.delete(camera)
    session.commit()
    session.close()
