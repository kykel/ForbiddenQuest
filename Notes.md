# Pycharm Environment Notes

## Terminal Emulation
By default, the ide doesn't emulate via the terminal. This results in os.system("cls") commands not clearing the screen and instead outputting weird box symbols with a slash through them. This also effects the time module not running correctly.
 - https://stackoverflow.com/questions/56306486/os-systemcls-doesnt-clear-the-screen-in-pycharm

Solution:
 - Run > Edit Configurations
 - Create new configuration under python
 - Set the interpreter in drop down and the script to the mainfile.py
 - Click on hyperlink "Modify options"
 - Toggle "Emulate terminal in output console"

## Tasks
1. Update all scripts from python2 to python3.
   - Complete
2. Convert 'Primary Scripts' to Object Driven code.
3. Incorporate code as a library (core).

### Primary Scripts
1. bosses.py - WIP
2. combat.py - 
3. diceroll.py
4. items.py
5. loot_discovery.py
6. mainfile.py
7. memorycard.py
8. player.py
9. questcontrolfile.py
10. quests.py
11. shops.py
12. statbuilder.py
13. stats.py
14. status.py
15. storyline.py
16. utility.py

### Intended Outcome
1. bosses.py - All custom built bosses
2. creatures.py - Creature creation, both friend and enemy
3. mainfile.py - Main run file
4. utility.py - Handles all utility functions
5. npc.py - Static and random npc generation
6. shops.py - Custom and random shop generation
7. player.py - All player features
8. combat.py - Handles all combat management and generation
9. memorycard.py - Handles all file save and load

## Alternatvie Potentials
1. Possibly convert quests to YAML so I can hand write them? Might be difficult and not as effective.