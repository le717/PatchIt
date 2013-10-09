# -*- coding: utf-8 -*-
"""

    Hear, O Israel: YHWH our God, YHWH is one! - Deuteronmoy 6:4

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
PatchIt! v1.1.3 Unstable Modern Patch Creation code
"""

# General imports
import os
import tarfile
import time
import distutils.dir_util

# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

# App Logging module
import logging

# PatchIt! Constants
import constants as const

# Core PatchIt! module
import PatchIt

# Colored shell text
import Color as color
import Color.colors as colors

# RunAsAdmin wrapper
import runasadmin

# ------------ Begin Illegal File Check ------------ #


def file_check(path):
    """Checks for and removes illegal files"""
    # List of illegal files, taken from
    # http://www.howtogeek.com/137270/ and
    # windows.microsoft.com/en-US/windows-vista/Recognizing-dangerous-file-types

    blacklist = [
        # Programs
        ".exe", ".pif", ".application", ".gadget", ".msi", ".msp", ".com",
        ".scr", ".hta", ".cpl", ".msc", ".jar",
        # Scripts
        ".bat", ".cmd", ".vb", ".vbs", ".vbe", ".js", ".jse", ".ws", ".wsf",
        ".wsc", ".wsh", ".ps1", ".ps1xml", ".ps2", ".ps2xml", ".psc1",
        ".psc2", ".msh", ".msh1", ".msh2", ".mshxml", ".msh1xml",
        ".msh2xml", ".py", ".pyw", ".au3",
        # Resources
        ".dll", ".icd", ".pyd", ".pyo",
        # Shortcuts\Registry\Misc
        ".scf", ".lnk", ".inf", ".reg", ".db", ".PiP",
        # Office Macros
        ".doc", ".xls", ".ppt", ".docm", ".dotm", ".xlsm", ".xltm", ".pptm",
        ".potm", ".ppam", ".ppsm", ".sldm",
        # Archives
        ".zip", ".tar", ".gz", ".7z", ".wim", ".lzma", ".rar", ".bz2",
        ".bzip2", "gzip", ".tgz", ".rpm", ".deb", ".dmg", ".fat", ".ntfs",
        ".cab", ".iso", ".xz", ".nrg", ".bin", ".PiA"
    ]

    # --- Begin Temporary Folder Configuration -- #

    # Make the locations global for use in other locations
    global temp_folder, temp_location

    # Temporary directory for compression
    temp_folder = "PatchIt_Temp_Folder"

    # The full location to the temporary folder
    temp_location = os.path.join(path, temp_folder)

    # --- End Temporary Folder Configuration -- #

    # --- Begin Illegal File Scan -- #

    try:
        # Copy files to temporary location
        logging.info("Copying all contents of {0} to {1}".format(path,
                                                                 temp_location
                                                                 ))
        distutils.dir_util.copy_tree(path, temp_location)

        # Traversing the reaches of the (Temporary) Patch files...
        for root, dirnames, filenames in os.walk(temp_location):

            # Get the index and string of each item in the list
            for index, string in enumerate(filenames):

                # Split the filename into name and extension
                name, ext = os.path.splitext(string)

                # If an illegal file is found, as identified by the extension,
                # Check both ext and  ext.lower() so it is case insensitive
                if (ext.lower() in blacklist or ext in blacklist):
                    logging.warning("An illegal file ({0}) has been found!"
                                    .format(ext))

                    # Get the full path to it,
                    illegal_file = os.path.join(root, string)

                    # And remove it from the Patch files!
                    logging.info("Removing {0} from the Patch files".format(
                        illegal_file))
                    os.unlink(illegal_file)

    # Except some error occured, usually a PermissionError,
    # or an distutils error, but other stuff can occur,
    # so Exception so it is all caught
    except Exception:
        # Tracebacks are dumped to the log aready, so no need to repeat it here
        pass

    # --- End Illegal File Scan -- #


def delete_files():
    """Deletes temporary folder created during compression"""
    try:
        # Delete temporary directory
        #lint:disable
        logging.info("Delete all files at {0}".format(temp_location))
        distutils.dir_util.remove_tree(temp_location)
        #lint:enable

    # But in case the directory was not created
    except FileNotFoundError:  # lint:ok

        # Dump any error tracebacks to the log
        logging.error('''The temporary directory was not found!
It probably was created ealier.''')
        logging.exception("Oops! Something went wrong! Here's what happened\n",
                          exc_info=True)

# ------------ End Illegal File Check ------------ #


# ------------ Begin Patch Info Character and Length Checks ------------ #


def charCheck(text):
    """Checks for illegal characters in text"""
    # List of all illegal characters
    illegal_chars = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]

    # Get the length of the text, minus one for proper indexing
    len_of_text = len(text) - 1

    # Assign variable containing result of check; default to False
    illa = False

    # -1 so the first character is caught too
    while len_of_text != -1:

        # This character is allowed
        if text[len_of_text] not in illegal_chars:
            # The check goes in reverse, checking the last character first.
            len_of_text -= 1

        # This character is not allowed
        elif text[len_of_text] in illegal_chars:
            # Change value of variable; kill the loop, as we only need
            # to find one illegal character to end the (ball) game.
            illa = True
            break

    # An illegal character was found
    if illa:
        # Mark as global to display the illegal character in messages
        global char

        # Assign variable containing the illegal character
        char = text[len_of_text]
        return True

    # Return False only if no illegal character is found
    return False


#def filenameCheck(text):
    #"""Check for illegal name in text"""
     ## List of all illegal filenames
    #illegal_names = ["aux", "com1", "com2", "com3",
                     #"com4", "con", "lpt1", "lpt2",
                     #"lpt3", "prn", "nul"]

    ## Mark as global to display illegal file name in messages
    #global bad_name
    #bad_name = text

    ## If the name is present in the list
    #if text.lower() in illegal_names:
        #return True

    ## If the name is not present in the list
    #else:
        #return False


def patchName():
    """Ask for Patch Name"""
    # Mark as global to remove silly "None" error
    global name
    name = input("Name: ")

    # An invalid character was entered
    if charCheck(name):
        logging.warning(
            '"{0}" is an illegal character and is not allowed in the Patch name!'
            .format(char))
        colors.text('\n"{0}" is an illegal character!\n'.format(char),
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()

    ## An invalid file name was entered
    #elif filenameCheck(name):
        #logging.warning(
            #'"{0}" is an illegal file name and is not allowed in the Patch name!'
            #.format(bad_name))
        #colors.text('\n"{0}" is an illegal file name!\n'.format(bad_name),
                    #color.FG_LIGHT_RED)

        ## Loop back through the Patch Name Process
        #logging.info("Looping back through patchName()")
        #patchName()

    ## The field was longer than 80 characters
    #elif len(name) >= 81:
        #logging.warning("The Patch name was more than 80 characters!")
        #colors.text("\nThe Name field must be 80 characters or less!\n",
                    #color.FG_LIGHT_RED)

        ## Loop back through the Patch Name Process
        #logging.info("Looping back through patchName()")
        #patchName()

    # No characters were entered
    elif len(name) == 0:
        logging.warning("The Patch name field was left blank!")
        colors.text("\nThe Name field must be filled out!\n",
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()

     # I want to quit the process
    elif name.lower() == "q":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.text("\nCanceling creation of PatchIt! Patch",
                    color.FG_LIGHT_RED)
        PatchIt.main()

    # An invalid character was not entered/the field was filled out
    else:
        logging.info("All characters in Patch name are allowed")
        logging.info("The name field was filled out")
        return name


def patchVersion():
    """Ask for Patch Version"""
    # Mark as global to remove silly "None" error
    global version
    version = input("Version: ")

    # An invalid character was entered
    if charCheck(version):
        logging.warning(
            '"{0}" is an illegal character and is not allowed in the Patch version!'
            .format(char))
        colors.text('\n"{0}" is an illegal character!\n'.format(char),
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    ## An invalid file name was entered
    #elif filenameCheck(version):
        #logging.warning(
            #'"{0}" is an illegal file name and is not allowed in the Patch version!')
        #colors.text('\n"{0}" is an illegal file name!\n'.format(bad_name),
                    #color.FG_LIGHT_RED)

        ## Loop back through the Patch Version Process
        #logging.info("Looping back through patchVersion()")
        #patchVersion()

    ## The field was longer than 12 characters
    #elif len(name) >= 13:
        #logging.warning("The Patch version was more than 12 characters!")
        #colors.text("\nThe Version field must be 12 characters or less!\n",
                    #color.FG_LIGHT_RED)

        ## Loop back through the Patch Version Process
        #logging.info("Looping back through patchVersion()")
        #patchVersion()

    # No characters were entered
    elif len(version) == 0:
        logging.warning("The Patch version field was left blank!")
        colors.text("\nThe Version field must be filled out!\n",
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    # An invalid character was not entered/the field was filled out
    else:
        logging.info("All characters in Patch version are allowed")
        logging.info("The version field was filled out")
        return version


def patchAuthor():
    """Ask for Patch Author"""
    # Mark as global to remove silly "None" error
    global author
    author = input("Author: ")

    # No characters were entered
    if len(author) == 0:
        logging.warning("The Patch author field was left blank!")
        colors.text("\nThe Author field must be filled out!\n",
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Author Process
        logging.info("Looping back through patchAuthor()")
        patchAuthor()

    # The field was filled out
    else:
        logging.info("The author field was filled out")
        return author


def patchDesc():
    """Ask for Patch Author"""
    # Mark as global to remove silly "None" error
    global desc
    desc = input("Description: ")

    # No characters were entered
    if len(desc) == 0:
        logging.warning("The Patch description field was left blank!")
        colors.text("\nThe Description field must be filled out!\n",
                    color.FG_LIGHT_RED)

        # Loop back through the Patch Author Process
        logging.info("Looping back through patchDesc()")
        patchDesc()

    # The field was filled out
    else:
        # Check for, and replace any horizontal bars with a new line
        if "|" in desc:
            desc = desc.replace("|", "\n")

        logging.info("The description field was filled out")
        return desc


# ------------ End Patch Info Character and Length Checks ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #


def patchInfo(*args):
    """Ask for PatchIt! Patch details"""
    logging.info("Create a PatchIt! Patch")
    colors.text("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    colors.text('\nType "q" in the Name field to cancel.\n\n', color.FG_WHITE)

    logging.info("Ask for Patch name")
    patchName()

    logging.info("Ask for Patch version")
    patchVersion()

    logging.info("Ask for Patch author")
    patchAuthor()

    logging.info("Ask for Patch description")
    patchDesc()

    # Set value of Game Field
    logging.info("Set value of Game field")
    game = "LEGO Racers"

    # Set value of MP field
    logging.info("Set value of MP field")
    mp = "MP"

    # Run function to select files for compression
    selectPatchFiles(game, mp)


def selectPatchFiles(game, mp):
    """Select the Patch fils for compression"""
    # Draw (then withdraw) the root Tk window
    root = Tk()
    root.withdraw()

    # Overwrite root display settings
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can receive the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # The files to be compressed
    patch_files = filedialog.askdirectory(
        parent=root,
        title="Select the files for {0} (Version: {1})".format(
            name, version)  # lint:ok
    )

    # The user clicked the cancel button
    if not patch_files:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select any files to compress!")
        colors.text("\nCannot find any files to compress!", color.FG_LIGHT_RED)
        time.sleep(1)
        PatchIt.main()

    # The user selected files for Patch creation
    else:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()
        logging.info("User selected files at {0} for Patch compression".format(
            patch_files))
        logging.info('''The final Patch details are:

{0}
Version: {1}
Author: {2}

"{3}"
'''.format(name, version, author, desc))  # lint:ok
        logging.info("Switching to writePatch()")
        writePatch(patch_files, mp, game)


def writePatch(patch_files, mp, game):
    """Writes and compresses PatchIt! Patch"""
    try:
        # Declare the Patch PiP and Archive filenames
        the_patch = "{0}{1}.PiP".format(name, version)  # lint:ok
        the_archive = "{0}{1}.PiA".format(name, version)  # lint:ok
        logging.info("The final file names are {0} and {1}"
                     .format(the_patch, the_archive))

        # Run illegal file check
        logging.info("Run file_check() to check for and remove illegal files.")
        file_check(patch_files)

        # Change the working directory to the Patch Files directory
        logging.info("Change the working directory to {0}".format(
            patch_files))
        os.chdir(patch_files)

        # Compress the files
        logging.info('''Compress files located at {0} into an LZMA compressed
TAR archive to {1}'''.format(temp_location, patch_files))  # lint:ok

        with tarfile.open(the_archive, "w:xz") as tar_file:
            tar_file.add(temp_location, "")  # lint:ok

        # Write PiP file format, as defined in Documentation/PiP Format V1.1.md
        logging.info("Write {0} with Patch details using UTF-8 encoding"
                     .format(the_patch))

        with open("{0}".format(the_patch), 'wt', encoding='utf-8') as patch:
            patch.write('''// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[PiA]
{0}
[General]
{1}
{2}
{3}
{4}
{5}
[Description]
{6}'''.format(the_archive, name, version, author, mp, game, desc))  # lint:ok

        # The Patch was created successfully!
        logging.info("Error (exit) number '0'")
        #lint:disable
        logging.info("{0} Version: {1} created and saved to {2}"
                     .format(name, version, patch_files))
        colors.text('''
{0} (Version: {1}) successfully created and saved to
"{2}"'''.format(name, version, patch_files), color.FG_LIGHT_GREEN)
        #lint:enable

    # The user does not have the rights to write a PiP in that location
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! does not have the rights to create {0} (Version: {1})'''
                        .format(name, version))  # lint:ok

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ["PatchIt! does not have the rights to create {0} (Version: {1})"
                                    .format(name, version)]):  # lint:ok
            # Do nothing, go to main menu
            pass

    # Python itself had some I/O error/any exceptions not handled
    except Exception:
        logging.warning("Unknown error number")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! ran into an unknown error while trying to create
{0} (Version: {1})!'''
                        .format(name, version))  # lint:ok
        colors.text('''
PatchIt! ran into an unknown error while trying to create
{0} (Version: {1})!'''.format(name, version), color.FG_LIGHT_RED)  # lint:ok

        # Remove the incomplete PiA archive
        try:
            os.unlink(the_archive)

        # In case the file was never created in the first place
        except FileNotFoundError:  # lint:ok
            pass

        # Remove the incomplete PiP file
        try:
            os.unlink(the_patch)
        # In case the file was never created in the first place
        except FileNotFoundError:  # lint:ok
            pass

    finally:
        # Change the working directory back to the location of PatchIt!
        logging.info("Change the working directory back to {0}".format(
            const.app_folder))
        os.chdir(const.app_folder)
        # Run process to restore all the files in the Patch files
        logging.info("Run delete_files() to remove temporary folder")
        delete_files()
        PatchIt.main()


# ------------ End PatchIt! Patch Creation ------------ #
