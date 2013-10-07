# -*- coding: utf-8 -*-
"""
    In the beginning YHWH created the heaven and the earth. - Genesis 1:1

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
PatchIt! v1.1.2 Stable Legacy Patch Installation code
"""

# General imports
import linecache
import zipfile
import time
import random

# App Logging module
import logging

# Colored text
import Color as color
import Color.colors as colors

# Core PatchIt! module
import PatchIt

# LEGO Racers Gameplay tips
from Patch import racingtips

# LEGO Racers settings
from Game import Racers

# RunAsAdmin wrapper
import runasadmin


# ------------ Begin Legacy PatchIt! Patch Installation ------------ #


def readPatch(installpatch):
    """Reads and Installs Legacy PatchIt! Patch"""
    logging.info("Install a Legacy PatchIt! Patch")

    # Get all patch details
    logging.info("Reading line 3 of {0} for mod name".format(installpatch))
    installname = linecache.getline(installpatch, 3)
    logging.info("Reading line 34 of {0} for mod version".format(installpatch))
    installver = linecache.getline(installpatch, 4)
    logging.info("Reading line 5 of {0} for mod author".format(installpatch))
    installauthor = linecache.getline(installpatch, 5)
    logging.info("Reading line 7 of {0} for mod description".format(
        installpatch))
    installdesc = linecache.getline(installpatch, 7)

    # Strip the description for better display
    logging.info("Cleaning up description text")
    installdesc = installdesc.strip()

    # Clear file cache
    logging.info("Clearing Legacy PiP file cache...")
    linecache.clearcache()

    # Display all the info
    logging.info("Display all mod info")
    logging.info('\n{0} {1} {2} "{3}"\n'.format(installname, installver,
                 installauthor, installdesc))
    print('\n{0} {1} {2} "{3}"'.format(installname, installver, installauthor,
          installdesc))

    # Clean up name and version to put all the text on one line
    logging.info("Cleaning up mod name")
    installname = installname.strip("\n")
    logging.info("Cleaning up mod version")
    installver = installver.strip("\n")

    logging.info("Do you Do you wish to install {0} {1}?".format(installname,
                 installver))
    print("\nDo you wish to install {0} {1}?\n".format(installname,
          installver))
    confirminstall = input(r"[Y\N] > ")

    # No, I do not want to install the patch
    if confirminstall.lower() != "y":
        logging.warning("User does not want to install {0} {1}!".format(
            installname, installver))
        print("\nCanceling installation of {0} {1}...".format(installname,
              installver))
        time.sleep(0.5)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # Yes, I do want to install it!
    else:
        logging.info("User does want to install {0} {1}.".format(installname,
                     installver))

         # Run process to get the Racers installation path
        logging.info("Get installation path to the Racers installation")
        install_path = Racers.getRacersPath()

        logging.info("Reading line 9 of {0} for ZIP archive".format(
            installpatch))
        installzipfile = linecache.getline(installpatch, 9)

        # Create a valid ZIP archive
        logging.info("Cleaning up ZIP archive text")
        installzipfile = installzipfile.rstrip("\n")

        # Find the ZIP archive
        ziplocation = installpatch.rstrip("{0}{1}{2}".format(installname,
                                                             installver,
                                                             ".PiP"))
        logging.info("Found ZIP archive at {0}".format(ziplocation))

        try:
            # Actually extract the ZIP archive
            logging.info("Extract {0} to {1}".format(installzipfile,
                         install_path))
            with zipfile.ZipFile(ziplocation + installzipfile,
                                 "r") as extractzip:
                extractzip.extractall(path=install_path)

            # Display the LEGO Racers game tips
            logging.info("Display LEGO Racers gameplay tip")
            colors.text("\nHere's a tip!\n{0}\n".format(
                random.choice(racingtips.gametips)), color.FG_CYAN)

            # Installation was successful!
            logging.info("Error (exit) number '0'")
            logging.info("{0} {1} successfully installed to {2}".format(
                installname, installver, install_path))

            colors.text('{0} (Version: {1}) sucessfully installed to\n"{2}"'
                        .format(installname, installver, install_path),
                        color.FG_LIGHT_GREEN)

            # Log ZIP closure although it was closed automatically by `with`
            logging.info("Closing {0}".format(installzipfile))

            # Sleep for 1 second after displaying installation result
            # before kicking back to the main menu.
            time.sleep(1)

        # For some reason, it cannot find the ZIP archive
        except FileNotFoundError:  # lint:ok
            logging.info("Error number '2'")
            logging.exception('''Oops! Something went wrong!
Here's what happened
''', exc_info=True)

            # Strip the PiP ID text for a smoother error message
            logging.info("Cleaning up Version and Author text")
            installver = installver.lstrip("Version: ")
            installauthor = installauthor.lstrip("Author: ")
            logging.warning("Unable to find {0} at {1}!".format(installzipfile,
                                                                ziplocation))
            colors.text('''Cannot find files for {0} {1}!
Make sure {0}{1}.zip and {0}{1}.PiP
are in the same folder, and try again.

If the error continues, contact {3} and ask for a fixed version.'''
                        .format(installname, installver, installauthor),
                        color.FG_LIGHT_RED)

            # Sleep for 2 seconds after displaying installation result
            # before kicking back to the main menu.
            time.sleep(2)

        # The user does not have the rights to install to that location.
        except PermissionError:  # lint:ok
            logging.info("Error number '13'")
            logging.exception('''Oops! Something went wrong!
Here's what happened
''', exc_info=True)
            logging.warning('''PatchIt! does not have the rights to install {0} {1}
to
{2}!'''.format(installname, installver, install_path))

            # User did not want to reload with Administrator rights
            if not runasadmin.AdminRun().launch(
['''PatchIt! does not have the rights to install
{0} ({1}) to
{2}
'''.format(installname, installver, install_path)]):
                # Do nothing, go to main menu
                pass

        # Python itself had some I/O error/any exceptions not handled
        except Exception:
            logging.info("Unknown error number")
            logging.exception('''Oops! Something went wrong!
Here's what happened
''', exc_info=True)
            logging.warning('''

PatchIt! had an unknown error while to installing {0} {1} to {2}'''
                            .format(installname, installver, install_path))

            colors.text('''
PatchIt! ran into an unknown error while trying to install
{0} {1}
to
{2}!'''.format(
                installname, installver, install_path), color.FG_LIGHT_RED)

            # Sleep for 2 seconds after displaying installation result
            # before kicking back to the main menu.
            time.sleep(2)

        # This is run no matter if an exception was raised nor not.
        finally:
            logging.info("Proceeding to main menu")
            PatchIt.main()


# ------------ End Legacy PatchIt! Patch Installation ------------ #
