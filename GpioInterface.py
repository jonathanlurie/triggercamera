# this class aims to be the interface between the gpio port and another part of a sofware.
# It was written to be used for the Camera

# input description:
#
# BUTTON 1:	pinned on the 17th port
# usage:		both on pressed AND released states, but not with the same action.
# purpose:	when pressed, allow the potentiometers to change the sates.
#			when released, does not allow the potentiometers to change the sates
#
# BUTTON 2:	pinned on the 18th port
# usage:		just on a pressed action
# purpose:	take a photo

# import and setting
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import spidev # for potentiometers

# import the CameraControl class in order to use its functions from here
from CameraControl import *


class GpioInterface:
	
	m_cameraCtrl = None
	m_spi = None
	
	m_openPotReading = False
	
	m_NB_POTS = 8
	m_potsValues = None
	
	# Constructor
	def __init__(self):
		
		# potentiometers init stuff
		self.m_spi = spidev.SpiDev()   # create a new spidev object
		self.m_spi.open(0, 0)          # open bus 0, chip enable 0
		
		# creating the array with pots values
		self.m_potsValues = [0] * self.m_NB_POTS
		
		print(self.m_potsValues)
		
		# BUTTON 17
		# We plan to use the 17th port for triggering actions, so,
		# we put a pull up resistance to the 17th port
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		# BUTTON 17
		# subscribe th 17nt port to a generic callback : press or release (no matter)
		GPIO.add_event_detect(17, GPIO.BOTH, callback=self.button17_onBothCallback, bouncetime = 10)
		
		# BUTTON 18
		# We plan to use the 18th port for triggering actions, so,
		# we put a pull up resistance to the 18th port
		GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		# BUTTON 18
		# subscribe th 18nt port to a generic callback : press or release (no matter)
		GPIO.add_event_detect(18, GPIO.BOTH, callback=self.button18_onBothCallback, bouncetime = 10)
		
		
		
		# BUTTON 27
		# We plan to use the 27th port for triggering actions, so,
		# we put a pull up resistance to the 27th port
		GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		# BUTTON 27
		# subscribe th 27nt port to a generic callback : press or release (no matter)
		GPIO.add_event_detect(27, GPIO.BOTH, callback=self.button27_onBothCallback, bouncetime = 10)
		
		
		
		# BUTTON 4
		# We plan to use the 4th port for triggering actions, so,
		# we put a pull up resistance to the 4th port
		GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		# BUTTON 4
		# subscribe th 4nt port to a generic callback : press or release (no matter)
		GPIO.add_event_detect(4, GPIO.BOTH, callback=self.button4_onBothCallback, bouncetime = 10)
		
		
		
		# for testing, not used
		GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def setCameraCtrl(self, cam):
		self.m_cameraCtrl = cam

	# _________________________________________________________________________________________ BUTTON IO 17

	# BUTTON 17
	# when the BUTTON 17 is pressed
	def button17_onPress(self, channel):
		print "BUTTON 17: port 17 button pressed! (falling edge)"

	# BUTTON 17
	# when the BUTTON 17 is released
	def button17_onRelease(self, channel):
		print "BUTTON 17: port 17 button released! (rising edge)"

	# BUTTON 17
	# callback for both release AND press action.
	# when inside we have to check if it was a press or a release action
	def button17_onBothCallback(self, channel):
		# TODO: add a control to avoid two consecutive rising edges of falling edges
		if (GPIO.input(channel)):
			self.button17_onRelease(channel)
		else:
			self.button17_onPress(channel)
			
			
			
	# _________________________________________________________________________________________ BUTTON IO 18

	# BUTTON 18
	# when the BUTTON 18 is pressed
	def button18_onPress(self, channel):
		print "BUTTON 18: port 18 button pressed! (falling edge)"

	# BUTTON 18
	# when the BUTTON 18 is released
	def button18_onRelease(self, channel):
		print "BUTTON 18: port 18 button released! (rising edge)"

	# BUTTON 18
	# callback for both release AND press action.
	# when inside we have to check if it was a press or a release action
	def button18_onBothCallback(self, channel):
		# TODO: add a control to avoid two consecutive rising edges of falling edges
		if (GPIO.input(channel)):
			self.button18_onRelease(channel)
		else:
			self.button18_onPress(channel)
			
			
	# _________________________________________________________________________________________ BUTTON IO 27

	# BUTTON 27
	# when the BUTTON 27 is pressed
	def button27_onPress(self, channel):
		print "BUTTON 27: port 27 button pressed! (falling edge)"

	# BUTTON 18
	# when the BUTTON 27 is released
	def button27_onRelease(self, channel):
		print "BUTTON 27: port 27 button released! (rising edge)"

	# BUTTON 27
	# callback for both release AND press action.
	# when inside we have to check if it was a press or a release action
	def button27_onBothCallback(self, channel):
		# TODO: add a control to avoid two consecutive rising edges of falling edges
		if (GPIO.input(channel)):
			self.button27_onRelease(channel)
		else:
			self.button27_onPress(channel)
			
	
	# _________________________________________________________________________________________ BUTTON IO 27

	# BUTTON 4
	# when the BUTTON 27 is pressed
	def button4_onPress(self, channel):
		print "BUTTON 4: port 4 button pressed! (falling edge)"
		self.m_openPotReading = True
		self.endLessPotReading()

	# BUTTON 4
	# when the BUTTON 27 is released
	def button4_onRelease(self, channel):
		print "BUTTON 4: port 4 button released! (rising edge)"
		#print "potentiometer n0: " + str(self.readPotentiometer(0))
		self.m_openPotReading = False

	# BUTTON 4
	# callback for both release AND press action.
	# when inside we have to check if it was a press or a release action
	def button4_onBothCallback(self, channel):
		# TODO: add a control to avoid two consecutive rising edges of falling edges
		if (GPIO.input(channel)):
			self.button4_onRelease(channel)
		else:
			self.button4_onPress(channel)
			
			
			
			
	# Reads the potentiometer value from the LotOfPots shield
	# args: channel should be [0; 7]
	def readPotentiometer(self, channel):
		if channel > 7 or channel < 0:
			return -1

		# spi.xfer2 sends three bytes and returns three bytes:
		# byte 1: the start bit (always 0x01)
		# byte 2: configure bits, see MCP3008 datasheet table 5-2
		# byte 3: don't care
		r = self.m_spi.xfer2([1, 8 + channel << 4, 0])

		# Three bytes are returned; the data (0-1023) is in the 
		# lower 3 bits of byte 2, and byte 3 (datasheet figure 6-1)    
		v = ((r[1] & 3) << 8) + r[2]

		return v;
			

	# read all the pots values (every 0.1 sec) and store them in the list self.m_potsValues
	def endLessPotReading(self):
		while self.m_openPotReading:
			for i in range(self.m_NB_POTS):
				#value = self.readPotentiometer(i)
				#print "%4d" % value,
				self.m_potsValues[i] = self.readPotentiometer(i)
			
			#print(self.m_potsValues)	
			
			# saturation pot: #0 interval [0;1023] -> [-100; 100]
			saturationValue = self.changeScale(0, 1023, -100, 100, self.m_potsValues[0])
			self.m_cameraCtrl.setCameraSaturation(saturationValue)
			
			# brightness pot: #0 interval [0;1023] -> [0; 100]
			brightnessValue = self.changeScale(0, 1023, 0, 100, self.m_potsValues[1])
			self.m_cameraCtrl.setCameraBrightness(brightnessValue)
			
			# contrast pot: #0 interval [0;1023] -> [-100; 100]
			contrastValue = self.changeScale(0, 1023, -100, 100, self.m_potsValues[2])
			self.m_cameraCtrl.setCameraContrast(contrastValue)
			
			time.sleep(0.1)
				

			
	# print something, for testing
	def printState(self):
		print("hello there")
	
	# for testing, wait for something, and finally press BUTTON 1 or 2
	def waitFor24Port(self):
		try:
			print("waiting for something on port 24")
			GPIO.wait_for_edge(24, GPIO.RISING)
			print("something happened on 24th port")
			
		except KeyboardInterrupt:
			self.destructor()
	
	
	# transpose a value from intervale 1to its equivalent in intervale 2
	def changeScale(self, inter1Min, inter1Max, inter2Min, inter2Max, value):
		rangeInter1 = float(inter1Max - inter1Min)
		rangeInter2 = float(inter2Max - inter2Min)
		
		percentOfValueInInter1 = float(value - inter1Min) / rangeInter1
		valueInInter2 = percentOfValueInInter1 * rangeInter2 + float(inter2Min)
		
		return valueInInter2
		
		
		
	
	# cleaning
	def destructor(self):
		print("GPIO cleaning...")
		# GPIO needs it before leaving
		GPIO.cleanup()
		
		
		
		
		
		
		