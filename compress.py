# PatchIt! V1.0.2 Stable Patch Creation code

# Import only certain items instead of "the whole toolbox"
import PatchIt
import os
from os.path import join
from time import sleep
from shutil import (make_archive, move)
# Colored text (until complete GUI is written)
import color
import color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog
# App Logging modules
import logging


# ------------ Begin Thumbs.db Check And Delete Code ------------ #

def delThumbs(inputfiles):
    '''Checks for and Deletes Thumbs.db'''

    # Traverse through the subfolders
    for root, dir, files in os.walk(inputfiles):
        logging.info("Walking through {0}...".format(inputfiles))
        for item in files:

            # I've heard of a ethumbs.db file once before...
            if item.lower().endswith(".db"):
                logging.warning("Thumbs.db has been found!")

                '''Uncomment this to target just thumbs.db'''
                #if item.lower() == "thumbs.db":

                '''This will print upon every instance of thumbs.db. Not good.'''
                #print('''\nI found Thumbs.db in your files. I will delete it for you in a few seconds.
#Don't worry, Windows will recreate it.\n''')

                '''Actually delete the file(s)'''
                logging.info("Deleting Thumbs.db (don't worry, Windows will recreate it. ;))")
                os.unlink(join(root, item))

# ------------ End Thumbs.db Check And Delete Code ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def patchDesc():
    '''Mod Description input and length check'''

    # Because I can't see how to do it any other way
    global createdesc
    logging.info("Ask for mod description")
    createdesc = input("Description: ")

    # 162 characters will mess up PatchIt! entirely
    if len(createdesc) > 161:
            logging.warning("The description is too longer - longer than 161 characters!")
            colors.pc("\nYour description is too long! Please write it a bit shorter.\n", color.FG_LIGHT_RED)
            # Loop back through the input if it is longer
            logging.info("Loop back through for shorter description (patchDesc())")
            patchDesc()
    else:
        logging.info("Your description fits into the 161 character limit")
        # It fits into the limit, send it back to writepatch()
        return createdesc

def writePatch():
    '''Writes and compresses PatchIt! Patch'''

    colors.pc("\nCreate a {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_YELLOW)
    # Tells the user how to cancel the process
    print('Type "exit" in the "Name:" field to cancel.', end="\n")
    createname = input("\nName: ")

    # I want to quit the process
    if createname.lower() == "exit":
        #print("\nCanceling creation...")
        colors.pc("\nCanceling creation of {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_RED)
        sleep(0.5)
        PatchIt.main()

    # I want to continue on
    else:
        createver = input("Version: ")
        createauthor = input("Author: ")
        # See def patchdesc() above.
        patchdesc()

        # Hide the root Tk window
        root = tkinter.Tk()
        root.withdraw()

        # The files to be compressed
        # TODO: Make dialog active window automatically and do the same to main window when closed.
        inputfiles = filedialog.askdirectory(title="Select the files you wish to compress:")

        # The user clicked the cancel button
        if len(inputfiles) == 0:
            colors.pc("\nCannot find any files to compress!\n", color.FG_LIGHT_RED)
            sleep(1)
            PatchIt.main()

        # The user selected a folder to compress
        else:
            try:
                # Check for and delete thumbs.db
                delThumbs(inputfiles)

                # Write PiP file format, as defined in Documentation/PiP Format.md
                with open("{0}{1}.PiP".format(createname, createver), 'wt', encoding='utf-8') as createpatch:
                    print("// PatchIt! Patch format, created by le717 and rioforce.", file=createpatch)
                    print("[General]", file=createpatch)
                    print(createname, file=createpatch)
                    print("Version: {0}".format(createver), file=createpatch)
                    print("Author: {0}".format(createauthor), file=createpatch)
                    print("[Description]", file=createpatch)
                    print("{0}".format(createdesc), file=createpatch)
                    print("[ZIP]", file=createpatch)
                    print("{0}{1}.zip".format(createname, createver), file=createpatch, end="")

                # Compress the files
                zipfile = make_archive(inputfiles, format="zip", root_dir=inputfiles)

                # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format.md
                newzipfile = os.replace(zipfile, createname + createver + ".zip")

                # Declare the Patch and ZIP filenames
                patchfile = "{0}{1}.PiP".format(createname, createver)
                newzipfile = "{0}{1}.zip".format(createname, createver)

                # Move the Patch and ZIP to the folder the compressed files came from
                movepatch = move(patchfile, inputfiles)
                movezip = move(newzipfile, inputfiles)
                sleep(0.5)

                # The user does not have the rights to write a PiP in that location
            except PermissionError:
                print("\n{0} does not have the rights to save {1} {2} to\n{3}!\n".format(PatchIt.app, createname, createver, inputfiles))
                sleep(2)
                PatchIt.main()

                '''Windows continually throws up the *inputfiles* is not recognized as an internal or external command,
            operable program or batch file.' error, killing the exit codes, and I am unable to neither silence it nor hide it without
            looping back over all the code. So I had to redefine what is a clean exit and what isn't. Thus,
            1 == clean exit, 0, == exit with some error, and anything else is pure fail.
            I believe the error is due the fact I have it attached to the wrong code. The question now is,
            what do I attach it to so I can have proper exit codes?'''

            if os.system(inputfiles) == 1:
                print("\n{0} patch for {1} Version: {2} created and saved to\n{3}!\n".format(PatchIt.app, createname, createver, inputfiles))
                # Sleep for 2 second after displaying exit code before kicking back to the PatchIt! menu.
                sleep(2)
                PatchIt.main()

            elif os.system(inputfiles) == 0:
                print("\nCreation of {0} patch for {1} Version: {2} completed with an unknown error.\n".format(PatchIt.app, createname, createver))
                sleep(2)
                PatchIt.main()

            else:
                colors.pc("\nCreation of {0} patch for {1} Version: {2} failed!\n".format(app, createname, createver), color.FG_LIGHT_RED)
                #print("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver))
                sleep(2)
                PatchIt.main()

# ------------ End PatchIt! Patch Creation ------------ #