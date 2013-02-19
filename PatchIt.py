# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# PatchIt! 1.0 Beta 3, copyright 2013 le717 (http://triangle717.wordpress.com).

# Import only certain items instead of "the whole toolbox"
import os, sys, time, linecache # General use modules
from webbrowser import open # Special purpose module
from time import sleep
import zipfile, shutil # Zip extraction and compression modules, respectively
import PatchCreate
import PatchCreate.compress
import install

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, variables are a key part of Python, and doesn't require installing an optional module. :)'''

app = "PatchIt!"
majver = "Version 1"
minver = "Beta 3"
creator = "le717"
game = "LEGO Racers"
exist = os.path.exists

# ------------ Begin PatchIt! Initialization ------------ #

def preload():
    '''Python 3.3 and PatchIt! first-run check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run PatchIt!
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        # Don't open browser immediately
        sleep(2)
        open("http://python.org/download", new=2, autoraise=True) # New tab, raise browser window (if possible)
        # PatchIt! automatically closes after this
        sleep(5)
    else: # You are running <= Python 3.3
        # The settings file does not exist
        if not exist('settings'):
            writesettings()
        # The settings file does exist
        else:
            # Settings file does not need to be opened to use linecache
            linecache.clearcache() # Always clear cache before reading
            firstrun = linecache.getline('settings', 1)
            # Remove \n, \r, \t, or any of the like
            firstrun = firstrun.strip()
            linecache.clearcache()
            #firstrun.close
            # '0' defines a first-run
            if firstrun == "0":
                writesettings()
            # Any other number (Default, 1) means it has been run before
            else:
                main()


def main():
    '''PatchIt! Menu Layout'''
    print("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
    print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            sleep(0.5)
            PatchCreate.compress.writepatch()
        elif menuopt.lower() == "i":
            sleep(0.5)
            install.readpatch()
            #PatchInstall.install.readpatch()
        elif menuopt.lower() == "s":
        # 0.5 second sleep makes it seem like the program is not bugged by running so fast.
            sleep(0.5)
            readsettings()
        elif menuopt.lower() == "q":
            # Blank space makes everything nice and neat
            print()
            print("Goodbye!")
            sleep(1)
            raise SystemExit
        else:
            main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Settings ------------ #

def readsettings():
    '''Read PatchIt! settings'''
    # The settings file does not exist
    if not exist('settings'):
        writesettings()
    # The setting file does exist
    elif exist('settings'):
        # Use path as listed in gamecheck() for messages
        # The defined installation was not confirmed by gamecheck()
        if gamecheck() == False:
            sleep(0.5)
            print("\nCannot find {0} installation at {1}!".format(game, definedgamepath))
            writesettings()
        # The defined installation was confirmed by gamecheck()
        elif gamecheck() ==  True:
            sleep(0.5)
            print("\n{0} installation found at {1}".format(game, definedgamepath))
            changepath = input(r"Would you like to change this? (y\N)" + "\n\n> ")
            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                sleep(0.5)
                writesettings()
                # No, I do not want to change the defined installation
            else:
                #print("Canceling...")
                sleep(0.5)
                main()

def writesettings():
    '''Write PatchIt! settings'''
     # It does not matter if it exists or not, it has to be written
    if exist('settings') or not exist('settings'):
        newgamepath = input("\nPlease enter the path to your {0} installaton:\n\n> ".format(game))
        # Allow the user to cancel the change
        if newgamepath.lower() == 'exit':
            print("Canceling...")
            sleep(0.5)
            main()
        # Continue on with the change
        else:
            with open('settings', 'wt', encoding='utf-8') as settings:
                settings.seek(0)
                # Ensures first-run process will be skipped next time
                settings.write("1")
                settings.seek(1)
                settings.write("\n" + newgamepath)
                '''Removing this line breaks the entire first-run code.
                Once it writes the path, PatchIt! closes, without doing as much
                as running the path through gamecheck() nor going back to main()
                Possible TODO: Find out why this happens and remove it if possible.'''
                settings.close()
                readsettings()
def gamecheck():
    '''Confirm LEGO Racers installation'''
    linecache.clearcache()
    global definedgamepath
    definedgamepath = linecache.getline('settings', 2)
    definedgamepath = definedgamepath.strip()
    #definedgamepath.close()
    # If the settings file was externally edited and the path was removed
    if len(definedgamepath) == 0:
        return False
    # The only three items needed to confirm a LEGO Racers installation.
    elif exist(definedgamepath + "/GAMEDATA") and exist(definedgamepath + "/MENUDATA") and exist(definedgamepath + "/LEGORacers.exe"):
        return True
    # The installation path cannot be found
    else:
        return False

# ------------ End PatchIt! Settings ------------ #


#If PatchIt! is run by itself: preload(). If imported (else): display PatchIt! info.
if __name__ == "__main__":
    preload()
else:
    print()
    print("{0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))