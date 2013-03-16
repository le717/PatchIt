# PatchIt! V1.1 Unstable Modern Patch Installation code

# Import only certain items instead of "the whole toolbox"
import PatchIt,  os, time, linecache, gametips, zipfile
from os.path import exists, join
from random import choice
# Colored text (until complete GUI is written)
import color, color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog
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

    # Select the patch file

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # TODO: Make dialog active window automatically and do the same to main window when closed.
    logging.info("Display file selection dialog for PatchIt! Patch (*.PiP)")
    patch = filedialog.askopenfilename(
    title="Please select a PatchIt! Patch",
    defaultextension=".PiP",
    filetypes=fileformat)

    # The user clicked the cancel button
    if len(patch) == 0:
        logging.warning("User did not select a PatchIt! Patch for installation!")
        colors.pc("\nCould not find a PatchIt! patch to read!\n", color.FG_LIGHT_RED)
        time.sleep(1)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # The user selected a patch
    else:
        logging.info("User selected a PatchIt! Patch")

        # Confirm that this is a patch, as defined in Documentation/PiP Format.md'
        # Also check if it uses the modern or legacy format, as defined in
        # PatchIt! Dev-log #7 (http://wp.me/p1V5ge-EX)
        logging.info("Reading line 1 of {0} for PiP validity check and Patch format"
        .format(patch))
        validline = linecache.getline(patch, 1)
        logging.info("The validity line reads\n{0}".format(validline))


        # It's a legacy Patch
        if validline == "// PatchIt! Patch format, created by le717 and rioforce.\n":
            logging.warning("{0} is a legacy PatchIt patch!\n".format(patch))
            colors.pc('''{0} is a legacy PatchIt! Patch.
It will be installed using the legacy installation routine.
It may be best to check if a newer version of this mod is available.\n'''.format(patch), color.FG_LIGHT_GREEN)
            # Give them time to actually read the message.
            time.sleep(5)
            logging.info("Switching to legacy PatchIt! Patch Installation routine *name here*")
            raise SystemExit

        # It's a modern Patch
        elif validline == "// PatchIt! PiP file format V1.1, developed by le717 and rioforce\n":
            logging.info("{0} is a modern PatchIt! Patch".format(patch))
            logging.info("Proceeding to modern PatchIt! Patch Installation routine (readModernPatch(patch))")
            readModernPatch(patch)
##            raise SystemExit

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
    logging.info("Reading line 7 of {0} for mod name".format(patch))
    name = linecache.getline(patch, 7)
    logging.info("Reading line 6 of {0} for mod version".format(patch))
    version = linecache.getline(patch, 6)
    logging.info("Reading line 5 of {0} for mod author".format(patch))
    author = linecache.getline(patch, 5)
##    logging.info("Reading line 8 of {0} for mod type".format(patch))
##    modtype = linecache.getline(patch, 8)
    logging.info("Reading lines 10-12 of {0} for mod description".format(patch))

    # Read lines 10-12, or until there is no more text
    with open(patch, 'rt', encoding='utf-8') as file:
        while True:
            lines = file.readlines()[9:]
            if len(lines) == 0:
                break
            # Remove list that is is returned as, removes need for .strip()
            desc = "".join(lines)

    # Clear cache so file is completely re-read next time
    logging.info("Clearing PiP file cache...")
    linecache.clearcache()

    # Display all the info
    logging.info("Display all mod info")
    logging.info('\n{0} {1} {2} "{3}"\n'.format(name, version, author, desc))
    print('\n{0} {1} {2} "{3}"'.format(name, version, author, desc), end="\n")

    # Strip the name and version to put all the text on one line
    logging.info("Cleaning up mod name")
    name = name.strip("\n")
    logging.info("Cleaning up mod version")
    version = version.strip("\n")

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
        installModernPatch(patch, name, version, author)

def installModernPatch(patch, name, version, author):
    '''Installs a Mondern PatchIt!'''

        logging.info("User does want to install {0} {1}.".format(name, version))
        raise SystemExit

        # Read the settings file for installation (LEGO Racers directory)
        logging.info("Reading line 5 of settings for LEGO Racers installation")
        installpath = linecache.getline('settings', 5)

        # Create a valid folder path
        logging.info("Cleaning up installation text")
        installpath = installpath.rstrip("\n")
        logging.info("Reading line 3 of {0} for ZIP archive".format(patch))
        installzipfile = linecache.getline(patch, 3)

        # Again, clear cache so everything completely re-read every time
        logging.info("Clearing settings file cache...")
        linecache.clearcache()

        # Create a vaild ZIP archive
        logging.info("Cleaning up ZIP archive text")
        installzipfile = installzipfile.rstrip("\n")

        # Find the ZIP archive
        ziplocation = patch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))
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

        # The user does not have the rights to install to that location.
        except PermissionError:
            logging.info("Error number '13'")
            logging.warning("{0} does not have the rights to install {1} {2} to {3}!".format(PatchIt.app, installname, installver, installpath))
            colors.pc("\n{0} does not have the rights to install {1} {2} to {3}!\n".format(PatchIt.app, installname, installver, installpath), color.FG_LIGHT_RED)

        # Python itself had some I/O error/any unhandled exceptions
        except Exception:
            logging.info("Unknown error number")
            logging.warning("{0} ran into an unknown error while trying to install {1} {2} to {3}!".format(PatchIt.app, installname, installver, installpath))
            colors.pc("\n{0} ran into an unknown error while trying to install\n{1} {2} to {3}!\n".format(PatchIt.app, installname, installver, installpath), color.FG_LIGHT_RED)

        # This is run no matter if an exception was raised nor not.
        finally:
            # Sleep for 4.5 seconds after displaying installation result before kicking back to the PatchIt! menu.
            time.sleep(4.5)
            logging.info("Proceeding to main menu")
            PatchIt.main()

# ------------ End PatchIt! Patch Installation ------------ #