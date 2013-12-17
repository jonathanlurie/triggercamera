from xml.dom import minidom


class featureParser:

	m_xmlDocument = None
	m_featureList = None
	m_isFileReadable = None

	# CONSTRUCTOR
	# initialize a feature parser with the xml file address
	def __init__(self, xmlFileAddess):
		try:	
			self.m_xmlDocument = minidom.parse(xmlFileAddess)
			self.m_featureList = self.m_xmlDocument.getElementsByTagName('feature')
			self.m_isFileReadable = True
		except:
			print("ERROR: The xml file is not readable.")
			self.m_isFileReadable = False

	
	
	# PULBIC
	# returns the minimum value of the feature named featureName
	def getFeatureMinValue(self, featureName):
		val = self._getFeatureSubFeature(featureName, "min_value")

		if(val == None):
			print("ERROR: no minimum value for the feature " + featureName)
			return None
		else:
			return val

	# PULBIC
	# returns the maximum value of the feature named featureName
	def getFeatureMaxValue(self, featureName):
		val = self._getFeatureSubFeature(featureName, "max_value")

		if(val == None):
			print("ERROR: no maximum value for the feature " + featureName)
			return None
		else:
			return val

	# PULBIC
	# returns the default value of the feature named featureName
	def getFeatureDefaultValue(self, featureName):
		val = self._getFeatureSubFeature(featureName, "default_value")

		if(val == None):
			print("ERROR: no default value for the feature " + featureName)
			return None
		else:
			return val

	# PULBIC
	# returns the description of the feature named featureName
	def getFeatureDescription(self, featureName):
		val = self._getFeatureSubFeature(featureName, "description")

		if(val == None):
			print("ERROR: no description for the feature " + featureName)
			return None
		else:
			return val


	# PRIVATE
	# check if a feature exists in the DOM tree.
	# returns True so, False if not
	def _doesFeatureExist(self, featureName):
		if( not self.m_isFileReadable):
			return False

		found = False		

		for ft in self.m_featureList :
			if(ft.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip() == featureName.strip()):
				found = True
				break

		if(not found):
			print("ERROR: the feature " + featureName + " does not exist.")
		
		return found


	# PRIVATE
	# gives the value of a subFeature of the feature named "feature"
	def _getFeatureSubFeature(self, featureName, subFtName):
		# check if the file exists
		if( not self.m_isFileReadable):
			return None
		
		# checks if the feature exists
		if(not self._doesFeatureExist(featureName)):
			return None

		subFeature = None

		for ft in self.m_featureList :
			if(ft.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip() == featureName.strip()):
				try:
					subFeature = ft.getElementsByTagName(subFtName)[0].childNodes[0].nodeValue.strip()
					break
				except:
					print("ERROR: the sub feature named " + subFtName + " does not exist.")
		return subFeature



if __name__ == "__main__":


	fpr = featureParser('/home/madfish/projets/triggercamera/features.xml')
	print(fpr.getFeatureMinValue("saturation"))
	print(fpr.getFeatureMaxValue("saturation"))
	print(fpr.getFeatureDefaultValue("saturation"))
	print(fpr.getFeatureDescription("saturation"))





















