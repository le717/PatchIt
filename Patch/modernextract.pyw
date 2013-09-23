# -*- coding: utf-8 -*-
"""
    For YHWH so loved the world, that He gave His only begotten Son,
    that whosoever believeth in Him should not perish, but have
    everyalasting life. - John 3:16

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
PatchIt! V1.1.2 Unstable Modern Patch Installation code
"""

# General imports
import os
import time
import tarfile
import random

# Logging module
import logging

# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

# Core PatchIt! module
import PatchIt

# LEGO Racers settings
from Game import (Racers, LOCO)

# Legacy installation process
from Patch import legacyextract

# LEGO Racers gameplay tips
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
        time.sleep(0.7)

        PatchIt.main(count=1)

    # The user selected a patch
    else:
        logging.info("User selected a PatchIt! Patch")

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Pass selected file to Patch Identification process
        logging.info("Switching to checkPatch(patch)")
        checkPatch(patch)


def checkPatch(patch):
    """Checks if Patch uses the proper encoding,
    if it is an modern or legacy Patch,
    or if it is a PatchIt! Patch at all"""
    # Check encoding of Patch file
    logging.info("Checking encoding of {0}".format(patch))

    # Open it, read just the area containing the byte mark
    with open(patch, "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (  # The "Patch" uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The "Patch" uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The "Patch" uses UCS-2 Little Endian
        or encoding == b"\xff\xfe/"
    ):

        # It is not written using ANSI or UTF-8-NOBOM, go to main menu
        logging.warning("{0} is written using an unsupported encoding!".format(
            patch))
        logging.warning("{0} is not a valid PatchIt Patch!\n".format(patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        time.sleep(1)
        PatchIt.main(count=1)

    # It is written using ANSI or UTF-8-NOBOM, continue reading it
    # Confirm that this is a patch, as defined in Documentation/PiP Format.md
    # Also check if it uses the modern or legacy format, as defined in
    # PatchIt! Dev-log #7 (http://wp.me/p1V5ge-EX)
    logging.info("Reading line 1 of {0} for PiP validity check and Archive format".format(
        patch))
    with open(patch, "rt", encoding="utf-8") as f:
        lines = f.readlines()[0:2]
    valid_line = "".join(lines[0])
    archive_line = "".join(lines[1:])

    logging.info("Cleaning up validity lines")
    valid_line = valid_line.strip()
    archive_line = archive_line.strip()
    logging.info("The validity lines reads\n{0} and \n{1}"
                 .format(valid_line, archive_line))

    # PiP File Format 1.1.x validity line
    current_valid_line = "// PatchIt! PiP file format V1.1, developed by le717 and rioforce"
    # PiP File Format 1.0.x validity line
    orginal_valid_line = "// PatchIt! Patch format, created by le717 and rioforce."

    # It's a legacy Patch
    if (valid_line == orginal_valid_line and archive_line == "[General]"):
        logging.warning("{0} is a legacy PatchIt patch!\n".format(patch))
        colors.text('''\n"{0}"\nis a legacy PatchIt! Patch.
It will be installed using the legacy installation routine.
It may be best to check if a newer version of this mod is available.'''
                    .format(patch), color.FG_CYAN)

        # Delete validity lines from memory
        del lines[:]
        # Give them time to actually read the message.
        # Switch to legacy Patch Installation routine
        time.sleep(3)
        logging.info("Switching to Legacy Patch Installation routine")
        legacyextract.readPatch(patch)

    # It's a modern Patch
    elif (valid_line == current_valid_line and archive_line == "[PiA]"):
        logging.info("{0} is a modern PatchIt! Patch".format(patch))

        # Delete validity lines from memory
        del lines[:]
        # Go to the (modern) Patch Installation method
        logging.info("Proceeding to Modern Patch Installation routine")
        readModernPatch(patch)

    # It's a V1.1.0 transition Patch, a version that is NEVER to be used
    elif (valid_line == current_valid_line and archive_line == "[ZIP]"):
        logging.warning("{0} is not a valid PatchIt patch!\n".format(patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        # Delete validity lines from memory
        del lines[:]

        # Switch to main menu
        time.sleep(1)
        PatchIt.main(count=1)

    # It's not a Patch at all! D:
    # The same message as V1.1.0 Patch
    elif (valid_line != current_valid_line and archive_line != "[PiA]"):
        logging.warning("{0} is not a valid PatchIt patch!\n".format(patch))
        colors.text('\n"{0}"\nis not a valid PatchIt! Patch!'.format(patch),
                    color.FG_LIGHT_RED)

        # Delete validity lines from memory
        del lines[:]
        # Switch to main menu
        time.sleep(1)
        PatchIt.main(count=1)


# ------------ End PatchIt! Patch Selection and Identification  ------------ #


# ------------ Begin PatchIt! Patch Installation ------------ #


def readModernPatch(patch):
    """Reads PatchIt! Patch Details"""
    # Get all patch details
    with open(patch, "rt", encoding="utf-8") as f:
        logging.info("Reading contents of Patch")
        # Global so the data from it can be deleted after installation
        global all_lines
        all_lines = f.readlines()[:]

    # Assign Patch PiA
    logging.info("Assigning line 3 of {0} to PiA Archive".format(patch))
    patch_archive = all_lines[2]

    # Assign Patch Name
    logging.info("Assigning line 5 of {0} to Name".format(patch))
    name = all_lines[4]

    # Assign Patch Version
    logging.info("Assigning line 6 of {0} to Version".format(patch))
    version = all_lines[5]

    # Assign Patch Author
    logging.info("Assigning line 7 of {0} to Author".format(patch))
    author = all_lines[6]

    # Assign Patch MP
    logging.info("Assigning line 8 of {0} to MP".format(patch))
    mp = all_lines[7]

    # Assign Patch Game
    logging.info("Assigning line 9 of {0} to Game".format(patch))
    game = all_lines[8]

    # Assign Patch Description to lines 11-13,
    # or until there is no more text
    logging.info("Assigning lines 11-13 of {0} to Description".format(patch))
    desc = all_lines[10:]

    # Convert (and remove) list to string
    desc = "".join(desc)

    # Clean up the Patch info
    logging.info("Cleaning up Patch Archive")
    patch_archive = patch_archive.strip()
    logging.info("Cleaning up Patch Name")
    name = name.strip()
    logging.info("Cleaning up Patch Author")
    author = author.strip()
    logging.info("Cleaning up Patch Version")
    version = version.strip()
    logging.info("Cleaning up Patch Description")
    desc = desc.strip()
    logging.info("Cleaning up MP field")
    mp = mp.strip()
    logging.info("Cleaning up Game field")
    game = game.strip()

    # Display all the info
    logging.info("Display all Patch info")

    patch_info = '''\n{0}
Version: {1}
Author: {2}
Game: {3}

"{4}"'''.format(name, version, author, game, desc)

    # Display the info
    print(patch_info)

    logging.info("Do you Do you wish to install {0} (Version: {1})?".format(
        name, version))
    print("\nDo you wish to install {0} (Version: {1})? {2}".format(
        name, version, r"(Y\N)"))
    confirm_install = input("\n> ")

    # No, I do not want to install the patch
    if confirm_install.lower() != "y":
        logging.warning("User does not want to install {0} (Version: {1})!"
                        .format(name, version))
        colors.text("\nCanceling installation of {0} (Version: {1})".format(
            name, version), color.FG_LIGHT_RED)
        time.sleep(0.5)
        PatchIt.main(count=1)

    else:
        # Yes, I do want to install it!
        logging.info("User does want to install {0} (Version: {1}).".format(
            name, version))
        logging.info("Proceeding to installModernPatch()")
        installModernPatch(patch, name, version, author, game, mp,
                           patch_archive)


def installModernPatch(patch, name, version, author, game, mp, patch_archive):
    """Installs a Modern PatchIt! Patch"""
    # This is a LEGO LOCO patch, read the LOCO settings
    if game == "LEGO LOCO":

        # Run process to get the LOCO installation path
        logging.info("Run getLOCOPath() to get installation path for LOCO")
        install_path = LOCO.getLOCOPath()

    # This is a LEGO Racers patch, read the Racers settings
    elif game == "LEGO Racers":

        # Run process to get the Racers installation path
        logging.info("Get installation path to the Racers installation")
        install_path = Racers.getRacersPath()

    # In case the Game field says something else
    else:
        logging.error("This Patch wants to be installed for an unsupported game!")
        logging.info("Telling user about this unsupported game")
        # Tell user about this issue
        colors.text('''\n{0} (Version: {1}) was created for {2}.
PatchIt! only supports LEGO Racers and LEGO LOCO.
You may want to contact {3} and ask them if this is an error,
and request a proper Patch.'''.format(name, version, game, author),
                    color.FG_LIGHT_RED)

        # Give the user time to read the mesage
        time.sleep(5)
        # Go back to the main menu
        PatchIt.main(count=1)

    # Create a valid folder path
    logging.info("Cleaning up installation path")
    install_path = install_path.strip()

    # Find the PiA archive
    patch_location = os.path.dirname(patch)
    logging.info("Locate PiA archive at {0}".format(patch_location))

    try:
        # Actually extract the PiA archive
        logging.info("Extracting {0} to {1}".format(patch_archive,
                                                    install_path))

        with tarfile.open(os.path.join(patch_location, patch_archive),
                          "r") as tar_file:
            tar_file.extractall(install_path)

        # Display gameplay tip/MP only if Patch was successfully installed
        # Display the Racers gameplay tip
        if game == "LEGO Racers":
            logging.info("Display LEGO Racers gameplay tip")
            colors.text("\nHere's a tip!\n{0}\n".format(
                random.choice(racingtips.gametips)), color.FG_CYAN)

        # Display the LEGO LOCO map resolution.
        elif game == "LEGO LOCO":
            logging.info("Display LEGO LOCO map resolution")
            colors.text('''\nHeads up! {0} {1} was created using {2} resolution.
It may be best to play LEGO LOCO in that same resolution to avoid
cutting off any elements.'''.format(name, version, mp), color.FG_CYAN)

        # Installation was successful!
        logging.warning("Error (exit) number '0'")
        logging.info('''

{0} (Version: {1}) successfully installed to {2}'''
                     .format(name, version, install_path))
        colors.text('{0} (Version: {1}) sucessfully installed to\n"{2}"'.format(
            name, version, install_path), color.FG_LIGHT_GREEN)

        # Log Archive closure although it was closed automatically by `with`
        logging.info("Closing {0}".format(patch_archive))

        # Sleep for 1 second after displaying installation result
        # before kicking back to the main menu.
        time.sleep(1)

    # For some reason, it cannot find the Patch archive
    except FileNotFoundError:
        logging.warning("Error number '2'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

Unable to find {0} at {1}!'''.format(patch_archive, patch_location))
        colors.text('''\nCannot find Patch files for {0} (Version: {1})!
Make sure "{2}" and "{3}"
are both located at

{4}

and try again.

If this error continues, contact {5} and ask for a fixed version.'''
                    .format(name, version, os.path.basename(patch),
                    patch_archive, patch_location, author),
                    color.FG_LIGHT_RED)

        # Sleep for 2 seconds after displaying installation result
        # before kicking back to the main menu.
        time.sleep(2)

    # The user does not have the rights to install to that location
    except PermissionError:
        logging.warning("Error number '13'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

PatchIt! does not have the rights to install {0} (Version: {1}) to {2}'''
                        .format(name, version, install_path))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ['''PatchIt! does not have the rights to install
{0} (Version: {1}) to
{2}
'''.format(name, version, install_path)]):
            # Do nothing, go to main menu
            pass

    # Python itself had some I/O error/any unhandled exceptions
    except Exception:
        logging.warning("Unknown error number")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)

        logging.warning('''

PatchIt! had an unknown error while to installing {0} (Version: {1}) to {2}'''
                        .format(name, version, install_path))
        colors.text('''
PatchIt! ran into an unknown error while trying to install
{0} (Version: {1}) to

{2}
'''.format(name, version, install_path), color.FG_LIGHT_RED)

        # Sleep for 2 seconds after displaying installation result
        # before kicking back to the ,ain menu.
        time.sleep(2)

    # This is run no matter if an exception was raised nor not.
    finally:
        # Delete all PiP data to free up resources
        del all_lines[:]
        logging.info("Deleting all data from {0}{1}.PiP".format(name, version))
        PatchIt.main(count=1)


# ------------ End PatchIt! Patch Installation ------------ #
