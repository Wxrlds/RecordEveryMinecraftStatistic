import csv

from utils.regexUtils import replaceXwithY


# Generates the setup command
# How the command should look like
# /scoreboard objectives add <internalName> minecraft.<statType>:minecraft.<block/item/entity> "Display Name"
# /scoreboard objectives add b_minecraft_iron_sword minecraft.broken:minecraft.iron_sword "Broke Iron Sword"
def generateScoreboardCommands(dump, prefix, statTypeVerb, statSetupFile, statUninstallFile):
	# Open the dump file
	with open(dump, newline='') as dumpCSV:
		dumpReader = csv.reader(dumpCSV, delimiter=',', quotechar='"')
		# Skip heading
		dumpReader.__next__()
		# For every row of the csv dump file
		for row in dumpReader:
			# The registryID of the item
			registryID = row[1]

			# Generate the internal name from prefix, underscore_ and the registry ID
			internalName = f'{prefix}_{replaceXwithY(":", "_", registryID)}'

			# Generate the statType
			statType = f'minecraft.{statTypeVerb.lower()}'

			# Generate the registry ID statType
			statTypeRegistryID = replaceXwithY(":", ".", registryID)

			# Generate the displayName
			displayName = f'"{replaceXwithY("_", " ", statTypeVerb)} {displayNameFromRegistry(registryID)}"'

			# Generate the setup command
			setupCommand = f'scoreboard objectives add {internalName} {statType}:{statTypeRegistryID} {displayName}'

			# Write the setup command

			writeToFile(setupCommand, statSetupFile)

			# Generate the uninstall command
			uninstallCommand = f'scoreboard objectives remove {internalName}'

			# Write the uninstall command
			writeToFile(uninstallCommand, statUninstallFile)


# Generates the setup command
# How the command should look like
# /scoreboard objectives remove <name>
# /scoreboard objectives remove b_minecraft_iron_sword
def generateUninstallCommand(dump, prefix, statUninstallFile):
	# Open the dump file
	with open(dump, newline='') as dumpCSV:
		dumpReader = csv.reader(dumpCSV, delimiter=',', quotechar='"')
		# Skip heading
		dumpReader.__next__()
		# For every row of the csv dump file
		for row in dumpReader:
			# The registryID of the item
			registryID = row[1]

			# Generate the internal name from prefix, underscore_ and the registry ID
			internalName = f'{prefix}_{replaceXwithY(":", "_", registryID)}'


# Generates the display name by removing the colon:
# and making the registry ID Title Case
def displayNameFromRegistry(registryName):
	# Replaces colon with space
	registryName = replaceXwithY(r':', r' ', registryName)

	# Replaces underscore with space
	registryName = replaceXwithY(r'_', r' ', registryName)

	# Removes the minecraft prefix
	registryName = replaceXwithY(r'minecraft', '', registryName)

	# Removes space before and after
	registryName = registryName.strip()

	# Converts registry name to title case
	registryName = registryName.title()
	return registryName


def writeToFile(command, file):
	with open(file, 'a') as outputFile:
		outputFile.write(f'{command}\n')
