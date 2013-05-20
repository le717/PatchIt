# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! -  the standard and simple way to package and install mods for LEGO Racers
    Created 2013 Triangle717 <http://triangle717.wordpress.com>

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
# PatchIt! V1.1.0 Stable, created 2013 Triangle717 (http://triangle717.wordpress.com)

# General use modules
import sys
import os
import time
import linecache
import webbrowser
import platform

# App Logging
import logging


import tkinter as tk
from tkinter import ttk
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)


# Patch Creation and Installation modules
import modernextract as extract
import moderncompress as compress

# Colored shell text
import Color as color, Color.colors as colors

# Global variables
app = "PatchIt!"
majver = "Version 1.1.1"
minver = "Unstable"
creator = "Triangle717"

# Name of PatchIt! Exe/Py
filename = os.path.basename(sys.argv[0])
# Location of PatchIt! Exe/Py
appfolder = os.path.join(sys.argv[0].rstrip(filename))
# Location of Settings folder
settingsfol = os.path.join(sys.argv[0].rstrip(filename), "Settings")
# PatchIt! App Icon
appicon = os.path.join("Icons", "PatchItIcon.ico")

# GLobal game settings
lrgame = "LEGO Racers"
locogame = "LEGO LOCO"
lrsettings = "Racers.cfg"
locosettings = "LOCO.cfg"

# ------------ Begin PatchIt! Initialization ------------ #

def Args():
    '''PatchIt! Command-line Arguments'''

    logging.debug("Command-line arguments processor started")

    # Declare test parameter (-t, --test) as global for use in other places
    global test
    test = False
    # The shell extension
    shell = []

    for i in range(1, len(sys.argv)):
        argument = sys.argv[i]

        # Arguments lists
        test_params = ["--test", "-t"]
        help_params = ["--help", "-h"]

        for value in help_params:
            # If the help parameter was passed
            if argument == value:
                logging.info("The help parameter (-h, --help) was passed, displaying help messages")
                print("\n{0} {1} Command-line arguments".format(app, majver))
                print(r'''
Optional arguments
==================

-h, --help

Display this help message and exit.

-t, --test

Enable PatchIt! experimental features.

{0} \\File Path\\

Confirm and install a PatchIt! Patch without going through the menu first.

NOTE: If --test parameter is to be passed in addition to a file path,
it must come after the file path.'''.format(filename))
                time.sleep(10)
                logging.info('''PatchIt! is shutting down
                ''')
                logging.shutdown()
                raise SystemExit

        for value in test_params:
            # If the test parameter is passed
            if argument == value:
                test = True
                os.system("title {0} {1} {2} - Experimental Mode".format(app, majver, minver))
                logging.info("The test parameter (-t, --test) was passed, enabling experimental features")

            # A file path was passed
            else:
                logging.info("The shell extension was invoked")
                shell.append(argument)

    # Process file or run program, depending on parameters
    if len(shell) > 0:
        for file in shell:
            # If it is a file, switch to Patch Installation
            if os.path.isfile(file):
                logging.info("A file path was passed, switching to extract.checkPatch()")
                extract.checkPatch(file)

            # It was a directory, or a non-existant file
            else:
                logging.warning("Either an invalid file path or no other parameters were passed!")
                # Switch to main menu
                main()

def info():
    '''PatchIt! and System checks'''

    # Check if Python is x86 or x64
    # Based on code from the Python help file (platform module) and my own tests
    if sys.maxsize == 2147483647:
        py_arch = "x86"
    else:
        py_arch = "AMD64"

    logging_file = os.path.join(appfolder, "Logs", 'PatchIt.log')
    logging.info("Begin logging to {0}".format(logging_file))
    logging.info("You are running {0} Python {1} on {2} {3}.".format(py_arch, platform.python_version(), platform.machine(), platform.platform()))
    logging.info('''
                                #############################################
                                        {0} {1} {2}
                                        Copyright 2013 {3}
                                                PatchIt.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/PatchIt/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))
    pass

def preload():
    '''PatchIt! Settings checks'''

    # One of the settings files do not exist
    if not os.path.exists(settingsfol):
        logging.warning("PatchIt! Settings do not exist!")
        logging.info("Proceeding to write PatchIt! settings (Settings())")
        Settings()

    # The PatchIt! settings folder does exist (implied else block here)

    # If the Racers or LOCO settings check come back True, go to menu.
    # No need for a False check; that is written into the functions already
    if CheckLRSettings() == True or CheckLOCOSettings() == True:
        # Switch to main menu
        main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! About Box  ------------ #

def about():
    '''Tkinter About Box'''

    root = tk.Tk()
    # Window title
    root.title("About {0} {1}".format(app, majver))
    # The box cannot be any smaller than this
    root.minsize("400", "165")

    # Give it focus
    root.deiconify()
    root.lift()
    root.focus_force()

    frame = ttk.Frame(root, padding="7 7 7 7")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    # PatchIt! Logo
    pi_logo = tk.PhotoImage(file="Icons/PiTk.gif")
    image_frame = ttk.Label(root)
    image_frame['image'] = pi_logo
    image_frame.grid(column=0, row=0, sticky=tk.N, pady="7")

    # Displayed text
    label = ttk.Label(frame, text='''





            {0} {1} {2}
               Released ?? ??, 2013

            Created 2013 Triangle717

"PatchIt! - The standard and simple way to
package and install mods for LEGO Racers"
'''.format(app, majver, minver))
    label.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    def close_about(*args):
        '''Closes the About Window'''
        root.destroy()
        main()

    # Close About Window button
    close = ttk.Button(frame, default="active", text="Close", command=close_about).grid(column=1, row=1)
    # GitHub Project Button
    github = ttk.Button(frame, text="GitHub Project", command=lambda:webbrowser.open_new_tab("http://bit.ly/PatchIt")).grid(column=0, row=1)
    # Creator's website button
    creator_site =  ttk.Button(frame, text="Triangle717", command=lambda:webbrowser.open_new_tab("http://wp.me/P1V5ge-I3")).grid(column=2, row=1)
    for child in frame.winfo_children(): child.grid_configure(padx=2, pady=2)
    # Binds the Return ("Enter") key, closes the About Window
    root.bind('<Return>', close_about)
    # Make it load
    root.iconbitmap(appicon)
    root.mainloop()

# ------------ End PatchIt! About Box  ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #

def main():
    '''PatchIt! Menu Layout'''

    # Blank space (\n) makes everything nice and neat
    colors.pc("\nWelcome to {0} {1} {2}\ncreated 2013 {3}.".format(app, majver, minver, creator), color.FG_WHITE)
    if not test:
        logging.info("Display normal menu to user")
        print('''Please make a selection:\n
[a] About PatchIt!
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    if test:
        logging.info("Display --test menu to user")
        print('''Please make a selection:\n
[a] About PatchIt!
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[j] JAM Extractor
[s] PatchIt! Settings
[q] Quit''')

    menuopt = input("\n> ")
    while True:
        # About PatchIt! box
        if menuopt.lower() == "a":
            logging.info("User pressed '[a] About PatchIt!'")
            logging.info("Calling About Box (about())")
            about()

        # Patch Creation
        elif menuopt.lower() == "c":
            logging.info("User pressed '[c] Create a PatchIt! Patch'")

            # Call the Patch Creation module
            logging.info("Calling Patch Compression module (compress.patchInfo())")
            compress.patchInfo()

        # Patch Installation
        elif menuopt.lower() == "i":
            logging.info("User pressed '[i] Install a PatchIt! Patch'")

            # Call the Patch Installation module
            logging.info("Calling Patch Installation module (extract.selectPatch())")
            extract.selectPatch()

        # JAM Extractor wrapper
        elif menuopt.lower() == "j":
            if test:
                import handlejam
                logging.info("User pressed '[j] JAM Extractor'")
                # Call the JAM Extractor wrapper module
                logging.info("Calling JAM Extractor wrapper module (handlejam.main())")
                handlejam.main()
            else:
                logging.info("User pressed an undefined key")
                main()

        # PatchIt! Settings
        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            logging.info("Calling PatchIt! Settings Menu (Settings())")
            Settings()

        # Easter egg. :P
        elif menuopt.lower() == 'e':
            logging.warning('"It''s a trap!"')
            colors.pc("\nOoh, you shouldn't have done that, Sir!", color.FG_LIGHT_RED)
            time.sleep(2)
            colors.pc("\n\nNow you must face...", color.FG_LIGHT_RED)
            time.sleep(4)
            colors.pc("\n\nTHE COW!", color.FG_LIGHT_RED)
            time.sleep(0.3)
            webbrowser.open_new_tab("http://triangle717.files.wordpress.com/2013/03/fabulandcow.jpg")
            logging.info("PatchIt! is shutting down to remind the user never to do this again. :P")
            logging.shutdown()
            raise SystemExit

        # Close PatchIt!
        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            logging.info('''PatchIt! is shutting down
            ''')
            if test:
                # If the test parameter was passed, skip the message
                logging.shutdown()
                raise SystemExit
            colors.pc("\nThank you for patching with {0}".format(app), color.FG_LIGHT_YELLOW)
            time.sleep(1)
            logging.shutdown()
            raise SystemExit

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()

# ------------ End PatchIt! Menu Layout ------------ #


# ------------ Begin PatchIt! Settings ------------ #


def Settings():
    '''PatchIt! Settings Menu'''

    print("\nDo you want to view your {0} or {1} settings?".format(lrgame, locogame))
    print('''
[r] LEGO Racers
[l] LEGO LOCO
[q] Quit''')
    settingsopt = input("\n\n> ")

    # Run LEGO Racers settings
    if settingsopt.lower() == "r":
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

            # Use path defined in LRGameCheck() for messages
            logging.warning("LEGO Racers installation was not found! at {0}".format(racers_path))
            colors.pc("\nCannot find {0} installation at\n{1}!\n".format(lrgame, racers_path), color.FG_LIGHT_RED)

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO Racers settings (LRWriteSettings())")
            LRWriteSettings()

        # The defined installation was confirmed by LRGameCheck()
        else:
            logging.info("LEGO Racers installation was found at {0}.".format(racers_path))
            print('\n{0} installation found at\n"{1}"!\n\n'.format(lrgame, racers_path) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO Racers installation")
                logging.info("Proceeding to write PatchIt! LEGO Racers settings (LRWriteSettings())")
                LRWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info("User does not want to change defined LEGO Racers installation or pressed an undefined key")
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
    new_racers_game = filedialog.askdirectory(
    parent=root,
    title="Please select your {0} installation".format(lrgame),
    initialdir=appfolder
    )

    # The user clicked the cancel button
    if len(new_racers_game) == 0:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO Racers installation!")
        #colors.pc("\nCould not find a LEGO Racers installation!", color.FG_LIGHT_RED)

        logging.info("Switching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO Racers installation at {0}".format(new_racers_game))

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

            # Run check for 1999 or 2001 version of Racers
            logging.info("Run LRVerCheck(newgamepath) to check what version of Racers user has")
            logging.info("Write brief comment telling what version of Racers this is")
            LRVer = LRVerCheck(new_racers_game)

            logging.info("Write LEGO Racers version to fifth line")
            print("# Your version of LEGO Racers", file=racers_file)
            print(LRVer, file=racers_file)

            logging.info("Write brief comment explaining what the folder path means")
            logging.info("Write new LEGO Racers installation to seventh line (killing the new line ending)")
            print("# Your LEGO Racers installation path", file=racers_file)
            # end="" So \n will not be written
            print(new_racers_game, file=racers_file, end="")

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
    logging.info("Reading line 7 of settings for LEGO Racers installation")
    global racers_path
    racers_path = linecache.getline(os.path.join(settingsfol, lrsettings), 7)

    # Clear cache so settings file is completely re-read everytime
    logging.info("Clearing installation cache...")
    linecache.clearcache()

    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    racers_path = racers_path.strip()

     # The only three items needed to confirm a LEGO Racers installation.
    if os.path.exists(os.path.join(racers_path, "legoracers.exe".lower())) and os.path.exists(os.path.join(racers_path, "lego.jam".lower()))\
    and os.path.exists(os.path.join(racers_path, "goldp.dll".lower())):
        logging.info("LEGORacers.exe, LEGO.JAM, and GolDP.dll were found at {0}".format(racers_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif len(racers_path) == 0:
        logging.warning("LEGO Racers installation is empty!")
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("LEGORacers.exe, LEGO.JAM, and GolDP.dll were not found at {0}!".format(racers_path))
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

        # '0\n' defines a first-run
        # len() == 0 means file is empty or non-existant
        # \n means the number was removed, but all other text is still in place
        if lr_firstrun == "0\n" or len(lr_firstrun) == 0 or lr_firstrun == "\n":
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

            # Use path defined in LOCOGameCheck() for messages
            logging.warning("LEGO LOCO installation was not found!".format(loco_path))
            colors.pc("\nCannot find {0} installation at {1}!\n".format(locogame, loco_path), color.FG_LIGHT_RED)

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO LOCO settings (LOCOWriteSettings())")
            LOCOWriteSettings()

        # The defined installation was confirmed by LOCOGameCheck()
        else:
            logging.info("LEGO LOCO installation was found at {0}.".format(loco_path))
            print('\n{0} installation found at "{1}"!\n'.format(locogame, loco_path) + r"Would you like to change this? (y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO LOCO installation")
                logging.info("Proceeding to write PatchIt! LEGO LOCO settings (LOCOWriteSettings())")
                LOCOWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info("User does not want to change defined LEGO LOCO installation or pressed an undefined key")
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
    title="Please select your {0} installation".format(locogame),
    initialdir=appfolder
    )

    # The user clicked the cancel button
    if len(new_loco_game) == 0:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO LOCO installation!")
        #colors.pc("\nCould not find a LEGO LOCO installation!", color.FG_LIGHT_RED)

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

            logging.info("Write new LEGO LOCO installation to fifth line (killing the new line ending)")
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

    # You have NO idea how much this small variable helps the code below
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

        # '0\n' defines a first-run
        # len() == 0 means file is empty or non-existant
        # \n means the number was removed, but all other text is still in place
        if lr_firstrun == "0\n" or len(lr_firstrun) == 0 or lr_firstrun == "\n":
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
