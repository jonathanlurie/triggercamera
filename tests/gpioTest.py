import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# we put a pull up resistance to the 17nt port
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# we put a pull down resistance to the 24nt port
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# we define a threaded callback function.
# this will run another thread when the event is detected
def button1_onPressCallback(channel):
	print "port 17 button pressed! (falling edge)"

# the same, but for a release callback
def button1_onReleaseCallback(channel):
	print "port 17 button released! (rising edge)"

# a callback for both release AND press action.
# when inside we have to check if it was a press or a release action
def button1_bothCallback(channel):
	
	if (GPIO.input(channel)):
		button1_onReleaseCallback(channel)
	else:
		button1_onPressCallback(channel)

# subsccribes the 17nt port to a press callback
#GPIO.add_event_detect(17, GPIO.FALLING, callback=button1_onPressCallback, bouncetime=300)

# subscribe the 17nt port to a release callback
#GPIO.add_event_detect(17, GPIO.RISING, callback=button1_onReleaseCallback, bouncetime=300)

# subscribe th 17nt port to a more generic callback : press or release (no matter)
GPIO.add_event_detect(17, GPIO.BOTH, callback=button1_bothCallback, bouncetime = 10)


try:
	# this call is actually just for waiting...
	print("Waiting for rising edge on port 24\n")
	GPIO.wait_for_edge(24, GPIO.RISING)
	print("Rising edge detectded on port 24!")
	
	
except KeyboardInterrupt:
	# GPIO needs it before leaving
	GPIO.cleanup()
	
GPIO.cleanup()