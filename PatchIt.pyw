"""
    This file is part of PatchIt!

    PatchIt! -  the standard yet simple way to package and install mods for LEGO Racers
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

# General use modules
import sys, os, linecache, webbrowser, time, platform
# Patch Creation and Installation modules
import modernextract as extract, moderncompress as compress
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
settingsfol = "Settings"

# GLobal game settings
lrgame = "LEGO Racers"
locogame = "LEGO LOCO"
lrsettings = "LRsettings"
locosettings = "LOCOsettings"

# ------------ Begin PatchIt! Initialization ------------ #

def cmdArgs():
    '''PatchIt! Command-line Arguments'''

    # Command-line arguments parser
    parser = argparse.ArgumentParser(description="{0} {1} Command-line arguments".format(app, majver))
    parser.add_argument("-t", "--test",
    help="Enable {0} Experiential features".format(app),
    action="store_true")
    args = parser.parse_args()

    # Declare test parameter (-t, --test) as global for use in other places.
    global test
    test = args.test

def preload():
    '''PatchIt! first-run checks'''

    # Check if Python is x86 or x64, taken from Python help file (platform module)
    if sys.maxsize > 2**32:
        py_arch = "x64"
    else:
        py_arch = "x86"


    logging.info("You are running Python {0} {1} on {2} {3}.".format(py_arch, platform.python_version(), platform.machine(), platform.platform()))
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

    # One of the settings files do not exist
    if not os.path.exists(settingsfol):
        logging.warning("PatchIt! Settings do not exist!")
        logging.info("Proceeding to write PatchIt! settings (Settings())")
        Settings()

    # The PatchIt! settings folder does exist (implied else block here)

    if test:
        if CheckLRSettings() == True or CheckLOCOSettings() == True:
            main()

    elif not test:
        if CheckLRSettings() == True:
            main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #

def main():
    '''PatchIt! Menu Layout'''

    # Blank space (\n) makes everything nice and neat
    colors.pc("\nHello, and welcome to {0} {1} {2},\ncopyright 2013 {3}.".format(app, majver, minver, creator), color.FG_WHITE)
    if not test:
        logging.info("Display normal menu to user")
        print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    elif test:
        print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[j] JAM Extractor
[s] PatchIt! Settings
[q] Quit''')
    logging.info("Display --testing menu to user")
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == 'e':
            logging.warning('"It''s a trap!"')
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
            logging.info("Calling Patch Installation module (extract.selectPatch())")
            extract.selectPatch()

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
                # JAM Extractor wrapper
                import handlejam
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
        logging.info("Proceeding to PatchIt! LEGO Racers Settings (LRReadSettings())")
        LRReadSettings()

    elif test:
        print("\nDo you want to view your {0} or {1} settings?".format(lrgame, locogame))
        print('''
[r] LEGO Racers
[l] LEGO LOCO''')
        settingsopt = input("\n\n> ")

        # Run LEGO Racers settings
        if settingsopt.lower() == "r":
            time.sleep(0.5)
            logging.info("User choose LEGO Racers")
            logging.info("Proceeding to PatchIt! LEGO Racers Settings (LRReadSettings())")
            LRReadSettings()

        # Run LOCO settings
        elif settingsopt.lower() == "l":
            logging.info("User choose LEGO LOCO")
            logging.info("Proceeding to PatchIt! LEGO LOCO Settings (LOCOReadSettings())")
            LOCOReadSettings()

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            logging.info("Switching to main menu")
            main()


# ----- Begin PatchIt! LEGO Racers Settings Reading ----- #

def LRReadSettings():
    '''Read PatchIt! LEGO Racers settings'''

    # The settings file does not exist
    if not os.path.exists(os.path.join(settingsfol, lrsettings)):
        logging.warning("LEGO Racers Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO Racers settings (LRWriteSettings())")
        LRWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(settingsfol, lrsettings)):
        logging.info("LEGO Racers Settings does exist")
        # The defined installation was not confirmed by LRGameCheck()
        if LRGameCheck() == False:
            time.sleep(0.5)

            # Use path defined in LRGameCheck() for messages
            logging.warning("LEGO Racers installation was not found! at {0}".format(definedgamepath))
            colors.pc("\nCannot find {0} installation at\n{1}!\n".format(lrgame, definedgamepath), color.FG_LIGHT_RED)

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO Racers settings (LRWriteSettings())")
            LRWriteSettings()

        # The defined installation was confirmed by LRGameCheck()
        else:
            time.sleep(0.5)
            logging.info("LEGO Racers installation was found at {0}.".format(definedgamepath))
            print('\n{0} installation found at\n"{1}"!\n\n'.format(lrgame, definedgamepath) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO Racers installation")
                time.sleep(0.5)
                logging.info("Proceeding to write PatchIt! LEGO Racers settings (LRWriteSettings())")
                LRWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info("User does not want to change defined LEGO Racers installation or pressed an undefined key")
                # Sleep for 1 second before kicking back to the menu.
                time.sleep(1)
                logging.info("Switching to main menu")
                main()

# ----- End PatchIt! LEGO Racers Settings Reading ----- #

# ----- Begin PatchIt! LEGO Racers Settings Writing ----- #

def LRWriteSettings():
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

        logging.info("Switching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO Racers installation at {0}".format(newgamepath))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(settingsfol):
            os.mkdir(settingsfol)

        # Write settings, using UTF-8 encoding
        logging.info("Open 'LRsettings' for writing with UTF-8 encoding")
        with open(os.path.join(settingsfol, lrsettings), 'wt', encoding='utf-8') as racers_file:

            # As partially defined in PatchIt! Dev-log #6 (http://wp.me/p1V5ge-yB)
            logging.info("Write line denoting what program this file belongs to")
            print("// PatchIt! V1.1.x LEGO Racers Settings", file=racers_file)

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write brief comment explaining what the number means")
            logging.info("Write '1' to line 3 to skip first-run next time")
            print("# Ensures the first-run process will be skipped next time", file=racers_file)
            print("1", file=racers_file)

            logging.info("Write brief comment explaining what the folder path means")

            logging.info("Write new LEGO Racers installation to fifth line")
            print("# Your LEGO Racers installation path", file=racers_file)
            print(newgamepath, file=racers_file)

            # Run check for 1999 or 2001 version of Racers
            logging.info("Run LRVerCheck(newgamepath) to check what version of Racers user has")
            LRVer = LRVerCheck(newgamepath)

            logging.info("Write brief comment telling what version of Racers this is")
            logging.info("Write LEGO Racers version to seventh line (killing the new line ending)")
            print("# Your version of LEGO Racers", file=racers_file)
            # end="" So \n will not be written
            print(LRVer, file=racers_file, end="")

            '''Removing "settings.close()" breaks the entire first-run code.
            Once it writes the path, PatchIt! closes, without doing as much
            as running the path through gamecheck() nor going back to main()
            Possible TODO: Find out why this is happening and remove it if possible.'''

        logging.info("Closing file")
        racers_file.close()
        logging.info("Proceeding to PatchIt! LEGO Racers Settings (LRReadSettings())")
        LRReadSettings()

# ----- End PatchIt! LEGO Racers Settings Writing ----- #

# ----- Begin LEGO Racers Installation, Version and Settings Check ----- #

def LRGameCheck():
    '''Confirm LEGO Racers installation'''

    # global it is can be used in other messages
    logging.info("Reading line 5 of settings for LEGO Racers installation")
    global definedgamepath
    definedgamepath = linecache.getline(os.path.join(settingsfol, lrsettings), 5)

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

def LRVerCheck(new_racers_game):
    '''Checks if LEGO Racers installation is a 1999 or 2001 release'''

    if not os.path.exists(os.path.join(new_racers_game, "legoracers.icd".lower())):
        logging.info("LEGORacers.icd was not found, this is the 2001 release")
        LRVer = "2001"
        return LRVer
    elif os.path.exists(os.path.join(new_racers_game, "legoracers.icd".lower())):
        logging.info("LEGORacers.icd was found, this is the 1999 release")
        LRVer = "1999"
        return LRVer

def CheckLRSettings():
    '''Checks if LEGO LOCO Settings and First-run info'''

    # The LEGO Racers settings don't exist
    if not os.path.exists(os.path.join(settingsfol, lrsettings)):
        logging.warning("LEGO Racers Settings do not exist!")
        Settings()

    elif os.path.exists(os.path.join(settingsfol, lrsettings)):
        logging.info("LEGO Racers Settings do exist")

        # Settings file does not need to be opened to use linecache
        logging.info("Reading line 3 for LEGO Racers first-run info")
        lr_firstrun = linecache.getline(os.path.join(settingsfol, lrsettings), 3)

        # Always clear cache after reading
        logging.info("Clearing Racers first-run cache...")
        linecache.clearcache()

        # '0' defines a first-run
        # "" means file is empty or non-existant
        # \n means the number was removed, but all other text is still in place
        if lr_firstrun == "0" or lr_firstrun == "" or lr_firstrun == "\n":
            logging.warning("PatchIt! has never been run!")
            logging.info("Proceeding to write PatchIt! settings (Settings())")
            Settings()

        # Any other number (Default == 1) means it has been run before
        else:
            logging.info("First-run info found, this is not the first-run. Switching to main menu.")
            # Does not sleep, for user doesn't know about this
            return True

# ----- End LEGO Racers Installation, Version and Settings Check ----- #


# ----- Begin PatchIt! LEGO LOCO Settings Reading ----- #

def LOCOReadSettings():
    '''Read PatchIt! LEGO LOCO settings'''

    # The settings file does not exist
    if not os.path.exists(os.path.join(settingsfol, locosettings)):
        logging.warning("LEGO LOCO Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO LOCO settings (LOCOWriteSettings())")
        LOCOWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(settingsfol, locosettings)):
        logging.info("LEGO LOCO Settings does exist")
        # The defined installation was not confirmed by LOCOGameCheck()
        if LOCOGameCheck() == False:
            time.sleep(0.5)

            # Use path defined in LOCOGameCheck() for messages
            logging.warning("LEGO LOCO installation was not found!".format(loco_path))
            colors.pc("\nCannot find {0} installation at {1}!\n".format(locogame, loco_path), color.FG_LIGHT_RED)

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO LOCO settings (LOCOWriteSettings())")
            LOCOWriteSettings()

        # The defined installation was confirmed by LOCOGameCheck()
        else:
            time.sleep(0.5)
            logging.info("LEGO LOCO installation was found at {0}.".format(loco_path))
            print('\n{0} installation found at "{1}"!\n'.format(locogame, loco_path) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO LOCO installation")
                time.sleep(0.5)
                logging.info("Proceeding to write PatchIt! LEGO LOCO settings (LOCOWriteSettings())")
                LOCOWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info("User does not want to change defined LEGO LOCO installation or pressed an undefined key")
                # Sleep for 1 second before kicking back to the menu.
                time.sleep(1)
                logging.info("Switching to main menu")
                main()

# ----- End PatchIt! LEGO LOCO Settings Reading ----- #

# ----- Begin PatchIt! LEGO LOCO Settings Writing ----- #

def LOCOWriteSettings():
    '''Write PatchIt! LEGO LOCO settings'''

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

    # Select the LEGO LOCO installation
    logging.info("Display folder selection dialog for LEGO LOCO installation")
    new_loco_game = filedialog.askdirectory(
    parent=root,
    title="Please select your {0} installation".format(locogame)
    )

    # The user clicked the cancel button
    if len(new_loco_game) == 0:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO LOCO installation!")
        time.sleep(1)

        logging.info("Switching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO LOCO installation at {0}".format(new_loco_game))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(settingsfol):
            os.mkdir(settingsfol)

        # Write settings, using UTF-8 encoding
        logging.info("Open 'LOCOsettings' for writing with UTF-8 encoding")
        with open(os.path.join(settingsfol, locosettings), 'wt', encoding='utf-8') as loco_file:

            # As partially defined in PatchIt! Dev-log #6 (http://wp.me/p1V5ge-yB)
            logging.info("Write line denoting what program this file belongs to")
            print("// PatchIt! V1.1.x LEGO LOCO Settings", file=loco_file)

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write brief comment explaining what the number means")
            logging.info("Write '1' to line 3 to skip first-run next time")
            print("# Ensures the first-run process will be skipped next time", file=loco_file)
            print("1", file=loco_file)

            logging.info("Write brief comment explaining what the folder path means")

            logging.info("Write new LEGO Racers installation to fifth line (killing the new line ending)")
            print("# Your LEGO LOCO installation path", file=loco_file)
            print(new_loco_game, file=loco_file, end="")

            '''Removing "settings.close()" breaks the entire first-run code.
            Once it writes the path, PatchIt! closes, without doing as much
            as running the path through gamecheck() nor going back to main()
            Possible TODO: Find out why this is happening and remove it if possible.'''

        logging.info("Closing file")
        loco_file.close()
        logging.info("Proceeding to PatchIt! LEGO LOCO Settings (LOCOReadSettings())")
        LOCOReadSettings()

# ----- End PatchIt! LEGO LOCO Settings Writing ----- #

# ----- Begin LEGO LOCO Installation and Settings Check ----- #

def LOCOGameCheck():
    '''Confirm LEGO LOCO installation'''

    # global it is can be used in other messages
    logging.info("Reading line 5 of settings for LEGO LOCO installation")
    global loco_path
    loco_path = linecache.getline(os.path.join(settingsfol, locosettings), 5)

    # Clear cache so settings file is completely re-read everytime
    logging.info("Clearing installation cache...")
    linecache.clearcache()

    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    loco_path = loco_path.strip()

    exe_folder = os.path.join("exe".upper())

     # The only three items needed to confirm a LEGO LOCO installation.
    if os.path.exists(os.path.join(loco_path, exe_folder, "loco.exe".lower())) and os.path.exists(os.path.join(loco_path, exe_folder, "lego.ini".lower()))\
    and os.path.exists(os.path.join(loco_path, "art-res".lower())):
        logging.info("Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}".format(loco_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif len(loco_path) == 0:
        logging.warning("LEGO LOCO installation written in {0} is empty!".format(locosettings))
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}".format(loco_path))
        return False

def CheckLOCOSettings():
    '''Checks if LEGO LOCO Settings and First-run info'''

    # The LEGO LOCO settings don't exist
    if not os.path.exists(os.path.join(settingsfol, locosettings)):
        logging.warning("LEGO LOCO Settings do not exist!")
        Settings()

    # The LEGO LOCO settings do exist (inplied else block here)
    elif os.path.exists(os.path.join(settingsfol, locosettings)):
        logging.info("LEGO LOCO Settings do exist")
        # Settings file does not need to be opened to use linecache

        logging.info("Reading line 3 for LEGO LOCO first-run info")
        loco_firstrun = linecache.getline(os.path.join(settingsfol, locosettings), 3)

        # Always clear cache after reading
        logging.info("Clearing LOCO first-run cache...")
        linecache.clearcache()

        # '0' defines a first-run
        # "" means file is empty or non-existant
        # \n means the number was removed, but all other text is still in place
        if loco_firstrun == "0" or loco_firstrun == "" or loco_firstrun == "\n":
            logging.warning("PatchIt! has never been run!")
            logging.info("Proceeding to write PatchIt! settings (Settings())")
            Settings()

        # Any other number (Default == 1) means it has been run before
        else:
            logging.info("LOCO First-run info found; this is not the first-run. Switching to main menu.")
            # Do not sleep, for user doesn't know about this
            return True

# ----- End LEGO LOCO Installation and Settings Check ----- #


# ------------ End PatchIt! Settings ------------ #