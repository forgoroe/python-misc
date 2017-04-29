#Rename files in the current directory that end with /\(\d+\)/ to files that start with the \d+ 
#followed by '-' and the filename without the number

import os, re

print('Initial filenames', '\n', os.listdir('.'))

for fileName in os.listdir('.'):
	match = re.search(r'\(.+\)', fileName)

	if match is not None:
		number = match.group(0)[1:-1]
		filenameWithoutNumbers = ''.join(fileName.split(match.group(0)))
		os.rename(fileName, fileName.replace(fileName, number + ' - ' + filenameWithoutNumbers))

print('Final filenames', '\n', os.listdir('.'))