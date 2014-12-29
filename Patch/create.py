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
import logging
import distutils.dir_util

__all__ = ("CreatePatch")


class CreatePatch(object):

    def __init__(self):

        self.__patchName = None
        self.__patchVersion = None
        self.__patchAuthor = None
        self.__patchDesc = None

        # TODO Perform this in AppData, perhaps?
        self.__tempLocation = "PatchIt-Temp-Folder"
        self.__patchFiles = None

        self.__badChars = ("\\", "/", ":", "*", "?", '"', "<", ">", "|")
        self.__badNames = ("aux", "com1", "com2", "com3", "com4", "con",
                           "lpt1", "lpt2", "lpt3", "prn", "nul")
        self.__whiteList = (
            "LEGOMSC", "*.ADB", "*.BDB", "*.BMP", "*.BVB", "*.CCB", "*.CDB",
            "*.CEB", "*.CMB", "*.CPB", "*.CRB", "*.DDB", "*.EMB", "*.EVB",
            "*.FDB", "*.GCB", "*.GDB", "*.GHB", "*.HZB", "*.IDB", "*.LEB",
            "*.LRS", "*.LSB", "*.MAB", "*.MDB", "*.MIB", "*.MSB", "*.PCB",
            "*.PCM", "*.PWB", "*.RAB", "*.RCB", "*.RRB", "*.SBK", "*.SDB",
            "*.SKB", "*.SPB", "*.SRF", "*.TDB", "*.TGA", "*.TGB", "*.TIB",
            "*.TMB", "*.TRB", "*.TUN", "*.WDB")

    def _charCheck(self, userText):
        """Check the input for any illegal characters.

        @param {String} userText The text to check.
        @returns {Tuple} TODO.
        """
        for char in userText:
            if char in self.__badChars:
                return (True, char)
        return (False, None)

    def _fileNameCheck(self, userText):
        """Check if a file has an illegal filename.

        @param {String} userText The text to check.
        @returns {Boolean} TODO.
        """
        return userText.lower() in self.__badNames

    def setPatchFiles(self, patchFiles):
        self.__patchFiles = patchFiles.replace("\\", os.path.sep)
        self.__tempLocation = os.path.join(self.__patchFiles, self.__tempLocation)
        return True

    def checkInput(self, userText, field=None):
        """Run the user input though some validity checks.

        @param {String} userText The text to check.
        @param {String} [field=None] The type of input being checked.
        @returns {Tuple} TODO.
        """
        # Blank input
        if len(userText) == 0:
            return (False, "blank")

        # Invalid characters
        badChar = self._charCheck(userText)
        if badChar[0]:
            return (False, "input", badChar[1])

        # File name for Name and Version inputs only
        if field in ("name", "version"):
            if self._fileNameCheck(userText):
                return (False, "name")

        return (True,)

    def upperCaseConvert(self):
        """Convert file names to uppercase per LEGO.JAM requirements.

        @returns {Boolean} Always returns True.
        """
        try:
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
                    myFile = os.path.join(root, fname)

                    # Rename the file to be all uppercase if needed
                    if fname != fname.upper():
                        os.replace(myFile, os.path.join(root, fname.upper()))

        # Tracebacks are dumped to the log already,
        # we simply have to catch them
        except Exception:
            pass
        finally:
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



p = CreatePatch()
#p.checkInput("nul")
#p.setPatchFiles("Testing/Sample patch upper")
#p.upperCaseConvert()
#p.deleteFiles()



#import os
#import tarfile
#import time
#import distutils.dir_util
#import fnmatch
#import logging
#
#import tkinter
#from tkinter import filedialog
#
#import Color as color
#import Color.colors as colors
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


#def patchName():
#    """Ask for Patch Name"""
#    # Mark as global to remove silly "None" error
#    global name
#    name = input("Name: ")
#
#    # An invalid character was entered
#    if charCheck(name):
#        logging.warning(
#            '"{0}" is an illegal character and is not allowed in the Patch name!'
#            .format(char))
#        colors.text('\n"{0}" is an illegal character!\n'.format(char),
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Name Process
#        patchName()
#
#    ## An invalid file name was entered
#    #elif filenameCheck(name):
#        #logging.warning(
#            #'"{0}" is an illegal file name and is not allowed in the Patch name!'
#            #.format(bad_name))
#       #colors.text('\n"{0}" is an illegal file name!\n'.format(bad_name),
#                    #color.FG_LIGHT_RED)
#
#        ## Loop back through the Patch Name Process
#        #patchName()
#
#    # No characters were entered
#    elif len(name) == 0:
#        logging.warning("The Patch name field was left blank!")
#        colors.text("\nThe Name field must be filled out!\n",
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Name Process
#        patchName()
#
#     # I want to quit the process
#    elif name.lower() == "q":
#        logging.warning("User canceled PatchIt! Patch Creation!")
#        colors.text("\nCanceling creation of PatchIt! Patch",
#                    color.FG_LIGHT_RED)
#        PatchIt.main()
#    logging.info("All characters in Patch name are allowed")
#    logging.info("The name field was filled out")
#    return name
#
#
#def patchVersion():
#    """Ask for Patch Version"""
#    # Mark as global to remove silly "None" error
#    global version
#    version = input("Version: ")
#
#    # An invalid character was entered
#    if charCheck(version):
#        logging.warning(
#            '"{0}" is an illegal character and is not allowed in the Patch version!'
#            .format(char))
#        colors.text('\n"{0}" is an illegal character!\n'.format(char),
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Version Process
#        patchVersion()
#
#    ## An invalid file name was entered
#    #elif filenameCheck(version):
#        #logging.warning(
#            #'"{0}" is an illegal file name and is not allowed in the Patch version!')
#        #colors.text('\n"{0}" is an illegal file name!\n'.format(bad_name),
#                    #color.FG_LIGHT_RED)
#
#        ## Loop back through the Patch Version Process
#        #patchVersion()
#
#    # No characters were entered
#    elif len(version) == 0:
#        logging.warning("The Patch version field was left blank!")
#        colors.text("\nThe Version field must be filled out!\n",
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Version Process
#        patchVersion()
#    logging.info("All characters in Patch version are allowed")
#    logging.info("The version field was filled out")
#    return version
#
#
#def patchAuthor():
#    """Ask for Patch Author"""
#    # Mark as global to remove silly "None" error
#    global author
#    author = input("Author: ")
#
#    # No characters were entered
#    if len(author) == 0:
#        logging.warning("The Patch author field was left blank!")
#        colors.text("\nThe Author field must be filled out!\n",
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Author Process
#        patchAuthor()
#    logging.info("The author field was filled out")
#    return author
#
#
#def patchDesc():
#    """Ask for Patch Author"""
#    # Mark as global to remove silly "None" error
#    global desc
#    desc = input("Description: ")
#
#    # No characters were entered
#    if len(desc) == 0:
#        logging.warning("The Patch description field was left blank!")
#        colors.text("\nThe Description field must be filled out!\n",
#                    color.FG_LIGHT_RED)
#
#        # Loop back through the Patch Author Process
#        patchDesc()
#
#    # Check for, and replace any horizontal bars with a new line
#    if "|" in desc:
#        desc = desc.replace("|", "\n")
#    logging.info("The description field was filled out")
#    return desc
#
#
#def patchInfo(*args):
#    """Ask for PatchIt! Patch details"""
#    logging.info("Create a PatchIt! Patch")
#    colors.text("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)
#
#    # Tells the user how to cancel the process
#    colors.text('\nType "q" in the Name field to cancel.\n\n', color.FG_WHITE)
#
#    logging.info("Ask for Patch name")
#    patchName()
#
#    logging.info("Ask for Patch version")
#    patchVersion()
#
#    logging.info("Ask for Patch author")
#    patchAuthor()
#
#    logging.info("Ask for Patch description")
#    patchDesc()
#
#    # Set value of Game Field
#    logging.info("Set value of Game field")
#    game = "LEGO Racers"
#
#    # Set value of MP field
#    logging.info("Set value of MP field")
#    mp = "MP"
#
#    # Run function to select files for compression
#    selectPatchFiles(mp, game)
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
#        time.sleep(1)
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
