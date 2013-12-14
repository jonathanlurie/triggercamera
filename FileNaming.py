# class to find the right, not already-existing name for a file

import glob
import os

class FileNaming:
	
	m_outputFolder = None
	m_picturePrefix = None
	m_videoPrefix = None
	m_pictureExt = None
	m_videoExt = None
	m_lastPictureIndex = None
	m_lastVideoIndex = None
	
	def __init__(self):
		self.m_outputFolder = "/home/pi/projects/camcorder/output/"
		self.m_picturePrefix = "piPict_"
		self.m_videoPrefix = "piVid_"
		self.m_pictureExt = ".jpg"
		self.m_videoExt = ".h264"
		self.m_nextPictureIndex = -1
		self.m_nextVideoIndex = -1
		
		
	# parse the "output" folder and look for the last filename that matched the pattern.
	# then associate the last+1 to the next image index
	def defineNextPictureIndex(self):
		
		tempMaxIndex = self.m_nextPictureIndex
		
		for files in glob.glob(self.m_outputFolder + self.m_picturePrefix + "*" + self.m_pictureExt):
			# filename with ext
			fileWithExt = os.path.basename(files)
			
			# filename without ext
			fileWithoutExt = os.path.splitext(fileWithExt)[0]
			
			# file without sufix
			fileNoSufix = fileWithoutExt.split(self.m_picturePrefix)[1]
			
			# convert the indexing part to integer
			try:
				tempMaxIndex = int(fileNoSufix)
				
				# associate to m_lastPictureIndex if the biggest
				if(tempMaxIndex > self.m_nextPictureIndex):
					self.m_nextPictureIndex = tempMaxIndex
					
			except ValueError:
				print(fileNoSufix + " is not an integer")
				
		print("the maximum found index is: " + str(self.m_nextPictureIndex))
		
		self.m_nextPictureIndex += 1
		
		
	# return the next picture name to be used.
	# if needed, it lauches defineNextPictureIndex() first.
	def getNewPictureName(self):
		if(self.m_nextPictureIndex == -1):
			self.defineNextPictureIndex()
		
		alreadyExists = 1
		
		# to be sure, we check if this filename does not already exist
		while alreadyExists:
			
			nextPictureName = self.m_outputFolder  + self.m_picturePrefix + str(self.m_nextPictureIndex) + self.m_pictureExt
			
			
			
			if(os.path.exists(nextPictureName)):
				self.m_nextPictureIndex += 1
			else:
				alreadyExists = 0
				
		print("the next file is: " + nextPictureName)
		return nextPictureName
		
		
		

		
	# parse the "output" folder and look for the last filename that matched the pattern.
	# then associate the last+1 to the next image index
	def defineNextVideoIndex(self):
		
		tempMaxIndex = self.m_nextVideoIndex
		
		for files in glob.glob(self.m_outputFolder + self.m_videoPrefix + "*" + self.m_videoExt):
			# filename with ext
			fileWithExt = os.path.basename(files)
			
			# filename without ext
			fileWithoutExt = os.path.splitext(fileWithExt)[0]
			
			# file without sufix
			fileNoSufix = fileWithoutExt.split(self.m_videoPrefix)[1]
			
			# convert the indexing part to integer
			try:
				tempMaxIndex = int(fileNoSufix)
				
				# associate to m_lastVideoIndex if the biggest
				if(tempMaxIndex > self.m_nextVideoIndex):
					self.m_nextVideoIndex = tempMaxIndex
					
			except ValueError:
				print(fileNoSufix + " is not an integer")
				
		print("the maximum found index is: " + str(self.m_nextVideoIndex))
		
		self.m_nextVideoIndex += 1
		
		
	# return the next picture name to be used.
	# if needed, it lauches defineNextPictureIndex() first.
	def getNewVideoName(self):
		if(self.m_nextVideoIndex == -1):
			self.defineNextVideoIndex()
		
		alreadyExists = 1
		
		# to be sure, we check if this filename does not already exist
		while alreadyExists:
			
			nextVideoName = self.m_outputFolder  + self.m_videoPrefix + str(self.m_nextVideoIndex) + self.m_videoExt
			
			
			
			if(os.path.exists(nextVideoName)):
				self.m_nextVideoIndex += 1
			else:
				alreadyExists = 0
				
		print("the next file is: " + nextVideoName)
		return nextVideoName
		
		
		
		
		