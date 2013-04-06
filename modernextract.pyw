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
# PatchIt! V1.1.0 Unstable Modern Patch Installation code

import os, time, linecache, random
import PatchIt, legacyextract
import gametips, zipfile
# Colored shell text
import color, color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging module
import logging

# ------------ Begin PatchIt! Patch Identification  ------------ #

def checkPatch():
    '''Select a PatchIt! Patch, checks if file uses
        the modern or legacy format,
        or if it is a PatchIt! Patch at all'''

    print("\nInstall a PatchIt! Patch\n")
    logging.info("Install a PatchIt! Patch")

    # PiP label for Patch selection dialog box
    fileformat = [("PatchIt! Patch", "*.PiP")]

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

    # Select the patch file
    logging.info("Display file selection dialog for PatchIt! Patch (*.PiP)")
    patch = filedialog.askopenfilename(
    parent=root,
    title="Please select a PatchIt! Patch",
    defaultextension=".PiP",
    filetypes=fileformat)

    # The user clicked the cancel button
    if len(patch) == 0:

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select a PatchIt! Patch for installation!")
        colors.pc("\nCould not find a PatchIt! patch to read!\n", color.FG_LIGHT_RED)
        time.sleep(1)

        logging.info("Proceeding to main menu")
        PatchIt.main()

    # The user selected a patch
    else:
        logging.info("User selected a PatchIt! Patch")

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # Confirm that this is a patch, as defined in Documentation/PiP Format.md'
        # Also check if it uses the modern or legacy format, as defined in
        # PatchIt! Dev-log #7 (http://wp.me/p1V5ge-EX)
        logging.info("Reading line 1 of {0} for PiP validity check and Patch format"
        .format(patch))
        validline = linecache.getline(patch, 1)
        logging.info("The validity line reads\n\n{0}".format(validline))

        # It's a legacy Patch
        if validline == "// PatchIt! Patch format, created by le717 and rioforce.\n":
            logging.warning("{0} is a legacy PatchIt patch!\n".format(patch))
            colors.pc('''{0} is a legacy PatchIt! Patch.
It will be installed using the legacy installation routine.
It may be best to check if a newer version of this mod is available.\n'''.format(patch), color.FG_LIGHT_GREEN)

            # Dump PiP validity cache after reading
            logging.info("Clearing PiP validity cache...")
            linecache.clearcache()

            # Give them time to actually read the message.
            time.sleep(5)
            logging.info("Switching to legacy PatchIt! Patch Installation routine (legacyextract.readpatch(patch))")
            legacyextract.readPatch(patch)
            # raise SystemExit

        # It's a modern Patch
        elif validline == "// PatchIt! PiP file format V1.1, developed by le717 and rioforce\n":
            logging.info("{0} is a modern PatchIt! Patch".format(patch))

            # Dump PiP validity cache after reading
            logging.info("Clearing PiP validity cache...")
            linecache.clearcache()

            logging.info("Proceeding to modern PatchIt! Patch Installation routine (readModernPatch(patch))")
            readModernPatch(patch)

        # It's not a Patch at all! D:
        elif validline != "// PatchIt! PiP file format V1.1, developed by le717 and rioforce\n":
            logging.warning("{0} is not a valid PatchIt patch!\n".format(patch))
            colors.pc("{0} is not a valid PatchIt! Patch!\n".format(patch), color.FG_LIGHT_RED)

            # Dump PiP validity cache after reading
            logging.info("Clearing PiP validity cache...")
            linecache.clearcache()
            time.sleep(1)
            logging.info("Proceeding to main menu")
            PatchIt.main()

# ------------ End PatchIt! Patch Identification  ------------ #


# ------------ Begin PatchIt! Patch Installation ------------ #

def readModernPatch(patch):
    '''Reads PatchIt! Patch Details'''

    # Get all patch details
    logging.info("Valid PatchIt! Patch selected")
    logging.info("Reading line 7 of {0} for name".format(patch))
    name = linecache.getline(patch, 7)
    logging.info("Reading line 6 of {0} for version".format(patch))
    version = linecache.getline(patch, 6)
    logging.info("Reading line 5 of {0} for author".format(patch))
    author = linecache.getline(patch, 5)
##    logging.info("Reading line 8 of {0} for MP".format(patch))
##    mp = linecache.getline(patch, 8)
##    logging.info("Reading line 9 of {0} for Game".format(patch))
##    game = linecache.getline(patch, 9)
    logging.info("Reading lines 10-12 of {0} for description".format(patch))

    # Read lines 11-13, or until there is no more text
    with open(patch, 'rt', encoding='utf-8') as file:
        while True:
            desclines = file.readlines()[10:]
            if len(desclines) == 0:
                break
            # Convert (and remove) list to string
            desc = "".join(desclines)

    # Clear cache so file is completely re-read next time
    logging.info("Clearing PiP file cache...")
    linecache.clearcache()

    logging.info("Cleaning up mod name")
    name = name.rstrip("\n")
    logging.info("Cleaning up mod version")
    version = version.strip("\n")
    logging.info("Cleaning up mod version")
    desc  = desc.strip()

    # Display all the info
    logging.info("Display all mod info")

    mod_info = '''\n{0}
Version {1}
{2}
"{3}"'''.format(name, version, author, desc)

    logging.info(mod_info)

    print(mod_info, end="\n")

    # Strip the name and version to put all the text on one line
##    # logging.info("Cleaning up mod name")
##    # name = name.strip("\n")
##    # logging.info("Cleaning up mod version")
##    # version = version.strip("\n")

    logging.info("Do you Do you wish to install {0} {1}?".format(name, version))
    print("\nDo you wish to install {0} {1}? {2}".format(name, version, r"(y\N)"))
    confirminstall = input("\n> ")

    # No, I do not want to install the patch
    if confirminstall.lower() != "y":
        logging.warning("User does not want to install {0} {1}!".format(name, version))
        print("\nCanceling installation of {0} {1}...".format(name, version))
        time.sleep(1)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    else:
        # Yes, I do want to install it!
        logging.info("User does want to install {0} {1}.".format(name, version))
        installModernPatch(patch, name, version, author)

def installModernPatch(patch, name, version, author):
    '''Installs a Modern PatchIt! Patch'''

    # Read the settings file for installation (LEGO Racers directory)
    logging.info("Reading line 5 of settings for LEGO Racers installation")
    installationpath = linecache.getline(os.path.join("Settings", "LRsettings"), 5)

    # Create a valid folder path
    logging.info("Cleaning up installation text")
    installationpath = installationpath.rstrip("\n")
    logging.info("Reading line 3 of {0} for ZIP archive".format(patch))
    ziparchive = linecache.getline(patch, 3)

    # Again, clear cache so everything is completely re-read every time
    logging.info("Clearing settings file cache...")
    linecache.clearcache()

    # Create a vaild ZIP archive
    logging.info("Cleaning up ZIP archive text")
    ziparchive = ziparchive.rstrip("\n")

    # Find the ZIP archive
    ziplocation = patch.rstrip("{0}{1}{2}".format(name, version, ".PiP"))
    logging.info("Locate ZIP archive at {0}".format(ziplocation))

    # Display the Racers game tips
    logging.info("Display LEGO Racers gameplay tip")
    colors.pc(random.choice(gametips.gametips), color.FG_LIGHT_GREEN)

    try:
        # Actually extract the ZIP archive
        logging.info("Extract {0} to {1}".format(ziparchive, installationpath))
        with zipfile.ZipFile(ziplocation + ziparchive, "r") as extractzip:
            extractzip.extractall(path=installationpath)

        # Installation was sucessful!
        logging.info("Error (exit) number '0'")
        logging.info("{0} {1} sucessfully installed to {2}".format(name, version, installationpath))
        print("\n{0} {1} sucessfully installed!\n".format(name, version))

        # Log ZIP closure although it was closed automatically by with
        logging.info("Closing {0}".format(ziparchive))

    # For some reason, it cannot find the ZIP archive
    except FileNotFoundError:
        logging.info("Error number '2'")

        # Strip the ID text for a smoother error message
        logging.info("Cleaning up Version and Author text")
        version = version.lstrip("Version: ")
        author = author.lstrip("Author: ")
        logging.warning("Unable to find {0} at {1}!".format(ziparchive, ziplocation))
        colors.pc('''Cannot find files for {0} {1}!
Make sure {2}{3}.zip and {4}{5}.PiP
are in the same folder, and try again.

If the error continues, contact {6}and ask for a fixed version.'''
        .format(name, version, name, version, name, version, author), color.FG_LIGHT_RED)
        # There has to be an easier way to format the message without repeating name/version 3 times each...

    # The user does not have the rights to install to that location.
    except PermissionError:
        logging.info("Error number '13'")
        logging.warning("{0} does not have the rights to install {1} {2} to {3}!".format(PatchIt.app, name, version, installationpath))
        colors.pc("\n{0} does not have the rights to install {1} {2} to\n{3}!\n".format(PatchIt.app, name, version, installationpath), color.FG_LIGHT_RED)

    # Python itself had some I/O error/any unhandled exceptions
    except Exception:
        logging.info("Unknown error number")
        logging.warning("{0} ran into an unknown error while trying to install {1} {2} to {3}!".format(PatchIt.app, name, version, installationpath))
        colors.pc("\n{0} ran into an unknown error while trying to install\n{1} {2} to\n{3}!\n".format(PatchIt.app, name, version, installationpath), color.FG_LIGHT_RED)

    # This is run no matter if an exception was raised nor not.
    finally:
        # Sleep for 4.5 seconds after displaying installation result before kicking back to the PatchIt! menu.
        time.sleep(4.5)
        logging.info("Proceeding to main menu")
        PatchIt.main()

# ------------ End PatchIt! Patch Installation ------------ #
