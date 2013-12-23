# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013-2014 Triangle717 <http://Triangle717.WordPress.com/>

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
PatchIt! LEGO Racers Settings
"""

import os

# App Logging
import logging

# GUI library
import tkinter as tk

# File/Folder Dialog Boxes
from tkinter import (Tk, filedialog)

# PatchIt! modules
import PatchIt
import constants as const
from Settings import encoding

# ----- Begin PatchIt! LEGO Racers Settings Reading ----- #


def getRacersPath():
    """Special-use function to get and return the Racers installation path"""
    # The LEGO Racers settings do not exist
    if not os.path.exists(os.path.join(const.settings_fol, const.LR_settings)):
        logging.warning("Could not find LEGO Racers settings!")
        LRReadSettings()

    # The LEGO Racers settings do exist
    # Check file encoding
    if encoding.check_encoding(os.path.join(
        const.settings_fol, const.LR_settings)):

        # The settings cannot be read for installation,
        # go write them so this Patch can be installed
        logging.warning("LEGO Racers Settings cannot be read!")
        LRReadSettings()

    # The LEGO Racers settings can be read
    # Read the settings file for installation (LEGO Racers directory)
    logging.info("Reading line 7 of settings for LEGO Racers installation")

    try:
        with open(os.path.join(const.settings_fol, const.LR_settings),
                  "rt", encoding="utf-8") as f:
            racers_install_path = f.readlines()[6]

        # Create a valid folder path
        logging.info("Cleaning up installation path")
        racers_install_path = racers_install_path.strip()
        return racers_install_path

    # It may exist, but it doesn't mean the path is set up
    except IndexError:
        logging.error("The LEGO Racers Installation has not been set up!")
        LRWriteSettings()


def LRReadSettings():
    """Read PatchIt! LEGO Racers settings"""
    # The settings file does not exist
    if not os.path.exists(os.path.join(const.settings_fol, const.LR_settings)):
        logging.warning("LEGO Racers Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO Racers settings")
        LRWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(const.settings_fol, const. LR_settings)):
        logging.info("LEGO Racers Settings do exist")

        # The first-run check came back False,
        # Go write the settings so we don't attempt to read a blank file
        if not CheckLRSettings():
            logging.warning('''The first-run check came back False!
Writing LEGO Racers settings so we don't read an empty file.''')
            LRWriteSettings()

        # The defined installation was not confirmed by LRGameCheck()
        if not LRGameCheck():
            # Use path defined in LRGameCheck() for messages
            logging.warning("LEGO Racers installation was not found at {0}"
                            .format(LR_path))
            root = Tk()
            root.withdraw()
            tk.messagebox.showerror("Invalid installation!",
                                    "Cannot find {0} installation at {1}"
                                    .format(const.LR_game, LR_path))
            root.destroy()

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO Racers settings")
            LRWriteSettings()

        # The defined installation was confirmed by LRGameCheck()
        else:
            print('\nA {0} {1} release was found at\n\n"{2}"\n\n{3}\n'.format(
                const.LR_game, LR_ver, LR_path,
                "Would you like to change this?"))

            change_racers_path = input(r"[Y\N] > ")

            # Yes, I want to change the defined installation
            if change_racers_path.lower() == "y":
                logging.info("User wants to change the Racers installation")
                logging.info("Proceeding to write new LEGO Racers settings")
                LRWriteSettings()

            # No, I do not want to change the defined installation
            else:
                logging.info('''User does not want to change the LEGO Racers
installation or pressed an undefined key''')
                PatchIt.main()


# ----- End PatchIt! LEGO Racers Settings Reading ----- #


# ----- Begin PatchIt! LEGO Racers Settings Writing ----- #


def LRWriteSettings():
    """Write PatchIt! LEGO Racers settings"""
    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root Tk window settings to hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can receive the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the LEGO Racers installation
    logging.info("Display file dialog for LEGO Racers installation")
    new_racers_game = filedialog.askopenfilename(
        parent=root,
        title="Where is LEGORacers.exe",
        defaultextension=".exe",
        filetypes=[("LEGORacers.exe", "*.exe")]
    )

    # Get the directory the Exe is in
    new_racers_game = os.path.dirname(new_racers_game)

    # The user clicked the cancel button
    if not new_racers_game:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Go back to the main menu
        logging.warning("User did not select a new LEGO Racers installation!")
        PatchIt.main()

    # The user selected a folder
    else:
        logging.info("User selected a new LEGO Racers installation at {0}"
                     .format(new_racers_game))

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(const.settings_fol):
            os.mkdir(const.settings_fol)

        # Write settings, using UTF-8 encoding
        logging.info("Open 'Racers.cfg' for writing using UTF-8-NOBOM encoding")
        with open(os.path.join(const.settings_fol, const.LR_settings),
                  "wt", encoding="utf-8") as racers_file:

            # As partially defined in PatchIt! Dev-log #6
            # (http://wp.me/p1V5ge-yB)
            logging.info("Write line telling what program this file belongs to")
            racers_file.write("// PatchIt! V1.1.x LEGO Racers Settings\n")

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Brief comment explaining what the number means")
            racers_file.write("# Ensures the first-run process will be skipped next time\n")
            logging.info("Write '1' to line 3 to skip first-run next time")
            racers_file.write("1\n")

            # Run check for 1999 or 2001 version of Racers
            logging.info("Find the version of LEGO Racers")
            LRVer = LRVerCheck(new_racers_game)

            logging.info("Write brief comment telling what version this is")
            racers_file.write("# Your version of LEGO Racers\n")
            logging.info("Write game version to fifth line")
            racers_file.write(LRVer)

            logging.info("Write brief comment explaining the folder path")
            racers_file.write("\n# Your LEGO Racers installation path\n")
            logging.info("Write new installation path to seventh line")
            racers_file.write(new_racers_game)

        # Log closure of file (although the with handle did it for us)
        logging.info("Closing Racers.cfg")
        logging.info("Proceeding to read LEGO Racers Settings")
        LRReadSettings()


# ----- End PatchIt! LEGO Racers Settings Writing ----- #


# ----- Begin LEGO Racers Installation, Version and Settings Check ----- #


def LRGameCheck():
    """Confirms LEGO Racers installation"""
    # Check encoding of Settings file
    logging.info("Checking encoding of {0}".format(
        os.path.join(const.settings_fol, const.LR_settings)))

    if encoding.check_encoding(os.path.join(
        const.settings_fol, const.LR_settings)):

        # The settings cannot be read
        logging.warning("LEGO Racers Settings cannot be read!")

        # Mark as global it is can be used in other messages
        global LR_path
        # Define blank path, since we can't read the settings
        LR_path = '" "'
        return False

    # The settings can be read, so do it (implied else block here)
    logging.info("Reading line 7 for LEGO Racers installation")
    with open(os.path.join(const.settings_fol, const.LR_settings),
              "rt", encoding="utf-8") as game_confirm:
        lines = game_confirm.readlines()[:]

    # Get just the string from the list
    # Mark as global it is can be used in other messages
    global LR_ver
    LR_ver = "".join(lines[4])
    LR_path = "".join(lines[6])

    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    LR_path = LR_path.strip()
    LR_ver = LR_ver.strip()

    # Delete the reading to free up system resources
    logging.info("Deleting raw reading of {0}".format(const.LR_settings))
    del lines[:]

    # The only three items needed to confirm a LEGO Racers installation.
    if (os.path.exists(
        os.path.join(LR_path, "legoracers.exe".lower())
        )
        and os.path.exists(
            os.path.join(LR_path, "lego.jam".lower())
        )
            and os.path.exists(
                os.path.join(LR_path, "goldp.dll".lower()))):

        logging.info("LEGORacers.exe, LEGO.JAM, and GolDP.dll were found at {0}"
                     .format(LR_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif not LR_path:
        logging.warning("LEGO Racers installation is empty!")
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning("LEGORacers.exe, LEGO.JAM, and GolDP.dll were not found at {0}!"
                        .format(LR_path))
        return False


def LRVerCheck(new_racers_game):
    """Is this a 1999 or 2001 release of LEGO Racers?"""
    # LEGORacers.icd was not found, this is a 2001 release
    if not os.path.exists(
            os.path.join(new_racers_game, "legoracers.icd".lower())):
        logging.info("LEGORacers.icd was not found, this is the 2001 release")
        LRVer = "2001"
        return LRVer

    # LEGORacers.icd was found, this is a 1999 release
    else:
        # Log the result, send back the result
        logging.info("LEGORacers.icd was found, this is the 1999 release")
        LRVer = "1999"
        return LRVer


def CheckLRSettings():
    """Gets LEGO Rackers Settings and First-run info"""
    # The LEGO Racers settings do not exist
    if not os.path.exists(os.path.join(const.settings_fol, const.LR_settings)):
        logging.warning("LEGO Racers Settings do not exist!")
        return False

    # The LEGO Racers settings do exist
    elif os.path.exists(os.path.join(const.settings_fol, const.LR_settings)):
        logging.info("LEGO Racers Settings do exist")

        # Check encoding of Settings file
        if encoding.check_encoding(os.path.join(
        const.settings_fol, const.LR_settings)):

            # The settings cannot be read, return False
            logging.warning("LEGO Racers Settings cannot be read!")
            return False

        # The settings can be read, so do it (implied else block here)
        logging.info("Reading line 3 for LEGO Racers first-run info")
        with open(os.path.join(const.settings_fol, const.LR_settings), "rt",
                  encoding="utf-8") as first_run_check:
            lr_first_run = first_run_check.readlines()[2]

        # Strip the path to make it valid
        logging.info("Cleaning up installation text")
        lr_first_run = lr_first_run.strip()

        # '0' means this is a "first-run"
        # '1' is the only valid value meaning the first-run has been completed
        if (lr_first_run.lower() == "0" or
                lr_first_run.lower() != "1"):
            logging.warning("PatchIt! has never been run!")
            return False

        # Any other condition, return True
        else:
            logging.info("First-run info found, this is not the first-run")
            return True


# ----- End LEGO Racers Installation, Version and Settings Check ----- #
