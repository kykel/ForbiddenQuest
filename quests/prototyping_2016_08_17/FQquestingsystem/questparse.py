#!/usr/bin/python

#Need to add in word parser to parse tabular quest format
#or look into csv module for using spreadsheet

#Components
##############
# Either parse tabular quest file or uses imported csv module
# Do I want it to pull the quests real time or store them?
# > I could store entire quest file in a list or dictionary and pull as needed
# Returns data when called by 'main.py' script
# Does not print, only processes data

def readin(x):
	#Takes in file and stores in a list
	quests=[]
	fh = open(x,'r+')
	for line in fh:
		#Splits every line via tabs and strips off newlines
		line = line.strip().split("\t")
		for word in line:
			#Stores each index to a list in chronological numerical order.
			quests.append(word)
	return quests

#function that waits for a reference number and searches file.
