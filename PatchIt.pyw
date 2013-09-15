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

-------------------------------------
PatchIt! V1.1.2 Unstable Core Module
"""

# General use modules
import sys
import os
import webbrowser
import platform
import subprocess
import argparse

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
from Game import (Racers, LOCO, rungame)

# PatchIt! "Constants"
from constants import (
    app, majver, minver, build_num, creator, LR_game, LOCO_game,
    app_folder, settings_fol, app_icon, Pi_settings)


# ------------ Begin PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Command-line Arguments ------------ #

def args():
    """PatchIt! Command-line Arguments"""
    logging.info("Command-line arguments processor started")

    parser = argparse.ArgumentParser(
        description="{0} {1} {2} Command-line Arguments".format(
            app, majver, minver))

    # Experimental Mode argument
    parser.add_argument("-t", "--test",
                        help='Enable PatchIt! experimental features',
                        action="store_true")

    # Open file argument
    parser.add_argument("-o", "--open",
                        help='''Confirm and install a PatchIt! Patch without going through the menu first''')

    # Register all the parameters
    args = parser.parse_args()

    # Declare parameters
    debugarg = args.test
    openfile = args.open

    # If the debug parameter is passed, enable the debugging messages
    if debugarg:
        global test
        test = True
        os.system("title {0} Version {1} {2} - Experimental Mode".format(
            app, majver, minver))
        logging.info("Starting PatchIt! in Experimental Mode")

    # The debug parameter was not passed, don't display debugging message
    else:
        test = False
        logging.info("Starting PatchIt! in Normal Mode")

    # If the open argument is valid,
    if openfile is not None:
        # If it is a file, switch to Patch Installation
            if os.path.isfile(openfile):
                logging.info("A file path was given, switching to extract.checkPatch()")
                extract.checkPatch(openfile)

            # It was a directory, or a non-existent file
            else:
                logging.warning("Invalid path or no parameters were given!")
                # Do nothing, let RunIt.py do its work
                pass


# ------------ End PatchIt! Command-line Arguments ------------ #


def info():
    """PatchIt! and System checks"""
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
    """PatchIt! Settings checks"""
    # Write general PatchIt! settings.
    # A check is not needed for this, it is always written.
    PiSettings()

    # Assign variables for easier access
    hasLRSettings = Racers.CheckLRSettings()
    hasLOCOSettings = LOCO.CheckLOCOSettings()

    # If the Racers settings is present but not LOCO,
    # go to main menu
    if hasLRSettings and not hasLOCOSettings:
        main(count=1)

    # If the LOCO settings is present but not Racers,
    # go to main menu
    elif hasLOCOSettings and not hasLRSettings:
        main(count=1)

    # If both the Racers and LOCO settings are present,
    # go to main menu
    elif hasLRSettings and hasLOCOSettings:
        main(count=1)

    # Any other condition
    else:
        Settings()


# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! About Box  ------------ #


def about(*args):
    """Tkinter About Box"""

    root = tk.Tk()
    # Window title
    root.title("About {0} Version {1}".format(app, majver))
    # The box cannot be other size
    root.minsize("420", "280")
    root.maxsize("420", "280")

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
                              Build {3}
               Released ?? ??, 2013

            Created 2013 Triangle717

"PatchIt! - The standard and simple way to
package and install mods for LEGO Racers"
'''.format(app, majver, minver, build_num))
    label.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    def close_about(*args):
        """Closes the About Window"""
        root.destroy()
        # Reset the count since we opened the window
        main(count=1)

    # Close About Window button
    close = ttk.Button(frame, default="active", text="Close",
                       command=close_about)
    close.grid(column=1, row=1, sticky=tk.N, pady="7")

    # GitHub Project Button
    github = ttk.Button(frame, text="Website",
                        command=lambda: webbrowser.open_new_tab(
                            "http://le717.github.io/PatchIt"))
    github.grid(column=0, row=1, sticky=tk.N, pady="7")

    # Creator's website button
    creator_site = ttk.Button(frame, text="Triangle717",
                              command=lambda: webbrowser.open_new_tab(
                                  "http://wp.me/P1V5ge-I3"))
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


def main(*args, count):  # lint:ok
    """PatchIt! Menu Layout"""
    count += 1
    # If the user has pressed an valid key 5 times or this is app launch
    if (count == 2 or count == 6):
        # Reset the count back to one,
        if count == 6:
            count = 1
        # And display the menu only at the valid times
        colors.text("\nWelcome to {0} Version {1} {2}\ncreated 2013 {3}".format(
            app, majver, minver, creator), color.FG_WHITE)

        # Normal menu display
        if not test:
            logging.info("Display normal menu to user")
            print('''
Please make a selection:

[a] About PatchIt!
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[r] Run LEGO Racers
[q] Quit''')
        # Experimental menu display
        if test:
            logging.info("Display --test menu to user")
            print('''
Please make a selection:

[a] About PatchIt!
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[j] JAM Extractor
[s] PatchIt! Settings
[r] Run LEGO Racers
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
                from Game import handlejam
                logging.info("User pressed '[j] JAM Extractor'")

                # Run the JAM Extractor wrapper
                logging.info("Running JAM Extractor wrapper")
                handlejam.main()

              # The Experimental Mode was not activated
            else:
                logging.info("The JAM Extractor wrapper cannot be activate in normal mode.")
                colors.text("\nThat is an invalid option!", color.FG_LIGHT_RED)
                main(count=count)

        # PatchIt! Settings
        elif menuopt.lower() == "s":
            logging.info("User pressed '[s] PatchIt! Settings'")
            logging.info("Running PatchIt! Settings Menu")
            Settings()

        # Easter egg
        elif menuopt.lower() == 'e':
            logging.info("User pressed the 'e' key")
            easteregg()

        # Run LEGO Racers
        elif menuopt.lower() == "r":
            path = Racers.getRacersPath()
            logging.shutdown()
            rungame.run(path)

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
            colors.text("\nThat is an invalid option!", color.FG_LIGHT_RED)
            main(count=count)


def easteregg(*args):
    """Hehehe"""
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
    """PatchIt! Settings Menu"""
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
        main(count=1)


# ------------ Begin PatchIt! General Settings ------------ #


def PiSettings():
    """Writes PatchIt! General Settings"""
    #TODO: Will be expanded with more data in a future release
    the_file = os.path.join(settings_fol, Pi_settings)
    logging.info("Writing {0}".format(the_file))
    if not os.path.exists(settings_fol):
        os.makedirs(settings_fol)

    with open(os.path.join(the_file), "wt", encoding="utf-8") as f:
        logging.info("Write line telling what program this file belongs to")
        f.write("// PatchIt! General Settings\n")

        # Write comment stating identifying the line
        logging.info("Writing comment identifying the line")
        f.write("# The version of PatchIt! you have\n")

        # Write the PatchIt! Major and Minor number,
        # as defined in the majver and minver variables
        logging.info("Writing version number of this copy of PatchIt")
        f.write("{0} {1} Build {2}".format(majver, minver, build_num))


# ------------ End PatchIt! General Settings ------------ #


# ------------ End PatchIt! Settings ------------ #
