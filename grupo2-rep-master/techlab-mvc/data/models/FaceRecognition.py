from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from data.database import Base
import datetime

class Frame(Base):
	__tablename__= "frames"
	id = Column(Integer, primary_key = True)
	image = Column(Text(4294967295))
	camera_id = Column(Integer, ForeignKey('cameras.id'))
	camera = relationship("Camera", backref = backref("camera", uselist=False))
	send_date = Column(DateTime, default=datetime.datetime.utcnow)

	def __init__(self, image, camera_id):
			self.image = image
			self.camera_id = camera_id

	
	def to_json(self):
			fields = dict()
			for column in self.__table__.columns:
					fields[column.name] = getattr(self, column.name)
	
			return fields

class Face(Base):
	__tablename__= "faces"
	id = Column(Integer, primary_key = True)
	image = Column(Text(4294967295))
	has_mask = Column(Boolean, default = False)
	frame_id = Column(Integer, ForeignKey('frames.id'))
	frame = relationship("Frame", backref = backref("face", uselist=False))
	
	def __init__(self, image, has_mask, frame):
			self.image = image
			self.has_mask = has_mask
			self.frame = frame
			
	def to_json(self):
			fields = dict()
			for column in self.__table__.columns:
					fields[column.name] = getattr(self, column.name)
	
			return fields
