import time
import picamera


# performs a simple full screen preview during 10 seconds
def preview10sec():
	camera = picamera.PiCamera()
	try:
		h = camera.start_preview()
		time.sleep(5)
		print h
		camera.stop_preview()
	finally:
		camera.close()
		
		
		
# performs a simple preview while changing the brightness all along		
def liveParamSetting():
	with picamera.PiCamera() as camera:
		camera.start_preview()
		try:
			for i in range(200):
				camera.saturation = i - 100
				time.sleep(0.2)
		finally:
			camera.stop_preview()
			

def previewAndRecord():	
	with picamera.PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.start_preview()
		camera.start_recording('output/foo.h264')
		camera.wait_recording(60)	# to use instead of time.sleep() for a recording purpose
		camera.stop_recording()
		camera.stop_preview()
		
		
# capture a jpeg with preview after setting some features
def captureJpgWithFeatures():
	with picamera.PiCamera() as camera:
		camera.resolution = (1280, 720)
		camera.start_preview()
		camera.exposure_compensation = 2
		#camera.exposure_mode = 'spotlight' # marche pas...
		camera.meter_mode = 'matrix'
		camera.image_effect = 'gpen'
		# Give the camera some time to adjust to conditions
		time.sleep(2)
		camera.capture('output/foo2.jpg')
		camera.stop_preview()
		
		
# just preview in black and white
def previewBW20sec():
	with picamera.PiCamera() as camera:
		camera.start_preview()
		try:
			print("luminosite avant capture " + str(camera.brightness))
			
			camera.saturation = -100
			#camera.brightness +=15
			camera.contrast = 50
			camera.shutter_speeeed = 35000
			
			for i in range(100):
				time.sleep(0.2)
				print("luminosite pendant capture " + str(camera.brightness))
		finally:
			camera.stop_preview()
			
# take a photo when 'p' is triggered
# 'q' to quit 
def takePhoto():
	#with picamera.PiCamera() as camera:
		#camera.resolution = (1280, 720)
		#camera.start_preview()
		print("debut de preview")
		trigger = 0


		while trigger != "q":
			#time.sleep(2)
		
			trigger = raw_input("prompt: ")
			print(trigger)
		
			if trigger=="p":
				time.sleep(0.2)
				print("p key pressed!")
				#camera.capture('output/foo2.jpg')
				trigger = 0
			
			
			
		#camera.stop_preview()
		print("fin de preview")
		
		
def manualSettingPreview():
	camera = picamera.PiCamera()
	try:
		
		# shutter speed (micro seconds int)
		camera.shutter_speed = int((1./60.) * 1000000)
		
		# the default is already 30 fps...
		camera.exposure_mode = 'fixedfps'
		
		# between -25 an 25, 0 is auto
		camera.exposure_compensation = 1
		
		# brightness, between 0 and 100, default at 50
		camera.brightness = 49
		
		# white balance
		camera.awb_mode =  'tungsten'
		
		# iso
		camera.iso = 800
		
		print(camera.AWB_MODES)
		
		camera.start_preview()
		time.sleep(20)
		camera.stop_preview()
	finally:
		camera.close()
		
if __name__ == "__main__":
	#preview10sec()
	#liveParamSetting()
	#previewAndRecord()
	#captureJpgWithFeatures()
	#previewBW20sec()
	#takePhoto()
	manualSettingPreview()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	