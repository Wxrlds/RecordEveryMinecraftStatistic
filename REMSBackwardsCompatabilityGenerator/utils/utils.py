import json

import requests as requests

from utils.regexUtils import replaceXwithY


# scoreboard players set username internalName value
def generateScoreboardCommands(statFile, username, outputFile):
	# Open the stat file
	with open(statFile, 'r') as statFile:
		# Put content of stat file into stats var
		stats = json.load(statFile)

		# statType: minecraft:broken
		# items: dict of items which were broken
		# item: the individual item
		# print(stats['stats'][statType][registryID])
		for statType, items in stats['stats'].items():
			for registryID in items:
				# Prefix of the stat
				prefix = generatePrefixFromStatType(statType)
				# The internal name of the stat
				internalName = f'{prefix}_{replaceXwithY(":", "_", registryID)}'
				# How often that stat was increased
				value = stats['stats'][statType][registryID]
				command = f'scoreboard players set {username} {internalName} {value}'
				# Writes command to file
				writeToFile(command, outputFile)


def generatePrefixFromStatType(statType):
	match statType:
		case 'minecraft:broken':
			prefix = 'b'
		case 'minecraft:crafted':
			prefix = 'c'
		case 'minecraft:dropped':
			prefix = 'q'
		case 'minecraft:picked_up':
			prefix = 'p'
		case 'minecraft:used':
			prefix = 'u'
		case 'minecraft:mined':
			prefix = 'm'
		case 'minecraft:killed':
			prefix = 'k'
		case 'minecraft:killed_by':
			prefix = 'd'
		case 'minecraft:custom':
			prefix = 'cu'
	return prefix


# Writes to file
def writeToFile(command, file):
	with open(file, 'a') as outputFile:
		outputFile.write(f'{command}\n')


# Converts UUID to Username
def resolveUUIDToUsername(uuid):
	# Headers of the request
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
		'Content-Type': 'application/json'
	}
	# URL to the username
	url = str(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}')
	# The request to Mojang
	data = requests.get(url, headers=headers).json()
	# The actual username
	username = data["name"]
	return username
