# -*- coding: utf-8 -*-
"""PatchIt! - The simple way to package and install LEGO Racers mods.

Created 2013-2015 Triangle717
<http://Triangle717.WordPress.com/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PatchIt! is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PatchIt! If not, see <http://www.gnu.org/licenses/>.

"""

import os
import re
import random
import logging
import tarfile
import distutils.dir_util

import tkinter
from tkinter import (filedialog, messagebox)

import constants as const
import Color as color
import Color.colors as colors
import Settings.utils as utils
from Patch import (pipatch, racingtips)

__all__ = ("CreatePatch")


class CreatePatch(object):

    """PatchIt! Patch Creation class."""

    def __init__(self):
        """Initialize the class."""
        logging.info("New CreatePatch instance")
        self.myPatch = None
        self.__patchLoc = None
        self.__piaFile = None
        self.__pipFile = None

        self.__tempLocation = os.path.join(utils.Utils().configPath, "Temp")
        self.__hasTempFiles = False

        self.__badChars = ("\\", "/", ":", "*", "?", '"', "<", ">", "|")
        self.__badNames = ("aux", "com1", "com2", "com3", "com4", "con",
                           "lpt1", "lpt2", "lpt3", "prn", "nul")
        self.__whiteList = (
            "legomsc", ".adb", ".bdb", ".bmp", ".bvb", ".ccb", ".cdb", ".ceb",
            ".cmb", ".cpb", ".crb", ".ddb", ".emb", ".evb", ".fdb", ".gcb",
            ".gdb", ".ghb", ".hzb", ".idb", ".leb", ".lrs", ".lsb", ".mab",
            ".mdb", ".mib", ".msb", ".pcb", ".pcm", ".pwb", ".rab", ".rcb",
            ".rrb", ".sbk", ".sdb", ".skb", ".spb", ".srf", ".tdb", ".tga",
            ".tgb", ".tib", ".tmb", ".trb", ".tun", ".wdb")

    def _displayError(self, title, message):
        """Display error message using a a Tkinter error dialog.

        @param title {String} Dialog error title.
        @param message {String} Dialog error message.
        @returns {Boolean} Always returns False.
        """
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror(title, message)
        root.destroy()
        return False

    def _charCheck(self, userText):
        """Check the input for any invalid characters.

        @param {String} userText The text to check.
        @returns {Tuple.<boolean, string|None>} True and the invalid character
            if an invalid character was found, False and None otherwise.
        """
        for char in userText:
            if char in self.__badChars:
                return (True, char)
        return (False, None)

    def _fileNameCheck(self, userText):
        """Check if a file has an invalid filename.

        @param {String} userText The text to check.
        @returns {Boolean} True if invalid filename, False otherwise.
        """
        return userText.lower() in self.__badNames

    def _copyTempFiles(self):
        """Copy Patch files to a temporary location.

        @returns {Boolean} Always returns True.
        """
        logging.info("Copy contents of {0} to {1}".format(
                     self.__patchLoc, self.__tempLocation))

        # Only copy the files if they do not already exist
        if not os.path.exists(self.__tempLocation):
            distutils.dir_util.copy_tree(self.__patchLoc,
                                         self.__tempLocation)
        self.__hasTempFiles = True
        return True

    def createPatch(self, details):
        """Create a Patch object.

        @param {Dict} details Patch details.
            See PiPatch::__init__() for details.
        @returns {Instance} PiPatch() instance.
        """
        self.myPatch = pipatch.PiPatch(details["Name"],
                                       details["Version"],
                                       details["Author"],
                                       details["Description"])
        return self.myPatch

    def checkInput(self, userText, field=None):
        """Run the user input though some validity checks.

        @param {String} userText The text to check.
        @param {String} [field=None] The type of input being checked.
        @returns {Tuple.<boolean[, string|None[, string]]>}
            If everything checks out, a single-index True.
            Otherwise, False, a string stating the type of error encountered,
            and in the invalid character check, a third index containing the
            invalid character.

            Possible error types and defination:
            * blank: Empty input
            * quit: Cancel the process
            * fname: Invalid file name (Name and Version only)
            * input: Invalid character (Name and Version only)
        """
        # Blank input
        if len(userText) == 0 or re.search(r"^\s+$", userText):
            return (False, "blank")

        # Cancel creation
        elif userText.lower() == "q":
            return (False, "quit")

        # Name and Version fields only
        if field in ("Name", "Version"):

            # File name
            if self._fileNameCheck(userText):
                return (False, "fname")

            # Invalid character
            badChar = self._charCheck(userText)
            if badChar[0]:
                return (False, "input", badChar[1])

        return (True,)

    def selectFiles(self):
        """Select the directory containing the Patch files.

        @returns {Boolean|String} False if user does not select a directory,
            otherwise a path to the directory containing the Patch files.
        """
        logging.info("Select the Patch files")
        # Tkinter prep
        root = tkinter.Tk()
        root.withdraw()
        root.overrideredirect(True)
        root.geometry('0x0+0+0')
        root.deiconify()
        root.lift()
        root.focus_force()

        # The files to be compressed
        patchFiles = filedialog.askdirectory(
            parent=root,
            title="Select the files for {0}".format(
                self.myPatch.prettyPrint())
        )

        # Restore focus
        root.destroy()

        # The user clicked the cancel button
        if not patchFiles:
            logging.warning("User did not select any files to compress!")
            self._displayError("Missing files!",
                               "Cannot find any files to compress!")
            return False

        # Store the path
        self.__patchLoc = patchFiles.replace("\\", os.path.sep)
        logging.info("The Patch files are located at {0}".format(
                     self.__patchLoc))
        return self.__patchLoc

    def fileCheck(self):
        """Check for and remove files that are not whitelisted.

        @returns {Boolean} Always returns True.
        """
        # Copy temp files if needed
        if not self.__hasTempFiles:
            self._copyTempFiles()

        # Get a file tree
        logging.info("Check for non-whitelisted files")
        for root, dirnames, filenames in os.walk(self.__tempLocation):
            for fname in filenames:

                # Split the file name and extension
                name, ext = os.path.splitext(fname.lower())

                # The extension and the file name (extension-less files)
                # are not in the  whitelist
                if (ext not in self.__whiteList and
                        name not in self.__whiteList):

                    # Delete the file
                    fileName = os.path.join(root, fname)
                    logging.info("Delete {0}".format(fileName))
                    os.unlink(fileName)

                    # Delete empty directories
                    emptyDir = os.path.dirname(fileName)
                    if not os.listdir(emptyDir):
                        logging.info("Delete empty directory {0}".format(
                                     emptyDir))
                        distutils.dir_util.remove_tree(emptyDir)
        return True

    def upperCaseConvert(self):
        """Convert file names to uppercase per game requirement.

        @returns {Boolean} Always returns True.
        """
        # Copy temp files if needed
        if not self.__hasTempFiles:
            self._copyTempFiles()

        # Get a file tree
        logging.info("Check for non-uppercased files")
        for root, dirnames, filenames in os.walk(self.__tempLocation):
            for fname in filenames:

                # Rename the file to be all uppercase if needed
                if fname != fname.upper():
                    logging.info("Rename {0} to be all uppercase".format(
                                 fname))
                    fileName = os.path.join(root, fname)
                    os.replace(fileName, os.path.join(root, fname.upper()))
        return True

    def deleteFiles(self):
        """Delete temporary folder created during compression.

        @returns {Boolean} Always returns True.
        """
        try:
            # Delete temporary directory
            logging.info("Delete temporary files from {0}".format(
                         self.__tempLocation))
            distutils.dir_util.remove_tree(self.__tempLocation)

        except FileNotFoundError:
            logging.exception("Something went wrong! Here's what happened\n",
                              exc_info=True)

    def savePatch(self):
        """Save a PatchIt! Patch to disk."""
        logging.info("Saving PatchIt! Patch")
        self.__piaFile = os.path.join(self.__patchLoc,
                                      self.myPatch.getArchiveName())
        self.__pipFile = os.path.join(self.__patchLoc,
                                      self.myPatch.getPatchName())

        try:
            # PiA archive
            with tarfile.open(self.__piaFile, "w:xz") as archive:
                archive.add(self.__tempLocation, "")

            # Display gameplay tip
            logging.info("LEGO Racers gameplay tip")
            colors.text("\n\nHere's a tip!\n{0}\n".format(
                random.choice(racingtips.gametips)), color.FG_CYAN)

            # PiP file
            with open(self.__pipFile, "wt", encoding="utf_8") as patch:
                patch.write(self.myPatch.getPatch())

            # Success!
            logging.info("Patch saved to {0}".format(self.__patchLoc))
            colors.text("\n{0} saved to\n{1}".format(self.myPatch.prettyPrint(),
                                                     self.__patchLoc),
                        color.FG_LIGHT_GREEN)
            return True

        # Any error
        except Exception as e:
            logging.exception("Something went wrong! Here's what happened\n",
                              exc_info=True)
            self._displayError("A error has occurred!",
                               """An error has occurred while saving your Patch.
Please report this to {0} for inspection.""".format(const.creator))


def main():
    logging.info("Create a PatchIt! Patch")
    colors.text("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)
    colors.text('\nType "q" in any field to cancel.', color.FG_WHITE)
    patch = CreatePatch()
    logging.info("Get Patch details")

    patchDetails = {}
    for value in ("Name", "Version", "Author", "Description"):
        userText = input("\n{0}: ".format(value)).strip()

        # Validate the input
        results = patch.checkInput(userText, value)
        while not results[0]:
            # Cancel creation process
            if results[1] == "quit":
                logging.warning("User canceled Patch creation!")
                colors.text("\nCancel creation of PatchIt! Patch",
                            color.FG_LIGHT_RED)
                return False

            # Blank input
            elif results[1] == "blank":
                logging.warning("The {0} field was left blank!".format(value))
                colors.text("\nThe field must be filled out!\n",
                            color.FG_LIGHT_RED)

            # Invalid character
            elif results[1] == "input":
                logging.warning("An invalid character was entered!")
                colors.text('\n"{0}" is an invalid character!\n'.format(
                            results[2]), color.FG_LIGHT_RED)

            # Invalid file name
            elif results[1] == "fname":
                logging.warning("An invalid file name was entered!".format(
                                userText))
                colors.text('\n"{0}" is an invalid file name!\n'.format(
                            userText), color.FG_LIGHT_RED)

            userText = input("\n{0}: ".format(value)).strip()
            results = patch.checkInput(userText, value)

        # Store the input
        logging.info("Store value for {0} field".format(value))
        patchDetails[value] = userText

    # Create a Patch object, locate the Patch files
    patch.createPatch(patchDetails)
    patchFiles = patch.selectFiles()

    # User canceled the selection
    if not patchFiles:
        return False

    # Copy temporary files, convert file name cases
    patch.fileCheck()
    patch.upperCaseConvert()

    # Save the Patch, remove temp files
    patch.savePatch()
    patch.deleteFiles()
    return True

#import runasadmin


#def writePatch(patch_files, mp, game):
#    """Writes and compresses PatchIt! Patch"""
#    try:
#        # The Patch was created successfully!
#        logging.info("Error (exit) number '0'")
#
#    # The user does not have the rights to write a PiP in that location
#    except PermissionError:  # lint:ok
#        logging.warning("Error number '13'")
#        logging.exception('''Oops! Something went wrong! Here's what happened
#
#''', exc_info=True)
#        logging.warning('''
#
#PatchIt! does not have the rights to create {0} (Version: {1})'''
#                        .format(name, version))  # lint:ok
#
#        # User did not want to reload with Administrator rights
#        if not runasadmin.AdminRun().launch(
#            ["PatchIt! does not have the rights to create {0} (Version: {1})"
#                                    .format(name, version)]):  # lint:ok
#            # Do nothing, go to main menu
#            pass
#
#    # Python itself had some I/O error/any exceptions not handled
#    except Exception:
#        logging.warning("Unknown error number")
#        logging.exception('''Oops! Something went wrong! Here's what happened
#
#''', exc_info=True)
#        logging.warning('''
#
#PatchIt! ran into an unknown error while trying to create
#{0} (Version: {1})!'''
#                        .format(name, version))  # lint:ok
#        colors.text('''
#PatchIt! ran into an unknown error while trying to create
#{0} (Version: {1})!'''.format(name, version), color.FG_LIGHT_RED)  # lint:ok
#
#        # Remove the incomplete PiA archive
#        try:
#            os.unlink(the_archive)
#
#        # In case the file was never created in the first place
#        except FileNotFoundError:  # lint:ok
#            pass
#
#        # Remove the incomplete PiP file
#        try:
#            os.unlink(the_patch)
#        # In case the file was never created in the first place
#        except FileNotFoundError:  # lint:ok
#            pass
