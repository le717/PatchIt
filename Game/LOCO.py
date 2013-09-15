# -*- coding: utf-8 -*-
"""
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
PatchIt! LEGO LOCO Settings
"""

import os

# App Logging
import logging

# GUI library
import tkinter as tk
# File/Folder Dialog Boxes
from tkinter import (Tk, filedialog)

# PatchIt! Constants
from constants import (LOCO_game, LOCO_settings, settings_fol)
import PatchIt


# ----- Begin PatchIt! LEGO LOCO Settings Reading ----- #


def LOCOReadSettings():
    """Read PatchIt! LEGO LOCO settings"""
    # The settings file does not exist
    if not os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.warning("LEGO LOCO Settings does not exist!")
        logging.info("Proceeding to write PatchIt! LEGO LOCO settings")
        LOCOWriteSettings()

    # The setting file does exist
    elif os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.info("LEGO LOCO Settings does exist")

        # The first-run check came back False,
        # Go write the settings so we don't attempt to read a blank file
        if not CheckLOCOSettings():
            logging.warning('''The first-run check came back False!
Writing LEGO LOCO settings so we don't read an empty file.''')
            LOCOWriteSettings()

        # The defined installation was not confirmed by LOCOGameCheck()
        if not LOCOGameCheck():

            # Use path defined in LOCOGameCheck() for messages
            logging.warning("LEGO LOCO installation was not found!".format(
                LOCO_path))
            root = Tk()
            root.withdraw()
            tk.messagebox.showerror("Invalid installation!",
                "Cannot find {0} installation at {1}".format(
                    LOCO_game, LOCO_path))
            root.destroy()

            # Go write the settings file
            logging.info("Proceeding to write PatchIt! LEGO LOCO settings")
            LOCOWriteSettings()

        # The defined installation was confirmed by LOCOGameCheck()
        else:
            logging.info("LEGO LOCO installation was found at {0}.".format(
                LOCO_path))
            print('\n{0} installation found at\n\n"{1}"\n\n{2}'.format(
                LOCO_game, LOCO_path,
                r"Would you like to change this? (Y\N)"))
            change_loco_path = input("\n> ")

            # Yes, I want to change the defined installation
            if change_loco_path.lower() == "y":
                logging.info("User wants to change the LEGO LOCO installation")
                logging.info("Proceeding to write new LEGO LOCO settings")
                LOCOWriteSettings()

                # No, I do not want to change the defined installation
            else:
                logging.info('''User does not want to change the LEGO LOCO
                installation or pressed an undefined key''')
                PatchIt.main(count=1)


# ----- End PatchIt! LEGO LOCO Settings Reading ----- #


# ----- Begin PatchIt! LEGO LOCO Settings Writing ----- #


def LOCOWriteSettings():
    """Write LEGO LOCO settings"""
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

    # Select the LEGO LOCO installation
    logging.info("Display folder selection dialog for LEGO LOCO installation")
    new_loco_game = filedialog.askopenfilename(
        parent=root,
        title="Where is LOCO.exe",
        defaultextension=".exe",
        filetypes=[("LOCO.exe", "*.exe")]
    )

    # Get the directory the Exe is in
    new_loco_game = os.path.dirname(new_loco_game)

    # The user clicked the cancel button
    if not new_loco_game:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Go back to the main menu
        logging.warning("User did not select a new LEGO LOCO installation!")
        PatchIt.main(count=1)

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

        # Write settings, using UTF-8NOBOM encoding
        logging.info("Open 'LOCO.cfg' for writing using UTF-8-NOBOM encoding")
        with open(os.path.join(settings_fol, LOCO_settings),
                  'wt', encoding='utf-8') as loco_file:

            # As partially defined in PatchIt! Dev-log #6
            # (http://wp.me/p1V5ge-yB)
            logging.info("Write line telling what program this file belongs to")
            loco_file.write("// PatchIt! V1.1.x LEGO LOCO Settings\n")

            # Write brief comment explaining what the number means
            # "Ensures the first-run process will be skipped next time"
            logging.info("Write comment explaining what the number means")
            loco_file.write("# Ensures the first-run process will be skipped next time\n")
            logging.info("Write '1' to line 3 to skip first-run next time")
            loco_file.write("1\n")

            logging.info("Write comment explaining the folder path")
            loco_file.write("# Your LEGO LOCO installation path\n")
            logging.info("Write new installation path to fifth line")
            loco_file.write(new_loco_game)

        # Log closure of file (although the with handle did it for us)
        logging.info("Closing LOCO.cfg")
        logging.info("Proceeding to read LEGO LOCO Settings")
        LOCOReadSettings()


# ----- End PatchIt! LEGO LOCO Settings Writing ----- #


# ----- Begin LEGO LOCO Installation and Settings Check ----- #


def LOCOGameCheck():
    """Confirms LEGO LOCO installation"""
    # Check encoding of Settings file
    logging.info("Check encoding of {0}".format(
        os.path.join(settings_fol, LOCO_settings)))

    # Open it, read just the area containing the byte mark
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
        LOCO_path = '" "'
        return False

    logging.info("Reading line 5 of settings for LEGO LOCO installation")
    with open(os.path.join(settings_fol, LOCO_settings),
              "rt", encoding="utf-8") as game_confirm:
        LOCO_path = game_confirm.readlines()[4]

    # Remove the list from the string
    LOCO_path = "".join(LOCO_path)

    # Strip the path to make it valid
    logging.info("Cleaning up installation text")
    LOCO_path = LOCO_path.strip()

     # The only items needed to confirm a LEGO LOCO installation.
    if (os.path.exists(os.path.join(LOCO_path, "exe".upper(), "loco.exe".lower()))
        and os.path.exists(os.path.join(LOCO_path, "exe".upper(), "lego.ini".lower()))
        and os.path.exists(os.path.join(LOCO_path, "art-res".lower()))
        ):
        logging.info("Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}"
        .format(LOCO_path))
        return True

    # If the settings file was externally edited and the path was removed
    elif not LOCO_path:
        logging.warning("LEGO LOCO installation written in {0} is empty!"
        .format(LOCO_settings))
        return False

    # The installation path cannot be found, or it cannot be confirmed
    else:
        logging.warning(
            "Exe\loco.exe, Exe\LEGO.INI, and art-res were found at {0}".format(
                LOCO_path))
        return False


def CheckLOCOSettings():
    """Gets LEGO LOCO Settings and First-run info"""
    # The LEGO LOCO settings do not exist
    if not os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.warning("LEGO LOCO Settings do not exist!")
        return False

    # The LEGO LOCO settings do exist (implied else block here)
    elif os.path.exists(os.path.join(settings_fol, LOCO_settings)):
        logging.info("LEGO LOCO Settings do exist")

        # Check encoding of Settings file
        logging.info("Checking encoding of {0}".format(
            os.path.join(settings_fol, LOCO_settings)))

        # Open it, read just the area containing the byte mark
        with open(os.path.join(settings_fol, LOCO_settings),
                  "rb") as encode_check:
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
        with open(os.path.join(settings_fol, LOCO_settings), "rt",
             encoding="utf-8") as first_run_check:
            loco_first_run = first_run_check.readlines()[2]

        # Strip the path to make it valid
        logging.info("Cleaning up installation text")
        loco_first_run = loco_first_run.strip()

        # '0' means this is a "first-run"
        # '1' is the only valid value meaning the first-run has been completed
        if (loco_first_run.lower() == "0" or
            loco_first_run.lower() != "1"):
            logging.warning("PatchIt! has never been run!")
            return False

        # Any other condition, return True
        else:
            logging.info("First-run info found, this is not the first-run")
            return True


# ----- End LEGO LOCO Installation and Settings Check ----- #
