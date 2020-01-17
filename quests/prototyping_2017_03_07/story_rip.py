#!/usr/bin/env python
#A throw-away script for ripping the storyline(print statements) out of my text game.
#Once finished ripping out the storyline, archive this script.


import re
#7mar2017
#Opening quest file.
questfile = 'treasurehunt.py'
fh = open(questfile, 'r')
#Opening text file to write to.
fw = open("treasurehunt_code_removed.txt", 'w')
#writes only to variables file
fv = open("treasurehunt_variable_assignements.txt", 'w')
#function count
cnt = -1
flags = -1
#writes a file for functions only
ff = open('treasurehunt_functions.txt','w')
#Writes storyline/functions only
fs = open('treasurehunt_storyline.txt','w')
leftover = open('treasurehunt_leftovers', 'w')

for line in fh:
	written = 0
	#Locates [time.sleep] statements.
	if 'time.sleep' in line:
		fs.write(str(cnt)+' -> '+line)
		fw.write(str(cnt)+' -> '+line)
		written = 1

	#Locates [print statements] and pulls out only text.
	if 'print' in line:
		line = line.rstrip()
		line = line.replace('#', '')
		line = line.replace('print', '')
		line = line.replace('"', '')
		fs.write(str(cnt)+'   >'+line+'\n') #Write to storyline file before removing newlines.
		line = line.replace('\\n', ' ')
		fw.write('---> ' + line+ '\n') #Write to code_removed file.
		written =1
	
	#Locates and saves [variable assignment statements].
	if " = " in line:
		#print "Variable assignment located."
		fv.write('---> ' + line)
		written =1
		
	#Locates pass statements and writes them for location of empty functions.	
	if re.search(r'\s+pass\s+', line):
		#print line
		fw.write('     ' + line)
		written = 1

	#Locates [functions] and saves them.
	if re.search(r'[a-zA-Z]+\([a-zA-Z0-9]*\)\:', line):
		cnt += 1
		#print line + '\n'
		fs.write('\n'+str(cnt)+' --> '+line)
		fw.write('\n' + str(cnt) + ' > ' + line)
		fv.write(line+'\n')
		ff.write(str(cnt)+' > '+line)
		leftover.write(line)
		written = 1
		

	#Locates [if statements] and saves them.
	if re.search(r'if [a-zA-Z0-9\_\.\(\)]+', line):
		if 'print' in line:
			pass
		elif '#' in line:
			pass
		else:
			#print "REGEX matched:", line
			fw.write('	 ' + line)
		written = 1
	#Locates and writes any leftover lines not accounted for.
	if written == 0:
		leftover.write(line)
fh.close()
fw.close()
fv.close()
fs.close()
ff.close()
leftover.close()
