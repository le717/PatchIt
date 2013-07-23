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
"""
# PatchIt! V1.1.1 Unstable Modern Patch Creation code

import PatchIt
import os
import shutil
import tarfile
import time
import distutils.dir_util
# Colored shell text
import Color as color
import Color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging module
import logging
# Original Character Check
#import re

# ------------ Begin Illegal File Check ------------ #


def file_check(path):
    '''Checks for, and moves illegal files to a temporary location'''

    # List of illegal files, taken from
    # http://www.howtogeek.com/137270/ and
    # windows.microsoft.com/en-US/windows-vista/Recognizing-dangerous-file-types

    blacklist = [
    # Programs
    ".exe", ".pif", ".application", ".gadget", ".msi", ".msp", ".com", ".scr",
    ".hta", ".cpl", ".msc", ".jar",
    # Scripts
    ".bat", ".cmd", ".vb", ".vbs", ".vbe", ".js", ".jse", ".ws", ".wsf", ".wsc",
    ".wsh", ".ps1", ".ps1xml", ".ps2",
    ".ps2xml", ".psc1", ".psc2", ".msh", ".msh1", ".msh2", ".mshxml",
    ".msh1xml", ".msh2xml", ".py", ".pyw", ".au3",
    # Resources
    ".dll", ".icd", ".pyd", ".pyo",
    # Shortcuts\Registry\Misc
    ".scf", ".lnk", ".inf", ".reg", ".db", ".PiP",
    # Office Macros
    ".doc", ".xls", ".ppt", ".docm", ".dotm", ".xlsm", ".xltm", ".pptm",
    ".potm", ".ppam", ".ppsm", ".sldm",
    # Archives
    ".zip", ".tar", ".gz", ".7z", ".wim", ".lzma", ".rar", ".bz2", ".bzip2",
    "gzip", ".tgz", ".rpm", ".deb", ".dmg", ".fat", ".ntfs", ".cab", ".iso",
     ".xz", ".nrg", ".bin", ".PiA"
    ]

    # --- Begin Temporary Folder Configuration -- #

    # Make the locations global for use in other locations
    global temp_folder, temp_location

    # Temporary folder for illegal files
    temp_folder = "PatchIt Temporary Folder"

    # The full location to the temporary folder
    temp_location = os.path.join(path, temp_folder)

    # --- End Temporary Folder Configuration -- #

    # --- Begin Illegal File Scan -- #

    try:
        # Copy files to temporary location
        logging.info("Copying all contents of {0} to {1}".format(path,
            temp_location))
        distutils.dir_util.copy_tree(path, temp_location)

        # Traversing the reaches of the (Temporary) Patch files...
        for root, dirnames, filenames in os.walk(temp_location):

            # Get the index and string of each item in the list
            for index, string in enumerate(filenames):
                # Split the filename into name and extension
                name, ext = os.path.splitext(string)

                # If an illegal file is found, as identified by the extension,
                # Check both ext and  ext.lower() so it is case insensitive
                if (ext.lower() in blacklist or
                    ext in blacklist):
                    logging.warning("An illegal file ({0}) has been found!"
                    .format(ext))
                    # Get the full path to it,
                    illegal_file = os.path.join(root, string)
                    # And remove it from the Patch files!
                    logging.info("Removing {0} from the Patch files".format(
                        illegal_file))
                    os.unlink(illegal_file)

    except PermissionError:
        pass

    # --- End Illegal File Scan -- #


def delete_files():
    '''Deletes temporary folder created during compression'''

    try:
        # Delete temporary directory
        logging.info("Delete all files at {0}".format(temp_location))
        distutils.dir_util.remove_tree(temp_location)
    except Exception:
        # Dump any error tracebacks to the log
        logging.warning("Unknown error number")
        logging.exception("Oops! Something went wrong! Here's what happened\n",
           exc_info=True)

# ------------ End Illegal File Check ------------ #


# ------------ Begin Patch Info Character and Length Checks ------------ #


def charCheck(text):
    '''Checks for invalid characters in text'''

    # A list of all illegal characters
    illegal_chars = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]

    # Mark as global to display invalid characters in messages
    global char
    # Get each character in the text
    for char in text:
        # A character was found
        if char in illegal_chars:
            return True
        # A character was not found
        else:
            return False

#def charCheck(text, search=re.compile(r'[^A-Za-z0-9-. ]').search):
    #'''Check if an invalid character was entered or not'''

    ## This returns True if everything is valid, and False if it isn't
    #return not bool(search(text))


def patchName():
    '''Ask for Patch Name'''

    # Mark as global to remove silly "None" error
    global name
    name = input("Name: ")

    # An invalid character was entered
    if charCheck(name):
        logging.warning("There were illegal characters in the Patch name!")
        colors.pc("\nYou have entered an illegal character!",
        color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()

    ## The field was longer than 80 characters
    #elif len(name) >= 81:
        #logging.warning("The Patch name was more than 80 characters!")
        #colors.pc("\nThe Name field must be 80 characters or less!",
        #color.FG_LIGHT_RED)

        ## Loop back through the Patch Name Process
        #logging.info("Looping back through patchName()")
        #patchName()

    # No characters were entered
    elif len(name) == 0:
        logging.warning("The Patch name field was left blank!")
        colors.pc("\nThe Name field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()

    # An invalid character was not entered/the field was filled out
    else:  # elif not charCheck(name)
        logging.info("All characters in Patch name are allowed")
        logging.info("The name field was filled out")
        return name


def patchVersion():
    '''Ask for Patch Version'''

    # Mark as global to remove silly "None" error
    global version
    version = input("Version: ")

    # An invalid character was entered
    if charCheck(version):
        logging.warning("There were illegal characters in the Patch version!")
        colors.pc("\nYou have entered an illegal character!",
        color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    ## The field was longer than 12 characters
    #elif len(name) >= 13:
        #logging.warning("The Patch version was more than 12 characters!")
        #colors.pc("\nThe Version field must be 12 characters or less!",
        #color.FG_LIGHT_RED)

        ## Loop back through the Patch Version Process
        #logging.info("Looping back through patchVersion()")
        #patchVersion()

    # No characters were entered
    elif len(version) == 0:
        logging.warning("The Patch version field was left blank!")
        colors.pc("\nThe Version field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    # An invalid character was not entered/the field was filled out
    else:  # elif not charCheck(version):
        logging.info("All characters in Patch version are allowed")
        logging.info("The version field was filled out")
        return version


def patchAuthor():
    '''Ask for Patch Author'''

    # Mark as global to remove silly "None" error
    global author
    author = input("Author: ")

    # No characters were entered
    if len(author) == 0:
        logging.warning("The Patch author field was left blank!")
        colors.pc("\nThe Author field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Author Process
        logging.info("Looping back through patchAuthor()")
        patchAuthor()

    # The field was filled out
    else:
        logging.info("The author field was filled out")
        return author


def patchDesc():
    '''Ask for Patch Author'''

    # Mark as global to remove silly "None" error
    global desc
    desc = input("Description: ")

    # No characters were entered
    if len(desc) == 0:
        logging.warning("The Patch description field was left blank!")
        colors.pc("\nThe Description field must be filled out!",
        color.FG_LIGHT_RED)

        # Loop back through the Patch Author Process
        logging.info("Looping back through patchDesc()")
        patchDesc()

    # The field was filled out
    else:
        logging.info("The description field was filled out")
        return desc


def MPField(game):
    '''Sets the value for the MP field,
    asks for map resolution for LEGO LOCO Patch'''

    # Mark as global to remove silly "None" error
    global mp

    # If  Racers Patch, automaticlly assign MP field
    if game == "LEGO Racers":
        logging.info("Setting value for LEGO Racers MP field")
        mp = "MP"
        return mp

    # This is a LOCO Patch (implied else block here)
    # Get the resolution the map was created in (it matters!)

    logging.info("What resolution was this LEGO LOCO map created with?")
    print('''\nWhat resolution was "{0}" created with?
Hint: if you are unsure, it will most likely be either'''.format(name))

    colors.pc('''
800x600,
1024x768,
1920x1024

If you used a custom resolution, be sure to enter that below.''',
color.FG_LIGHT_MAGENTA)

    try:
        # int() because the screen resolution is not expressed in
        # decimal numbers nor words, but whole numbers
        horz_res = int(input("\nWidth: "))
        vert_res = int(input("Height: "))

        # The final value
        mp = "{0}x{1}".format(horz_res, vert_res)
        logging.info("This map uses the {0} resolution".format(mp))
        logging.info("Returning resolution")
        return mp

    # A valid resolution was not entered
    except ValueError:
        logging.warning("User entered an invalid number!")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        colors.pc("You have entered a non-numerical character!")
        logging.info("Looping back through MPField()")
        MPField(game)


# ------------ End Patch Info Character and Length Checks ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #


def patchInfo(*args):
    '''Asks for PatchIt! Patch details'''

    logging.info("Create a PatchIt! Patch")
    colors.pc("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    colors.pc('Type "q" in the next field to cancel.\n', color.FG_WHITE)

    # Get what game this Patch is for
    logging.info("Is this patch for LEGO Racers, or LEGO LOCO?")

    print("Which game is this Patch created for?")
    print('''
[r] LEGO Racers
[l] LEGO LOCO
[q] Quit''')
    game_select = input("\n\n> ")

    # It's an LR Patch
    if game_select.lower() == "r":
        logging.info("User selected LEGO Racers")
        game = "LEGO Racers"

    # It's an LOCO Patch
    elif game_select.lower() == "l":
        logging.info("User selected LEGO LOCO")
        game = "LEGO LOCO"

     # I want to quit the process
    else:  # elif game_select.lower() == "q":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.pc("\nCanceling creation of PatchIt! Patch", color.FG_WHITE)
        logging.info("Switching to main menu")
        PatchIt.main()

    logging.info("Ask for Patch name")
    print("\n")
    patchName()

    logging.info("Ask for Patch version")
    patchVersion()

    logging.info("Ask for Patch author")
    patchAuthor()

    logging.info("Ask for Patch description")
    patchDesc()

    logging.info("Switching to MPField() to get value of MP field")
    MPField(game)

    # Run function to select files for compression
    selectPatchFiles(game, mp)


def selectPatchFiles(game, mp):
    '''Select the Patch fils for compression'''

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings so it will be hidden")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can receive the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # The files to be compressed
    patchfiles = filedialog.askdirectory(
    parent=root,
    title="Select the files for {0} (Version: {1})".format(name, version)
    )

    # The user clicked the cancel button
    if not patchfiles:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select any files to compress!")
        colors.pc("\nCannot find any files to compress!", color.FG_LIGHT_RED)
        time.sleep(1)
        logging.info("Switching to to main menu")
        PatchIt.main()

    # The user selected files for Patch creation
    else:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()
        logging.info("User selected files at {0} for Patch compression".format(
            patchfiles))
        logging.info('''The final Patch details are:

{0}
Version: {1}
Author: {2}
Game: {3}
{4}

"{5}"
'''.format(name, version, author, game, mp, desc))
        logging.info("Switching to writePatch()")
        writePatch(patchfiles, mp, game)


def writePatch(patchfiles, mp, game):
    '''Writes and compresses PatchIt! Patch'''

    try:
        # Declare the Patch PiP and Archive filenames
        thepatch = "{0}{1}.PiP".format(name, version)
        thearchive = "{0}{1}.PiA".format(name, version)
        logging.info("The final file names are {0} and {1}".format(thepatch,
        thearchive))

        # Run illegal file check
        logging.info("Run file_check() to check for and remove illegal files.")
        file_check(patchfiles)

        # Change the working directory to the Patch Files directory
        logging.info("Changing the working directory to {0}".format(patchfiles))
        os.chdir(patchfiles)

        # Compress the files
        logging.info('''Compress files located at {0} into an LZMA compressed
TAR archive, save archive to {1}'''.format(temp_location, patchfiles))
        with tarfile.open(thearchive, "w:xz") as tar_file:
            tar_file.add(temp_location, "")

        # Write PiP file format, as defined in Documentation/PiP Format V1.1.md
        logging.info("Write {0} with Patch details using UTF-8 encoding".format(
            thepatch))
        with open("{0}".format(thepatch), 'wt', encoding='utf-8') as patch:
            patch.write("// PatchIt! PiP file format V1.1, developed by le717 and rioforce\n")
            patch.write("[PiA]\n")
            patch.write("{0}\n".format(thearchive))
            patch.write("[GENERAL]\n")
            patch.write("{0}\n".format(author))
            patch.write("{0}\n".format(version))
            patch.write("{0}\n".format(name))
            patch.write("{0}\n".format(mp))
            patch.write("{0}\n".format(game))
            patch.write("[DESCRIPTION]\n")
            patch.write("{0}\n".format(desc))

        # The Patch was created successfully!
        logging.info("Error (exit) number '0'")
        logging.info("{0} Version: {1} created and saved to {2}".format(name,
        version, patchfiles))
        colors.pc('''
PatchIt! patch for {0} (Version: {1}) created and saved to
"{2}"'''.format(name, version, patchfiles), color.FG_LIGHT_GREEN)

    # The user does not have the rights to write a PiP in that location
    except PermissionError:
        logging.warning("Error number '13'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! does not have the rights to create {0} (Version: {1})'''.format(
    name, version))

        colors.pc("\nPatchIt! does not have the rights to create {0} (Version: {1})!"
        .format(name, version), color.FG_LIGHT_RED)

    # .PiP and/or .PiA already exists
    # Since shutil has been removed, can I change this to FileAlreadyExistsError
    except shutil.Error:
        logging.warning("shutil.Error")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

{0} or {1} already exists at "{2}" or "{3}"!'''.format(thepatch, thearchive,
    patchfiles, PatchIt.app_folder))

        colors.pc('''\n{0} or {1} already exists!
    Check either "{2}"\nor "{3}"
for the files, and move or delete them if necessary.'''.format(thepatch,
     thearchive, patchfiles, PatchIt.app_folder), color.FG_LIGHT_RED)

    # Python itself had some I/O error/any exceptions not handled
    except Exception:
        logging.warning("Unknown error number")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! ran into an unknown error while trying to create {0} (Version: {1})!'''
.format(name, version))
        colors.pc("\nPatchIt! ran into an unknown error while trying to create {0} (Version: {1})!"
        .format(name, version), color.FG_LIGHT_RED)
        try:
            os.unlink("{0}".format(thepatch))
            os.unlink("{0}".format(thearchive))
            # In case the file was never created in the first place
        except FileNotFoundError:
            pass

    finally:
        # Change the working directory back to the location of PatchIt!
        logging.info("Changing the working directory back to {0}".format(
            PatchIt.app_folder))
        os.chdir(PatchIt.app_folder)
        # Run process to restore all the files in the Patch files
        logging.info("Running delete_files() to remove temporary folder")
        delete_files()
        logging.info("Switching to main menu")
        PatchIt.main()


# ------------ End PatchIt! Patch Creation ------------ #