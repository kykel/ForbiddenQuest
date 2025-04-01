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

