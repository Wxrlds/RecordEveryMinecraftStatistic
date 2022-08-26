import csv

from utils.regexUtils import replaceXwithY
from utils.utils import displayNameFromRegistry, writeToFile


# "Type registry name","Stat name"
# "minecraft:custom","minecraft.custom:minecraft.animals_bred"

# /scoreboard objectives add <internalName> minecraft.<statType>:minecraft.<block/item/entity> "Display Name"
# /scoreboard objectives add b_minecraft_iron_sword minecraft.broken:minecraft.iron_sword "Broke Iron Sword"

# generateCustomSetupUninstallCommands(customDump, customStatTypePrefix, customStatTypeNoun, statSetupFile, statUninstallFile)
def generateCustomScoreboardCommands(dump, prefix, statSetupFile, statUninstallFile):
	with open(dump, newline='') as dumpCSV:
		dumpReader = csv.reader(dumpCSV, delimiter=',', quotechar='"')
		# Skip heading
		dumpReader.__next__()
		# For every row of the csv dump file
		for row in dumpReader:
			# The registryID of the custom stat
			registryID = row[1]

			# Generate the internal name
			internalName = replaceXwithY("minecraft.custom:", "", registryID)
			internalName = replaceXwithY("\.", "_", internalName)
			internalName = f'{prefix}_{internalName}'

			# Generate the displayName
			displayName = replaceXwithY("minecraft.custom:minecraft.", "", registryID)
			displayName = f'"{displayNameFromRegistry(displayName)}"'

			# Generate the setup command
			setupCommand = f'scoreboard objectives add {internalName} {registryID} {displayName}'

			# Write the setup command
			writeToFile(setupCommand, statSetupFile)

			# Generate the uninstall command
			uninstallCommand = f'scoreboard objectives remove {internalName}'

			# Write the uninstall command
			writeToFile(uninstallCommand, statUninstallFile)
