"""
    This file is part of PatchIt!

    PatchIt! -  the standard yet simple way to packaging and install mods for LEGO Racers
    Copyright 2013 Triangle717 <http://triangle717.wordpress.com>

    PatchIt! is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PatchIt! is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.
"""
# PatchIt! V1.1.0 Unstable, copyright 2013 Triangle717 (http://triangle717.wordpress.com)

import sys, os, linecache # General use modules
import webbrowser, time
# Patch Creation and Installation modules
import modernextract as extract, moderncompress as compress
# JAM Extractor wrapper
import handlejam
# Colored shell text
import color, color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging modules
import logging, thescore
# Command-line arguments
import argparse

# Global variables
app = "PatchIt!"
majver = "Version 1.1.0"
minver = "Unstable"
creator = "Triangle717"

lrgame = "LEGO Racers"
locogame = "LEGO LOCO"

# ------------ Begin PatchIt! Initialization ------------ #

def cmdArgs():
    '''PatchIt! Command-line Arguments'''

    # Command-line arguments parser
    parser = argparse.ArgumentParser(description="{0} {1} Command-line arguments".format(app, majver))
    parser.add_argument("-t", "--test",
    help="Enable {0} Experiential features".format(app),
    action="store_true")
    args = parser.parse_args()

    # Declare force parameter (-t, --test) as global for use in other places.
    global test
    test = args.test


def preload():
    '''Python 3.3.0 and PatchIt! first-run check'''

    logging.info("Begin logging to {0}".format(thescore.logging_file))
    logging.info('''
                                #############################################
                                        {0} {1} {2}
                                        Copyright 2013 {3}
                                        TheWritingsofPatchIt.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/PatchIt/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))

     # You need to have at least Python 3.3.0 to run PatchIt!
    if sys.version_info < (3,3,0):
        logging.warning("You are not running Python 3.3.0 or higher!\nYou need to get a newer version to run PatchIt!")
        colors.pc("\nYou need to download Python 3.3.0 or greater to run {0} {1} {2}.".format(app, majver, minver), color.FG_LIGHT_RED)

        # Don't open browser immediately
        time.sleep(2)
        logging.info("Open new tab in web browser to http://python.org/download")
        webbrowser.open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)

        # Close PatchIt!
        logging.info("Display message for three seconds")
        time.sleep(3)
        logging.info("PatchIt! is shutting down.")
        raise SystemExit

    # You are running >= Python 3.3.0
    else:
        logging.info("You are running Python 3.3.0 or greater. PatchIt! will continue.")
        # The settings file does not exist
        if not os.path.exists('lrsettings'):
            logging.warning("Settings file does not exist!")
            logging.info("Proceeding to write PatchIt! LEGO Racers settings (writeSettingsLR())")
            writeSettingsLR()

        # The settings file does exist
        else:
            logging.info("Settings file does exist")
            # Settings file does not need to be opened to use linecache

            logging.info("Reading line 3 for first-run info")
            firstrun = linecache.getline('lrsettings', 3)

            # Remove \n, \r, \t, or any of the like
            logging.info("Cleaning up line text")
            firstrun = firstrun.strip()

             # Always clear cache after reading
            logging.info("Clearing first-run cache...")
            linecache.clearcache()

            # '0' defines a first-run
            # "" if file is empty or non-existant
            if firstrun == "0" or firstrun == "":
                logging.warning('''First-run info not found!
                Proceeding to write PatchIt! settings (writeSettingsLR())''')
                writeSettingsLR()
            # Any other number (Default, 1) means it has been run before
            else:
                logging.info("First-run info found, this is not the first-run. Proceeding to main menu.")
                # Does not sleep, for user doesn't know about this unless it is run on < 3.3.0
                main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #

def main():
    '''PatchIt! Menu Layout'''

    # Blank space (\n) makes everything nice and neat
    colors.pc("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator), color.FG_WHITE)
    print('''\nPlease make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    logging.info("Display menu to user")
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == 'e':
            logging.warning('"It''s a trap!')
            colors.pc("\nOoh, you shouldn't have done that, Sir!", color.FG_LIGHT_RED)
            time.sleep(2)
            colors.pc("\n\nNow you must face...", color.FG_LIGHT_RED)
            time.sleep(4)
            colors.pc("\n\nTHE COW!", color.FG_LIGHT_RED)
            time.sleep(0.3)
            webbrowser.open_new_tab("http://triangle717.files.wordpress.com/2013/03/fabulandcow.jpg")
            logging.info("PatchIt! is shutting down without a proper Python exit routine (os._exit(0)) to remind the user never to do this again. :P")
            os._exit(0)

        elif menuopt.lower() == "c":
            logging.info("User pressed '[c] Create a PatchIt! Patch'")
            time.sleep(0.5)
            # Call the Patch Creation module
            logging.info("Calling Patch Compression module (compress.patchInfo())")
            compress.patchInfo()

        elif menuopt.lower() == "i":
            logging.info("User pressed '[i] Install a PatchIt! Patch'")
            time.sleep(0.5)

            # Call the Patch Installation module
            logging.info("Calling Patch Installation module (extract.checkPatch())")
            extract.checkPatch()

        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            logging.info("Calling PatchIt! Settings Menu (Settings())")
            Settings()

        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            colors.pc("\nThank you for patching with {0}".format(app), color.FG_LIGHT_YELLOW)
            time.sleep(3)
            logging.info('''PatchIt! is shutting down
            ''')
            raise SystemExit


        if menuopt.lower() == "j":
            if test:
                logging.info("User pressed '[j] JAM Extractor'")
                time.sleep(0.5)
                # Call the JAM Extractor wrapper module
                logging.info("Calling JAM Extractor wrapper module (handlejam.main())")
                handlejam.main()
            else:
                main()

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            # Do not sleep here, since we are already on the menu
            main()

# ------------ End PatchIt! Menu Layout ------------ #


# ------------ Begin PatchIt! Settings ------------ #


def Settings():
    '''PatchIt! Settings Menu'''

    if not test:
        # 0.5 second sleep makes it seem like the program is not bugged by running so fast.
        time.sleep(0.5)
        logging.info("Calling PatchIt! LEGO Racers Settings (readSettingsLR())")
        readSettingsLR()

    elif test:
        print("\nDo you want to view your {0} or {1} settings?".format(lrgame, locogame))
        print('''
[r] LEGO Racers
[l] LEGO LOCO''')

        settingsopt = input("\n\n> ")

        if settingsopt.lower() == "r":
            time.sleep(0.5)
            logging.info("Calling PatchIt! LEGO Racers Settings (readSettingsLR())")
            readSettingsLR()
        elif settingsopt.lower() == "l":
            print("LOCO Settings")
            raise SystemExit
        else:
            main()


# ----- Begin PatchIt! LEGO Racers Settings Reading ----- #

def readSettingsLR():
    '''Read PatchIt! LEGO Racers settings'''

    # The settings file does not exist
    if not os.path.exists('lrsettings'):

        logging.warning("Settings file does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO Racers settings (writeSettingsLR())")
        writeSettingsLR()

    # The setting file does exist
    elif os.path.exists('lrsettings'):

        logging.info("Settings file does exist")
        # The defined installation was not confirmed by gameCheckLR()
        if gameCheckLR() == False:
            time.sleep(0.5)

            # Use path defined in gamecheck() for messages
            logging.warning("LEGO Racers installation was not found!".format(definedgamepath))
            colors.pc("\nCannot find {0} installation at {1}!\n".format(lrgame, definedgamepath), color.FG_LIGHT_RED)

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO Racers settings (writeSettingsLR())")
            writeSettingsLR()

        # The defined installation was confirmed by gamecheck()
        else:
            time.sleep(0.5)
            logging.info("LEGO Racers installation was found at {0}.".format(definedgamepath))
            print('\n{0} installation found at "{1}"!\n'.format(lrgame, definedgamepath) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO Racers installation")
                time.sleep(0.5)
                logging.info("Proceeding to write PatchIt! LEGO Racers settings (writeSettingsLR())")
                writeSettingsLR()

                # No, I do not want to change the defined installation
            else:
                logging.info("User does not want to change defined LEGO Racers installation or pressed an undefined key")
                # Sleep for 1 second before kicking back to the menu.
                time.sleep(1)
                logging.info("Proceeding to main menu")
                main()

# ----- End PatchIt! LEGO Racers Settings Reading ----- #

# ----- Begin PatchIt! LEGO Racers Settings Writing ----- #

def writeSettingsLR():
    '''Write PatchIt! LEGO Racers settings'''

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to (basically) completely hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the LEGO Racers installation
    logging.info("Display folder selection dialog for LEGO Racers installation")
    newgamepath = filedialog.askdirectory(
    parent=root,
    title="Please select your {0} installation".format(lrgame)
    )

    # The user clicked the cancel button
    if len(newgamepath) == 0:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO Racers installation!")
        time.sleep(1)

        logging.info("Proceeding to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO Racers installation {0}".format(newgamepath))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Write settings, using UTF-8 encoding
        logging.info("Open 'lrsettings' for writing with UTF-8 encoding")
        with open('lrsettings', 'wt', encoding='utf-8') as settings:

            # As partially defined in PatchIt! Dev-log #6 (http://wp.me/p1V5ge-yB)
            logging.info("Write line denoting what program this file belongs to")
            print("// PatchIt! V1.1.x LEGO Racers Settings", file=settings)

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write brief comment explaining what the number means")
            logging.info("Write '1' to line 3 to skip first-run next time")
            print("# Ensures the first-run process will be skipped next time", file=settings)
            print("1", file=settings)

            logging.info("Write brief comment explaining what the folder path means")
            # end="" So \n will not be written
            logging.info("Write new LEGO Racers installation to fifth line (killing the new line ending)")
            print("# Your LEGO Racers installation path", file=settings)
            print(newgamepath, file=settings, end="")

            '''Removing "settings.close()" breaks the entire first-run code.
            Once it writes the path, PatchIt! closes, without doing as much
            as running the path through gamecheck() nor going back to main()
            Possible TODO: Find out why this is happening and remove it if possible.'''

            logging.info("Closing file")
            settings.close()
            logging.info("Proceeding to PatchIt! LEGO Racers Settings (readSettingsLR())")
            readSettingsLR()

# ----- End PatchIt! LEGO Racers Settings Writing ----- #

# ----- Begin LEGO Racers Installation Check ----- #

def gameCheckLR():
    '''Confirm LEGO Racers installation'''

    # global it is can be used in other messages
    logging.info("Reading line 5 of settings for LEGO Racers installation")
    global definedgamepath
    definedgamepath = linecache.getline('lrsettings', 5)

    # Clear cache so settings file is completely re-read everytime
    logging.info("Clearing installation cache...")
    linecache.clearcache()

    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    definedgamepath = definedgamepath.strip()

     # The only three items needed to confirm a LEGO Racers installation.
    if os.path.exists(os.path.join(definedgamepath, "legoracers.exe".lower())) and os.path.exists(os.path.join(definedgamepath, "lego.jam".lower()))\
    and os.path.exists(os.path.join(definedgamepath, "goldp.dll".lower())):
        logging.info("LEGORacers.exe, LEGO.JAM, and GolDP.dll were found at {0}".format(definedgamepath))
        return True

    # If the settings file was externally edited and the path was removed
    elif len(definedgamepath) == 0:
        logging.warning("LEGO Racers installation is empty!")
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("LEGORacers.exe, LEGO.JAM, and GolDP.dll were not found at {0}!".format(definedgamepath))
        return False

# ----- End LEGO Racers Installation Check ----- #

# ------------ End PatchIt! Settings ------------ #

if __name__ == "__main__":
    # Write window title (since there is no GUI)
    os.system("title {0} {1} {2}".format(app, majver, minver))

    # Run PatchIt! Initialization
    cmdArgs()
    preload()