#!/usr/bin/python
# The Wizard's Hollow
#The Blacksmith's Armory
#The Tamer's Den
import config
import questcontrolfile
config.clear()



class Shop():

	count = ['1.','2.','3.','4.','5.','6.','7.','8.','9.','10.']

	def __init__(self, name, description, artform, merchandise):
		self.name = name
		self. description = description
		self.artform = artform
		self.merchandise = merchandise

	def clerk(self):
		choice = raw_input("1. Buy\n2. Sell\n")
		if choice == '1':
			self.buy()
		else:
			pass

	def buy(self):
		print "Excellent! I have some wonderful merchandise to show you today."
		for i,c in zip(self.count, self.merchandise):
			print i,c
		#self.present()

	def sell(self):
		pass
		#print inventory

	def present(self):
		choice = raw_input("")
		questcontrolfile.funccall(choice, "shortsword", "longsword", "spear", "bow", "shield")
		






class Armory(Shop):

	merchandise = ["Shortsword", "Longsword", "Spear", "Bow", "Shield"]
	name = "The Blacksmith's Armory"
	description = "\nYou enter the armory to find yourself in a surprisingly nice room. A door leads to the back where the smell of iron and soot seeps in from. Obviously, the armory itself is in the back. The clerk at the front desk is a bear of a man and looks battle worn and hard, decorated more by scars than freckles.\n"
	artform = "Weapons"

	def __init__(self):
		pass
	
	def enter(self):
		print self.description
		print "'Welcome to my armory friend! All weapons expertly crafted by yours truly!' He bellows as you look around the store.\n'Looking for anything in particular? All my blades are freshly sharpened!'\n"
		self.clerk()



class Hollow(Shop):

	merchandise = ["Fire", "Ice", "Wind", "Heal", "Revive"]
	name = "The Wizard's Hollow"
	description = "\nYou enter the Wizard's Hollow and immediatly begin to wonder if being a wizard is the best career path for you. The place is unnervingly dark and once you're eyes finally adjust you see the walls are lined with shelves and jarred specimens.\nA rotting smell draws your eyes to one corner of the store where a floating bat stares at you through pale eyes in a tank...\n"
	artform = "magic"
		
	
	def __init__(self):
		pass

	def enter(self):
		print self.description
		print "\nA creepy old hag of a lady approaches from behind, more silent than a mouse.\n'Welcome to", self.name + "!' You jump when she speaks to you, surprised by how close she got without you seeing her.\n\n'May I assist you?' she asks.\n You find yourself staring at her glass eye..."
		self.clerk()

	


class Pets(Shop):

	merchandise = ["Hawk", "Rattlesnake", "Monitor Lizard", "Pony", "Goat", "Hunting Dog"]
	name = "The Tamer's den"
	description = "\nThe first thing you notice as you walk into the Tamer's Den, is the smell of urin and an assortment of wet animal smells, mostly dog.\nThe place is huge, more a barn than store, and just past the front desk it stretches back into pens and stables. A large fence lines the ceiling and comes down the walls into atriaries for the magnificent assortment of birds the owner sports.\nBehind the desk a thin pale man with bright blue eyes stares at you eagerly.\n"
	artform = "Companions"

	def __init__(self):
		pass
	
	def enter(self):
		print self.description
		print "'May I help you? Normally, we have quite the wonderful selection but I'm afraid most of my animals are actually purchased already. Supply and demand you know...\n We do however, have some variety left if you'd like to look.'\n"
		self.clerk()



def decision():
	choice = raw_input("Where do you want to go?\n1. Wizard's Hollow\n2. Blacksmith's Armory\n3. Tamer's Den\n")
	if choice == '1':
		WH.enter()
	elif choice == '2':
		BA.enter()
	elif choice == '3':
		TD.enter()
	else:
		print "Incorrect choice\n"


WH = Hollow()
BA = Armory()
TD = Pets()
decision()

#class shop(self):


#hollow = shop(dffgd, dfdfs,ddvvd)

#armary = shop()
#armary.desciption = vvsddv

#shop to enter = *armary

#shoptoenter.enter()
#shoptoenter = *hollow
#shoptoenter.enter()



