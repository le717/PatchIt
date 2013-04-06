"""
    This file is part of PatchIt!

    PatchIt! -  the standard yet simple way to package and install mods for LEGO Racers
    Copyright 2013 Triangle717 <http://triangle717.wordpress.com>

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
# PatchIt! V1.1.0 Unstable Modern Patch Creation code

import PatchIt, os, shutil, time
# Colored shell text
import color, color.colors as colors
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
# App Logging modules
import logging

# ------------ Begin Thumbs.db Check And Delete Code ------------ #

def delThumbs(patchfiles):
    '''Checks for and Deletes Thumbs.db'''

    # Traversing the files in each subfolder..
    logging.info("Walking through {0}...".format(patchfiles))
    for root, dir, files in os.walk(patchfiles):
        for item in files:

            """Uncomment this to target all *.db files"""
            #if item.lower().endswith(".db"):
            if item.lower() == "thumbs.db":
                logging.warning("Thumbs.db has been found!")

                """This will print upon every instance of thumbs.db. Not good. TODO: Fix it!"""
                #print('''\nI found Thumbs.db in your files. I will delete it for you in a few seconds.
#Don't worry, Windows will recreate it.\n''')

                """Actually delete the file(s)"""
                logging.info("Deleting Thumbs.db (don't worry, Windows will recreate it. ;))")
                os.unlink(os.path.join(root, item))

# ------------ End Thumbs.db Check And Delete Code ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def patchInfo():
    '''Asks for PatchIt! Patch details'''

    logging.info("Create a PatchIt! Patch")
    colors.pc("\nCreate a PatchIt! Patch\n", color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    logging.info('Type "exit" in the "Name:" field to cancel the Patch Creation process.')
    print('Type "exit" in the "Name:" field to cancel.', end="\n")

    logging.info("Ask for Patch name")
    name = input("\nName: ")

    # I want to quit the process
    if name.lower() == "exit":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.pc("\nCanceling creation of {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_RED)
        time.sleep(0.5)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # I want to continue on (implied else block)
    logging.info("Ask for Patch version")
    version = input("Version: ")

    logging.info("Ask for Patch author")
    author = input("Author: ")

    logging.info("Ask for Patch description")
    desc = input("Description: ")

    # Get what game this patch is for
    logging.info("Switching to gameSelect() for game selection")
    which_game = gameSelect()

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to (basically) completely hide it")
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
        colors.pc("\nCannot find any files to compress!\n", color.FG_LIGHT_RED)
        time.sleep(1)
        logging.info("Switching to to main menu")
        PatchIt.main()

    # The user selected files for Patch creation
    else:
        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()
        logging.info("Switching to to writePatch(patchfiles, name, version, author, desc, which_game)")
        writePatch(patchfiles, name, version, author, desc, which_game)

def gameSelect():
    '''Select what game this Patch is for'''

    logging.info("Is this patch for LEGO Racers, or LEGO LOCO?")
    print("\nWhat game is this Patch created for?")
    print('''
[r] LEGO Racers
[l] LEGO LOCO''')
    game_select = input("\n\n> ")

    if game_select.lower() == "r":
        logging.info("User selected LEGO Racers")
        which_game = "LEGO Racers"
        logging.info("Returning which_game variable")
        return which_game
    elif game_select.lower() == "l":
        logging.info("User selected LEGO LOCO")
        which_game = "LEGO LOCO"
        logging.info("Returning which_game variable")
        return which_game

def writePatch(patchfiles, name, version, author, desc, which_game):
    '''Writes and compresses PatchIt! Patch'''

    # The user selected a folder to compress
    try:
        logging.info("User selected files at {0} for Patch compression".format(patchfiles))
        # Check for and delete thumbs.db
        logging.info("Switching to delThumbs(patchfiles)")
        delThumbs(patchfiles)

        # Write PiP file format, as defined in Documentation/PiP Format V1.1.md
        logging.info("Write {0}{1}.PiP with Patch details using UTF-8 encoding".format(name, version))
        with open("{0}{1}.PiP".format(name, version), 'wt', encoding='utf-8') as patch:
            print("// PatchIt! PiP file format V1.1, developed by le717 and rioforce", file=patch)
            print("[ZIP]", file=patch)
            print("{0}{1}.zip".format(name, version), file=patch)
            print("[GENERAL]", file=patch)
            print(author, file=patch)
            print(version, file=patch)
            print(name, file=patch)
            print("MP", file=patch)
            print(which_game, file=patch)
            print("[DESCRIPTION]", file=patch)
            print("{0}".format(desc), file=patch, end="")

        # Compress the files
        logging.info("Compress files located at {0} into a ZIP archive".format(patchfiles))
        zipfile = shutil.make_archive(patchfiles, format="zip", root_dir=patchfiles)

        # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format V1.1.md
        logging.info("Rename ZIP archive to {0}{1}.zip, as defined in {2}".format(name, version, "Documentation/PiP Format V1.1.md"))
        newzipfile = os.replace(zipfile, name + version + ".zip")

        # Declare the Patch and ZIP filenames
        thepatch = "{0}{1}.PiP".format(name, version)
        newzipfile = "{0}{1}.zip".format(name, version)
        logging.info("The final file names are {0} and {1}".format(thepatch, newzipfile))

        # Move the Patch and ZIP to the folder the compressed files came from
        logging.info("Moving {0} from {1} to {2}".format(thepatch, os.getcwd(), patchfiles))
        shutil.move(thepatch, patchfiles)
        logging.info("Moving {0} from {1} to {2}".format(newzipfile, os.getcwd(), patchfiles))
        shutil.move(newzipfile, patchfiles)

        # The Patch was created sucessfully!
        logging.info("Exit code '0'")
        logging.info("{0} Version: {1} created and saved to {2}".format(name, version, patchfiles))
        print("\n{0} patch for {1} Version: {2} created and saved to\n{3}!\n".format(PatchIt.app, name, version, patchfiles))

    # The user does not have the rights to write a PiP in that location
    except PermissionError:
        logging.info("Error number '13'")
        logging.warning("{0} does not have the rights to save {1} {2}".format(PatchIt.app, name, version))
        colors.pc("\n{0} does not have the rights to create {1} {2}!\n".format(PatchIt.app, name, version), color.FG_LIGHT_RED)

    # .PiP and/or .zip already exists
    except FileExistsError:
        logging.info("Error number '183'")
        logging.warning("{0}{1}.PiP or .zip already exists at {2} or {3}!".format(name, version, patchfiles, os.getcwd()))
        colors.pc("\n{0}{1}.PiP or {2}{3}.zip already exists!\nCheck either {4} or\n{5} for the files,\nand move or delete them if necessary.\n".format(name, version, name, version, patchfiles, os.getcwd()), color.FG_LIGHT_RED)

    # Python itself had some I/O error/any exceptions not handled
    except Exception:
        logging.info("Unknown error number")
        logging.warning("{0} ran into an unknown error while trying to create {1} {2}!".format(PatchIt.app, name, version))
        colors.pc("\n{0} ran into an unknown error while trying to create {1} {2}!\n".format(PatchIt.app, name, version), color.FG_LIGHT_RED)

    finally:
        # Sleep for 2 seconds after displaying creation result before kicking back to the PatchIt! menu.
        time.sleep(2)
        logging.info("Proceeding to main menu")
        PatchIt.main()

# ------------ End PatchIt! Patch Creation ------------ #