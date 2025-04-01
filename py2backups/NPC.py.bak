#!/usr/bin/env python

#26NOV2018 - NPC (init, intro, str) all complete // QuestMaster - initial setup (init, load_quests, display_quests, move_quest, __str__)

import Player

class NPC:
    def __init__(self, name="BOB", description="A random NPC.", introtext="'Hello there.'"):
        self.name = name
        self.description = description
        self.introtext = introtext
    
    def intro(self):
        return self.introtext
    
    def __str__(self):
        return self.name + "\n" + self.description + "\n" + self.introtext
        
    
class QuestMaster(NPC):
    
    #Needs to be able to validate and load an existing incomplete quest
    
    def __init__(self, name, quest="Skeleton Key"):
        NPC.__init__(self,name="JIM")
        self.quest = quest
    
    def load_quests(self):
        pass
    
    def display_quests(self):
        pass
    
    def move_quest(self):
        pass
    
    
    def __str__(self):
        return NPC.__str__(self) + "\n" + self.quest

    
if __name__ == "__main__":
    npc = NPC()
    print npc, "\n"
    
    questnpc = QuestMaster("Erik")
    print questnpc
    