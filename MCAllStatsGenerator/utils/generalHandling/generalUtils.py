import csv


# Writes the general stats to file
# This is mostly hardcoded because there is
# no real way to dump this data (yet?)
# and did not change in however many
# Minecraft versions so ¯\_(ツ)_/¯


def generateGeneralScoreboardCommands(dump, prefix, statSetupFile, statUninstallFile):
	# Write the setup command
	with open(statSetupFile, 'a') as setupOutpuFile:
		with open(dump, newline='') as dumpCSV:
			dumpReader = csv.reader(dumpCSV, delimiter=',', quotechar='"')
			# Skip heading
			dumpReader.__next__()
			for row in dumpReader:
				displayName = row[0]
				internalName = row[1]
				setupCommand = f'scoreboard objectives add {prefix}_{internalName} {internalName} "{displayName}"\n'
				setupOutpuFile.write(setupCommand)

	with open(statUninstallFile, 'a') as uninstallOutpuFile:
		# Write the uninstall command
		with open(statSetupFile, 'a') as setupOutpuFile:
			with open(dump, newline='') as dumpCSV:
				dumpReader = csv.reader(dumpCSV, delimiter=',', quotechar='"')
				# Skip heading
				dumpReader.__next__()
				for row in dumpReader:
					internalName = row[1]
					uninstallCommand = f'scoreboard objectives remove {prefix}_{internalName}\n'
					uninstallOutpuFile.write(uninstallCommand)
