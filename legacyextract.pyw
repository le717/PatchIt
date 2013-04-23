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
# PatchIt! V1.1.0 Stable Legacy Patch Installation code

# Import only certain items instead of "the whole toolbox"
import PatchIt, linecache, gametips, zipfile, os
from os.path import exists, join
from random import choice
from time import sleep
# Colored text
import Color as color, Color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog
# App Logging module
import logging

# ------------ Begin Legacy PatchIt! Patch Installation ------------ #

def readPatch(installpatch):
    '''Reads and Installs Legacy PatchIt! Patch'''

    logging.info("Install a Legacy PatchIt! Patch")

    # Get all patch details
    logging.info("Reading line 3 of {0} for mod name".format(installpatch))
    installname = linecache.getline(installpatch, 3)
    logging.info("Reading line 34 of {0} for mod version".format(installpatch))
    installver = linecache.getline(installpatch, 4)
    logging.info("Reading line 5 of {0} for mod author".format(installpatch))
    installauthor = linecache.getline(installpatch, 5)
    logging.info("Reading line 7 of {0} for mod description".format(installpatch))
    installdesc = linecache.getline(installpatch, 7)

    # Strip the description for better display
    logging.info("Cleaning up description text")
    installdesc = installdesc.strip()

    # Clear file cache
    logging.info("Clearing Legacy PiP file cache...")
    linecache.clearcache()

    # Display all the info
    logging.info("Display all mod info")
    logging.info('\n{0} {1} {2} "{3}"\n'.format(installname, installver, installauthor, installdesc))
    print('\n{0} {1} {2} "{3}"'.format(installname, installver, installauthor, installdesc), end="\n")

    # Clean up name and version to put all the text on one line
    logging.info("Cleaning up mod name")
    installname = installname.strip("\n")
    logging.info("Cleaning up mod version")
    installver = installver.strip("\n")

    logging.info("Do you Do you wish to install {0} {1}?".format(installname, installver))
    print("\nDo you wish to install {0} {1}? {2}".format(installname, installver, r"(y\N)"))
    confirminstall = input("\n> ")

    # No, I do not want to install the patch
    if confirminstall.lower() != "y":
        logging.warning("User does not want to install {0} {1}!".format(installname, installver))
        print("\nCanceling installation of {0} {1}...".format(installname, installver))
        sleep(1)
        logging.info("Proceeding to main menu")
        PatchIt.main()

        # Yes, I do want to install it!
    else:
        logging.info("User does want to install {0} {1}.".format(installname, installver))

        # Read the settings file for installation (LEGO Racers directory)
        # Updated in semi-accordance with PatchIt! Dev-log #6
        logging.info("Reading line 5 of settings for LEGO Racers installation")
        installpath = linecache.getline(os.path.join("Settings", "Racers.cfg"), 5)

        # Create a valid folder path
        logging.info("Cleaning up installation text")
        installpath = installpath.rstrip("\n")
        logging.info("Reading line 9 of {0} for ZIP archive".format(installpatch))
        installzipfile = linecache.getline(installpatch, 9)

        # Again, clear cache
        logging.info("Clearing settings file cache...")
        linecache.clearcache()

        # Create a vaild ZIP archive
        logging.info("Cleaning up ZIP archive text")
        installzipfile = installzipfile.rstrip("\n")

        # Find the ZIP archive
        ziplocation = installpatch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))
        logging.info("Found ZIP archive at {0}".format(ziplocation))

        # Display the Racers game tips
        logging.info("Display LEGO Racers gameplay tip")
        colors.pc("\nHere's a tip!\n" + choice(gametips.gametips), color.FG_LIGHT_GREEN)
        try:
            # Actually extract the ZIP archive
            logging.info("Extract {0} to {1}".format(installzipfile, installpath))
            with zipfile.ZipFile(ziplocation + installzipfile, "r") as extractzip:
                extractzip.extractall(path=installpath)

            # Installation was sucessful!
            logging.info("Error (exit) number '0'")
            logging.info("{0} {1} sucessfully installed to {2}".format(installname, installver, installpath))
            print("\n{0} {1} sucessfully installed!\n".format(installname, installver))

            # Log ZIP closure although it was closed automatically by with
            logging.info("Closing {0}".format(installzipfile))

        # For some reason, it cannot find the ZIP archive
        except FileNotFoundError:
            logging.info("Error number '2'")
            # Strip the PiP ID text for a smoother error message
            logging.info("Cleaning up Version and Author text")
            installver = installver.lstrip("Version: ")
            installauthor = installauthor.lstrip("Author: ")
            logging.warning("Unable to find {0} at {1}!".format(installzipfile, ziplocation))
            colors.pc('''Cannot find files for {0} {1}!
Make sure {2}{3}.zip and {4}{5}.PiP
are in the same folder, and try again.

If the error continues, contact {6}and ask for a fixed version.'''
            .format(installname, installver, installname, installver, installname, installver, installauthor), color.FG_LIGHT_RED)
            # There has to be an easier way to format the message without repeating installname/ver 3 times each...
            # Sleep a bit longer so the error message can be read.

            # The user does not have the rights to install to that location.
        except PermissionError:
            logging.info("Error number '13'")
            logging.warning("{0} does not have the rights to install {1} {2} to {3}!".format(PatchIt.app, installname, installver, installpath))
            colors.pc("\n{0} does not have the rights to install {1} {2} to {3}!\n".format(PatchIt.app, installname, installver, installpath), color.FG_LIGHT_RED)

        # Python itself had some I/O error / any exceptions not handled
        except Exception:
            logging.info("Unknown error number")
            logging.warning("{0} ran into an unknown error while trying to install {1} {2} to {3}!".format(PatchIt.app, installname, installver, installpath))
            colors.pc("\n{0} ran into an unknown error while trying to install\n{1} {2} to {3}!\n".format(PatchIt.app, installname, installver, installpath), color.FG_LIGHT_RED)

        # This is run no matter if an exception was raised nor not.
        finally:
            # Sleep for 4.5 seconds after displaying installation result before kicking back to the PatchIt! menu.
            sleep(4.5)
            logging.info("Proceeding to main menu")
            PatchIt.main()

# ------------ End Legacy PatchIt! Patch Installation ------------ #
