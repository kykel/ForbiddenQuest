import random

#declare variable lists

weapon_type = ['longsword','dagger','blade','spear','scimitar','khopesh','tentacles','knife','dildo','rapier','shortsword','broadsword','kukri','spork','thingy','toothpick','mace','bucket','rock','frying pan','bucket']
adjectives = ['glistening', 'flaming', 'dasterly','oozing', 'vibrating', 'vengeful','gloomy','questionable','corrupted','glowing','disenchanted','ultimate','ghostly yet still somehow physical all at the same time', 'blazing', 'burning','ordinary','','extraordinary','magical','depressing','overpowered','sexy','god','rapey','seemingly dangerous','plastic','twisted','bent', 'freezing', 'menacing','flimsy','useless','floppy','crude','broken']
finaladj = ['destruction','reckoning','avenging','the baneful','death(yours, not theirs...)','the void','death','failure','the... umm... oh god... omg, that fucking disgusting..(vomits furiously)','reaping','cursing','annihilation','ending','raping','stuff','terror','horror','maming','mysteriousness','the... umm... what the fuck is this thing?','things','eviceration','plastic','destiny','bludgeoning','uselessness','doom']

weapon = 'The ' + random.choice(adjectives) + ' ' + random.choice(weapon_type) + ' of ' + random.choice(finaladj)
#print "Wow. You walk into the room and find a weapon just lying on the floor. Talk about lucky.\n"
print "You acquire", weapon
