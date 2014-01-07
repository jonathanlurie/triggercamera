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
	
	# default value for video preview (True: preview activated, False: preview deactivated)
	m_isPreviewActivated = None
	
	
	def __init__(self, fileNaming):
		print("camera initialization...")
		self.m_camera = picamera.PiCamera()
		self.m_camera.EXPOSURE_MODE = "fixedfps"
		self.m_camera.led = False
		
		self.m_fileNaming = fileNaming
		
		self.m_isCurentlyRecording = False
		self.m_isPreviewActivated = True
		
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
				self.m_camera.led = True
				
		#except:
			#self.m_isCurentlyRecording = False
			#print("exception in startVideoRecording.")
		
	def stopVideoRecording(self):
		try:
			if(self.m_isCurentlyRecording == True):
				print("video recording stoped.")
				self.m_isCurentlyRecording = False
				self.m_camera.stop_recording()
				self.m_camera.led = False
			
		except:
			print("exception in stopVideoRecord.")
		
	
	# By default, the preview is activated (by Main function), but can be switch on/off
	# by this function
	def switchPreviewOnOff(self):
		if(self.m_isPreviewActivated):
			self.stopPreview()
		else:
			self.startPreview()
			
		self.m_isPreviewActivated = not self.m_isPreviewActivated
		
	
	# launches ot stops the video recording.
	# this function does both for triggering both action by the very same click button
	def switchRecordingOnOff(self):
		print("bool recording: " + str(self.m_isCurentlyRecording) )
		
		if(self.m_isCurentlyRecording):
			self.stopVideoRecording()
		else:
			self.startVideoRecording()
			
	
	# set the camera saturation value, must be [-100, 100]
	def setCameraSaturation(self, val):
		self.m_camera.saturation = int(val)
		
	# set the camera brightness value, must be [0, 100]
	def setCameraBrightness(self, val):
		self.m_camera.brightness = int(val)
	
		
	# set the camera brightness value, must be [-100, 100]
	def setCameraContrast(self, val):
		self.m_camera.contrast = int(val)
		
		
	# NOT WORKING
	# set the ISO of the camera
	# it is actually the closest from those values which will be chosen
	# 100, 200, 320, 400, 500, 640, 800
	def setCameraISO(self, val):

		if(val<400):
			
			self.m_camera.ISO = 100
		else:
			self.m_camera.ISO = 800

#		self.m_camera.ISO = int(val)


	# set the camera shutter speed in micro seconds
	def setCameraShutterSpeed(self, val):
		self.m_camera.shutter_speed = int(val)

	# NOT WORKING
	def setExpoCompensation(self, val):
		self.m_camera.exposure_compensastion = int(val)
		print self.m_camera.exposure_compensastion
		
	def destructor(self):
		self.m_camera.close()