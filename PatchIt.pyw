# -*- coding: utf-8 -*-
"""
    Jesus said to him, “I am the way, the truth, and the life.
    No one comes to YHWH except through Me. - John 14:6

    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

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
# PatchIt! V1.1.2 Unstable Core Module

# General use modules
import sys
import os
import webbrowser
import platform
import subprocess

# App Logging
import logging

# GUI library
import tkinter as tk
from tkinter import ttk

# Patch Creation and Installation modules
from Patch import modernextract as extract
from Patch import moderncompress as compress

# Colored shell text
import Color as color
import Color.colors as colors

# LEGO Racers settings
from Game import (Racers, LOCO)

# PatchIt! "Constants"
from constants import (
    app, majver, minver, creator, LR_game, LOCO_game,
    exe_name, app_folder, settings_fol, app_icon, Pi_settings)


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
                print("\n{0} Version {1} Command-line arguments".format(
                    app, majver))
                # Use input rather than print so user can close the window
                # at anytime, rather than it closing after x seconds
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
                os.system("title {0} Version {1} {2} - Experimental Mode"
                .format(app, majver, minver))
                logging.info('''The test parameter was given,
enabling Experimental Mode''')
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

            # It was a directory, or a non-existent file
            else:
                logging.warning("Invalid path or no parameters were given!")
                # Do nothing, let RunIt.py do its work
                pass


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
    logging.info("You are running {0} {1} {2} on {3} {4}.".format(
        platform.python_implementation(), py_arch, platform.python_version(),
         platform.machine(), platform.platform()))
    logging.info('''
                                #############################################
                                        {0} Version {1} {2}
                                          Created 2013 {3}
                                                PatchIt.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/PatchIt/issues
                                    and attach this file for an quicker fix!
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
    hasLRSettings = Racers.CheckLRSettings()
    hasLOCOSettings = LOCO.CheckLOCOSettings()

    # Write general PatchIt! settings.
    # A check is not needed for this, it is always written.
    PiSettings()

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
    elif hasLRSettings and hasLOCOSettings:
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
    github = ttk.Button(frame, text="Website",
         command=lambda:
         webbrowser.open_new_tab("http://le717.github.io/PatchIt"))
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
    colors.text("\nWelcome to {0} Version {1} {2}\ncreated 2013 {3}".format(
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

            # Run the Patch Creation process
            logging.info("Running Patch Compression process")
            compress.patchInfo()

        # Patch Installation
        elif menuopt.lower() == "i":
            logging.info("User pressed '[i] Install a PatchIt! Patch'")

            # Run the Patch Installation process
            logging.info("Running Patch Installation process")
            extract.selectPatch()

        # JAM Extractor wrapper
        elif menuopt.lower() == "j":
            # If Experimental Mode was activated
            if test:
                import handlejam
                logging.info("User pressed '[j] JAM Extractor'")

                # Run the JAM Extractor wrapper
                logging.info("Running JAM Extractor wrapper")
                handlejam.main()

              # The Experimental Mode was not activated
            else:
                logging.info("User pressed an undefined key")
                main()

        # PatchIt! Settings
        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            logging.info("Running PatchIt! Settings Menu")
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
    tk.messagebox.askquestion("Uh-oh",
        "Would you like see your punishment for pressing that key?")
    subprocess.call([
        os.path.join("Icons", "cghbnjcGJfnvzhdgbvgnjvnxbv12n1231gsxvbhxnb.jpg")
        ], shell=True)
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
        Racers.LRReadSettings()

    # Run LOCO settings
    elif settingsopt.lower() == "l":
        logging.info("User choose LEGO LOCO")
        logging.info("Proceeding to PatchIt! LEGO LOCO Settings")
        LOCO.LOCOReadSettings()

    # Undefined input
    else:
        logging.info("User pressed an undefined key")
        main()


# ------------ Begin PatchIt! General Settings ------------ #


def PiSettings():
    '''Writes PatchIt! General Settings'''

    # Writes general PatchIt! settings,
    # Will be expanded with more data in a future release
    logging.info("Writing {0}".format(os.path.join(settings_fol, Pi_settings)))
    with open(os.path.join(settings_fol, Pi_settings),
              "wt", encoding="utf-8") as f:
        logging.info("Write line telling what program this file belongs to")
        f.write("// PatchIt! General Settings\n")

        # Write comment stating identifying the line
        logging.info("Writing comment identifying the line")
        f.write("# The version of PatchIt! you have\n")

        # Write the PatchIt! Major and Minor number,
        # as defined in the majver and minver variables
        logging.info("Writing version number of this copy of PatchIt")
        f.write("{0} {1}".format(majver, minver))


# ------------ End PatchIt! General Settings ------------ #


# ------------ End PatchIt! Settings ------------ #