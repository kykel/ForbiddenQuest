#!/usr/bin/env python
import re
import time

filename = 'treasurehunt_storyline.txt'
fn = open(filename,'r')
lines = []

def func1():

	for line in fn:
		lines.append(line)

	for line in lines:

		#Locates time.sleep statements
		if 'time.sleep' in line:
			sleep = re.findall(r'(?<=sleep\()[0-9]+(?=\))', line)

			sleep = int(str(sleep[0]))
			print sleep
			#time.sleep(int(sleep))
		line = line.rstrip()

		#Splits print statements by newlines.
		moarlines = line.split('\\n')
		for l in moarlines:
			print l
func1()
fn.close()