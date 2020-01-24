#!/usr/bin/env python

import time

#Custom Imports
import mainfile
import quests
import stats
import config



def story():
    #mainfile.namefunc()
    #global name
    #print "You find yourself at a crossroads. The road splits into a three way before you. You can go left,right or straight."
    print "\nIt is an honor to meet you,", config.name + ".","\nI am Akendrial, third king of the third age of Vandaal. Long has prophecy fortold of your coming and long have I waited for you. Though, I'm afraid that prophecy was not specific as to who exactly you were.\n"
    race = raw_input("\nIf I may ask, of what ancestory are you?\n1. <Elf>\n2. <Human>\n3. <Dwarf>\n4. <Or something else entirely>\n")
    if race == '1':
        race = 'Elf'
        print "Excellent! An agile Elf, warrior of the wood! How I've dreamed of meeting your kind.\n"
    elif race == '2':
        race = 'Human'
        print "It is an honor to meet you then brother. I was quite the adventurer myself as a lad.\n"
    elif race == '3':
        race = 'Dwarf'
        print "Ah yes! The sturdy dwarf, miner of the stony depths. Your kind has ever been a mystery to us surface dwellers. An honor to meet you, to be sure.\n"
    else:
        race = raw_input("Interesting. So what ancestory are you exactly?\n")
        print "OH! Of course. Your kind are so rare here. Forgive me! I am meerly shocked by your presence.\n"

    land = raw_input("\nAnd if I may be so bold, from what land do you hail?\n")
    print "OH! Of course. I have heard tales of", land + ".", "It is a quite a magical land.\n My own kingdom was once as lush and beautiful as the tales of ", land, " but I'm afraid my land has since come under a horrible threat. I fear I must ask for you help in this matter.\n"
    answer = raw_input("Will you help us?")
    done = 0
    while done == 0:

        if answer == 'yes':
            print "Oh Thank you! Thank you so much. You are indeed the warrior of prophecy. You must set off at once, there is little time left. I have spoken with my people and many have already agreed to accompany you upon this dark journey.\n"
            done = 1
        elif answer == 'no':
            print "\nThe king in a sudden and uncontrollable rage rips a dagger out from beneath his kingly robes and stabs you and as you fall to the floor your vision fades and all goes black. \nGoodbye cruel world.\n"
            print "AAAAHHHHHHHHHH!"
            print "AAAAHHHHHHHHHH!"
            print "AAAAHHHHHHHHHH!"
            print "AAAAHHHHHHHHHH!"
            print "AAAAHHHHHHHHHH!"
            print "AAAAHHHHHHHHHH!"
            exit()

        else:
            print "I'm sorry", name, "but I'm afraid your language is still new to me and I didn't quite understand that.\n"
            answer = raw_input("Will you help us?\n")


    print "You soon depart the king's good company on your quest to defeat Rirakoor, the great purple dragon in the east.\nFor many years the dragon has plagued the land. It is your quest to defeat it.\n"
    print "Paused...\n\n"
    time.sleep(2)
    print "You've parted company with the king, ten of his most trusted knights joining you on your quest. You contemplate the lucidity of your decision a moment but then push it aside.\nHow hard could it be to kill a dragon after all.\n"
    print "The men follow you down, decked in armor and you realize that you have little to fight with. Luckily, the king well equipped you with treasure for your quest. Surely you can afford something.\n"
    print "You exit through the gate to the main city below. The buildings stretch on for blocks.\n"
    pause = raw_input("Press enter.\n")
    stores()
    return 0



#class Stores:

    #print "As you walk down the stree you glance around. To your right you notice a place called The Wizard's Hollow. No doubt, it is a mages shop.\nTo the left of it you see The Blacksmith's Armory and a few more shops down stands The Tamer's Den.\nHaving always been a freelancer you realize this is a chance to try a new style of combat or continue without a trade.\n"
    #store = raw_input("Where do you want to go?\n(Pick location based by number.)\n1. The Wizard's Hollow\n2. The Blacksmith's Armory\n3. The Tamer's Den\n4. Continue (without entering a shop)\n")
    #store = int(store)
    #def __init__(self, name, description):
      #  self.name = name
     #   self.description = description

    #class Wizardhollow(Stores):
       # self.

    #class Blacksmitharmory(Stores):

    #class tamerden(Stores):

   # class ignore(Stores):


def stores():
    print "As you walk down the stree you glance around. To your right you notice a place called The Wizard's Hollow. No doubt, it is a mages shop.\nTo the left of it you see The Blacksmith's Armory and a few more shops down stands The Tamer's Den.\nHaving always been a freelancer you realize this is a chance to try a new style of combat or continue without a trade.\n"
    store = raw_input("Where do you want to go?\n(Pick location based by number.)\n1. The Wizard's Hollow\n2. The Blacksmith's Armory\n3. The Tamer's Den\n4. Continue (without entering a shop)\n")
    #store = int(store)
    if store == '1':
        print "Shop currently under construction. Sorry. Oh well, nothing to do but get on the road.\n"
        quests.main()
        #print "You decide to check out The Wizard's Hollow, the place for all things magical and occult.\nSomething about the strange and mysterious, the unexplainable you could say, has always intrigued you.\n"
        #char userclass[7] = "Wizard";
        #cout << "Your userclass " <<userclass<< "is the Wizard.";}

    elif store == '2':
        print "Shop currently under construction. Sorry. Oh well, nothing to do but get on the road.\n"
        quests.main()
        #print "You decide, being typically more the warrior of sorts, to take a look at The Blacksmith's Armory.\nThe man's weapons are spoken of with praise for many leagues in all directions.\nMaybe he has something you'll find useful."
        #char userclass[8] = "Warrior";

    elif store == '3':
        print "Shop currently under construction. Sorry. Oh well, nothing to do but get on the road.\n"
        quests.main()
        #print "Even from here, blocks aways you can hear the rumble of the beasts, calling to you as your own inner animal has all these years.\nSomething about their sound reminds you of the yearning for freedom that you yourself took to the road in search for.\nThe choice is an obvious one or you."
        #char userclass[6] = "Tamer";

    elif store == '4':
        print "You choose instead to risk it on the road as you always have. Bare and beastly! Time to go.\n"
        quests.main()

    else:
        print "You suddenly feel in over your head. What the hell were you thinking. A dragon? Seriously?\nGlancing back you notice the guards aren't looking. You make a run for it. Soon you find yourself bolting through alleys and around street corners.\nThe guards give chase, but are too slow to keep up. You find yourself in an alley, seemingly safe until a shadowy figure appears at the other end.\n."
        print "He 'asks' for your money. You of course being of a rather greedy nature refuse. He swings. You swing back. He misses. You don't.\nYou both exchange another blow and you think you've got it in the bag when suddenly a sharp pain cuts through your back. He had a partner, and now as you tumble to the ground, drowning in your own blood, you get to watch them make off with your money. Shitty luck.\n"
        print "You've died. Obviously."
        return 0


#storyline()
#stores()
#mainfile.main()
#quests.skeletonkey(name)
#import mainfile #imports other file.
