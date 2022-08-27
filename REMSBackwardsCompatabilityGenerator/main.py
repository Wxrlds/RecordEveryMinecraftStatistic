import os
from pathlib import Path

from utils.regexUtils import replaceXwithY
from utils.utils import resolveUUIDToUsername, generateScoreboardCommands, writeToFile

# Path to all stat files of the players
playerstatDumps = Path('./dumps')

# Path to output dir
outputDir = Path('./output')
individualSetupDir = Path(outputDir / 'setup')
os.makedirs(individualSetupDir, exist_ok=True)

for statFile in os.listdir(playerstatDumps):
	# Removes the .json extension from the UUID
	uuid = replaceXwithY(r'\.json', r'', statFile)
	# Gets the username from the UUID
	# Also prints out the current UUID and username in case they do not exist
	print(uuid)
	username = resolveUUIDToUsername(uuid)
	print(username)

	# Path of the stat file
	statFile = Path(playerstatDumps / statFile)
	outputFile = Path(individualSetupDir / f'{username}-Stats.mcfunction')

	generateScoreboardCommands(statFile, username, outputFile)

for file in os.listdir(individualSetupDir):
	file = Path(individualSetupDir / file)
	with open(file) as setupFile:
		writeToFile(setupFile.read(), Path(outputDir / 'setup.mcfunction'))
