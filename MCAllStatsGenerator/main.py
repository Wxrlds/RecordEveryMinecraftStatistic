import os
from pathlib import Path

from utils.customHandling.customUtils import generateCustomScoreboardCommands
from utils.generalHandling.generalUtils import generateGeneralScoreboardCommands
from utils.utils import generateScoreboardCommands, writeToFile

# Path of all dump files
dumpDir = Path('./dumps')

# Paths to item, block, entity and custom dumps
itemDump = Path(dumpDir / 'items.csv')
blockDump = Path(dumpDir / 'blocks.csv')
entityDump = Path(dumpDir / 'entities.csv')
customDump = Path(dumpDir / 'stat-types.csv')
generalDump = Path(dumpDir / 'general.csv')

# Path to all output dirs
outputDir = Path('./output')

# Path to setup and uninstall output dirs
setupDir = Path(outputDir / 'setup')
uninstallDir = Path(outputDir / 'uninstall')
os.makedirs(setupDir, exist_ok=True)
os.makedirs(uninstallDir, exist_ok=True)

# Verb and prefix of the stat types that work with an item
itemStatTypeVerbs = {
	# Verb    : Prefix
	'Broken': 'b',
	'Crafted': 'c',
	'Dropped': 'q',
	'Picked_Up': 'p',
	'Used': 'u'
}

# Verb and prefix of the stat types that work with a block
blockStatTypeVerbs = {
	# Verb    : Prefix
	'Mined': 'm',
}

# Verb and prefix of the stat types that work with an entity
entityStatTypeVerbs = {
	# Verb    : Prefix
	'Killed': 'k',
	'Killed_By': 'd'
}

# Noun and prefix of the custom stat types
customStatTypeNouns = {
	# Noun    : Prefix
	'Custom': 'cu'
}

# Noun Prefix of the general stat types
# Do not add more values or it will break!
generalStatTypeNouns = {
	# Noun    : Prefix
	'General': 'g'
}

# Generates all stat types that work with an item
for itemStatTypeVerb, itemStatTypePrefix in itemStatTypeVerbs.items():
	# Generate the file path for the setup and uninstall file
	statSetupFile = Path(setupDir / f'setup{itemStatTypeVerb}Stats.mcfunction')
	statUninstallFile = Path(uninstallDir / f'uninstall{itemStatTypeVerb}Stats.mcfunction')
	# Generates the setup and uninstall commands
	generateScoreboardCommands(itemDump, itemStatTypePrefix, itemStatTypeVerb, statSetupFile, statUninstallFile)

# Generates all stat types that work with a block
for blockStatTypeVerb, blockStatTypePrefix in blockStatTypeVerbs.items():
	# Generate the file path for the setup and uninstall file
	statSetupFile = Path(setupDir / f'setup{blockStatTypeVerb}Stats.mcfunction')
	statUninstallFile = Path(uninstallDir / f'uninstall{blockStatTypeVerb}Stats.mcfunction')
	# Generates the setup and uninstall commands
	generateScoreboardCommands(blockDump, blockStatTypePrefix, blockStatTypeVerb, statSetupFile, statUninstallFile)

# Generates all stat types that work with an entity
for entityStatTypeVerb, entityStatTypePrefix in entityStatTypeVerbs.items():
	# Generate the file path for the setup and uninstall file
	statSetupFile = Path(setupDir / f'setup{entityStatTypeVerb}Stats.mcfunction')
	statUninstallFile = Path(uninstallDir / f'uninstall{entityStatTypeVerb}Stats.mcfunction')
	# Generates the setup and uninstall commands
	generateScoreboardCommands(entityDump, entityStatTypePrefix, entityStatTypeVerb, statSetupFile, statUninstallFile)

# Generates all custom stats
for customStatTypeNoun, customStatTypePrefix in customStatTypeNouns.items():
	# Generate the file path for the setup and uninstall file
	statSetupFile = Path(setupDir / f'setup{customStatTypeNoun}Stats.mcfunction')
	statUninstallFile = Path(uninstallDir / f'uninstall{customStatTypeNoun}Stats.mcfunction')

	# Generates the setup and uninstall commands
	generateCustomScoreboardCommands(customDump, customStatTypePrefix, statSetupFile, statUninstallFile)

# Generates all general stats
for generalStatTypeNoun, generalStatTypePrefix in generalStatTypeNouns.items():
	# Generate the file path for the setup and uninstall file
	statSetupFile = Path(setupDir / f'setup{generalStatTypeNoun}Stats.mcfunction')
	statUninstallFile = Path(uninstallDir / f'uninstall{generalStatTypeNoun}Stats.mcfunction')

	# Generates the setup and uninstall commands
	generateGeneralScoreboardCommands(generalDump, generalStatTypePrefix, statSetupFile, statUninstallFile)

for file in os.listdir(setupDir):
	file = Path(setupDir / file)
	with open(file) as setupFile:
		writeToFile(setupFile.read(), Path(outputDir / 'setup.mcfunction'))

for file in os.listdir(uninstallDir):
	file = Path(uninstallDir / file)
	with open(file) as uninstallFile:
		writeToFile(uninstallFile.read(), Path(outputDir / 'uninstall.mcfunction'))
