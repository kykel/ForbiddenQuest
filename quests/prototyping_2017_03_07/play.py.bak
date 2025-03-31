#!/usr/bin/env python

import re

#09MAR2017
#Look into json and csv for quest text file.



#Declare needed variables
cnt = -1
functions = []
prints = []
adventure = {}
mastercnt = 0
#Opening quest file.
#questfile = 'treasurehunt.py'
questfile = "adventure.txt"
fh = open(questfile, 'r')

mastertabcnt = 0
mgtdict = {}
storagedict = {}

for line in fh:
	tabs = re.findall('\t',line)
	tabcnt = len(tabs)
	curtab='tab'+str(tabcnt)

	#Locates and skips [comments] with preceding spaces or words.
	if re.search(r'[\sa-zA-Z]+#',line):
		#print "Comment line:"
		#print line
		continue
	#Locates and skips [comments].
	if line.startswith('#'):
		#print "Comment Line:"
		#print line
		continue
	#Locates and skips [variable assignment].
	if " = " in line:
		continue
	#Locates and skips [if statements].
	if " == " in line:
		continue
	#Skips [time.sleep].
	if 'time.sleep' in line:
		continue
	#Locates [print statements] and pulls out only text.
	if 'print' in line:
		line = line.rstrip()
		line = line.lstrip()
		line = line.replace('#', '')
		line = line.replace('print', '')
		line = line.replace('"', '')
		lines = line.split('\\n')
		#print lines
		prints.append(line)

		### Debugging - not properly assigning last print statement

		#print "Line:", line 
		#print "tabcount:",tabcnt
		#print "current tab:", curtab
		#print "master tab count:", mastertabcnt
		#### Prototyping ####
		if tabcnt == mastertabcnt:
			if curfunc not in adventure:
				print "no function for this line exists."
			else:
				if len(lines)>1:
					adventure[curfunc].append(lines)
				else:
					adventure[curfunc].append(line)
		#This doesn't need to be in just the print statement. I may need to put this elsewhere.
		elif tabcnt < mastertabcnt:
			#print line
			if tabcnt >= 1:
				curtab = 'tab'+str(tabcnt-1)
			else:
				print "Line outside of function:", line
				continue
				#curtab = 'tab'+str(0)
			#print curtab
			mastertabcnt = tabcnt
			curfunc = mgtdict[curtab]

			if len(lines)>1:
				adventure[curfunc].append(lines)
			else:
				adventure[curfunc].append(line)
		else:
			if len(lines)>1:
				adventure[curfunc].append(lines)
			else:
				adventure[curfunc].append(line)
		
		

	#Locates [functions] and saves them.
	if re.search(r'def [a-zA-Z_]+\([a-zA-Z0-9]*\)', line):
		curfunc = line
		curfunc = curfunc.rstrip()
		curfunc = curfunc.lstrip()
		curfunc = curfunc.replace('def ','')
		curfunc = curfunc.replace('()','')
		##### Prototyping ####
		if curtab in mgtdict:
			if mgtdict[curtab] == curfunc:
				print 'duplicate function - error'
			else:
				mgtdict[curtab] = curfunc
		elif curtab not in mgtdict:
			mgtdict[curtab] = curfunc
		mastertabcnt=tabcnt+1

		adventure[curfunc]=[]
		functions.append(line)

#FUCK YES! THIS WORKS!
print '\n\nPrinting dictionary:\n', adventure

#Testing
print '\n\nPrinting management dictionary:\n', mgtdict