# PatchIt! V1.0.3 Stable Patch Installation code

# Import only certain items instead of "the whole toolbox"
import linecache
import PatchIt
import gametips
import zipfile
import os
from os.path import exists, join
from random import choice
from time import sleep
# Colored text (until complete GUI is written)
import color, color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog
# App Logging module
import logging


# ------------ Begin PatchIt! Patch Installation ------------ #

def readpatch():
    '''Reads and Installs PatchIt! Patch'''

    print("\nInstall a PatchIt! Patch\n")
    logging.info("Install a PatchIt! Patch")

    # PiP label for Patch selection dialog box
    fileformat = [("PatchIt! Patch", "*.PiP")]

    # Select the patch file

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # TODO: Make dialog active window automatically and do the same to main window when closed.
    logging.info("Display file selection dialog for PatchIt! Patch (*.PiP)")
    installpatch = filedialog.askopenfilename(
    title="Please select a PatchIt! Patch",
    defaultextension=".PiP",
    filetypes=fileformat)

    # The user clicked the cancel button
    if len(installpatch) == 0:
        logging.warning("User did not select a PatchIt! Patch for installation!")
        colors.pc("\nCould not find a PatchIt! patch to read!\n", color.FG_LIGHT_RED)
        sleep(1)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # The user selected a patch
    else:
        logging.info("User selected a PatchIt! Patch")
        # Confirm that this is a patch, as defined in Documentation/PiP Format.md'
        logging.info("Reading line 1 of {0} for PiP validity check".format(installpatch))
        confirmpatch = linecache.getline(installpatch, 1)

        # It's not a patch! D:
        if confirmpatch != "// PatchIt! Patch format, created by le717 and rioforce.\n": # Validity check
            logging.warning("{0} is not a valid PatchIt patch!\n".format(installpatch))
            colors.pc("{0} is not a valid PatchIt patch!".format(installpatch), color.FG_LIGHT_RED)

            # Dump PiP validity cache after reading
            logging.info("Clearing PiP validity cache...")
            linecache.clearcache()
            sleep(1)
            logging.info("Proceeding to main menu")
            PatchIt.main()

        # It is a patch! :D
        else:
            # Get all patch details
            logging.info("Valid PatchIt! Patch selected")
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

             # Clear cache so file is completely re-read next time
            logging.info("Clearing PiP file cache...")
            linecache.clearcache()

            # Display all the info
            logging.info("Display all mod info")
            logging.info('\n{0} {1} {2} "{3}"\n'.format(installname, installver, installauthor, installdesc))
            print('\n{0} {1} {2} "{3}"'.format(installname, installver, installauthor, installdesc), end="\n")

            # Strip the name and version to put all the text on one line
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
                logging.info("Reading line 2 of settings for LEGO Racers installation")
                installpath = linecache.getline('settings', 2)

                # Create a valid folder path
                logging.info("Cleaning up installation text")
                installpath = installpath.rstrip("\n")
                logging.info("Reading line 9 of {0} {1} for ZIP archive".format(installname, installver))
                installzipfile = linecache.getline(installpatch, 9)

                 # Again, clear cache so everything completely re-read every time
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
                colors.pc(choice(gametips.gametips), color.FG_LIGHT_GREEN)
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
                    # Strip the ID text for a smoother error message
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

# ------------ End PatchIt! Patch Installation ------------ #