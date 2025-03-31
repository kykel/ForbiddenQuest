#TREASURE HUNT QUEST



def treasurehunt():
    #Houses all introductions for quest functions.

    def questintro():
        
        def mansionintro():
            print "You enter the mansion, stepping lightly and cautiously. Already the walls look as though they are about to bleed. You may be a bit paranoid but hey, better safe than sorry is what your Auntie Genna used to say.\nThen again, she also got eaten by a wyvern that one of her booby traps had locked in her garden...\n"
            print "You glance around but all seems quiet. Maybe too quiet? Then again, it is an abandoned mansion. What really constitutes 'too quiet'?"
            print "After ten minutes of standing in place and staring about the room, holding the door open for fear of it slamming behind you, you finally let it go. It creeks its way back to the frame and closes. No slamming, no clicking locks. No trapped wyverns... yet.\nSo, you've made it this far.\n"
            config.clear()
            mansion()

        def gardenintro():
            print "Far to your left, wrapping around the side of the ominous structure you see the garden hedges, standing well over your head. It's common knowledge that gardens often lead to the green houses at the back of the building.\nIt's also common knowledge people often 'get lost' and don't come back out...\nStill, you decide to take a look.\n"
            #if flag is set you can enter.
            print "Unfortunately, at this time, the garden is too overgrown to enter. You'll need something to cut your way through the entrance to get in.\n"
            config.pause()
            config.clear()
            questintro()
   
        print "Against complete common sense(it's obvious you were the brightest among your parent's litter) you accept the offer.\nWhat could possibly go wrong?"
        print "After a long trudge you find yourself at the abandoned shell of a mansion, or rather castle. The quest master really underplayed the place."
        print "On your left you can see the garden, the mansion lay straight ahead and to your right is the rest of the grounds.\n\n"
        directions(gardenintro, mansionintro, grounds, questintro)
                


    #directions(direction)
    def mansion():
        #MANSION
        def library():

            def libraryintro():
                global libraryflag
                if libraryflag == 1:
                    pass
                elif libraryflag == 0:
                    libraryflag = 1
                    print "You attempt to push the door open but can only get it cracked, just enough to squeeze through. Something appears to barricading the door from the other side.\nAs soon as you squeeze into the room you see a nearby shelf has fallen over, restricting movement of the door.\nA look around the room(what you can see anyway) shows fallen books and odd, clawed footprints in the dust.\n"
                    choice = raw_input("Will you enter?")
                    yesorno(choice, library, mansion, mansion)
            
            def hiddenbook():
                print "You search the library relentlessly and find nothing. It's only when you are about to give up that you notice something. There is one book in particular that stands out.\nOn an oddly empty shelf, only half filled with books stands a single large green book. Title: Nevermore.\nA curious title to be sure. You decide to investigate further.\n"
                print "You reach for the book. Only, it won't budge. It's as though the book is glued to the shelf. You pull harder and then suddenly it comes loose, jerking free and sticking out from the shelf at an odd angle.\nAn odd grinding sound emanates from the wall and then the shelf suddenly parts, splitting down the middle and sliding to the side, opening a small body-width gap to squeeze through.\n"
                print "Peering inside you see that it's dark but a slightly visible staircase descends into a tunnel below.\n"
                choice = raw_input("Do you enter?\n(yes or no)\n")
                yesorno(choice, tunnel, library, library)


            #What is the trigger for this? a search with a random variable?
            def toatriary():
                print "You notice, far in the back corner, hidden by a fallen bookshelf is a door. The door isn't blocked but with the angle of the wall and the shelf had you not been looking for it you could have easily missed it.\n"
                choice = raw_input("There is no significant markings on the door. Do you wish to go through?")
                if choice == 'yes' or choice.lower == 'yes' or choice == '1':
                    atriary(2)
                elif choice == 'no' or choice.lower == 'no' or choice == '2':
                    library()
                else:
                    library()
            

            
            def tunnel():
                global torch
                if torch == 0:
                    print "Well, you have a torch but due to your lazieness it's unlit, and so the tunnel is darker than a black widow on a moonless night."
                    torch = 1

                elif torch == 1:
                    print "You follow the tunnel in darkness for as long as you can remember.\nNo seriously, after like... 4 and a half, maybe 4 and 3/4 minutes, you've lost all sense of time. You might as well have been down here a week.\n"
                    print "You navigate blindly, feeling your hands on the walls and shuffling your feet one at a time.\nIt's only when the feel of the terrain changes beneath your feet and the wall goes from smooth to rocky that you realize you've entered the cave.\n"
                    print "BRILLIANT! YOU'VE DONE IT! You've found the cave! With the treasure. At least you think you have. Only, you can't see shit because your dumb ass decided to trek into a dark and creepy tunnel without a torch or even a candle.\nBut hey, who needs light right.\nI'm sure they'll ask you that in heaven about 30 seconds when that ghoul who's lunging at you in the darkness right now is finished ripping out your entrails.\nCongrats. You've died.\n"
                    config.pause()
                    config.clear()
                    print "Game over.\n\n"
                    config.pause()
                    mainfile.main()

                elif torch == 2:
                    print "The tunnel stretches on far past your torch light. Still, you are determined and follow it into seeming oblivion. Quite possibly death but hey, you've come this far.\nI'm sure you can handle some creepy cave creature. Who knows, maybe this time next year they'll name a monument after you for discovering some creepy cave pigmies...\n\nBut I wouldn't count on that. That would imply you're going to survive.\nWhich is obviously not going to happen.\nCome on. Let's be real.\n You're walking into a dark creepy tunnel and nobody else cares you're here.\nYeah... You're fucked!\n"
                    time.sleep(5)
                    config.pause()
                    config.clear
                    print "The darkness seems to extend on forever. You walk for so long you start to wonder if you're moving at all.\nYou start thinking back to adventure school when one-eye, one-leg, decapitated arm Pete told you about his adventures in the Forest of Andabar and how he became trapped for weeks after getting trapped in a darkness enchanment, walking in the same circle for weeks.\nThe punch line, he didn't lose the arm and leg in combat...\n"
                    print "In the end however, the boring flat landscape of the stone tunnel melts away into a slightly less, but still noticeably creepy and boring canvas of cave rock.\nYay!\n"
                    print "The cave isn't very large and you find yourself bordering between anxiety and excitement. You've found it! Obviously you're better than all those blokes who failed. I mean come on! How hard was this really? It's not like...\n"
                    print "Wait....\nHas it not occurred to you that this is too easy?\nWell, of course it has! Even more so when you finally find yourself face to face with the creepiest, ugliest and foul smelling ghoul face you've ever seen.\nAnd judging but it's lunging at you and clacking teeth, it wants to eat you...\nGo figure.\n"
                    tunnel_victory()
                tunnel()


#                    Initiate boss battle with Cave_Ghoul

                def tunnel_victory():
                    print "You've killed the cave ghoul... Wow. That's a job well done. Gotta say, I didn't really think you had it in you. But you did it so I guess I was wrong.\nHeh.\nAnyway, congrats.\n"
                    config.pause()
                    print "\nYou follow the cave a few more feet when something glints in the distance. You step forward, at the ready only to see you've discovered a large metal chest.\nNeedless to say you won't be smashing this open. A quick glance tells you you'll need the key. You found that right?\n"
                    print "Success! You win!\n"
                    config.pause()
                    mainfile.main()
                    #if key flag is set you open chest and get loot.
                    #otherwise, you have to go find it.

            libraryintro()
            print "You've entered the library.\nYou cannot see past the bookshelves, standing from floor to ceiling, from one end of the room to the other in the parralling fashion typical of libraries.\nAmong the shadowed hallways of shelves, old tombs, dust and cobwebs clutter your vision. \n"
            choice = raw_input("Do you wish to search the library?")
            if choice == '1' or choice == 'yes' or choice.lower == 'yes':
                luck = random.randrange(1,20)
                if luck <=5:
                    hiddenbook()
                elif luck <=18:
                    toatriary()
                else:
                    print "You find nothing.\n"
                    config.pause()
                    library()
            elif choice == '2' or choice == 'no' or choice.lower == 'no':
                mansion()
            else:
                mansion()
            

            
        def dungeon():
            print "The door is jammed shut. You are unable to open it."
        
        def ballroom():
            
            def candle():
                global torch
                if torch == 0:
                    print "It appears to be an ordinary candle. If you had a torch maybe you could light it here."
                    ballroom()
                elif torch == 1:
                    config.clear()
                    print "You light your torch on the candle. With this you'll be able to explore the darker areas of the mansion.\nGreat, more places to get killed in.\n"
                    torch = 2
                    print "\nYou've aquired a lit torch.\n"
                    config.pause()
                    ballroom()

            def music():
                print "You decide to explore the room. The decision leaves you feeling rather unnerved as you quickly realize that the faint music you thought you heard was in fact not an illusion at all.\nEven worse, the music changes based on where you are in the room.\nCreepy............."
                config.pause()
                config.clear
                ballroom()

            print "A strange air seems to permeate the grand hall. You hear the faint sound of music and laughing to the air.\nAs you walk around the room, the temperature seems to change in different areas.\n"
            print "Overhead, a great glass dome stretches the length of the room. Candle racks burn, unchanged, as though by magic, on each of the stone pillars bordering the walls.\nOn the far end of the room, large glass windows expose the overgrown and manacingly dark atriary. There are no other doors in the room.\nOtherwise, the room appears empty.\n"
            choice = raw_input("What do you want to do?\n1. Inspect candles.\n2. Explore room\n3. Return to the main lobby.\n")
            funccall(choice, candle, music, mansion, ballroom, ballroom)

            
        def emptyroom():
            #Add random descriptions
            print "Aside from assorted furniture and items, a table, its chairs, an ugly painting over the fireplace mantle, and such, the room is empty."
            mansion()
        
        def basement():
            def flooded():
                print "You walk your way down the steps and into the water. The water is colder than ice.\nStill, somehow you thought this was a good idea...\n"
                print "You're wading through the water, seeing nothing of usefullness when suddenly something moves in the water.\nNaturally, you're terrified. You make a break for the door when it trips you, causing you to drop your torch as you crash into the water.\n"
                print "You come up in complete darknes. Oh god. What have you gotten yourself into?\nYou get a very good idea when something sharp and unnatural plunges into your right calf muscle.\nThe last sound you'll ever make is a very unbrave squeal as you're dragged under the dark watery void.\nCongrats. You've died.\n"
                config.pause()
                print "Game Over."
                config.pause()
                mainfile.main()

            global torch
            if torch == 0:
                print "The basement is dark and flooded. With a torch you'd be able to see, but judging by the amount of water it might be best to steer clear."
                print "I'm sure you'd rather your legacy not be remembered as the guy eaten by basement leeches..."
                mansion()
            elif torch == 1:
                print "Well, you have a torch but due to your laziness it's unlit. A lot of good that's going to do here... Moron."
                mansion()
            elif torch == 2:
                yesorno(choice, flooded, mansion, mansion)


        print "You've entered the mansion. A large empty room with three doors and a set of stairs going up to the second floor, currently shrouded in darkness.\n"
        print "There are three doors around you, a heavy oak door left, a dark mohogany door straight and another on the right. A fourth door under the stairs displays in bold letters: BASEMENT.\nMaybe you can find some kind of light source in one of those directions.\n"
        choice = raw_input("1. Heavy oak door left\n2. Dark mahogany door straight\n3. Dark mohogany door right\n4. Basement\n5. Back outside")
        funccall(choice, emptyroom, library, ballroom, basement, treasurehunt)
            
    def atriary(x):
        def frominside():
            print "You close the door behind you. The atriary isn't even much of an atriary anymore. Much of the glass in its construction is cracked and dirty, many panes broken in several places. You hear nor see no birds, but that is no surprise really as all vegetation in the room is dead.\n"
            print "Yet for all the misery, at least it's well lit and you see no obvious threats in the room."
            choice = raw_input("What do you want to do?\n1. Explore\n2. Cut through to other side\n3. Wait\n4. Return to where you came from\n")
            funccall(choice, atriaryexplore, westdoor, atriarywait, mansion, mansion)
            
        def atriaryexplore():
            print "You begin exploring the room. Most of the plants have died. A few odd looking trees have broken through their pots and their roots have dug into the ground. They seem the only plants to have escape starvation.\nAside from this you see nothing.\n"
            atriary(2)
        
        
        def westdoor():
            print "You find the door on the opposite end of the atriary is unfortunately locked and you can't seem to get it open.\nNo worries, the garden is rather menacing looking through the glass anyway.\n"
            print "You return to the library instead.\n"
            mansion()
        
        def atriarywait():
            print "You decide to sit and wait.\n"
            time.sleep(10)
            print "Nothing happens.\n"
            mansion()
        
            
        def fromoutside():
            pass
            
            
        
        if x == 1:
            fromoutside()
        if x == 2:
            frominside()
            
    def gardenmaze():
        #GARDENMAZE
        
        # def atriary() This and the mansion function both have access as the atriary connects them together.
        def hedgemaze():
            pass
            def threeway():
                pass
            def twoway():
                pass
            def deadend():
                print "You've reached a dead end. You go back to your last intersection."
                pass    
            def pathleft():
                pass
            def pathright():
                pass
        
        def fountain():
            pass
            
        def overgrowth():
            pass

        print "Currently nothing to do here. Sorry. Until the hedge is cleared out you can't enter the hedgemaze.\n"
        choice = raw_input("Where do you want to go?\n1. Mansion\n2. Grounds\n")
        yesorno(choice, mansion, grounds, hedgemaze)
            
    #########################################################################################################################################

    #########################################################################################################################################

    #########################################################################################################################################


    def grounds():
        #GROUNDS
        #This function needs to be encompass all of minigraveyard.
        print "The hedge garden looks a bit too overgrown for you but opt to explore rather than enter the ominous structure before you. The sun has only just risen and even in broad daylight the place makes creepy sound nice.\nNevermind what the inside must look like. You decide to navigate your way through the maze of dieing trees and storage sheds that litter the grounds.\n"
        print "Up ahead you can make out a structure and an old fence. A few tombstones as well.\n"
        #print "The path however splits three ways, to follow the side of the mansion around toward the back on the left, straight toward the tombstones ahead, and off out of sight on the right.\n"
        #Add in ramshackle sheds to search for syth to clear entrance to hedgemaze garden
        choice = raw_input("Where do you want to go?\n1. Continue toward the graveyard.\n2. Return to the mansion. \n3. Return to the garden.\n")
        funccall(choice, minigraveyard, mansion, gardenmaze, grounds, grounds)

    
            
    def minigraveyard():
        
        #This function needs to be incorporated into grounds. There's no reason for minigraveyard() to exist.
        
        def makechoice():
            config.clear()
            print "You follow the path through the grounds for a while. Finally, the knarled trees and ramshackle death sheds part to a small clearing. Before you is a small graveyard.\nThankfully, it's more of a fenced area of tombstones than actual graveyard. The path rounds the left side of the decrepit fence to circle around the back of the building.\n"
            print "A small mosuleaum, barely big enough for a single coffin sits at the back of the plots. On the right of the small graveyard a single tombstone sits lonely and separate from the rest of it's kind.\n"
            choice = raw_input("What do you want to do?\n1. Inspect the graveyard.\n2. Inspect the mosuleaum.\n3. Inspect the lone tombstone.\n4. Follow the path to the back of the mansion.\n")
            if choice.lower() == 'left' or choice == '1':
                newtombstone()
            elif choice.lower() == 'right' or choice == '2':
                singlemosuleaum()
            elif choice.lower() == 'straight' or choice == '3':
                lonelystone()
            elif choice.lower() == 'around' or choice == '4':
                rearpath()
            else:
                grounds()





            

        def newtombstone():
            i = 1
            print "You wander through the graveyard inspecting the different stones. One in particular catches your eye and as you near the stone you notice, it seems newer than the rest. In fact, by the lack of moss and sea salt collected on it, it's clear it's been placed only recently. Even more, the dirt appears to have been recently dug up.\n"
            
            while i == 1:
                choice = raw_input("What do you want to do?\n1. Read the tombstone.\n2. Leave this tombstone and inspect elsewhere.\n3. Dig up the grave.\n")
                if choice == '1':
                    config.clear()
                    print "RIP(ieces)\nHERE LIES THEODORE\nHE ENTERED WHERE HE DIDN'T BELONG\n"
                    print "A warning?\n"
                    config.pause()
                    newtombstone()
                elif choice == '2':
                    print "There's probably nothing worth reading on a stupid rock anyway.\n"
                    i = 0
                    minigraveyard()
                elif choice == '3':
                    i = 0
                    digginggrave()

        def lonelystone(): 
            def lonelystone1():
                choice = raw_input("What do you want to do?\n1. Read the tombstone.\n2. Return to graveyard.\n3. Dig up grave.\n4. Attempt to break the tombstone.\n")
                if choice == '1':
                    print "The stone reads: 'Here Lies Riddle Never, but never did he die.'\n"
                    config.pause()
                    lonelystone1()
                elif choice == '2':
                    minigraveyard()
                elif choice == '3':
                    config.clear()
                    print "After hours of digging, because you are a sick fuck that digs up resting corpses and you also don't have a shovel(way to go on that one moron), you finally come to the conclusion there is nothing buried here.\n" 
                    print "Maybe if you had a shovel you could dig deeper. Otherwise, it appears there's nothing here.\n"
                    config.pause() 
                    makechoice()
                elif choice == '4':
                    print "You attempt to smash the tombstone with your boot but despite the crack it refuses to break. Maybe with the right tools but for now it appears there's nothing you can do.\n"
                    config.pause()
                    makechoice()
                else:
                    minigraveyard()
            print "You approach the lonely tombstone. It is old, possibly older than the rest of the graveyard and its epitaph is barely readable. Moss covers most of its surface and a large crack stretch across its center.\n"
            print "It feels almost sad, like an old memory you've forgotten. Something about the stone feels important.\nAfter several minutes of tracing the fading words with your fingers you manage a translation.\n"
            lonelystone1()

        def singlemosuleaum():
            i = 1
            print "There are no handles on the thick metal doors. Only a large odd shaped keyhole.\n"
            while i == 1:
                choice = raw_input("What do you want to do?\n1. Push on door.\n2. Use key.\n3. Return to graveyard.\n")
                if choice == '1':
                    print "You push on door but it doesn't budge.\n"
                elif choice == '2':
                    if items.key == '1':
                        choice1 = raw_input("The door opens. Enter?\n(yes or no)\n")
                        if choice1 == 'yes':
                            i = 0
                            entermosuleaum()
                        else:
                            makechoice()
                    elif items.key == '0':
                        print "You don't have a key.\n"
                    else:
                        print "Incorrect input.\n"
                elif choice == '3':
                    i = 0
                    minigraveyard()
        
        def entermosuleaum():
            def sarcophagus():
                print "You push hard against the lid, because, just as always you seem to think 'This' is the brightest idea in the world. Don't worry, I won't laugh when the mummy is gouging your eyes from their sockets.\n" 
                print "The lid slides open, albeit with great difficulty. Dust sprays up into the air and you step back coughing heavily as you choke on it.\n" 
                print "Finally, you look inside and unsurprisingly, there's a dead guy. Or rather, skeleton.\nDon't worry. It doesn't move. At least, not yet...\n"
                print "Around the skeleton's neck is a sparkling gold chain, a large yellow topaz attached to the chain.\n"
                choice = raw_input("Will you take it?\n(yes or no)\n")
                if choice == 'yes':
                    config.clear()
                    print "You take the necklace and ..."
                    time.sleep(2)
                    print "Wait for it..."
                    time.sleep(3)
                    print "Almost there..."
                    time.sleep(5)
                    print "Any moment now..." 
                    time.sleep(10)
                    print "HAHAHAHA! GOTCHA. Oh, you should have seen your face.\nNothing happens.\n" 
                    items.necklace = '1'
                    config.pause()
                    entermosuleaum()
                elif choice == 'no':
                    entermosuleaum()
            i=0
            while i == 0:        
                print "The mosuleaum is rather empty. Aside from a few small ash earns and a single sarcophagus in the center you see nothing else.\n" 
                choice = raw_input("What do you want to do?\n1. Check urns.\n2. Open sarcophagus.\n3. Return to graveyard.\n")
                if choice == '1':
                    print "Aside from collected dust, there is nothing special about the urns."
                    pass
                elif choice == '2':
                    sarcophagus()
                elif choice == '3':
                    minigraveyard()
                else:
                    pass
                
                        
                    

        def digginggrave():
            config.clear()
            print "Being the sick fuck that you are, you decide to dig up the grave. You catch a glimpse of the tombstone. It reads something about 'RIP(ieces)'.\nThis is going to be fun.\n"
            print "You dig for what seems like forever, using your hands as you have nothing else to dig with. As you the dirt begins to level out to a wooden coffin you realize you've found the treasure you sought and boy does it smell fantastic.\n"
            print "The coffin is rotted beyond imagining and peels apart like wet paper as your fingers attempt to scrape dirt away from its surface. You stand up to get a better look when the lid suddenly gives and your feet plung through the soft wood.\nLuckily, something soft and slushy melts away under your feet, bracing your fall.\nHowever, now you find yourself stuck knee-deep in metaphorical shit that doesn't feel so metaphorical.\n"
            print "\nAnd then you feel it.\nSomething's moved in the coffin, bumping into your leg. Chill bumps rise on your neck. Panic sets in.\nSuddenly you're struggling to get your legs free. It hits the other leg. An inaudible cry escapes your mouth when something suddenly bites into your calf.\nPanic turns to desparation and then you're free, the biting cling letting go of our leg as you leap from the whole you've dug.\nYou roll away and sit stunned, staring at the hole.\n"
            print "You wait several moments staring at the hole, too afraid to move for worry that something's going to spring up after you. The wound on your leg throbs dull-ly.\n"
            print "You inspect the bite, fighting back vomit as the rotting sludge coating your legs. What the fuck were you thinking!?\n"
            print "The bite isn't too bad, just enough to break skin but it bleeds little. Your bigger stresser at this point should be the risk of infection. It might be a good idea to look for somewhere to clean it."
            status.undeadflag = 1
            status.undead(status.cntrinc(1))
            choice = raw_input("What do you want to do?\n1. Re-inspect the hole.\n2. Further inspect the grounds.\n3. Head for the mansion to try to find a place to clean your wound.\n")
            if choice == '1':
                print "Though terrified beyond all reason, you somehow manage to crawl back over to the grave and peer in. Whatever assaulted you is nowhere in sight. Maybe it fell back into the coffin."
                print "Something glints in the hole near where you fell through. You could swear there was nothing there before. Maybe it got thrown out of the coffin during your struggle."
                choice1 = raw_input("What do you want to do?\n1. Climb back into the hole to get the shiny object.\n2. Try to reach the object from outside the hole.\n3. Leave the hole; return to the graveyard.")
                if choice1 == '1':
                    grabkey(1)
                elif choice1 == '2':
                    grabkey(2)
                elif choice1 == '3':
                    minigraveyard()
            elif choice == '2':
                grounds()
            elif choice == '3':
                mansion()
            else:
                minigraveyard()
                    
        def grabkey(x):
            config.clear()
            if x == 1:
                print "You climb into the hole to examine the shiny object. Fear rattles in your limbs and you're extra careful not to step on top of the coffin this time.\nStill, those yummy juices have fermented the damp soil into now putrid mud.\n"
                print "In the end though the operation goes down without a hitch. You climb from the hole with a fistful of mud and clean off the object to see you've found an odd shaped key.\n"
                config.pause()
                items.key = '1'
            elif x == 2:
                print "You lay close to the edge and reach for the glint but it's just out of reach. You scoot just a bit further and your fingers manage to scrape some mud away from the object, though it still remains out of reach.\nYou can now make out the shape of a shiny key.\n"
                print "You slide forward just a bit more, hanging halfway into the hole now. Planting your free arm against the side of the hole to steady you, you reach out and...\n"
                print "Something slams into the lid of the coffin from inside. Panic sweeps from you as you flinch and lose your grip.\nYou fall, face first, pulling your arms up to brace as you crash through the lid of the coffin.\n"
                print "You come up gasping for air as vomit rises up from your stomach to expel the rotted sludge from your mouth. Things are bumping around you and as you struggle to climb free you see the pile of dismembered limbs floating in the fluid.\n"
                print "You manage to jump free just as a chomping, rotting head floats to the surface, eyes you through pale eyes. You scream and fall back into the side of the grave.\nFor a second you glimpse the key and reach out, grabbing mud and all. Hopefully you managed to grab it.\n"
                print "In the end you escape and as you roll over in the grass outside the hole you see the key in your hand. Success!\n"
                items.key = '1'
                config.pause()
                config.clear()
                status.undead(status.cntrinc(1))

            makechoice()
                
                
               
        def rearpath():
            print "The path before you is narrow and ends cornered between the rear wall of the mansion on your left, the cliff's edge on the right, and the sheer glass wall of the atriary at the opposite end.\nAside from the soothing crashing of the waves on the rocks below, there is nothing here."
            choice = raw_input("What do you want to do?\n1. Wander around aimlessly.\n2. Jump off cliff.\n3. Return to graveyard.")
            if choice == '1':
                print "You wander around aimlessly for several minutes when suddenly you find yourself back in the graveyard...\n\nWeird..."
                config.pause()
                minigraveyard()
            elif choice == '2':
                config.clear()
                print "The doctors always told you that you couldn't fly but hey, where's the fun in believing that.\nThis is your moment!\nYou'll show them!"
                config.pause()
                print "You run, spread your fleshy arm wings and you fly!"
                time.sleep(1)
                print "Straight down..."
                time.sleep(2)
                print "And down..."
                time.sleep(5)
                print "Still falling..." 
                time.sleep(5)
                print "And..\n"
                time.sleep(5)
                print "\nNope.\nRocks.\nHehehe.\nFucking moron.\n\nYou've died!\n"
                exit()
            elif choice == '3':
                minigraveyard()
            else:
                config.clear()
                print "THIS IS AN ERROR! FIX IT!\n\n\n"
                sys.exit(0)
                
            

        makechoice()
 
    questintro()   


