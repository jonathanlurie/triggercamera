# implement some basic feature taken from picamera, in order to build a real camera.


import time
import picamera

from FileNaming import *

class CameraControl:
	
	# the camera object
	m_camera = None
	
	# the file naming manager
	m_fileNaming = None
	
	# boolean at true is it's currently recording a video
	m_isCurentlyRecording = None
	
	def __init__(self, fileNaming):
		print("camera initialization...")
		self.m_camera = picamera.PiCamera()
		self.m_fileNaming = fileNaming
		
		self.m_isCurentlyRecording = False
		
	def startPreview(self):
		self.m_camera.start_preview()
		
		
	def stopPreview(self):
		self.m_camera.stop_preview()
		
	def captureJpeg(self):
		#time.sleep(2)
		try:
			self.m_camera.capture(self.m_fileNaming.getNewPictureName())
		except AttributeError:
			print("picamera AttributeError...")
			
	def startVideoRecording(self):
		#try:
			if(self.m_isCurentlyRecording == False):
				print("start recording video...")
				self.m_isCurentlyRecording = True
				self.m_camera.start_recording(self.m_fileNaming.getNewVideoName(), format='h264', bitrate=int(5 * 1000000))
				time.sleep(10)
				self.stopVideoRecording()
				
		#except:
			#self.m_isCurentlyRecording = False
			#print("exception in startVideoRecording.")
		
	def stopVideoRecording(self):
		try:
			if(self.m_isCurentlyRecording == True):
				print("video recording stoped.")
				self.m_isCurentlyRecording = False
				self.m_camera.stop_recording()
				
			
		except:
			print("exception in stopVideoRecord.")
		
	
	# set the camera saturation value, must be [-100, 100]
	def setCameraSaturation(self, val):
		self.m_camera.saturation = int(val)
		
	# set the camera brightness value, must be [0, 100]
	def setCameraBrightness(self, val):
		self.m_camera.brightness = int(val)
	
		
	# set the camera brightness value, must be [-100, 100]
	def setCameraContrast(self, val):
		self.m_camera.contrast = int(val)
		
		
	def destructor(self):
		self.m_camera.close()