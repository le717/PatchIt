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

# PatchIt! V1.0.1 Stable, copyright 2013 le717 (http://triangle717.wordpress.com)

# Import only certain items instead of "the whole toolbox"
import os, linecache # General use modules
from webbrowser import open_new_tab # Used in preload()
from sys import version_info
from os.path import exists
from time import sleep
# Patch Creation and Installation modules
import extract
import compress
# Colored text (until complete GUI is written)
import color
import color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, variables are a key part of Python, and doesn't require installing an optional module. :)'''

app = "PatchIt!"
majver = "Version 1.0.1"
minver = "Stable"
creator = "le717"
game = "LEGO Racers"

# ------------ Begin PatchIt! Initialization ------------ #

def preload():
    '''Python 3.3.0 and PatchIt! first-run check'''
    if version_info < (3,3,0): # You need to have at least Python 3.3.0 to run PatchIt!
        colors.pc("\nYou need to download Python 3.3.0 or greater to run {0} {1} {2}.".format(app, majver, minver), color.FG_LIGHT_RED)
        # Don't open browser immediately
        sleep(2)
        open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)
        # PatchIt! automatically closes after this
        sleep(3)

    # You are running >= Python 3.3.0
    else:
        # The settings file does not exist
        if not exists('settings'):
            writesettings()

        # The settings file does exist
        else:
            # Settings file does not need to be opened to use linecache

            firstrun = linecache.getline('settings', 1)
            # Remove \n, \r, \t, or any of the like
            firstrun = firstrun.strip()

             # Always clear cache after reading
            linecache.clearcache()

            # '0' defines a first-run
            if firstrun == "0" or firstrun == "":
                writesettings()
            # Any other number (Default, 1) means it has been run before
            else:
                # Does not sleep, for user doesn't know about this unless it is run on < 3.3.0
                main()


def main():
    '''PatchIt! Menu Layout'''
    #print("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
    colors.pc("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator), color.FG_WHITE)
    print('''\nPlease make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            sleep(0.5)
            # Call the Patch Creation module
            compress.writePatch()
        elif menuopt.lower() == "i":
            sleep(0.5)
            # Call the Patch Installation module
            extract.readpatch()
        elif menuopt.lower() == "s":
            # 0.5 second sleep makes it seem like the program is not bugged by running so fast.
            sleep(0.5)
            readsettings()
        elif menuopt.lower() == "q":
            # Blank space (\n) makes everything nice and neat
            colors.pc("\nThank you for patching with {0}".format(app), color.FG_LIGHT_YELLOW)
            sleep(1)
            raise SystemExit
        # Undefined input
        else:
            # Do not sleep here, since we are already on the menu
            main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Settings ------------ #

def readsettings():
    '''Read PatchIt! settings'''

    # The settings file does not exist
    if not exists('settings'):
        writesettings()
    # The setting file does exist
    elif exists('settings'):

        # The defined installation was not confirmed by gamecheck()
        if gamecheck() == False:
            sleep(0.5)
            # Use path defined in gamecheck() for messages
            colors.pc("\nCannot find {0} installation at {1}!".format(game, definedgamepath), color.FG_LIGHT_RED)
            # Go write the settings file
            writesettings()

        # The defined installation was confirmed by gamecheck()
        # TODO: Find a better way to do this
        elif gamecheck() ==  True:
            sleep(0.5)
            print("\n{0} installation found at {1}!\n".format(game, definedgamepath) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                sleep(0.5)
                writesettings()
                # No, I do not want to change the defined installation

            else:
                # Always sleep for 1 second before kicking back to the menu.
                sleep(1)
                main()

def writesettings():
    '''Write PatchIt! settings'''

     # It does not matter if it exists or not, it has to be written
    if exists('settings') or not exists('settings'):

        # Hide the root Tk window
        root = tkinter.Tk()
        root.withdraw()

        # Select the LEGO Racers installation
        newgamepath = filedialog.askdirectory(title="Please select your {0} installation".format(game))

        # The user clicked the cancel button
        if len(newgamepath) == 0:
            #print("Canceling...") # Again, for lack of a better messages
            sleep(1)
            main()

        # The user selected a folder
        else:
            # Write file, using UTF-8 encoding
            try:
                with open('settings', 'wt', encoding='utf-8') as settings:
                    # Ensures first-run process will be skipped next time
                    print("1", file=settings)
                    # end="" So there won't be a \n written
                    print(newgamepath, file=settings, end="")

                    '''Removing "settings.close()" breaks the entire first-run code.
                    Once it writes the path, PatchIt! closes, without doing as much
                    as running the path through gamecheck() nor going back to main()
                    Possible TODO: Find out why this is happening and remove it if possible.'''

                    settings.close()
                    readsettings()

            # User does not have the rights to write the settings file
            except PermissionError:
                colors.pc("\nUnable to change {0} installation to {1}!".format(game, newgamepath), color.FG_LIGHT_RED)
                sleep(2)
                main()

def gamecheck():
    '''Confirm LEGO Racers installation'''

    # For use in other messages
    global definedgamepath
    definedgamepath = linecache.getline('settings', 2)

    # Clear cache so settings fiele is completely re-read everytime
    linecache.clearcache()

    # Strip the path to make it valid
    definedgamepath = definedgamepath.strip()

    # If the settings file was externally edited and the path was removed
    if len(definedgamepath) == 0:
        return False

     # The only three items needed to confirm a LEGO Racers installation.
    elif exists(definedgamepath + "/GAMEDATA") and exists(definedgamepath + "/MENUDATA") and exists(definedgamepath + "/LEGORacers.exe"):
        return True

    # The installation path cannot be found, or it cannot be confirmed
    else:
        return False


# ------------ End PatchIt! Settings ------------ #


# Run preload() upon PatchIt! launch
if __name__ == "__main__":
    preload()
# TODO: Find out why I'm getting an import error when PatchIt! is imported
#else:
    #print("\n{0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
