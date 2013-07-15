# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! -  the standard and simple way to package and install mods for LEGO® Racers
    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

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
# PatchIt! V1.1.1 Unstable Core Module

# General use modules
import sys
import os
import webbrowser
import platform
import subprocess

# App Logging
import logging

import tkinter as tk
from tkinter import ttk
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

# Patch Creation and Installation modules
from Patch import modernextract as extract
from Patch import moderncompress as compress

# Colored shell text
import Color as color
import Color.colors as colors

# Global variables
app = "PatchIt!"
majver = "1.1.1"
minver = "Unstable"
creator = "Triangle717"

# Name of PatchIt! Exe/Py
exe_name = os.path.basename(sys.argv[0])
# Location of PatchIt! Exe/Py
app_folder = os.path.dirname(sys.argv[0])
# Location of Settings folder
settings_fol = os.path.join(app_folder, "Settings")
# PatchIt! App Icon
app_icon = os.path.join(app_folder, "Icons", "PatchItIcon.ico")

# GLobal game settings
LR_game = "LEGO Racers"
LOCO_game = "LEGO LOCO"
LR_settings = "Racers.cfg"
LOCO_settings = "LOCO.cfg"

# ------------ Begin PatchIt! Initialization ------------ #


def args():
    '''PatchIt! Command-line Arguments'''

    logging.info("Command-line arguments processor started")

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
            # If the help parameter was given
            if argument == value:
                logging.info("The help parameter (-h, --help) was given, displaying help messages")
                print("\n{0} Version {1} Command-line arguments".format(app, majver))
                # Use input rather than print so user can close the window
                # at anytime, rather than it closing after 10 seconds
                input(r'''
Optional arguments
==================

-h, --help

Display this help message and exit.

-t, --test

Enable PatchIt! experimental features.

{0} \\File Path\\

Confirm and install a PatchIt! Patch without going through the menu first.

NOTE: If --test parameter is to be given in addition to a file path,
it must come after the file path.

Press the Enter key to close.'''.format(exe_name))
                logging.info('''PatchIt! is shutting down
                ''')
                logging.shutdown()
                raise SystemExit(0)

        for value in test_params:
            # If the test parameter is given
            if argument == value:
                test = True
                os.system("title {0} Version {1} {2} - Experimental Mode".format(
                    app, majver, minver))
                logging.info("The test parameter (-t, --test) was given, enabling experimental features")
                preload()

            # A file path was given
            else:
                logging.info("The shell extension was invoked")
                shell.append(argument)

    # Process file or run program, depending on parameters
    if len(shell) > 0:
        for file in shell:
            # If it is a file, switch to Patch Installation
            if os.path.isfile(file):
                logging.info("A file path was given, switching to extract.checkPatch()")
                extract.checkPatch(file)

            # It was a directory, or a non-existant file
            else:
                logging.warning("Either an invalid file path or no other parameters were given!")
                # Switch to main menu
                main()


def info():
    '''PatchIt! and System checks'''

    # Check if Python is x86 or x64
    # Based on code from Python help for platform module and my own tests
    if sys.maxsize == 2147483647:
        py_arch = "x86"
    else:
        py_arch = "AMD64"

    logging_file = os.path.join(app_folder, "Logs", 'PatchIt.log')
    logging.info("Begin logging to {0}".format(logging_file))
    logging.info("You are running {0} Python {1} on {2} {3}.".format(
        py_arch, platform.python_version(), platform.machine(),
         platform.platform()))
    logging.info('''
                                #############################################
                                        {0} Version {1} {2}
                                        Copyright 2013 {3}
                                                PatchIt.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/PatchIt/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))


def preload():
    '''PatchIt! Settings checks'''

    # One of the settings files do not exist
    if not os.path.exists(settings_fol):
        logging.warning("PatchIt! Settings do not exist!")
        logging.info("Proceeding to write PatchIt! settings (Settings())")
        Settings()

    # The PatchIt! settings folder does exist (implied else block here)

    # Assign variables for easier access
    hasLRSettings = CheckLRSettings()
    hasLOCOSettings = CheckLOCOSettings()

    # If the Racers settings is present but not LOCO,
    # go to main menu
    if hasLRSettings and not hasLOCOSettings:
        main()

    # If the LOCO settings is present but not Racers,
    # go to main menu
    elif hasLOCOSettings and not hasLRSettings:
        main()

    # If both the Racers and LOCO settings are present,
    # go to main menu
    elif hasLRSettings and hasLRSettings:
        main()

    # Any other condition
    else:
        Settings()


# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! About Box  ------------ #


def about(*args):
    '''Tkinter About Box'''

    root = tk.Tk()
    # Window title
    root.title("About {0} Version {1}".format(app, majver))
    # The box cannot be any smaller than this
    root.minsize("420", "260")
    root.maxsize("420", "260")

    # Give it focus
    root.deiconify()
    root.lift()
    root.focus_force()

    # Frame settings
    frame = ttk.Frame(root, padding="7 7 7 7")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

    # PatchIt! Logo
    pi_logo = tk.PhotoImage(file="Icons/PiTk.gif")
    image_frame = ttk.Label(root)
    image_frame['image'] = pi_logo
    image_frame.grid(column=0, row=0, sticky=tk.N, pady="7")

    # Displayed text
    label = ttk.Label(frame, text='''





            {0} Version {1} {2}
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
    close = ttk.Button(frame, default="active", text="Close",
         command=close_about)
    close.grid(column=1, row=1, sticky=tk.N, pady="7")
    # GitHub Project Button
    github = ttk.Button(frame, text="GitHub",
         command=lambda: webbrowser.open_new_tab("http://git.io/PatchIt"))
    github.grid(column=0, row=1, sticky=tk.N, pady="7")
    # Creator's website button
    creator_site = ttk.Button(frame, text="Triangle717",
         command=lambda: webbrowser.open_new_tab("http://wp.me/P1V5ge-I3"))
    creator_site.grid(column=2, row=1, sticky=tk.N, pady="7")

    # Small bit of padding around the elements
    for child in frame.winfo_children():
        child.grid_configure(padx=2, pady=2)

    # Bind the Return ("Enter") key to close the About Window
    root.bind('<Return>', close_about)

    # Make it load
    root.iconbitmap(app_icon)
    root.mainloop()


# ------------ End PatchIt! About Box  ------------ #


# ------------ Begin PatchIt! Menu Layout ------------ #


def main(*args):
    '''PatchIt! Menu Layout'''

    # Blank space (\n) makes everything nice and neat
    colors.pc("\nWelcome to {0} Version {1} {2}\ncreated 2013 {3}.".format(
        app, majver, minver, creator), color.FG_WHITE)
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
            logging.info("Opening About Box")
            about()

        # Patch Creation
        elif menuopt.lower() == "c":
            logging.info("User pressed '[c] Create a PatchIt! Patch'")

            # Call the Patch Creation module
            logging.info("Calling Patch Compression module")
            compress.patchInfo()

        # Patch Installation
        elif menuopt.lower() == "i":
            logging.info("User pressed '[i] Install a PatchIt! Patch'")

            # Call the Patch Installation module
            logging.info("Calling Patch Installation module")
            extract.selectPatch()

        # JAM Extractor wrapper
        elif menuopt.lower() == "j":
            if test:
                import handlejam
                logging.info("User pressed '[j] JAM Extractor'")
                # Call the JAM Extractor wrapper module
                logging.info("Calling JAM Extractor wrapper module")
                handlejam.main()
            else:
                logging.info("User pressed an undefined key")
                main()

        # PatchIt! Settings
        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            logging.info("Calling PatchIt! Settings Menu (Settings())")
            Settings()

        # Easter egg
        elif menuopt.lower() == 'e':
            logging.info("User pressed the 'e' key")
            easteregg()

        # Close PatchIt!
        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            logging.info('''PatchIt! is shutting down
            ''')
            logging.shutdown()
            raise SystemExit(0)

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()


def easteregg(*args):
    '''Hehehe'''
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(app_icon)
    tk.messagebox.showerror("Uh-oh", "That was bad.")
    tk.messagebox.showerror("Uh-oh", "You should not have pressed that key.")
    tk.messagebox.askquestion("Uh-oh", "Would you like see your punishment for pressing that key?")
    subprocess.call([os.path.join("Icons", "cghbnjcGJfnvzhdgbvgnjvnxbv12n1231gsxvbhxnb.jpg")], shell=True)
    logging.info("PatchIt! is shutting down.")
    logging.shutdown()
    raise SystemExit(0)


# ------------ End PatchIt! Menu Layout ------------ #


# ------------ Begin PatchIt! Settings ------------ #


def Settings(*args):
    '''PatchIt! Settings Menu'''

    print("\nDo you want to view your {0} or {1} settings?".format(
        LR_game, LOCO_game))
    print('''
[r] LEGO Racers
[l] LEGO LOCO
[q] Quit''')
    settingsopt = input("\n> ")

    # Run LEGO Racers settings
    if settingsopt.lower() == "r":
        logging.info("User choose LEGO Racers")
        logging.info("Proceeding to PatchIt! LEGO Racers Settings")
        LRReadSettings()

    # Run LOCO settings
    elif settingsopt.lower() == "l":
        logging.info("User choose LEGO LOCO")
        logging.info("Proceeding to PatchIt! LEGO LOCO Settings")
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
    if not os.path.exists(os.path.join(settings_fol, LR_settings)):
        logging.warning("LEGO Racers Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO Racers settings")
        LRWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(settings_fol, LR_settings)):
        logging.info("LEGO Racers Settings do exist")

        # The defined installation was not confirmed by LRGameCheck()
        if not LRGameCheck():

            # Use path defined in LRGameCheck() for messages
            logging.warning("LEGO Racers installation was not found at {0}"
            .format(LR_path))
            #colors.pc('\nCannot find {0} installation at\n"{1}"!\n'.format(
    #LR_game, LR_path), color.FG_LIGHT_RED)
            root = tk.Tk()
            root.withdraw()
            tk.messagebox.showerror("Invalid installation!",
            "Cannot find {0} installation at {1}".format(LR_game, LR_path))

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO Racers settings")
            LRWriteSettings()

        # The defined installation was confirmed by LRGameCheck()
        else:
            logging.info("LEGO Racers installation was found at {0}.".format(
                LR_path))
            print('\n{0} installation found at\n"{1}"!\n\n'.format(
                LR_game, LR_path) + r"Would you like to change this? (Y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO Racers installation")
                logging.info("Proceeding to write PatchIt! LEGO Racers settings")
                LRWriteSettings()

            # No, I do not want to change the defined installation
            else:
                logging.info('''User does not want to change the LEGO Racers
                installation or pressed an undefined key''')
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
    logging.info("Overwrite root Tk window settings to basically hide it")
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
    title="Please select your {0} installation".format(LR_game),
    initialdir=app_folder
    )

    # The user clicked the cancel button
    if not new_racers_game:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO Racers installation!")
        #colors.pc("\nCould not find a LEGO Racers installation!",
            #color.FG_LIGHT_RED)

        logging.info("Switching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO Racers installation at {0}"
        .format(new_racers_game))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(settings_fol):
            os.mkdir(settings_fol)

        # Write settings, using UTF-8 encoding
        logging.info("Open 'LR_settings' for writing using UTF-8-NOBOM encoding")
        with open(os.path.join(settings_fol, LR_settings),
            'wt', encoding='utf-8') as racers_file:

            # As partially defined in PatchIt! Dev-log #6
            # (http://wp.me/p1V5ge-yB)
            logging.info("Write line denoting what program this file belongs to")
            racers_file.write("// PatchIt! V1.1.x LEGO Racers Settings\n")

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write brief comment explaining what the number means")
            logging.info("Write '1' to line 3 to skip first-run next time")
            racers_file.write("# Ensures the first-run process will be skipped next time\n")
            racers_file.write("1\n")

            # Run check for 1999 or 2001 version of Racers
            logging.info("Run LRVerCheck(newgamepath) to check what version of Racers user has")
            logging.info("Write brief comment telling what version of Racers this is")
            LRVer = LRVerCheck(new_racers_game)

            logging.info("Write LEGO Racers version to fifth line")
            racers_file.write("# Your version of LEGO Racers\n")
            racers_file.write(LRVer)

            logging.info("Write brief comment explaining what the folder path means")
            logging.info("Write new LEGO Racers installation to seventh line (killing the new line ending)")
            racers_file.write("\n# Your LEGO Racers installation path\n")
            racers_file.write(new_racers_game)

        # Log closure of file (although the with handle did it for us)
        logging.info("Closing Racers.cfg")
        logging.info("Proceeding to PatchIt! LEGO Racers Settings")
        LRReadSettings()


# ----- End PatchIt! LEGO Racers Settings Writing ----- #


# ----- Begin LEGO Racers Installation, Version and Settings Check ----- #


def LRGameCheck():
    '''Confirm LEGO Racers installation'''

    # Check encoding of Settings file
    logging.info("Checking encoding of {0}".format(
        os.path.join(settings_fol, LR_settings)))
    with open(os.path.join(settings_fol, LR_settings), "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (  # The settings file uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The settings file uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The settings file uses UCS-2 Little Endian
        or encoding == b"\xff\xfe/"):

        # The settings cannot be read
        logging.warning("LEGO Racers Settings cannot be read!")

        # Mark as global it is can be used in other messages
        global LR_path
        # Define blank path, since we can't read the settings
        LR_path = " "
        return False

    # The settings can be read, so do it (implied else block here)
    logging.info("Reading line 7 for LEGO Racers installation")
    with open(os.path.join(settings_fol, LR_settings),
        "rt", encoding="utf-8") as f:
        LR_path = f.readlines()[6]

    # Remove the list from the string
    LR_path = "".join(LR_path)
    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    LR_path = LR_path.strip()

     # The only three items needed to confirm a LEGO Racers installation.
    if (os.path.exists(os.path.join(LR_path, "legoracers.exe".lower()))
        and os.path.exists(os.path.join(LR_path, "lego.jam".lower()))
        and os.path.exists(os.path.join(LR_path, "goldp.dll".lower()))
        ):
        logging.info("LEGORacers.exe, LEGO.JAM, and GolDP.dll were found at {0}"
        .format(LR_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif not LR_path:
        logging.warning("LEGO Racers installation is empty!")
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("LEGORacers.exe, LEGO.JAM, and GolDP.dll were not found at {0}!".format(LR_path))
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

    # The LEGO Racers settings do not exist
    if not os.path.exists(os.path.join(settings_fol, LR_settings)):
        logging.warning("LEGO Racers Settings do not exist!")
        return False

    # The LEGO Racers settings do exist
    elif os.path.exists(os.path.join(settings_fol, LR_settings)):
        logging.info("LEGO Racers Settings do exist")

        # Check encoding of Settings file
        logging.info("Checking encoding of {0}".format(
            os.path.join(settings_fol, LR_settings)))
        with open(os.path.join(settings_fol, LR_settings), "rb") as encode_check:
            encoding = encode_check.readline(3)

        if (  # The settings file uses UTF-8-BOM encoding
            encoding == b"\xef\xbb\xbf"
            # The settings file uses UCS-2 Big Endian encoding
            or encoding == b"\xfe\xff\x00"
            # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):

            # The settings cannot be read, return False
            logging.warning("LEGO Racers Settings cannot be read!")
            return False

        # The settings can be read, so do it (implied else block here)
        logging.info("Reading line 3 for LEGO Racers first-run info")
        with open(os.path.join(settings_fol, LR_settings), "rt", encoding="utf-8") as f:
            lr_first_run = f.readlines()[2]

        # Remove the list from the string
        lr_first_run = "".join(lr_first_run)
        # Strip the path to make it valid
        logging.info("Cleaning up installation text")
        lr_first_run = lr_first_run.strip()

        # '0' means this is a "first-run"
        # len() >= 1 means file is not empty
        if lr_first_run != "0" or len(lr_first_run) >= 1:
            logging.info("First-run info found, this is not the first-run. Switching to main menu.")
            return True

        # Any other condition, return False
        else:
            logging.warning("PatchIt! has never been run!")
            return False


# ----- End LEGO Racers Installation, Version and Settings Check ----- #


# ----- Begin PatchIt! LEGO LOCO Settings Reading ----- #


def LOCOReadSettings():
    '''Read PatchIt! LEGO LOCO settings'''

    # The settings file does not exist
    if not os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.warning("LEGO LOCO Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO LOCO settings")
        LOCOWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.info("LEGO LOCO Settings does exist")

        # The defined installation was not confirmed by LOCOGameCheck()
        if not LOCOGameCheck():

            # Use path defined in LOCOGameCheck() for messages
            logging.warning("LEGO LOCO installation was not found!".format(
                LOCO_path))
            #colors.pc('\nCannot find {0} installation at "{1}"!\n'.format(
                #LOCO_game, LOCO_path), color.FG_LIGHT_RED)
            root = tk.Tk()
            root.withdraw()
            tk.messagebox.showerror("Invalid installation!",
                "Cannot find {0} installation at {1}".format(
                    LOCO_game, LOCO_path))

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO LOCO settings")
            LOCOWriteSettings()

        # The defined installation was confirmed by LOCOGameCheck()
        else:
            logging.info("LEGO LOCO installation was found at {0}.".format(
                LOCO_path))
            print('\n{0} installation found at "{1}"!\n'.format(
                LOCO_game, LOCO_path) + r"Would you like to change this? (Y\N)")
            changepath = input("\n\n> ")

            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                logging.info("User wants to change defined LEGO LOCO installation")
                logging.info("Proceeding to write PatchIt! LEGO LOCO settings")
                LOCOWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info('''User does not want to change the LEGO LOCO
                installation or pressed an undefined key''')
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
    logging.info("Overwrite root Tk window settings to basically hide it")
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
    title="Please select your {0} installation".format(LOCO_game),
    initialdir=app_folder
    )

    # The user clicked the cancel button
    if not new_loco_game:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a new LEGO LOCO installation!")
        ##colors.pc("\nCould not find a LEGO LOCO installation!", color.FG_LIGHT_RED)

        logging.info("Switching to main menu")
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO LOCO installation at {0}".format(
            new_loco_game))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(settings_fol):
            os.mkdir(settings_fol)

        # Write settings, using UTF-8 encoding
        logging.info("Open 'LOCO_settings' for writing using UTF-8-NOBOM encoding")
        with open(os.path.join(settings_fol, LOCO_settings),
            'wt', encoding='utf-8') as loco_file:

            # As partially defined in PatchIt! Dev-log #6 (http://wp.me/p1V5ge-yB)
            logging.info("Write line denoting what program this file belongs to")
            loco_file.write("// PatchIt! V1.1.x LEGO LOCO Settings\n")

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write brief comment explaining what the number means")
            logging.info("Write '1' to line 3 to skip first-run next time")
            loco_file.write("# Ensures the first-run process will be skipped next time\n")
            loco_file.write("1\n")

            logging.info("Write brief comment explaining what the folder path means")

            logging.info("Write new LEGO LOCO installation to fifth line (killing the new line ending)")
            loco_file.write("# Your LEGO LOCO installation path\n")
            loco_file.write(new_loco_game)

        # Log closure of file (although the with handle did it for us)
        logging.info("Closing LOCO.cfg")
        logging.info("Proceeding to PatchIt! LEGO LOCO Settings")
        LOCOReadSettings()


# ----- End PatchIt! LEGO LOCO Settings Writing ----- #


# ----- Begin LEGO LOCO Installation and Settings Check ----- #


def LOCOGameCheck():
    '''Confirm LEGO LOCO installation'''

    # Check encoding of Settings file
    logging.info("Checking encoding of {0}".format(os.path.join(settings_fol, LOCO_settings)))
    with open(os.path.join(settings_fol, LOCO_settings), "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (  # The settings file uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The settings file uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The settings file uses UCS-2 Little Endian
        or encoding == b"\xff\xfe/"):

        logging.warning("LEGO LOCO Settings cannot be read!")
        # Mark as global it is can be used in other messages
        global LOCO_path
        LOCO_path = " "
        return False

    logging.info("Reading line 5 of settings for LEGO LOCO installation")
    with open(os.path.join(settings_fol, LOCO_settings), "rt", encoding="utf-8") as f:
        LOCO_path = f.readlines()[4]

    # Remove the list from the string
    LOCO_path = "".join(LOCO_path)
    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    LOCO_path = LOCO_path.strip()

     # The only three items needed to confirm a LEGO LOCO installation.
    if (os.path.exists(os.path.join(LOCO_path, "exe".upper(), "loco.exe".lower()))
        and os.path.exists(os.path.join(LOCO_path, "exe".upper(), "lego.ini".lower()))
        and os.path.exists(os.path.join(LOCO_path, "art-res".lower()))
        ):
        logging.info("Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}".format(LOCO_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif not LOCO_path:
        logging.warning("LEGO LOCO installation written in {0} is empty!".format(LOCO_settings))
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}".format(LOCO_path))
        return False


def CheckLOCOSettings():
    '''Checks if LEGO LOCO Settings and First-run info'''

    # The LEGO LOCO settings do not exist
    if not os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.warning("LEGO LOCO Settings do not exist!")
        return False

    # The LEGO LOCO settings do exist (inplied else block here)
    elif os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.info("LEGO LOCO Settings do exist")

        # Check encoding of Settings file
        logging.info("Checking encoding of {0}".format(os.path.join(settings_fol, LOCO_settings)))
        with open(os.path.join(settings_fol, LOCO_settings), "rb") as encode_check:
            encoding = encode_check.readline(3)

        if (  # The settings file uses UTF-8-BOM encoding
            encoding == b"\xef\xbb\xbf"
            # The settings file uses UCS-2 Big Endian encoding
            or encoding == b"\xfe\xff\x00"
            # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):

            # The settings cannot be read, return False
            logging.warning("LEGO LOCO Settings cannot be read!")
            return False

        # The settings can be read, so do it (implied else block here)
        logging.info("Reading line 3 for LEGO LOCO first-run info")
        with open(os.path.join(settings_fol, LOCO_settings), "rt", encoding="utf-8") as f:
            loco_first_run = f.readlines()[2]

        # Remove the list from the string
        loco_first_run = "".join(loco_first_run)
        # Strip the path to make it valid
        logging.info("Cleaning up installation text")
        loco_first_run = loco_first_run.strip()

        # '0' means this is a "first-run"
        # len() >= 1 means file is not empty
        if loco_first_run != "0" or len(loco_first_run) >= 1:
            logging.info("LOCO First-run info found; this is not the first-run. Switching to main menu.")
            return True

        # Any other condition, return False
        else:
            logging.warning("PatchIt! has never been run!")
            return False


# ----- End LEGO LOCO Installation and Settings Check ----- #


# ------------ End PatchIt! Settings ------------ #
