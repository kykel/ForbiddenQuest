#!/usr/bin/env python

#24OCT2018 - Current capabilities: Load quest, start quest, branch traversal
#28OCT2018 - Flag added. (keyitem, gold, item, damage, weapon)
#28OCT2018 - Weapons, keyitems, keyitem flag and gold all add to inventory correctly. Items do not need to be added to tracker, only recorded in quest saves.
#27NOV2018 - Need to finish WIN condition. Need to account for items in tracker.
#28NOV2018 - Added win_condition flag, adjusted running() while loop to match. Added in quest load capability.
#29NOV2018 - Added delete_keyitem function under Special Rooms but it needs to be finished.





import json
import subprocess
import sys, os, player

class quest_parser:
    
    def __init__(self, questname, player):
        self.questdata = {}
        self.currentbranch = ''
        self.branchname = ''
        self.branchdata = {}
        self.questname = questname
        self.quest_dir = 'quest_saves/'
        self.tracker = {}
        self.player = player
        self.win_condition = False
        
    #loads in the json dictionary for the new quest.
    def data_load(self):
    	self.questname = self.questdata['questname']
    	self.treename = self.questdata['treename']
    	self.branchname = self.treename
    	self.currentbranch = "{"+self.questname+"}:"+"["+self.treename+"]"
    	self.previousbranch = ''
    	self.questtree = "{"+self.questname+"}:"+"["+self.treename+"]"
    	self.branchdata = self.questdata[self.currentbranch]
    
    #Sets up a new quest.	
    def new_quest(self):
    	with open(self.quest_dir+self.questname) as data_file:
    	    self.questdata = json.load(data_file)
    	self.data_load()
    	self.build_tracker()
	    	    
    #Begins gameplay of quest.
    def start_quest(self):
        self.clear()
        print "Quest: " + self.questdata['questname'] + '\n'
        print "You arrive at {}.".format(self.questdata['treename'])
        self.player.questlog[self.questname] = "Incomplete"
        self.running()
	
    #Main program function
    def running(self):
        branchtext = self.secondarytext
        while self.win_condition == False:
            self.quest_save()
            print "Location: {}\n".format(self.branchname)
            #Checks to see if branch has changed and updates branch text accordingly
            if self.currentbranch != self.previousbranch:
                branchtext = self.check_tracker()
            branchtext()
            self.find_treasure()
            self.check_flag()
            self.damage_room()
            #self.boss_battle() - Need to add in a boss battle functionality
            self.death_text()
            if self.player.hp <= 0:
                print "\nGame Over.\n"
                break
            self.change_branches(self.pointers())
            self.clear()
        
    #Prints out introtext
    def introtext(self):
        print self.branchdata['introtext'], "\n"
     
    #Prints out secondarytext    
    def secondarytext(self):
        print self.branchdata['secondarytext'], "\n"
    
    #Checks and returns the next pointer. - Need to finish WIN flag.
    def pointers(self):
        #Temporary stand in - Need to fix WIN flag to return to main game. Move WIN flag to change_branches()
        if 'WIN' in self.branchdata['pointers']:
            return 'WIN'
        elif 'DEAD END' in self.branchdata['pointers']:
            return 'DEAD END'
        elif 'question' in self.branchdata:
            print self.branchdata['question']
        else:
            print "Where do you want to go?"
        print " : ".join(self.branchdata['pointers']), "\n"
        ui = self.userInput()
        if ui in self.branchdata['pointers']:
            return ui
        elif ui == 'exit':
            sys.exit()
        elif ui == 'inventory':
            self.player.show_inventory()
            return ''
        else:
            return ''
        
    #Returns input from user   
    def userInput(self):
        return raw_input()
    
    #Traverses tree branches - takes input as x and adjusts branch as necessary.
    def change_branches(self, x):
        #Assigns the current branch as previous for tracking
        self.previousbranch = self.currentbranch
        #Goes back to parent branch
        if x.lower() == 'back':    
            branchparts = self.currentbranch.split(':')
            self.currentbranch = ":".join(branchparts[:-1])
            self.branchdata = self.questdata[self.currentbranch]
        #Allows user to select any branch within the branch tree.
        elif x.lower() == 'return':
            branchparts = self.currentbranch.split(':')
            printparts = self.currentbranch.split(':')[2:]
            printparts.insert(0,self.treename)
            print "Choose an option:\n", " : ".join(printparts), "\n"
            ans = self.userInput()
            for i in branchparts:
                cnt = branchparts.count(i)
                if cnt > 1:
                    print "*** Duplicate branch names exist in tree. Defaulting to top most branch. ***\n\n"
                    break
            for i in branchparts:
                if ans.lower() in i.lower():
                    branchparts = branchparts[:branchparts.index(i) + 1]
                    self.currentbranch = ":".join(branchparts)
                    self.branchdata = self.questdata[self.currentbranch]
                    self.wait()
                    break
                else:
                    "Incorrect option. Try again.\n"
        #Returns to parent branch of the DEAD END branch.
        elif x == 'DEAD END':
            print "Nothing further to do here.\n"
            #self.branchdata['pointers'].add('passed')
            branchparts = self.currentbranch.split(':')
            self.currentbranch = ":".join(branchparts[:-1])
            self.branchdata = self.questdata[self.currentbranch]
            self.wait()
            self.previousbranch = self.currentbranch
        #Enters a new child branch
        elif x in self.branchdata['pointers']:
            #self.previousbranch = self.currentbranch
            self.currentbranch += ":" + x
            self.branchdata = self.questdata[self.currentbranch]
        elif x == 'WIN':
            print "\n\nQuest Completed.\n\n"
            self.player.questlog[self.questname] = 'Complete'
            self.wait()
            self.win_condition = True
        else:
            print "Incorrect choice. Try again.\n"
            self.wait()
        #Grabs the very last index of the branch (branchname)
        self.branchname = self.currentbranch.split(':')[-1]
    
    #########################################################################################################################
    
    #Special Rooms
    
    #########################################################################################################################
    
    #Checks branch for treasure and awards it to player            
    def find_treasure(self):
        if 'keyitem' in self.branchdata:
            print self.branchdata['itemintrotext']
            self.player.add_keyitem(self.branchdata['keyitem'], self.branchdata['keyitemdescription'])
            del self.branchdata['keyitem']
            
        if 'gold' in self.branchdata:
            print self.branchdata['itemintrotext']
            self.player.add_gold(self.branchdata['gold'])
            del self.branchdata['gold']
            
        if 'weapondict' in self.branchdata:
            print self.branchdata['itemintrotext']
            self.player.add_item(self.branchdata['weapondict']['name'], self.branchdata['weapondict'])
            del self.branchdata['weapondict']
            
    #Checks for a room for damage and damages player.        
    def damage_room(self):
        if 'damage' in self.branchdata:
            print "You take {} damage.".format(self.branchdata['damage'])
            hp = self.player.take_damage(self.branchdata['damage'])
            print "You have {} life left.".format(hp)

    #Prints out death text and sets player hp to 0
    def death_text(self):
        if 'deathtext' in self.branchdata:
            print self.branchdata['deathtext']
            self.player.hp = 0
    
    #Need to account for the removal of key items.        
    def delete_keyitem(self):
        pass

    #########################################################################################################################
    
    #Flags
    
    #########################################################################################################################
    
    #Tracker needs to account for key situations only happening once. I may need to adjust this in quest_build.py. Maybe add final result of flag after flag has been met.
    
    #Checks and calls flags.        
    def check_flag(self):
        if 'flag' in self.branchdata:
            if self.branchdata['flagcondition'][0] == 'keyitem':
                self.flag_keyitem()
    
    #Checks and changes pointers to reflect keyitem flag activation
    def flag_keyitem(self):
        keyitem = self.branchdata['flagcondition'][1]
        if keyitem in self.player.keyitems:
            if 'DEAD END' in self.branchdata['pointers']:
                for i in self.branchdata['flagpointer']:
                    self.branchdata['pointers'].append(i)
                self.branchdata['pointers'].remove('DEAD END')
                try:
                    self.branchdata['question'] += " " + self.branchdata['flagquestion']
                except:
                    self.branchdata['question'] = self.branchdata['flagquestion']
        self.wait()
        
    #########################################################################################################################
    
    #Utilities
    
    #########################################################################################################################
    
    #Builds a tracker for the quest.
    def build_tracker(self):
        for key,val in self.questdata.items():
            if key.startswith(self.questtree):
                self.tracker[key] = 'unvisited'
    
    #Checks if branch has been visited and returns either introtext or secondary text respectively.    
    def check_tracker(self):
        if self.tracker[self.currentbranch] == 'unvisited':
            self.tracker[self.currentbranch] = 'visited'
            return self.introtext
        else:
            return self.secondarytext
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait(self):
        raw_input("\nPress enter to continue.")
        
    #########################################################################################################################
    
    #Saves and Load
    
    #########################################################################################################################
    
    #Saves the current quest
    def quest_save(self):
        self.questdata['tracker'] = self.tracker
        self.player.questlog[self.questname] = ['Incomplete',self.questdata]
	
	#Load previous quest
    def load_quest(self):
        self.questdata = self.player.questlog[self.questname][1]
        self.tracker = self.questdata['tracker']
        self.data_load()
	    
		
		

if __name__ == "__main__":
    #import player
    p = player.Player()
    q = quest_parser("test quest.json", p)
    q.new_quest()
    q.start_quest()