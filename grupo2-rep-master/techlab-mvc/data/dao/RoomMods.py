from data.database import session_factory
from data.models.Room import Room

def CreateRoom(name, area):
    session = session_factory()
    room = Room(name, area)
    session.add(room)
    session.commit()
    session.close()

def GetRoom(id=None):
    session = session_factory()
    if id is not None:
        room = session.query(Room).filter(Room.id == id).first()
    else:
        rooms = list()
        room = session.query(Room).all()
        for r in room:
            rooms.append(r.to_json())
        room = rooms

    session.close()
    return room

def UpdateRoom(id, name, area):
    session = session_factory()
    room = session.query(Room).filter(Room.id == id).first()
    room.set_valor(name)
    room.set_valor(area)
    session.add(room)
    session.commit()
    session.close()
    return room

def DeleteRoom(Id):
    session = session_factory()
    room = session.query(Room).filter(Room.id == Id).first()
    session.delete(room)
    session.commit()
    session.close()