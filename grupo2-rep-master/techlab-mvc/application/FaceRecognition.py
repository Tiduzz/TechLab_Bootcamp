# import the necessary packages
import sys
sys.path.append('/home/techlab-mvc')

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os
import io
import imageio
from PIL import Image as Img
import datetime
from sqlalchemy import DateTime
from data.dao.ReportMods import CreateReports
from data.dao.FaceRecognitionMods import create_frame_face
from data.dao.FaceRecognitionMods import create_frame, create_frame_face
import base64
from IPython.display import display, clear_output, Image
cameraid = 2 #escolhe a camera que você quer salvar o frame

#Use 'jpeg' instead of 'png' (~5 times faster)
def showarray(a, fmt='jpeg'):
    f = io.BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)
    display(Image(data=f.getvalue()))
    

def detect_faces(image_gray, scale, neighbors):
    classifier = 'haarcascade_frontalface_default.xml'
    classifier_path = os.path.join('/usr/local/share/opencv4/haarcascades/', classifier)

    classifier = cv2.CascadeClassifier(classifier_path)

    if not classifier.empty():
        faces = classifier.detectMultiScale(image_gray, scale, neighbors)
        
        return faces
				
    return []

#Função que vai corrigir a cor das imagens antes de salvar na base64
def create(salva_base64, camera_id):
	retval, buffer = cv2.imencode('.jpg', salva_base64)
	encoded_string = base64.b64encode(buffer)
	encoded_string.decode('utf-8')
	return create_frame(encoded_string, camera_id)

#Função que vai contar as faces com e sem mascara e salvar na base64
def create_face(face, has_mask, frame):
	retval, buffer = cv2.imencode('.jpg', face)
	encoded_string = base64.b64encode(buffer)
	encoded_string.decode('utf-8')
	return create_frame_face(encoded_string, has_mask, frame)

def LoadReport(faces,noquan,id_cameras):
	quan = len(faces)
	return CreateReports(quan, 0, noquan, cameraid)


#Modelo do techlab Pré Treinado
model = load_model('/home/techlab-mvc/custom_mask_detector.model')

def detect_face_in_video():
	file = "/home/techlab-mvc/video6.mp4"
	video = imageio.get_reader(file, "ffmpeg")
	f = video.iter_data()
	metadata = video.get_meta_data()
	
	for image in video.iter_data():
		image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
		img_median = cv2.medianBlur(image_gray, 5) #Reduz ruidos dos frames
		faces = detect_faces(img_median, 1.2, 5)
		
		noquan = 0
		for i in range(len(faces)):
			x, y, w, h = faces[i]
			image_rect = cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)

			face_img = image[y:y+h, x:x+w]
			face = cv2.resize(face_img, (224, 224))
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)
				
			(mask, withoutMask) = model.predict(face)[0]

			#Função para borrar os rostos encontrados
			roi_filtro = img_median[y:y+h, x:x+w]
			blur = cv2.GaussianBlur(roi_filtro,(37, 37), 37)
			img_median[y:y+h, x:x+w] = blur
			
			# determine the class label and color we'll use to draw
			# the bounding box and text
			label = "Mask" if mask > withoutMask else "No Mask"
			if label == "Mask":
				color = (0, 255, 0)
				frame_created = create(img_median, cameraid)
				create_face(face_img, True, frame_created)
				print("de mascara", mask)
			else: 
				color = (0, 0, 255)
				frame_created = create(img_median, cameraid)
				create_face(face_img, False, frame_created)
				print("sem mascara", withoutMask)
				noquan = noquan+1
			
			# include the probability in the label
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
			
			#display the label and bounding box rectanble on the output frame
			cv2.putText(image, label, (x, y - 10),
					cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
			cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
		
		LoadReport(faces,noquan,None)
		
		#if j%100 == 0:
		#	if label == "Mask":
		#		cv2.imwrite('face_mask'+str(i)+'.jpg',image)
				##salva_base64 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
				#create(salva_base64)
		#	else:
		#		cv2.imwrite('face_nomask'+str(i)+'.jpg',image)
				#salva_base64 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
				#create(salva_base64)
		#j+=1

detect_face_in_video()