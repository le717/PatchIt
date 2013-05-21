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
# PatchIt! V1.1.0 Stable Modern Patch Creation code

import PatchIt
import os
import shutil
import time
# Colored shell text
import Color as color, Color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging module
import logging
# Character Check
import re

# ------------ Begin Thumbs.db Check And Delete Code ------------ #

def delThumbs(patchfiles):
    '''Checks for and Deletes Thumbs.db'''

    # Traversing the files in each subfolder..
    logging.info("Walking through {0}, looking for Thumbs.db".format(patchfiles))
    for root, dirs, files in os.walk(patchfiles):

        # Limits the amount of folders to walk through
        # GAMEDATA has 26 subfolders in all,
        # but MENUDATA as 35, so we do 35
        # to ensure all folders are checked
        if root.count(os.path.sep) >= 35:
            break

        # Thumbs.db was found
        if 'Thumbs.db' in files:
            logging.warning("Thumbs.db has been found in " + root + "!")
            # TODO: This STILL repeats itself every time Thumbs.db is found...
            colors.pc('\nThumbs.db has been found in\n"{0}"\nIt will be deleted in a few seconds.\nDon''t worry, Windows will recreate it.'.format(root), color.FG_LIGHT_RED)

            # Delete Thumbs.db
            os.unlink(os.path.join(root, "Thumbs.db"))

    else:
        logging.warning("Could not find Thumbs.db!")


# ------------ End Thumbs.db Check And Delete Code ------------ #


# ------------ Begin Patch Info Character and Length Checks ------------ #

def charCheck(text, search=re.compile(r'[^A-Za-z0-9. ]').search):
    '''Check if an invalid character was entered or not'''

    # This returns True if everything is valid, and False if it isn't
    return not bool(search(text))

def patchName():
    '''Ask for Patch Name'''

    name = input("Name: ")

    # An invalid character was entered
    if charCheck(name) == False:
        logging.warning("There were illegal characters in the Patch name!")
        colors.pc("\nYou have entered an illegal character!", color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()

    # The field was longer than 80 characters
##    elif len(name) >= 81:
##        logging.warning("The Patch name was more than 80 characters!")
##        colors.pc("\nThe Name field must be 80 characters or less!", color.FG_LIGHT_RED)
##
##        # Loop back through the Patch Name Process
##        logging.info("Looping back through patchName()")
##        patchName()

    # No characters were entered
    elif len(name) == 0:
        logging.warning("The Patch name field was left blank!")
        colors.pc("\nThe Name field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Name Process
        logging.info("Looping back through patchName()")
        patchName()


    # An invalid character was not entered/the field was filled out
    else:
        logging.info("All characters in Patch name are allowed")
        logging.info("The name field was filled out")
        return name

def patchVersion():
    '''Ask for Patch Version'''

    version = input("Version: ")

    # An invalid character was entered
    if charCheck(version) == False:
        logging.warning("There were illegal characters in the Patch version!")
        colors.pc("\nYou have entered an illegal character!", color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    # The field was longer than 12 characters
##    elif len(name) >= 13:
##        logging.warning("The Patch version was more than 12 characters!")
##        colors.pc("\nThe Version field must be 12 characters or less!", color.FG_LIGHT_RED)
##
##        # Loop back through the Patch Version Process
##        logging.info("Looping back through patchVersion()")
##        patchVersion()

    # No characters were entered
    elif len(version) == 0:
        logging.warning("The Patch version field was left blank!")
        colors.pc("\nThe Version field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Version Process
        logging.info("Looping back through patchVersion()")
        patchVersion()

    # An invalid character was not entered/the field was filled out
    else:
        logging.info("All characters in Patch version are allowed")
        logging.info("The version field was filled out")
        return version

def patchAuthor():
    '''Ask for Patch Author'''

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

    desc = input("Description: ")

    # No characters were entered
    if len(desc) == 0:
        logging.warning("The Patch description field was left blank!")
        colors.pc("\nThe Description field must be filled out!", color.FG_LIGHT_RED)

        # Loop back through the Patch Author Process
        logging.info("Looping back through patchDesc()")
        patchDesc()

    # The field was filled out
    else:
        logging.info("The description field was filled out")
        return desc

# ------------ End Patch Info Character and Length Checks ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def patchInfo():
    '''Asks for PatchIt! Patch details'''

    logging.info("Create a PatchIt! Patch")
    colors.pc("\nCreate a PatchIt! Patch", color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    logging.info('Type "q" in the next field to cancel the Patch Creation process.')
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

        # Value for MP field
        mp = "MP"

    # It's an LOCO Patch
    elif game_select.lower() == "l":
        logging.info("User selected LEGO LOCO")
        game = "LEGO LOCO"

     # I want to quit the process
    else: #elif game_select.lower() == "q":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.pc("\nCanceling creation of PatchIt! Patch", color.FG_WHITE)
        logging.info("Switching to main menu")
        PatchIt.main()

    logging.info("Ask for Patch name (patchName())")
    print("\n")
    name = patchName()

    logging.info("Ask for Patch version (patchVersion())")
    version = patchVersion()

    logging.info("Ask for Patch author (patchAuthor())")
    author = patchAuthor()

    logging.info("Ask for Patch descriptoin (patchDesc())")
    desc = patchDesc()

    if game == "LEGO LOCO":
        # Get the resolution the map was created in (it matters!) for the MP field
        logging.info("Switching to LOCORes(name) to get map resolution")
        mp = LOCORes(name)

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to basically hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # The files to be compressed
    patchfiles = filedialog.askdirectory(
    parent=root,
    title="Select the files you wish to compress into your Patch"
    )

    # The user clicked the cancel button
    if len(patchfiles) == 0:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        logging.warning("User did not select any files to compress!")
        colors.pc("\nCannot find any files to compress!", color.FG_LIGHT_RED)
        time.sleep(1)
        logging.info("Switching to to main menu")

    # The user selected files for Patch creation
    else:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()
        logging.info("User selected files at {0} for Patch compression".format(patchfiles))
        logging.info('''The final Patch details are:

{0}
Version: {1}
Author: {2}
Game: {3}
{4}

"{5}"
'''.format(name, version, author, game, mp, desc))
        logging.info("Switching to writePatch(patchfiles, name, version, author, desc, mp, game)")
        writePatch(patchfiles, name, version, author, desc, mp, game)

def LOCORes(name):
    '''Enter the resolution this LOCO map was created with'''

    logging.info("What resolution was this LEGO LOCO map created with?")
    print('''\nWhat resolution was "{0}" created with?
Hint: if you are unsure, it will most likely be either'''.format(name))

    colors.pc('''
800x600,
1024x768,
1920x1024

If you used a custom resolution, be sure to enter that into the fields below.''', color.FG_LIGHT_MAGENTA)

    try:
        # int() because screen resolution is not expressed in decimial numbers nor words, but numbers
        res_horz = int(input("\nWidth: "))
        res_vert = int(input("Height: "))
        mp = "{0}x{1}".format(res_horz, res_vert)
        logging.info("This map was the {0} resolution".format(mp))
        logging.info("Returning mp variable")
        return mp

    # A valid resolution was not entered
    except ValueError:
        logging.warning("User entered an invalid number!")
        logging.exception("Oops! Something went wrong! Here's what happened\n", exc_info=True)
        colors.pc("You have entered a non-numerical character!")
        logging.info("Looping back through LOCORes()")
        LOCORes(name)


def writePatch(patchfiles, name, version, author, desc, mp, game):
    '''Writes and compresses PatchIt! Patch'''

    # The user selected a folder to compress
    try:
        # Check for and delete thumbs.db
        logging.info("Switching to delThumbs(patchfiles)")
        delThumbs(patchfiles)

        # Declare the Patch and ZIP filenames
        thepatch = "{0}{1}.PiP".format(name, version)
        thezipfile = "{0}{1}.zip".format(name, version)
        logging.info("The final file names are {0} and {1}".format(thepatch, thezipfile))

        # Write PiP file format, as defined in Documentation/PiP Format V1.1.md
        logging.info("Write {0} with Patch details using UTF-8 encoding".format(thepatch))
        with open("{0}".format(thepatch), 'wt', encoding='utf-8') as patch:
            print("// PatchIt! PiP file format V1.1, developed by le717 and rioforce", file=patch)
            print("[ZIP]", file=patch)
            print("{0}".format(thezipfile), file=patch)
            print("[GENERAL]", file=patch)
            print(author, file=patch)
            print(version, file=patch)
            print(name, file=patch)
            print(mp, file=patch)
            print(game, file=patch)
            print("[DESCRIPTION]", file=patch)
            print("{0}".format(desc), file=patch, end="")

        # Compress the files
        logging.info("Compress files located at {0} into a ZIP archive".format(patchfiles))
        zipfile = shutil.make_archive(patchfiles, format="zip", root_dir=patchfiles)

        # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format V1.1.md
        logging.info("Rename ZIP archive to {0}, as defined in {1}".format(thezipfile, "Documentation/PiP Format V1.1.md"))
        newzipfile = os.replace(zipfile, thezipfile)

        # Move the Patch and ZIP to the folder the compressed files came from
        logging.info("Moving {0} from {1} to {2}".format(thepatch, os.getcwd(), patchfiles))
        shutil.move(thepatch, patchfiles)
        logging.info("Moving {0} from {1} to {2}".format(thezipfile, os.getcwd(), patchfiles))
        shutil.move(thezipfile, patchfiles)

        # The Patch was created sucessfully!
        logging.info("Error (exit) number '0'")
        logging.info("{0} Version: {1} created and saved to {2}".format(name, version, patchfiles))
        colors.pc('\n{0} patch for {1} Version: {2} created and saved to\n"{3}"'.format(PatchIt.app, name, version, patchfiles), color.FG_LIGHT_GREEN)

    # The user does not have the rights to write a PiP in that location
    except PermissionError:
        logging.warning("Error number '13'")
        logging.exception("Oops! Something went wrong! Here's what happened\n", exc_info=True)
        logging.warning("{0} does not have the rights to create {1} {2}".format(PatchIt.app, name, version))
        colors.pc("\n{0} does not have the rights to create {1} {2}!".format(PatchIt.app, name, version), color.FG_LIGHT_RED)
        # Delete incomplete PiP
        logging.info('Deleting incomplete Patch ({0})'.format(thepatch))
        os.unlink(os.path.join(os.getcwd(), "{0}".format(thepatch)))

    # .PiP and/or .zip already exists
    except shutil.Error:
        logging.warning("shutil.Error")
        logging.exception("Oops! Something went wrong! Here's what happened\n", exc_info=True)
        logging.warning('{0} or {1} already exists at "{2}" or "{3}"!'.format(thepatch, thezipfile, patchfiles, os.getcwd()))
        colors.pc('\n{0} or {1} already exists!\nCheck either "{2}"\nor "{3}"\nfor the files, and move or delete them if necessary.'.format(thepatch, thezipfile, patchfiles, os.getcwd()), color.FG_LIGHT_RED)

    # Python itself had some I/O error/any exceptions not handled
    except Exception:
        logging.warning("Unknown error number")
        logging.exception("Oops! Something went wrong! Here's what happened\n", exc_info=True)
        logging.warning("{0} ran into an unknown error while trying to create {1} {2}!".format(PatchIt.app, name, version))
        colors.pc("\n{0} ran into an unknown error while trying to create {1} {2}!".format(PatchIt.app, name, version), color.FG_LIGHT_RED)

    finally:
        # Sleep for 2 seconds after displaying creation result before kicking back to the PatchIt! menu.
        time.sleep(2)
        logging.info("Switching to main menu")

# ------------ End PatchIt! Patch Creation ------------ #