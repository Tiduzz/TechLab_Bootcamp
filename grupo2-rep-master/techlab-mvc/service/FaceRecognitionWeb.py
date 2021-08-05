#import sys
#sys.path.append('/home/sigrid/Desktop/grupo2-rep/techlab-mvc')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
from data.dao.FaceRecognitionMods import get_frame, get_all_frames, getUsersWithoutMask, getUsersByRoom, getUsersWithMask, getFramebyIdCamera
#from application.face_recognition import face_detect


class AllFramesAPI(RequestHandler):
	def set_default_headers(self):
		print("setting headres")
		#self.set_header("Acess-Control_Allow_Origin", "*")
		origin = self.request.headers.get('Origin')
		if origin:
			self.set_header('Access-Control-Allow-Origin', origin)

		self.set_header("Acess-Control_Allow_Headers", "x-requested-with")
		self.set_header("Acess-Control_Allow_Origin", 'POST, GET, OPTIONS')
		
	def get(self):
		frames = get_all_frames()
		data = []
		for i in range(len(frames)):
			f= {
				"id": frames[i].id, 
				"image": frames[i].image
			}
			data.append(f)
		
		self.write({"frame": data})


class OneFrameAPI(RequestHandler):
	def set_default_headers(self):
		print("setting headers")
		self.set_header("Acess-Control_Allow_Origin", "*")
		self.set_header("Acess-Control_Allow_Headers", "x-requested-with")
		self.set_header("Acess-Control_Allow_Origin", 'POST, GET, OPTIONS')
		
	def get(self, id):
		res = get_frame(id)
		frame = {
			"id": res.id,
			"frame": res.image
		}
		self.write({"frame": frame})

class AllFramesFaceNoMaskAPI(RequestHandler):
	def set_default_headers(self):
		print("setting headres")
		origin = self.request.headers.get('Origin')
		if origin:
			self.set_header('Access-Control-Allow-Origin', origin)

		self.set_header("Acess-Control_Allow_Headers", "x-requested-with")
		self.set_header("Acess-Control_Allow_Origin", 'POST, GET, OPTIONS')
		
	def get(self):
		frames_nomask = getUsersWithoutMask()
		data = []
		for i in range(len(frames_nomask)):
			fr= {
				"id": frames_nomask[i].id, 
				"image": frames_nomask[i].image,
				"has_mask": frames_nomask[i].has_mask
			}
			data.append(fr)
		
		self.write({"frame": data })

class ReportsAPI(RequestHandler):
	def set_default_headers(self):
		print("setting headres")
		origin = self.request.headers.get('Origin')
		if origin:
			self.set_header('Access-Control-Allow-Origin', origin)

		self.set_header("Acess-Control_Allow_Headers", "x-requested-with")
		self.set_header("Acess-Control_Allow_Origin", 'POST, GET, OPTIONS')
		
	def get(self, id=None):
		if id == None:
			#mask = getUsersWithMask()
			nomask = getUsersWithoutMask(id)
			report = getFramebyIdCamera()
			#calc = (len(nomask))*100/((len(mask))+(len(nomask)))
			self.write({'data': 
				report
				})
			

class ReportbyDayAPI(RequestHandler):
	def set_default_headers(self):
		print("setting headres")
		origin = self.request.headers.get('Origin')
		if origin:
			self.set_header('Access-Control-Allow-Origin', origin)

		self.set_header("Acess-Control_Allow_Headers", "x-requested-with")
		self.set_header("Acess-Control_Allow_Origin", 'POST, GET, OPTIONS')
		
	def get(self,date):
		print(date)
		reports = GetReportByDate(date)
		var = reports.to_json()
		var['date_time'] = var['date_time'].strftime("%A")
		self.write({'reports': var})
		

def GetUrlFaceRecognition():
	urls = [
		("/api/facemask", ReportsAPI),
		("/api/facereports", ReportsAPI)
	]
	return urls


def GetUrlFaceRecognitionFrame():
	urls = [
		("/api/frame", AllFramesAPI),
		("/api/frame/([0-9]*)", OneFrameAPI)
	]
	return urls


def GetUrlReportByDay():
    urls = [
        ('/api/reportbyday/([0-9]*)', ReportbyDayAPI)
    ]
    return urls
