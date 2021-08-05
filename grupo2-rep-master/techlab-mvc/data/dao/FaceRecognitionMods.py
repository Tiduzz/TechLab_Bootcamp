import sys
sys.path.append('/home/sigrid/Desktop/tecnoria/techlab-mvc')

from data.database import session_factory
from data.models.FaceRecognition import Frame, Face
from data.models.Room import Room
from data.models.Camera import Camera
from datetime import datetime

def create_frame(image, camera_id):
	session = session_factory()
	#send_date = datetime.now()
	new_frame = Frame(image, camera_id)
	
	session.add(new_frame)
	session.commit()
	print("Frame Salvo!")
	f_id = new_frame.id
	session.close()
	return f_id

def create_frame_face(face, has_mask, frame):
	session = session_factory()
	f = session.query(Frame).filter(Frame.id == frame).first()
	new_face = Face(face, has_mask, f)
	
	session.add(new_face)
	session.commit()
	print("Rosto Salvo!")
	session.close()
	return new_face

def get_frame(id):
	session = session_factory()
	frame = session.query(Frame).filter(Frame.id == id).first()
	session.close()
	return frame

def get_all_frames():
	session = session_factory()
	frames = session.query(Frame).all()
	session.close()
	return frames

def getUsersWithoutMask(id=None):
	session = session_factory()
	if id is not None:
			nomask = session.query(Face).filter(Face.id == id).first()
	else:
			nomasks = list()
			nomask = session.query(Face).filter(Face.has_mask == False).all()
			for m in nomask:
					nomasks.append(m.to_json())
			nomask = nomasks 
	
	session.close()
	return nomask

def getFramebyIdCamera():
	session = session_factory()
	faces = session.query(Face, Room).filter(
  Room.id == Camera.RoomId,
  Camera.id == Frame.camera_id,
  Face.frame_id == Frame.id
	).all()

	report = {}
	faces_total = {}

	for f,r in faces:
		if r.name in report:
			if f.has_mask == False:
					report[r.name] += 1
			faces_total[r.name] +=1
		else:
			if f.has_mask == False:
					report[r.name] = 1
			faces_total[r.name] = 1
	
	labels=list()
	series=list()

	for n in report:
		labels.append(n)
		#series.append(100*(report[n]/faces_total[n]))
		series.append(report[n])
	
	relatorio_final= {
		"labels": labels,
		"series": [series]
	}
		#report[n] = ('{}%'.format(100*(report[n]/faces_total[n])))
	#print(report)

	session.close()
	return relatorio_final
	
if __name__ == "__main__":
		faces = getFramebyIdCamera()
		print(faces)

def getUsersByRoom(id=None):
	session = session_factory()
	if id is not None:
			roomid = session.query(Camera.RoomId).filter(Camera.id == id).first()
			salaid = session.query(Room.name).filter(Room.id == roomid).first()
	else:
			salasid = list()
			salaid = session.query(Room.name).filter(Room.id and Face.has_mask == False).all()
			roomid = session.query(Camera.RoomId).filter(Camera.id).all()
	
	session.close()
	return salaid
	

def getUsersWithMask(id=None):
	session = session_factory()
	if id is not None:
			mask = session.query(Face).filter(Face.id == id).first()
	else:
			masks = list()
			mask = session.query(Face).filter(Face.has_mask == True).all()
			for m in mask:
					masks.append(m.to_json())
			mask = masks 
	
	session.close()
	return mask

def GetReportByDate(date):
    session = session_factory()
    reports = session.query(Frame).filter(Frame.date_time == date).workday().first()
    session.close()
    return reports

def GetReportByTime(time):
    session = session_factory()
    reports = session.query(Frame).filter(Frame.date_time == time).first()
    session.close()
    return reports

