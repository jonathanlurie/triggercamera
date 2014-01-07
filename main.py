from GpioInterface import *
from CameraControl import *
from FileNaming import *


# main

if __name__ == "__main__":
	try:
		# create the file manager and init it
		FileNmg = FileNaming()
		FileNmg.defineNextPictureIndex()
		FileNmg.defineNextVideoIndex()
		
		gpioTest = GpioInterface()
		cameraCtrl = CameraControl(FileNmg)
		
		gpioTest.setCameraCtrl(cameraCtrl)
		
		cameraCtrl.startPreview()
		
		#cameraCtrl.startVideoRecording()
		
		gpioTest.waitFor24Port()
		
		cameraCtrl.stopPreview()
		
		
		
		# destruct stuff
		gpioTest.destructor()
		cameraCtrl.destructor()
		
	except KeyboardInterrupt:
		
		gpioTest.destructor()