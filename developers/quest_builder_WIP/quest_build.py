#!/usr/bin/env python

import json


#readline.parse_and_bind('tab: complete')
#readline.parse_and_bind('set editing-mode vi')

#Quest Builder
#Basic program to walk the user through a quest building scenario.

#9May2018 - Just finished updating the help menu on Basic information. 
#14May2018 - Completed multiple functions. Currently working on yesORno function.
#14May2018 - Finalized data format structure of nested dictionaries. Modified prompt features. Need to finished modifying builder function.
#16May2018 - Lots finished. Completed save and load features. Completed linear pivoting.
#17May2018 - Fixed save and load functionality. Found bug in change_branch(). Currently building out yes/no experimental functions.
#20May2018 - Removed yesorno branch functionality. Converted yes/no option into a branch and added features to branch_construction builder. Completed item and yes/no functionality.
#24May2018 - Successfully created first draft of program to include yes/no, multi-options, trap damage, items, etc. Revamped print function to make it cleaner.
#8-18OCT2018 - Made lots of adjustments to code. Flag system now built in. Now need to update the quest parser. To add: WIN functionality. LOOP functionality, combat.
#18OCT2018 - Added cancel/delete to flag option. Added WIN to pointers.
#22OC2018 - Added in a branch checker on EXIT. Branch dictionaries are created as pointers are created now.
#26OCT2018 - ADD: a master dictionary that tracks all keyitems. Keyitems are not allowed to be duplicated at any point within the game.

#29NOV2018 - Minor changes to base functionality. Added flag item outcome.

'''
Additional features:
FLAG: randomizer
FLAG: LOOP



'''

import os, sys

class Questbuilder():
    
    def __init__(self):
        self.savefile = ''
        self.storydict = {}
        self.prompt_options = ['Menu> ']
        self.current = self.prompt_options[0]
        self.prompt = self.prompt_options[0]
        self.branches = []
        self.running = {}
        self.savepoint = ''

    def menu(self):
        while True:
            self.clear()
            print "Welcome to the Quest Builder Program."
            print "If you need assistance at any time on the development, formatting, or options within the build program, simply type HELP for your options, or MANUAL for a more indepth reference."
            print "All quests automatically save at the close of a quest tree. You can save at any point by simply typing SAVE."
            print "Most options presented in game will be numbered. For ease of use, use the numbers for choice selection."
            print "Selecting the tutorial option will have walk you through the first quest tree to teach you the basic structure and format when building your quests."
            print "Menu:\n1. New Storyline\n2. Load Storyline\n3. Save Current Working Storyline\n4. Open Manual\n5. Tutorial\n6. Exit\nAny other key to return to previous prompt\n"
            o = self.input_prompt()
            print "option:", o
            if o == '1': self.newstory()
            elif o == '2': self.load()
            elif o == '3': self.save()
            elif o == '4': self.helpmenu()
            elif o == '5': self.tutorial()
            elif o == '6': self.exit()
            else:
                break

    #def menu(self, menutext, options):
        # pass function dict as:
        # >>> x = { '1': self.newstory , '2': self.load , '3': self.save , '4': self.helpmenu , '5': self.tutorial , '6': self.exit }
    #    while True:
    #        self.clear()
    #        print(menutext)
    #        try:
    #            x[self.input_prompt()]()
    #        except KeyError:
    #            break


    def helpmenu(self):
        self.clear()
        print "SAVE:        Saves the current working storyline to the original annotated save file (name of quest)."
        print "MANUAL:        Loads the manual. This contains indepth knowledge on how the program works and how quests are formatted, as well as how to change the format if you wish."
        print "LOAD:        Loads a previously started storyline. Will present all available saved quests first."
        print "MENU:        Returns to main menu. This will not lose any current working data."
        print "OPTIONS:        Prints current available prompt options."
        print "TUTORIAL:    Uses a descriptive step by step tutorial to walk you through the development of your first quest tree within your storyline."
        print "\nBasic Format:"
        print "Tree: Main locations in a quest. Typically larger geographical locations.\nExample: A mansion has the building itself, the grounds, and potential side areas such as a garden or graveyard."
        print "branch: Areas within a main location.\nExample: A mansion has rooms. Gardens have various areas or quadrants. A graveyard may have a tomb or multiple you can enter."
        print "Pointer: These are avenues you can travel through from your current location. Basically connectors from trees to branches or branches to other branches.\nExample: A mansion may have a main floor, long hallways, a basement, or upstairs but there may also be branches within these adjacent places such as additional rooms or patios."
        print "NOTE: Keep in mind that the tree, branch, pointer structure is more for reference. See MANUAL for more in-depth information."

    #Save function.
    def save(self):
        self.clear()
        try:
            print "Save time"
            if self.savefile == '':
                self.savefile = raw_input("Enter savefile name:\n")#+".txt"
            else:
                self.storydict['savepoint'] = self.savepoint
            
            if self.prompt not in self.storydict:
                self.storydict[self.prompt] = self.running
            else:
                self.merge_dictionaries()
            if self.savefile == self.storydict['questname']:    
                self.savefile = os.getcwd()+'/quest_saves/'+self.savefile+'.json'
            else:
                print "Save file:\n"+self.savefile+"\n"
            if os.path.isfile(self.savefile):
                print "You are about to overwrite a previously saved quest."
                ans = raw_input("Is this okay? [y/n]\n")
                if (ans.lower() == 'y') or (ans.lower() == 'yes'):
                    pass
                else: 
                    print "Not saving."
                    return 0
            with open(self.savefile, 'w') as outfile:
                json.dump(self.storydict, outfile)
            print "File successfully saved."
            #self.wait()
        except Exception as e:
            print "Failed to save file. Try again."
            print e
        self.wait()

    #Load function.
    def load(self):
        self.clear()
        print "Load time.\nNote: Names are case sensitive."
        path = os.getcwd() + '/quest_saves/'
        while True:
            print "\nAvailable save files:\n\n","    ".join(os.listdir(path)), "\n"
            loadfile = raw_input("Enter the name of your Quest: ")
            self.savefile = path+loadfile+'.json'
            if loadfile+'.json' in os.listdir(path):
                break
            else:
                self.clear()
                print "Incorrect load file name."
                self.wait()
                return 0
        with open(self.savefile) as data_file:    
            self.storydict = json.load(data_file)
        #self.wait()
        self.prompt = self.storydict['savepoint']
        self.prompt_options = self.storydict['savepoint'].split(':')
        self.current = self.prompt_options[-1]
        self.running = self.storydict[self.prompt]
        self.savepoint = self.prompt
        print "Quest successfully loaded."
        self.wait()
        self.builder()
        
    #Start new game.
    def newstory(self):
        
        '''
        - Stores questname and first tree(include data) to the storydictionary
        - Creates a savefile name based on questname
        - Stores the questname and first tree(intro/secondarytext, pointers) to the quest builder prompt
        
        - Calls builder
        '''
        
        self.clear()
        #Handles setup of questname and savefile
        while True:
            quests = [i.lower()[:-5] for i in os.listdir(os.getcwd()+'/quest_saves/')]
            questname = raw_input("Enter quest name (This is what will show in the quest master's roster as well as the save file name):\n")
            if questname.lower() in quests:
                print "Quest already exists. Try a new name.\n"
            else:
                print "New questname: " + questname
                break
        self.storydict['questname'] = questname
        print self.storydict['questname']
        #Autofill conditional for testing.
        if self.storydict['questname'] == '':
            self.storydict['questname'] = 'Shadowland'
            print self.storydict['questname']
        self.savefile = self.storydict['questname']
        self.prompt_options[0] = "{" + self.storydict['questname'] + "}"
        
        #Handles setup of first tree
        print "\nAs the quest begins, where is the first location you start at? This is the Quest Tree.\n"
        self.storydict['treename'] = self.tree()
        #Autofill conditional for testing.
        if self.storydict['treename'] == '':
            self.storydict['treename'] = 'The Dark Wood'
            print self.storydict['treename']
        self.prompt_options.append("["+self.storydict['treename']+"]")
        self.current = self.storydict['treename']
        
        #Sets up prompt
        self.prompt = "{" + self.storydict['questname'] + "}:"+"[{}]".format(self.storydict['treename'])
        
        #Handles tree introtext
        print "Enter a description of this location for the first time you arrive (introtext): {}\n\n".format(self.storydict['treename'])
        self.store_running('introtext',self.storygen())
        #Autofill conditional for testing.
        if self.running['introtext'] == '':
            self.running['introtext'] = 'A dark and ominous wood. All around you shadows move, despite there not being enough light to see them. The trees lean in, reaching for you. You feel as though something is watching you.\n\nNo... You KNOW something is watching you.\n'
            print self.running['introtext']
            self.wait()
        self.clear()
        
        #Handles tree secondary text
        print "Enter a description of this location that will appear every time you re-visit (secondarytext): {}\n\n".format(self.storydict['treename'])
        self.store_running('secondarytext',self.storygen())
        #Autofill conditional for testing.
        if self.running['secondarytext'] == '':
            self.running['secondarytext'] = 'Shadows within the dark wood watching you on all sides but nothing happens.'
            print self.running['secondarytext']
            self.wait()
        
        #Conditionals is either set in yes/no or location based options.
        #self.store_running('pointers',self.pointers())
        self.running['pointers'] = self.pointers()
        self.running['question'] = self.pointer_questions()
        self.storydict[self.prompt] = self.running
        self.storydict['keyitems'] = []
        #Enter main game line.
        self.builder()
        
    
    #Stores data to running dictionary or wipes it.
    def store_running(self, key, value):
        if self.current in self.prompt:
            self.running[key] = value
        else:
            self.running = {}
            self.running[key] = value
        
    
    #Collects story input.
    def storygen(self):
        story = ''
        print "Description (END to finish):\n"
        while True:
            text = self.input_prompt()
            if text == 'END':
                self.clear()
                break
            elif text == 'OPTIONS':
                print "\nEND:        Breaks from current prompt.\n"
            else:
                story = story + "\n" + text
        return story

    #Primary game building loop
    def builder(self):
        while True:
            self.clear()
            flags = 0
            
            #Establish the prompt menu
            print "Current branch:", self.prompt, '\n'
            try:
                print "Current children:\n" + " : ".join(self.running['pointers']) + "\n"
                if 'flag' in self.running:
                    print "Additional flag children:\n" + " : ".join(self.running['flagpointer']) + "\n"
                    flags = 1
            except:
                print "Current children:\n" + "None"
            
            
            option = raw_input("1. Build child branch\n2. Return to parent branch\n3. Enter child branch\n4. Display running data\n5. Edit current tree\nQUIT : MENU : EXIT\n")
            
            #Check to ensure current branch isn't a dead end.
            try:
                if 'flag' in self.running:
                    pass
                elif ((option == '1') or (option == '3')) and ('DEAD END' in self.running['pointers']):
                    print "Can't create new branch from here. Current branch is a 'DEAD END'."
                    self.wait()
                    continue
                #elif (option == '3' and 'DEAD END' in self.running['pointers']):
                #    print "Can't enter child branch from here. Current branch is a 'DEAD END'."
                #    self.wait()
                #    continue
                else:
                    pass
            except:
                print "Your if statment is failing...."
                self.wait()
            
            #Option conditionals after you select an option.
            if option == '1':
                try:
                    if flags == 0:
                        print "Areas available:\n" + " : ".join(self.running['pointers']) + '\n'
                        temp_pointers = self.running['pointers']
                    else:
                        temp_pointers = self.running['pointers'] + self.running['flagpointer']
                        print "Areas available:\n" + " : ".join(self.running['pointers']) + " : " + " : ".join(self.running['flagpointer']) + '\n'
                    #print "Flag: ", flags
                    self.current = raw_input("Where to next?\n")
                    
                    #if (flags == 1) and (self.current not in [x for x in self.running['flagpointer']]):
                    #    print "Incorrect flag option."
                    #    self.wait()
                    #elif self.current not in [x for x in self.running['pointers']]:
                    #    print "Incorrect option."
                    #    self.wait()
                    if self.current not in [x for x in temp_pointers]:
                        print "Incorrect option or flag option."
                        self.wait()
                    elif self.current == 'back':
                        print "This is not an editable option."
                        self.wait()
                    elif self.current == 'return':
                        print "This is not an editable option."
                        self.wait()
                    elif self.current == 'DEAD END':
                        print "This is not an editable option"
                        self.wait()
                    elif self.current == 'WIN':
                        print "This is not an editable option"
                        self.wait()
                    else:
                        self.change_branches('+')
                        self.branch_construction()
                except:
                    print "No branch children exist."
                    self.wait()
            elif option == '2':
                if (self.current in "{"+self.storydict['questname']+"}") or (self.current in "["+self.storydict['treename']+"]"):
                    print "Can't go back a branch. Already in first branch. Try creating a new branch instead."
                    self.wait()
                else:
                    self.change_branches('-')
            elif option == '3':
                try:
                    if flags == 0:
                        print "Areas available:\n" + " : ".join(self.running['pointers']) + '\n'
                        temp_pointers = self.running['pointers']
                    else:
                        print "Areas available:\n" + " : ".join(self.running['pointers']) + '\n'
                        print "Areas available:\n" + " : ".join(self.running['flagpointer']) + "\n"
                        temp_pointers = self.running['pointers'] + self.running['flagpointer']
                    self.current = raw_input("Where to next?\n")
                    #if (flags == 1) and (self.current not in [x for x in self.running['flagpointer']]):
                    #    print "Incorrect option."
                    #    self.wait()
                    #if (self.current not in [x for x in self.running['pointers']]):
                    #    print "Incorrect option."
                    #    self.wait()
                    if self.current not in [x for x in temp_pointers]:
                        print "Incorrection pointer or flag pointer."
                        self.wait()
                    elif self.current == 'back':
                        print "This is not an editable option."
                        self.wait()
                    elif self.current == 'return':
                        print "This is not an editable option."
                        self.wait()
                    elif self.current == 'DEAD END':
                        print "This is not an editable option"
                        self.wait()
                    elif self.current == 'WIN':
                        print "This is not an editable option"
                        self.wait()
                    else:
                        self.change_branches('+')
                except:
                    print "No further branches. Create new branches."
                    self.wait()
            elif option == '4':
                self.branch_print('all')
            elif option == 'QUIT':
                break
            elif option == 'MENU':
                self.menu()
            elif option == 'EXIT':
                self.exit()
                
            elif option == "5":
                self.edit()    
            elif option == 'dictionary':
                for key,val in self.storydict.items():
                    print key, ">", val, "\n"
                self.wait()
            else:
                print "Incorrect parameter. Try again."
            self.savepoint = self.prompt

    def branch_construction(self):
        while True:
            self.clear()
            print "Branch construction (HELP for instructions):\n\n"
            cmd = self.input_prompt()
            if cmd == "introtext":
                print "Intro text for {} branch:".format(self.current)
                self.running['introtext'] = self.storygen()
            elif cmd == "secondarytext":
                print "Secondary text for {} branch:".format(self.current)
                self.running['secondarytext'] = self.storygen()
            elif cmd == "pointers":
                self.running['pointers'] = self.pointers()
                if ("DEAD END" not in self.running['pointers']) and ("WIN" not in self.running['pointers']):
                    self.running['question'] = self.pointer_questions()
            elif ("display" in cmd) and (len(cmd) > 8):
                try:
                    c = cmd.split(" ")
                    self.branch_print(c[1])
                except:
                    pass #print "Incorrect command."
            elif cmd == "display":
                self.branch_print('all')
            elif cmd == "DONE" or cmd == "QUIT":
                break
            elif cmd == "HELP":
                self.clear
                print "Branch cmds:\n"
                print "introtext        opens input prompt to add introtext for current branch: {}".format(self.current)
                print "secondarytext        opens input prompt to add secondary (re-visit) text for current branch: {}".format(self.current)
                print "pointers        opens pointer/options prompt to give next set of options for the player for current branch: {}".format(self.current)
                print "item        opens input prompt to add text for when you discover an item as well as a designer prompt to design the item you acquire"
                print "death        opens input prompt to add text for a death scene of some kind (good for yes/no branches that end in instant death, these are DEAD END branches that end game play)"
                print "display            print out all currently saved data"
                print "flag        opens input prompt to build a flag condition for a branch"
                print "DMG        opens a prompt to input an amount of damage player takes from entering this branch"
                print "DONE/QUIT            Closes out current branch ({}) prompt to allow for the selection and start of new branches or return to previous branches".format(self.current)
                print "HELP            displays help menu"
                self.wait()
            
            #EXPERIMENTAL OPTIONS
            elif cmd == "item":
                self.acquire_item()
                
            elif cmd == "death":
                print "Death text for {} branch:".format(self.current)
                self.running['deathtext'] = self.storygen()
                #self.running['cmd'] = sys.exit
                
            elif cmd == "DMG":
                while True:
                    try:
                        self.running['damage'] = input("How much damage do you take (keep in mind, an explanation for this should be included in the introtext or secondarytext): ")
                        break
                    except:
                        print "Choose valid number."
            elif cmd == 'flag':
                self.flags()
            else: pass
        self.defaults()
        self.add_pointers('pointers')
        self.add_pointers('flagpointer')
        self.wait()
        
        
    def defaults(self):
        if 'introtext' not in self.running:
            self.running['introtext'] = 'Nothing important here.'
        if 'secondarytext' not in self.running:
            self.running['secondarytext'] = 'Nothing has changed since the last visit.'
                
    def edit(self):
        print "Entering editor." 
        self.wait()
        self.branch_construction()

    def change_branches(self,x):
        
        if self.prompt not in self.storydict:
            self.storydict[self.prompt] = self.running
        else:
            self.merge_dictionaries()
            
        if x == '-':
            del self.prompt_options[-1]
            self.current = self.prompt_options[-1]
            self.prompt = ":".join(self.prompt_options)
            try:
                self.running = self.storydict[self.prompt]
            except:
                print "No dictionary for {} present. Creating new dictionary.".format(self.prompt)
                self.running = {}
        elif x == '+':
            self.prompt_options.append(self.current)
            self.prompt = ":".join(self.prompt_options)
            if self.prompt in self.storydict:
                self.running = self.storydict[self.prompt]
            else:
                self.running = {}
        else:
            print "incorrect parameter."
            sys.exit()
        
        self.clear()
        print "\nNew prompt:", self.prompt
        self.wait()
    
    #Updates dictionary
    def merge_dictionaries(self):
        self.storydict[self.prompt].update(self.running)

    #Used for naming quest tree.
    def tree(self):
        treename = raw_input("Enter Quest Tree name (Examples: graveyard, mansion, forest) :\n")
        return treename

    #Used for naming quest branch.
    def branch(self):
        branchname = raw_input("Enter Branch option name (Examples: basement, attic, library, tunnel) :\n")
        return branchname
    
    #Question for pointers
    def pointer_questions(self):
         option = raw_input("What type of question is this?\nOptions:\n1. Yes or no question\n2. Custom question\n:  ")
         if option == '1':
             question = raw_input("Enter a yes or no question:\n")
         elif option == '2':
             question = raw_input("Enter a custom question:\n")
         else:
             print "Incorrect option."
             return ""
         return question
    
    #Opens prompt to select pointers for self.current (current branch)    
    def pointers(self):
        self.clear()
        option = raw_input("What options are available from here?\nOptions:\n1. Set a yes or no question.\n2. Create list of options.\n3. Dead End this branch.\n4. Add a WIN (quest complete) flag.\n")
        
        if option == '1':
            self.clear()
            #self.running['question'] = raw_input("Enter a yes or no question:\n")
            print "Pointers set to yes or no. Start new branch for (yes or no) pointer to detail what happens for each option."
            self.wait()
            return ['yes','no', 'back']
        elif option == '2':
            #self.running['question'] = raw_input("Enter a custom question:\n")
            locations = []
            print "Max of three options. Hit enter without entering anything if you wish to provide less.\n"
            #print self.prompt_options
            for i in range(1,4):
                #while True:
                local = self.branch()
                if local == '':
                    break
                else:
                    locations.append(local)
                    #break
            if len(locations) < 1:
                print "No options picked. This will be determined as a dead end branch."
                locations = ["DEAD END"]
                self.wait()
            else:
                if len(self.prompt_options) <= 2:
                        pass
                else:
                    choice = raw_input("Include a 'back' or 'return' option? [yes/no]\n")
                
                    if choice.lower() == 'no':
                        pass
                    else:
                        choice = raw_input("Choices are 'back' or 'return'. Back moves back one branch. Return allows for player to move to any previously visited branch.\n")
                        if choice == 'return':
                            locations.append('return')
                        else:
                            locations.append('back')
            return locations
        if option == '3':
            return ['DEAD END']
        elif option == '4':
            return ['WIN']
        else: 
            return ['creepy old shack','dark pool', 'underground cave', 'back']
            
    #Opens a flag setter
    def flags(self):
        while True:
            print "Required components for a in-game flag to be set on a branch:\n1. introtext (no secondarytext for flags)\n2. condition\n3. question\n4. pointers\n5. cancel/delete (removes current flag entirely)\n"
            cmd = raw_input("Which to edit first (END to close flag menu):\n:  ")
            self.running['flag'] = True
            options = ['flagtext','flagcondition','flagquestion','flagpointer']
            if (cmd.lower() == 'introtext') or (cmd == '1'):
                self.running['flagtext'] = self.storygen()
            elif (cmd.lower() == 'condition') or (cmd == '2'):
                self.running['flagcondition'] = self.conditionflag()
                if self.running['flagcondition'][0] == 'keyitem':
                    self.running['keyitemoutcome'] = self.flagitemoutcome()
            elif (cmd.lower() == 'question') or (cmd == '3'):
                self.running['flagquestion'] = self.pointer_questions()
            elif (cmd.lower() == 'pointers') or (cmd == '4'):
                self.running['flagpointer'] = self.pointers()
            elif (cmd.lower() == 'cancel') or (cmd == '5'):
                for i in options:
                    if i in self.running:
                        del self.running[i]
                del self.running['flag']
                break
            elif cmd.lower() == 'end':
                done = True
                for i in options:
                    if i not in self.running:
                        print "{} not complete.".format(i)
                        done = False
                if done == True:
                    
                    break
            else:
                print "Incorrect Option."
        
    #Create flag condition for branch
    def conditionflag(self):
        option = raw_input("Choose condition type:\n1. keyitem\n:  ")
        if (option == '1') or (option.lower() == 'keyitem'):
            option = 'keyitem'
            if 'keyitems' in self.storydict:
                print " : ".join(self.storydict['keyitems'])
            else:
                print "WARNING: No key items currently stored in keyitem dictionary.\nWhilst the player can acquire key items elsewhere in the game please ensure this key item is acquired either within this quest or elsewhere in the game prior to this point."
            keyitem = raw_input("Enter key item required for this flag\n:  ")
        else:
            print "Incorrect option. No condition will be set."
            return ""
        return [option,keyitem]
        
    #Determines what happens to key item after flag completion
    def flagitemoutcome(self):
         while True:
             option = raw_input("What happens to the key item after you complete this flag?\n1. Item removed from inventory\n2. Nothing. Item is kept in inventory\n")
             if option == '1':
                 return 'DELETE'
             elif option == '2':
                 return ''
             else:
                 print "Incorrect option. Try again.\n"
    
        
    #Item Generator
    def acquire_item(self):
        while True:
            
            self.clear()
            print "Welcome to the item generator prompt."
            print "1. Weapon\n2. Key Quest item\n3. Gold\n4. Custom\n5. Item intro text\n6. Item secondary text\n7. Done"
            ans = self.input_prompt()
            
            if ans == '1':
                self.running['weapondict'] = self.wepgen()
            elif ans == '2':
                self.keygen()
            elif ans == '3':
                try:
                    self.running['gold'] = input("Enter gold amount : ")
                except:
                    print "Must enter valid number."
            elif ans == '4':
                print "Enter a custom description for this event."
                self.running['customitem'] = raw_input("Custom item name: ")
                self.running['customitemdescription'] = self.storygen()
            elif ans == '5':
                print "Item intro text for {} branch (when you find this item):".format(self.current)
                self.running['itemintrotext'] = self.storygen()
            elif ans == '6':
                print "\nItem secondary text for {} branch (if you revisit this option/location):".format(self.current)
                self.running['itemsecondarytext'] = self.storygen()
            elif ans == '7':
                break
            else:
                print "Pick valid option."
            self.wait()
    
    #Weapon Generator
    def wepgen(self):
        weapondictionary = {}
        weapondictionary['weapontype'] = raw_input("Weapon type (shortsword, longsword, club, etc.): ")
        weapondictionary['name'] = raw_input("Weapon name: ")
        while True:
            try:
                mindmg = input("Weapon minimum damage: ")
                maxdmg = input("Weapon maximum damage: ")
                weapondictionary['damage'] = [mindmg,maxdmg]
                break
            except:
                print "Enter valid number."
        weapondictionary['description'] = self.storygen()
        return weapondictionary
    
    #Key Item Generator
    def keygen(self):
        self.running['keyitem'] = raw_input("Enter key quest item name: ")
        print "Enter key item description:"
        self.running['keyitemdescription'] = self.storygen()
        if 'keyitems' in self.storydict:
            if self.running['keyitem'] not in self.storydict['keyitems']:
                self.storydict['keyitems'].append(self.running['keyitem'])
        else:
            self.storydict['keyitems'] = []
            self.storydict['keyitems'].append(self.running['keyitem'])
        #self.wait()
        #potentially add more flag material later.
        
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def manual(self):
        pass
        #Include introtext format, secondary text format
    
    def wait(self):
        raw_input("\nPress enter to continue.")
    
    def tutorial(self):
        print "Opening Notes:\n1. Anytime a word is in quotes: 'Tree', 'Pointer', 'Branch'; this means it is a keyword, or title for a particular concept or format within the game. These will be explained further throughout the tutorial.\n\n2. Your starting geographical location is called a 'tree'. All other locations throughout the level are 'branches' of your 'tree'.\nExample: Tree: Mansion\nBranches: Basement, Main Floor, Attic\n\n3. ------------------------------"
        print "Let's get started and remember, have fun!"
        self.wait()
        #Run entire game inside a while loop.
        self.newstory()
        print "Now that we have created a basic introduction to your first location we'll take a look at how it would look in the game.\n"
        self.wait()
        self.clear()
        print "You decide to take the quest and soon you set off. You arrive at your location, {}, and take in your surroundings.".format(self.storydict['entry'])
        introtext = self.storygen()
        print self.storydict['entryintrotext']

        self.wait()
        print "Excellent. We have our starting location, our 'tree', and our 'intro text', a description that will appear the first time we arrive at this new location. However, obviously, we don't necessarily want this exact message to appear every time we enter. Let's add a 'primary text', or a text that appears anytime we re-visit this location. This may occassionally also be referenced as a 'secondary text'."
        print "An example of this could be:\nThe dusty old room appears exactly as you last saw it.\nOR\nNothing has changed.\n"
        print "Of course, a 'primary text'/'secondary text' isn't required but we'll add one for now."
        print "Primary text:\n"
        secondarytext = self.storygen()
        #while True:
    
    #Is this even needed?        
    def input_prompt(self):
        prompt = self.current + ": "
        return raw_input(prompt)
    
    #Convert all of this to a for loop    
    #Prints out branch information
    def branch_print(self, selection):
        self.clear()
        print "Current branch:\n" + self.prompt + '\n'
        if (selection == 'keyitem') or (selection == 'customitem'):
            if selection in self.running:
                print "{}: {}".format(selection.upper(), self.running[selection]), '\n'
                print "Description: {}".format(self.running[selection+'description']), '\n'
            else: print selection, "does not exist.\n"
        elif selection == 'weapon':
            if 'weapondict' in self.running:
                print "Weapon info:"
                for key,val in self.running['weapondict'].items():
                    print "{} : {}".format(key, val)
                print "\n"
            else: print "'{}' does not exist.".format(selection)
        elif selection in self.running:
            #print "New IF statement:\n"
            print "{}:\n".format(selection.upper())
            print self.running[selection]
        elif selection == 'all':
            for i in ['introtext','secondarytext','question','pointers','damage','deathtext','itemintrotext','itemsecondarytext','gold', 'flag', 'flagcondition','flagpointer','flagquestion']:
                try:
                    print i.upper() + ":"
                    print self.running[i], '\n'
                except Exception as e:
                    print e, "does not exist.\n"
            for i in ['keyitem','customitem']:
                if i in self.running:
                    print "{}: {}".format(i.upper(), self.running[i]), '\n'
                    print "Description: {}".format(self.running[i+'description']), '\n'
                else: print i, "does not exist.\n"
        
            print "Item information:"
            if 'weapondict' in self.running:
                print "Weapon info:"
                for key,val in self.running['weapondict'].items():
                    print "{} : {}".format(key, val)
                print "\n"
            else: print "'weapon' does not exist."
        else:
            print "{} does not exist.".format(selection)
                
        self.wait()
        self.clear()
        
    #Prints out all the keys that are not currently finished.
    def unfinished_keys(self):
        dead = []
        livebranch = []
        incomplete = []
        nodeadend = []
        win = []
        for key,value in self.storydict.items():
            if type(value) == dict:
                try:
                    temp = value['pointers']
                    if ('DEAD END' or 'WIN') in temp:
                        dead.append(key)
                        if 'WIN' in temp:
                            win.append(key)
                    else:
                        livebranch.append(key)
                except:
                    incomplete.append(key)
        for branch in livebranch:
            flag = False
            for d in dead:
                if branch in d:
                    flag = True
                    break
            if flag == False:
                nodeadend.append(branch)
        
        #print "\nComplete branches (contain pointers to child branches):\n"
        #for i in livebranch:
        #    print i
        
        
        print "\nIncomplete Branches (no pointers):\n"
        for i in incomplete:
            print i
            
        if len(win) < 1:
            print "\nWIN flag additionally not set. Quest is unwinnable without a branch having the 'WIN' flag set."
        else:
            print "\nWIN flag for quest:\n"
            for i in win:
                print i
                
    #Calls for game exit
    def exit(self):
        self.unfinished_keys()
        c = raw_input("\n\nAre you sure you still want to exit? [yes/no]\n : ")
        if c == 'no':
            pass
        else:
            sys.exit()
        
                    
            
    def add_pointers(self, pointer):
        if pointer in self.running:
            for i in self.running[pointer]:
                prompt = ":".join(self.prompt_options) + ":" + i
                if i == 'DEAD END':
                    pass
                elif i == 'WIN':
                    pass
                elif i == 'back':
                    pass
                elif i == 'return':
                    pass
                elif prompt not in self.storydict:
                    self.storydict[prompt] = {}
        
        #self.wait()

    #########################################################################################################################
    
    #Prototyping
    
    #########################################################################################################################

    def replacement_flag(self):
        '''
        Allows for the replacement of options. This is useful for a book on a bookshelf scenario. See below
        Flag = Missing book on bookshelf. -> Yes or no pointers to place book on shelf. -> yes opens new branch.
        Replace entire branch (either by choice or that containing flag) with a new branch that includes the door. (Replace pointers and secondarytext)
        Options:
        1) Replace a pointers and question in current branch.
        2) Adds new pointer to current branch.
        3) Replace a branch entirely (Will provide a prompt asking which branch.)
        
        OR
        Separate flags into permanant flags and temporary flags. 
        Flags that are only done once, which work like dead ends. They happen, provide the user with something and then disappear. You return a necklace to a statue and it disappears.
        Flags that are permanent stay. Such as placing a book on a shelf to open a secret passageway.
        '''
        pass
    
    def temp_flag(self):
        pass
    
    def permanent_flag(self):
        pass
    




if __name__ == "__main__":
    q = Questbuilder()
    q.clear()
    q.menu()
