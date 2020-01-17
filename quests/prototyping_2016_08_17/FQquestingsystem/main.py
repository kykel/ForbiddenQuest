#!/usr/bin/python

#All functionality should ultimately be called from this file.
#Use endless while loop to keep functions looping on themselves
#until exit command triggered.

import questparse
import controls

#Components:
################
# While loop
# All input pulls from controls file
# All storyline is pulled from questparse script and printed through here
def main():
	quests = []
	currentoption = 1
	#parse format
	#version#intro#options(point to a version)
	#quest = raw_input("Which quest to load?")
	quest = "questfile.txt"
	new = questparse.readin(quest)
	currentquest(new,currentoption)


def currentquest(new,curr):
	#Function takes in list of all quest options for the current quest. In example: quest 1 (currentoption, renamed curr inside this function)
	index = 0
	curqst = []
	for item in new:
		if item.startswith(str(curr)):
			curqst.append(item)
			curqst.append(new[index+1])
		index+=1
	print curqst


	while True:
		def gameprint():
			next = curr+2
			options=len(curr)
			print new[curr+1]
			#after print, pull all associated options.
			#for associated options, pull all appended (.num)(ex. cur"."len(1)") to the currentquest(curr)
			

			#WIP
			#WIP
			#WIP

			for item in curqst:
				i = 0
				if (item == i) and (item == len(curr))

			#add conditional that length should not be more than curr + concatenation or period and one additional number,
			#any number that has more than a length of curr + 2, should not be pulled.
			#have the gameprint() print out all options
			#	maybe a for loop that pulls only options of this currentquest flag into a list and only this list is used per cycle, then resets
			#pipe all of this(curr and options) into funccall() and return result
			#Now what do I do with result.
			#	I have a string with option in it.
			#	If I have funccall, return a function with quest number referenece, then recall gameprint() with that function
			#	So all funccall should do is return the particular reference picked back to gameprint()
			#	And then gameprint reruns the entire processself.
		
		def reroute():
			
			
		

		gameprint()
		break

def funccall(choice, option1, option2, option3, option4, returnoption):
    if choice == '1':
        return option1()
    elif choice == '2':
        return option2()
    elif choice == '3':
        return option3()
    elif choice == '4':
        return option4()
    else:
        "\n\nI do apologize but your action has resulted in a temporal fracture. Returning to a safer 'stamp' in time...\n\n"
        config.pause()
        config.clear() 
        returnoption()


if __name__ == '__main__':
	main()



