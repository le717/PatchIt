# -*- coding: utf-8 -*-
"""
    For YHWH so loved the world, that He gave His only begotten Son,
    that whosoever believeth in Him should not perish, but have
    everyalasting life. - John 3:16

    This file is part of PatchIt!

    PatchIt!
    The standard and simple way to package and install LEGO Racers mods

    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

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
PatchIt! v1.1.3 Unstable Patch Installation code
"""

# General imports
import os
import time
import tarfile
import random

# Logging module
import logging

# File/Folder Dialog Boxes
from tkinter import (Tk, filedialog)

# PatchIt! modules
import PatchIt
from Settings import encoding

# LEGO Racers settings and gameplay tips
from Game import Racers
from Patch import racingtips

# Colored shell text
import Color as color
import Color.colors as colors

# RunAsAdmin wrapper
import runasadmin


# ----------- Begin PatchIt! Patch Selection and Identification  ----------- #


def selectPatch(*args):
    """Select a PatchIt! Patch"""
    colors.text("\nInstall a PatchIt! Patch", color.FG_LIGHT_YELLOW)
    logging.info("Install a PatchIt! Patch")

    # Draw (then withdraw) the root Tk window
    root = Tk()
    root.withdraw()

    # Overwrite root display settings
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the patch file
    logging.info("Display file selection dialog for PatchIt! Patch (*.PiP)")
    patch = filedialog.askopenfilename(
        parent=root,
        title="Select a PatchIt! Patch",
        defaultextension=".PiP",
        filetypes=[("PatchIt! Patch", "*.PiP")]
    )

    # The user clicked the cancel button
    if not patch:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a PatchIt! Patch to install!")
        colors.text("\nCould not find a PatchIt! Patch to read!",
                    color.FG_LIGHT_RED)
        time.sleep(0.6)

        PatchIt.main()

    # The user selected a patch
    else:
        logging.info("User selected a PatchIt! Patch")

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Pass selected file to Patch Identification process
        logging.info("Switching to checkPatch()")
        checkPatch(patch)


def checkPatch(patch):
    """
    Checks if Patch uses the proper encoding,
    if it is an modern or legacy Patch,
    or if it is a PatchIt! Patch at all
    """
    # Check encoding of Patch file
    if encoding.check_encoding(patch):
        # It is not written using ANSI or UTF-8-NOBOM, go to main menu
        logging.warning("{0} is written using an unsupported encoding!".format(
            patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        time.sleep(1)
        PatchIt.main()

    # It is written using UTF-8-NOBOM, continue reading it
    # Confirm that this is a patch, as defined in Documentation/PiP Format.md
    # Also check if it uses the modern or legacy format, as defined in
    # PatchIt! Dev-log #7 (http://wp.me/p1V5ge-EX)
    logging.info("Read {0} for PiP validity line and Archive format".format(
        patch))

    with open(patch, "rt", encoding="utf-8") as f:
        lines = f.readlines()[0:2]
    validLine = "".join(lines[0])
    archiveLine = "".join(lines[1:])

    logging.info("Cleaning up validity lines")
    validLine = validLine.strip()
    archiveLine = archiveLine.strip()
    logging.info("The validity lines reads\n{0} and \n{1}"
                 .format(validLine, archiveLine))

    # PiP File Format 1.1.x validity line
    curValidLine = "// PatchIt! PiP file format V1.1, developed by le717 and rioforce"
    # PiP File Format 1.0.x validity line
    orgValidLine = "// PatchIt! Patch format, created by le717 and rioforce."

    # It's a legacy Patch
    if (validLine == orgValidLine and archiveLine == "[General]"):
        logging.warning("{0} is an unsupported legacy PatchIt! Patch!\n"
                        .format(patch))
        colors.text('''\n"{0}"\nis a legacy PatchIt! Patch.

Legacy PatchIt! Patches are no longer supported!
You should contact the person you recieve this from and ask
for an updated Patch, check if an updated version is available,
or download a copy of PatchIt! Version 1.1.2 Stable, the last release
to support this Patch version.'''
                    .format(patch), color.FG_LIGHT_RED)

        # Delete validity lines from memory
        del lines[:]

        # Give them time to actually read the message.
        # Switch to legacy Patch Installation routine
        time.sleep(3)

        # Switch to main menu
        PatchIt.main()

    # It's a modern Patch
    elif (validLine == curValidLine and archiveLine == "[PiA]"):
        logging.info("{0} is a modern PatchIt! Patch".format(patch))

        # Delete validity lines from memory
        del lines[:]

        # Go to the Patch Installation method
        logging.info("Proceeding to Patch Installation routine")
        readModernPatch(patch)

    # It's a V1.1.0 transition Patch, a version that is NEVER to be used
    elif (validLine == curValidLine and archiveLine == "[ZIP]"):
        logging.warning("{0} is not a valid PatchIt patch!\n".format(patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        # Delete validity lines from memory
        del lines[:]

        # Switch to main menu
        time.sleep(1)
        PatchIt.main()

    # It's not a Patch at all! D:
    # The same message as V1.1.0 Patch
    elif (validLine != curValidLine and archiveLine != "[PiA]"):
        logging.warning("{0} is not a valid PatchIt patch!\n".format(patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        # Delete validity lines from memory
        del lines[:]

        # Switch to main menu
        time.sleep(1)
        PatchIt.main()


# ------------ End PatchIt! Patch Selection and Identification  ------------ #


# ------------ Begin PatchIt! Patch Installation ------------ #


def readModernPatch(patch):
    """Reads PatchIt! Patch Details"""
    # Get all patch details
    logging.info("Reading contents of Patch")
    with open(patch, "rt", encoding="utf-8") as f:
        # Global so the data from it can be deleted after installation
        global allLines
        allLines = f.readlines()[:]

    # Assign Patch PiA
    logging.info("Assigning line 3 of {0} to PiA Archive".format(patch))
    patchArchive = allLines[2]

    # Assign Patch Name
    logging.info("Assigning line 5 of {0} to Name".format(patch))
    name = allLines[4]

    # Assign Patch Version
    logging.info("Assigning line 6 of {0} to Version".format(patch))
    version = allLines[5]

    # Assign Patch Author
    logging.info("Assigning line 7 of {0} to Author".format(patch))
    author = allLines[6]

    # Assign Patch MP
    logging.info("Assigning line 8 of {0} to MP".format(patch))
    mp = allLines[7]

    # Assign Patch Game field
    logging.info("Assigning line 9 of {0} to Game".format(patch))
    game = allLines[8]

    # Assign Patch Description to lines 11-13,
    # or until there is no more text
    logging.info("Assigning lines 11-13 of {0} to Description".format(patch))
    desc = allLines[10:]

    # Convert (and remove) list to string
    desc = "".join(desc)

    # Clean up the Patch info
    logging.info("Cleaning up all fields")
    patchArchive = patchArchive.strip()
    name = name.strip()
    author = author.strip()
    version = version.strip()
    desc = desc.strip()
    game = game.strip()
    mp = mp.strip()

    # The Game field says something other than LEGO Racers
    if game != "LEGO Racers":
        logging.error("Patch wants to be installed for an unsupported game!")
        # Tell user about this issue
        colors.text('''\n{0} (Version: {1}) says was created for {2}.
PatchIt! only supports LEGO Racers.
You may want to contact {3} and ask them if this is an error,
and request a proper Patch.'''.format(name, version, game, author),
                    color.FG_LIGHT_RED)

        # Give the user time to read the mesage
        time.sleep(5)

        # Delete all PiP data to free up resources
        del allLines[:]

        # Go back to the main menu
        PatchIt.main()

    # Remove Game field, as it is no longer needed
    del allLines[8]

    # Display all the info
    logging.info("Display all Patch info")

    patch_info = '''\n{0}
Version: {1}
Author: {2}

"{3}"'''.format(name, version, author, desc)

    # Display the info
    print(patch_info)

    # Prompt for installation
    logging.info("Do you Do you wish to install {0} (Version: {1})?".format(
        name, version))
    print("\nDo you wish to install {0} (Version: {1})?\n".format(
        name, version))

    confirmInstall = input(r"[Y\N] > ")

    # No, I do not want to install the patch
    if confirmInstall.lower() != "y":
        logging.warning("User does not want to install {0} (Version: {1})!"
                        .format(name, version))
        colors.text("\nCanceling installation of {0} (Version: {1})".format(
            name, version), color.FG_LIGHT_RED)
        time.sleep(0.5)
        PatchIt.main()

    else:
        # Yes, I do want to install it!
        logging.info("User does want to install {0} (Version: {1}).".format(
            name, version))
        logging.info("Proceeding to installModernPatch()")
        installModernPatch(patch, name, version, author, mp, patchArchive)


def installModernPatch(patch, name, version, author, mp, patchArchive):
    """Installs a Modern PatchIt! Patch"""

    # Get the Racers installation path
    logging.info("Get path to the Racers installation")
    installPath = Racers.getRacersPath()

    # Find the PiA archive
    patchLocation = os.path.dirname(patch)
    logging.info("Locate PiA archive at {0}".format(patchLocation))

    try:
        # Actually extract the PiA archive
        logging.info("Extracting {0} to {1}".format(patchArchive,
                                                    installPath))

        with tarfile.open(os.path.join(
                          patchLocation, patchArchive), "r") as tar_file:
            tar_file.extractall(installPath)

        # Display gameplay tip only if Patch was successfully installed
        logging.info("Display LEGO Racers gameplay tip")
        colors.text("\nHere's a tip!\n{0}\n".format(
            random.choice(racingtips.gametips)), color.FG_CYAN)

        # Installation was successful!
        logging.warning("Error (exit) number '0'")
        logging.info('''

{0} (Version: {1}) successfully installed to {2}'''
                     .format(name, version, installPath))
        colors.text('{0} (Version: {1}) sucessfully installed to\n"{2}"'.format(
            name, version, installPath), color.FG_LIGHT_GREEN)

        # Log Archive closure although it was closed automatically by `with`
        logging.info("Closing {0}".format(patchArchive))

        # Sleep for 1 second after displaying installation result
        # before kicking back to the main menu.
        time.sleep(1)

    # For some reason, it cannot find the Patch archive
    except FileNotFoundError:  # lint:ok
        logging.warning("Error number '2'")
        logging.exception('''Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

Unable to find {0} at {1}!'''.format(patchArchive, patchLocation))
        colors.text('''\nCannot find Patch files for {0} (Version: {1})!
Make sure "{2}" and "{3}"
are both located at

{4}

and try again.

If this error continues, contact {5} and ask for a fixed version.'''
                    .format(name, version, os.path.basename(patch),
                            patchArchive, patchLocation, author),
                    color.FG_LIGHT_RED)

        # Sleep for 2 seconds after displaying installation result
        # before kicking back to the main menu.
        time.sleep(2)

    # The user does not have the rights to install to that location
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception('''Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

PatchIt! does not have the rights to install {0} (Version: {1}) to {2}'''
                        .format(name, version, installPath))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ['''PatchIt! does not have the rights to install
{0} (Version: {1}) to
{2}
'''.format(name, version, installPath)]):
            # Do nothing, go to main menu
            pass

    # Python itself had some I/O error/any unhandled exceptions
    except Exception:
        logging.warning("Unknown error number")
        logging.exception('''Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

PatchIt! had an unknown error while to installing {0} (Version: {1}) to {2}'''
                        .format(name, version, installPath))
        colors.text('''
PatchIt! ran into an unknown error while trying to install
{0} (Version: {1}) to

{2}
'''.format(name, version, installPath), color.FG_LIGHT_RED)

        # Sleep for 2 seconds after displaying installation result
        # before kicking back to the ,ain menu.
        time.sleep(2)

    # This is run no matter if an exception was raised nor not.
    finally:
        # Delete all PiP data to free up resources
        del allLines[:]
        logging.info("Deleting all data from {0}{1}.PiP".format(name, version))
        PatchIt.main()


# ------------ End PatchIt! Patch Installation ------------ #
