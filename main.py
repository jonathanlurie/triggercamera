from GpioInterface import *
from CameraControl import *
from FileNaming import *


# main

if __name__ == "__main__":
	try:
		#
		#
		#       INIT STEP
		#
		#
		
		
		# initialize the file manager
		FileNmg = FileNaming()
		
		# initialize the GPIO manager
		gpioTest = GpioInterface()
		
		# initialize the camera controller
		cameraCtrl = CameraControl(FileNmg)
		
		# setting the ling between the GPIO manager and the camera controller
		gpioTest.setCameraCtrl(cameraCtrl)
		
		
		#
		#
		#       LAUNCH STEP
		#
		#
		
		# Starts the preview by default
		cameraCtrl.startPreview()
		
		#cameraCtrl.startVideoRecording()
		
		gpioTest.waitFor24Port()
		
		#cameraCtrl.stopPreview()
		
		
		
		# destruct stuff
		gpioTest.destructor()
		cameraCtrl.destructor()
		
		try:
			sys.stdout.close()
		except:
			pass
		
		try:
			sys.stderr.close()
		except:
			pass
			
	except KeyboardInterrupt:
		
		gpioTest.destructor()