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

# PatchIt! V1.0.2 Stable, copyright 2013 le717 (http://triangle717.wordpress.com)

# Import only certain items instead of "the whole toolbox"
import os, linecache # General use modules
from webbrowser import open_new_tab # Used in preload()
from sys import version_info
from os.path import exists, join
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
# App Logging module
import logging

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, variables are a key part of Python, and doesn't require installing an optional module. :)'''

app = "PatchIt!"
majver = "Version 1.0.2"
minver = "Stable"
creator = "le717"
game = "LEGO Racers"


# ------------ Begin WIP PatchIt! Logging Code ------------ #


def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    # The Logs folder does not exist in the current directory
    if not exists(join(os.getcwd(), "Logs")):

        # Create the Logs folder
        logsfolder = os.mkdir(join(os.getcwd(), "Logs"))
        print("\nLogs folder created\n") # Debug print


# ------------ End WIP PatchIt! Logging Code ------------ #

# ------------ Begin PatchIt! Initialization ------------ #

def preload():
    '''Python 3.3.0 and PatchIt! first-run check'''
    logging.info("Begin logging to {0}".format(logging_file))

     # You need to have at least Python 3.3.0 to run PatchIt!
    if version_info < (3,3,0):
        logging.warning("You are not running Python 3.3.0 or higher!\nYou need to get a newer version to run PatchIt!")
        colors.pc("\nYou need to download Python 3.3.0 or greater to run {0} {1} {2}.".format(app, majver, minver), color.FG_LIGHT_RED)

        # Don't open browser immediately
        logging.info("2 second sleep")
        sleep(2)
        open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)
        logging.info("Open new tab in web browser to http://python.org/download")

        # Close PatchIt! after this
        logging.info("3 second sleep")
        sleep(3)
        logging.info("PatchIt! is shutting down.")
        raise SystemExit

    # You are running >= Python 3.3.0
    else:
        logging.info("You are running Python 3.3.0 or greater. PatchIt! will continue.")
        # The settings file does not exist
        if not exists('settings'):
            logging.warning("Settings file does not exist!")
            logging.info("Proceeding to write PatchIt! settings (writesettings())")
            writesettings()

        # The settings file does exist
        else:
            logging.info("Settings file does exist")
            # Settings file does not need to be opened to use linecache

            firstrun = linecache.getline('settings', 1)
            logging.info("Reading line 1 for first-run info")
            # Remove \n, \r, \t, or any of the like
            firstrun = firstrun.strip()

             # Always clear cache after reading
            logging.info("Clearing file cache")
            linecache.clearcache()

            # '0' defines a first-run
            # "" if file is empty or non-existant
            if firstrun == "0" or firstrun == "":
                logging.warning('''First-run info not found!
                Proceeding to write PatchIt! settings (writesettings())''')
                writesettings()
            # Any other number (Default, 1) means it has been run before
            else:
                logging.info("First-run info found, this is not the first-run. Switching to menu.")
                # Does not sleep, for user doesn't know about this unless it is run on < 3.3.0
                main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #


def main():
    '''PatchIt! Menu Layout'''
    #print("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
    colors.pc("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator), color.FG_WHITE)
    print('''\nPlease make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    logging.info("Display menu to user")
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            logging.info("User pressed '[c] Create a PatchIt! Patch'")
            sleep(0.5)
            # Call the Patch Creation module
            logging.info("Calling Patch Compression module (compress.writePatch())")
            compress.writePatch()
        elif menuopt.lower() == "i":
            logging.info("User pressed '[i] Install a PatchIt! Patch'")
            sleep(0.5)
            logging.info("Calling Patch Installation module (extract.readpatch())")
            # Call the Patch Installation module
            extract.readpatch()
        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            # 0.5 second sleep makes it seem like the program is not bugged by running so fast.
            sleep(0.5)
            logging.info("Calling PatchIt! Settings (readsettings())")
            readsettings()
        elif menuopt.lower() == "q":
            # Blank space (\n) makes everything nice and neat
            logging.info("User pressed '[q] Quit'")
            colors.pc("\nThank you for patching with {0}".format(app), color.FG_LIGHT_YELLOW)
            sleep(1)
            logging.info("PatchIt! is shutting down")
            raise SystemExit
        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            # Do not sleep here, since we are already on the menu
            main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #

def readsettings():
    '''Read PatchIt! settings'''

    # The settings file does not exist
    if not exists('settings'):

        logging.warning("Settings file does not exist!")
        logging.info("Proceeding to write PatchIt! settings (writesettings())")
        writesettings()
    # The setting file does exist
    elif exists('settings'):

        logging.info("Settings file does exist")
        # The defined installation was not confirmed by gamecheck()
        if gamecheck() == False:
            logging.warning("LEGO Racers installation was not confirmed!")
            sleep(0.5)

            # Use path defined in gamecheck() for messages
            logging.info("Display warning message to user")
            colors.pc("\nCannot find {0} installation at {1}!\n".format(game, definedgamepath), color.FG_LIGHT_RED)
            # Go write the settings file
            writesettings()

        # The defined installation was confirmed by gamecheck()
        # TODO: Find a better way to do this
        elif gamecheck() ==  True:
            logging.info("LEGO Racers installation was confirmed")
            sleep(0.5)
            logging.info("Display confirmation message to user")
            print("\n{0} installation found at {1}!\n".format(game, definedgamepath) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO Racers installation")
                sleep(0.5)
                logging.info("Proceeding to write PatchIt! settings (writesettings())")
                writesettings()
                # No, I do not want to change the defined installation

            else:
                logging.info("User does not want to change defined LEGO Racers installation or pressed an undefined key")
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

     # The only three items needed to confirm a LEGO Racers installation.
    if exists(join(definedgamepath, "GAMEDATA")) and exists(join(definedgamepath, "MENUDATA")) and exists(join(definedgamepath, "LEGORacers.exe")):
        return True

    # If the settings file was externally edited and the path was removed
    elif len(definedgamepath) == 0:
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        return False


# ------------ End PatchIt! Settings ------------ #


# Run preload() upon PatchIt! launch
if __name__ == "__main__":
    appLoggingFolder()

    # -- Begin Logging Config -- #
    # TODO: Can I move this to a seperate function and it still work?
    logging_file = os.path.join(os.getcwd(), "Logs", 'MainLog.log')
    print("Logging to", logging_file) # Debug
    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s : %(levelname)s : %(message)s",
        filename = logging_file,
        filemode = 'a+',
    )
    # -- End Logging Config -- #

    preload()
else:
    print("\n{0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
