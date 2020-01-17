#!/usr/bin/env python

#Parser for questfile
#7Mar2017

import re
#Initial prototype complete. Add additional functionality.


#TODO
#account for functions - accomplished
#account for print statements - accomplished
#incorporate dictionary functionality - accomplished

#Later
#account for input
#account for function calls (time, etc)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tab = '\t'
#Set a count to current. Have every line count the tabs. If it doesn't match then increment or de-increment based on the new count. As long as its greater then increment up.
#If less increment down. If it ever matches then that function has ended. Every time it changes, add it to the current key in dictionary.
for line in fh:
	print line
	cnt = re.findall('\t',line)
	print cnt
	print len(cnt)
	#mastercnt start at 0. Finds a function. Count the tabs. 
	#
	#	only account for functions for prototype
	#		later will need to account for loops and if statements
	#if function, count the tabs. Compare to previous tabs. If more or less, then increment master count accordingly. 
	#	Create key in dictionary to account for new function.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for line in fh:
	if re.search(r'[\sa-zA-Z]+#',line):
		#print "Comment line:"
		#print line
		continue
	if line.startswith('#'):
		#print "Comment Line:"
		#print line
		continue
	if " = " in line:
		continue
	if " == " in line:
		continue
	if 'time.sleep' in line:
		continue
	#Locates [print statements] and pulls out only text.
	if 'print' in line:
		line = line.rstrip()
		line = line.lstrip()
		line = line.replace('#', '')
		line = line.replace('print', '')
		line = line.replace('"', '')
		#line = line.replace('\\n', ' ') #The replacement here will result in very long statements. I may be better off splitting sentences on \\n and then storying them.
		#print line
		lines = line.split('\\n')
		#print lines
		prints.append(line)
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
		adventure[curfunc]=[]
		functions.append(line)

#FUCK YES! THIS WORKS!
print '\n\nPrinting dictionary:\n', adventure
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#Now I need to attach the print statements to their functions.
#Best way to do this.
	#1. Store print statements with the function in a list based on the count. I.e. Count is stored in list first. Then compare for each print statment.
	#	If cnt on print statement is equal to list then append it.



#Now for reading into the program.
#This works. It allows for the printing from the text file.
def tempfunc(d,key,valuenum,valueindex):
	print len(d[key])
	print key
	if len(d[key]) > 1:
		temp = d[key][valuenum]
		if type(temp) == str:
			print temp
		else:
			if valueindex == 'a':
				for i in temp:
					print i
			else:
				print temp[valueindex]
	else:# length of key is only one
		if type(d[key]) == str:
			print d[key][valuenum]
		elif valueindex == 'a':
			for i in d[key][valuenum]:
				print i
		else:
			print d[key][valuenum]

#Testing function.		
def game():
	library = {'ocean':['fish','swim'],
	'forest':['wander','climbtree'],
	'cabin':['eat','sleep']
	}
	places = ['ocean','forest','cabin']
	while True:
		cnt = 1
		print "Where to?"
		for i in places:
			print str(cnt)+'. '+i
			cnt+=1
		choice = raw_input('\n')
		if choice not in places:
			choice = places[int(choice)-1]
		'''
		if choice == '1':
			choice = places[0]
		elif choice == '2':
			choice = places[1]
		elif choice == '3':
			choice = places[2]
			'''
		if choice in places:
			cnt = 1
			print "What to do?"
			for line in library[choice]:
				print str(cnt)+'. '+line
				cnt+=1
		choice2=raw_input('\n')
		if choice2 not in library[choice]:# == '1':
			choice2 = library[choice][int(choice2)-1]
		tempfunc(adventure,choice2,0,0)



game()

#tempfunc(adventure,'swim',0,'a')
#tempfunc(adventure,'swim',0,1)
#tempfunc(adventure,'wander',0,'a')
#tempfunc(adventure,'climbtree',0,0)
#tempfunc(adventure,'climbtree',1,'a')