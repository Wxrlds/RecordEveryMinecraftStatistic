import re


# Replaces X with Y in registryName
def replaceXwithY(x, y, registryName):
	regEx = re.compile(x)
	registryName = regEx.sub(y, registryName)
	return registryName
