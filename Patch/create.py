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
import logging
import distutils.dir_util

import pipatch
# import Color as color
# import Color.colors as colors
# import Settings.utils as utils

__all__ = ("CreatePatch")


class CreatePatch(object):

    def __init__(self):
        logging.info("New CreatePatch instance")
        self.myPatch = None

#        self.__tempLocation = os.path.join(utils.configPath, "Temp")
        self.__tempLocation = os.path.join("C:/tmp", "Temp")
        self.__patchFiles = None

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

    def setPatchFiles(self, patchFiles):
        self.__patchFiles = patchFiles.replace("\\", os.path.sep)
        return True

    def createPatch(self, details):
        """Create a Patch object.

        @param {Dict} details Patch details. See PiPatch::__init__() for details.
        @returns {Instance} PiPatch() instance.
        """
        self.myPatch = pipatch.PiPatch(details["Name"],
                                       details["Version"],
                                       details["Author"],
                                       details["Description"])
        return self.myPatch

    def _charCheck(self, userText):
        """Check the input for any illegal characters.

        @param {String} userText The text to check.
        @returns {Tuple.<boolean, string|None>} TODO.
        """
        for char in userText:
            if char in self.__badChars:
                return (True, char)
        return (False, None)

    def _fileNameCheck(self, userText):
        """Check if a file has an illegal filename.

        @param {String} userText The text to check.
        @returns {Boolean} True if illegal filename, False otherwise.
        """
        return userText.lower() in self.__badNames

    def checkInput(self, userText, field=None):
        """Run the user input though some validity checks.

        @param {String} userText The text to check.
        @param {String} [field=None] The type of input being checked.
        @returns {Tuple.<boolean[, string|None[, string]]>} TODO.
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

            # Invalid characters
            badChar = self._charCheck(userText)
            if badChar[0]:
                return (False, "input", badChar[1])

        return (True,)

    def fileCheck(self):
    """Check for and remove files that are not whitelisted.

    @returns {Boolean} Always returns True.
    """
    # Get a file tree
    for root, dirnames, filenames in os.walk(self.__tempLocation):
        for fname in filenames:

            # Split the file name and extension
            name, ext = os.path.splitext(fname.lower())

            # The extension and the file name (extension-less files)
            # are not in the  whitelist
            if ext not in whiteList3 and name not in whiteList3:

                # Delete the file
                fileName = os.path.join(root, fname)
                os.unlink(fileName)

                # Delete empty directories
                emptyDir = os.path.dirname(fileName)
                if not os.listdir(emptyDir):
                    distutils.dir_util.remove_tree(emptyDir)
    return True

    def upperCaseConvert(self):
        """Convert file names to uppercase per game requirement.

        @returns {Boolean} Always returns True.
        """
        # Copy files to temporary location
        logging.info("Copying contents of {0} to {1}".format(
                    self.__patchFiles, self.__tempLocation))

        # Only copy the files if they do not already exist
        if not os.path.exists(self.__tempLocation):
            distutils.dir_util.copy_tree(self.__patchFiles, self.__tempLocation)

        # Get a file tree
        for root, dirnames, filenames in os.walk(self.__tempLocation):
            for fname in filenames:
                # Get the path to each file
                fileName = os.path.join(root, fname)

                # Rename the file to be all uppercase if needed
                if fname != fname.upper():
                    os.replace(fileName, os.path.join(root, fname.upper()))
        return True

    def deleteFiles(self):
        """Deletes temporary folder created during compression.

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



def main():
#    logging.info("Create a PatchIt! Patch")
#    colors.text("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)
#    colors.text('\nType "q" in any field to cancel.\n', color.FG_WHITE)
    patch = CreatePatch()
    logging.info("Get Patch details")

    patchDetails = {}
    neededInput = ("Name", "Version", "Author", "Description")
    for value in neededInput:
        userText = input("\n{0}: ".format(value)).strip()

        # Validate the input
        results = patch.checkInput(userText, value)
        while not results[0]:
            # Cancel creation process
            if results[1] == "quit":
#                logging.warning("User canceled Patch creation!")
#                colors.text("\nCanceling creation of PatchIt! Patch",
#                            color.FG_LIGHT_RED)
                return False

            # Blank input
            elif results[1] == "blank":
                pass # TODO Temp
#                logging.warning("The {0} field was left blank!".format(value))
#                colors.text("\nThe field must be filled out!\n",
#                            color.FG_LIGHT_RED)

            # Illegal character
            elif results[1] == "input":
                pass # TODO Temp
#                logging.warning("An illegal character was entered!")
#                colors.text('\n"{0}" is an illegal character!\n'.format(results[2]),
#                            color.FG_LIGHT_RED)

            # Illegal file name
            elif results[1] == "fname":
                pass # TODO Temp
#                logging.warning("An illegal file name was entered!".format(userText))
#                colors.text('\n"{0}" is an illegal file name!\n'.format(userText),
#                            color.FG_LIGHT_RED)

            userText = input("\n{0}: ".format(value)).strip()
            results = patch.checkInput(userText, value)

        # Store the input
        patchDetails[value] = userText


    # Locate the Patch files
    # TODO patch.something()

    # Now that we have all the information needed, create a Patch object
    myPatch = patch.createPatch(patchDetails)
    #patch.setPatchFiles("Testing/Sample patch upper")
    #patch.upperCaseConvert()
    #patch.deleteFiles()


main()



#import tarfile
#import fnmatch
#
#import tkinter
#from tkinter import filedialog
#
#import constants as const
#import runasadmin


#def fileCheck(path):
#    """Check for and remove illegal files"""
#    # List of all file extenions present in a Racers installation
#    whiteList = [
#        "LEGOMSC", "*.ADB", "*.BDB", "*.BMP", "*.BVB", "*.CCB", "*.CDB",
#        "*.CEB", "*.CMB", "*.CPB", "*.CRB", "*.DDB", "*.EMB", "*.EVB",
#        "*.FDB", "*.GCB", "*.GDB", "*.GHB", "*.HZB", "*.IDB", "*.LEB",
#        "*.LRS", "*.LSB", "*.MAB", "*.MDB", "*.MIB", "*.MSB", "*.PCB",
#        "*.PCM", "*.PWB", "*.RAB", "*.RCB", "*.RRB", "*.SBK", "*.SDB",
#        "*.SKB", "*.SPB", "*.SRF", "*.TDB", "*.TGA", "*.TGB", "*.TIB",
#        "*.TMB", "*.TRB", "*.TUN", "*.WDB",
#    ]
#
#    # All unallowed files
#    badFiles = []
#
#    try:
#        # Traversing the reaches of the (Temporary) Patch files...
#        for root, dirnames, filenames in os.walk(temp_location):  # noqa
#            # Get each item in the list
#            for MyFile in filenames:
#
#                # Get the full path to each file, add it to badFile
#                # (we'll see why in a moment)
#                illegalFile = os.path.join(root, MyFile)
#                badFiles.append(illegalFile)
#
#                for ext in whiteList:
#                    # If a file extension is allowed,
#                    #remove that file from badFiles
#                    if fnmatch.fnmatch(MyFile, ext):
#                        badFiles.remove(illegalFile)
#
#        # Delete the illegal files
#        for baddie in badFiles:
#            os.unlink(baddie)
#
#            # If a folder that contained illegal files is empty,
#            # remove it too
#            badDir = os.path.dirname(baddie)
#            if not os.listdir(badDir):
#                distutils.dir_util.remove_tree(badDir)
#        del badFiles[:]
#
#    # Tracebacks are dumped to the log aready,
#    # we simply have to catch them
#    except Exception:
#        pass
#
#
#def selectPatchFiles(mp, game):
#    """Select the Patch fils for compression"""
#    # Draw (then withdraw) the root Tk window
#    root = tkinter.Tk()
#    root.withdraw()
#
#    # Overwrite root display settings
#    root.overrideredirect(True)
#    root.geometry('0x0+0+0')
#
#    # Show window again, lift it so it can receive the focus
#    # Otherwise, it is behind the console window
#    root.deiconify()
#    root.lift()
#    root.focus_force()
#
#    # The files to be compressed
#    patch_files = filedialog.askdirectory(
#        parent=root,
#        title="Select the files for {0} (Version: {1})".format(
#            name, version)  # lint:ok
#    )
#
#    # The user clicked the cancel button
#    if not patch_files:
#        # Give focus back to console window
#        logging.info("Give focus back to console window")
#        root.destroy()
#
#        logging.warning("User did not select any files to compress!")
#        colors.text("\nCannot find any files to compress!", color.FG_LIGHT_RED)
#        PatchIt.main()
#
#    # The user selected files for Patch creation
#    else:
#        # Give focus back to console window
#        logging.info("Give focus back to console window")
#        root.destroy()
#        logging.info("User selected files at {0} for Patch compression".format(
#            patch_files))
#        logging.info('''The final Patch details are:
#
#{0}
#Version: {1}
#Author: {2}
#
#"{3}"
#'''.format(name, version, author, desc))  # lint:ok
#        writePatch(patch_files, mp, game)


#def writePatch(patch_files, mp, game):
#    """Writes and compresses PatchIt! Patch"""
#    try:
#        # Declare the Patch PiP and Archive filenames
#        the_patch = "{0}{1}.PiP".format(name, version)  # lint:ok
#        the_archive = "{0}{1}.PiA".format(name, version)  # lint:ok
#        logging.info("The final file names are {0} and {1}"
#                     .format(the_patch, the_archive))
#
#        # Run uppercase extension conversion process
#        logging.info("Run upperCaseConvert() to uppercase convert extensions")
#        upperCaseConvert(patch_files)
#
#        # Run illegal file check
#        logging.info("Run file_check() to check for and remove illegal files")
#        fileCheck(patch_files)
#
#        # Change the working directory to the Patch Files directory
#        logging.info("Change the working directory to {0}".format(
#            patch_files))
#        os.chdir(patch_files)
#
#        # Compress the files
#        logging.info('''Compress files located at {0} into an LZMA compressed
#TAR archive to {1}'''.format(temp_location, patch_files))  # lint:ok
#
#        with tarfile.open(the_archive, "w:xz") as tar_file:
#            tar_file.add(temp_location, "")  # lint:ok
#
#        # Write PiP file format, as defined in Documentation/PiP Format V1.1.md
#        logging.info("Write {0} with Patch details using UTF-8 encoding"
#                     .format(the_patch))
#
#        with open("{0}".format(the_patch), "wt", encoding="utf_8") as patch:
#            patch.write('''// PatchIt! PiP file format V1.1, developed by le717 and rioforce
#[PiA]
#{0}
#[General]
#{1}
#{2}
#{3}
#{4}
#{5}
#[Description]
#{6}'''.format(the_archive, name, version, author, mp, game, desc))  # lint:ok
#
#        # The Patch was created successfully!
#        logging.info("Error (exit) number '0'")
#        #lint:disable
#        logging.info("{0} Version: {1} created and saved to {2}"
#                     .format(name, version, patch_files))
#        colors.text('''
#{0} (Version: {1}) successfully created and saved to
#"{2}"'''.format(name, version, patch_files), color.FG_LIGHT_GREEN)
#        #lint:enable
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
#
#    finally:
#        # Change the working directory back to the location of PatchIt!
#        logging.info("Change the working directory back to {0}".format(
#            const.appFolder))
#        os.chdir(const.appFolder)
#        # Run process to restore all the files in the Patch files
#        logging.info("Run process to remove temporary folder")
#        deleteFiles()
#        PatchIt.main()
