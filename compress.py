# PatchIt! V1.0.3 Stable Patch Creation code

# Import only certain items instead of "the whole toolbox"
import PatchIt
import os
from os.path import join
from time import sleep
import shutil
# Colored text (until complete GUI is written)
import color, color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog
# App Logging modules
import logging


# ------------ Begin Thumbs.db Check And Delete Code ------------ #

def delThumbs(inputfiles):
    '''Checks for and Deletes Thumbs.db'''

    # Traverse through the subfolders
    logging.info("Walking through {0}...".format(inputfiles))
    for root, dir, files in os.walk(inputfiles):
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
        logging.info("Proceed back to writePatch()")
        # It fits into the limit, send it back to writepatch()
        return createdesc

def writePatch():
    '''Writes and compresses PatchIt! Patch'''

    logging.info("Create a PatchIt! Patch")
    colors.pc("\nCreate a {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_YELLOW)

    # Tells the user how to cancel the process
    logging.info('Type "exit" in the "Name:" field to cancel the Patch Creation process.')
    print('Type "exit" in the "Name:" field to cancel.', end="\n")
    createname = input("\nName: ")

    # I want to quit the process
    if createname.lower() == "exit":
        logging.warning("User canceled PatchIt! Patch Creation!")
        colors.pc("\nCanceling creation of {0} Patch\n".format(PatchIt.app), color.FG_LIGHT_RED)
        sleep(0.5)
        logging.info("Proceeding to main menu")
        PatchIt.main()

    # I want to continue on
    else:
        logging.info("Ask for mod version")
        createver = input("Version: ")
        logging.info("Ask for mod author")
        createauthor = input("Author: ")
        logging.info("Proceeding to patchDesc().")
        # See def patchDesc() above.
        patchDesc()

        # Draw (then withdraw) the root Tk window
        logging.info("Drawing root Tk window")
        root = tkinter.Tk()
        logging.info("Withdrawing root Tk window")
        root.withdraw()

        # The files to be compressed
        # TODO: Make dialog active window automatically and do the same to main window when closed.
        inputfiles = filedialog.askdirectory(title="Select the files you wish to compress:")

        # The user clicked the cancel button
        if len(inputfiles) == 0:
            logging.warning("User did not select any files to compress!")
            colors.pc("\nCannot find any files to compress!\n", color.FG_LIGHT_RED)
            sleep(1)
            logging.info("Proceeding to main menu")
            PatchIt.main()

        # The user selected a folder to compress
        else:
            try:
                logging.info("User selected files at {0} for Patch compression".format(inputfiles))
                # Check for and delete thumbs.db
                logging.info("Proceed to delThumbs()")
                delThumbs(inputfiles)

                # Write PiP file format, as defined in Documentation/PiP Format.md
                logging.info("Write {0}{1}.PiP using UTF-8 encoding with mod details".format(createname, createver))
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
                logging.info('''

                        // PatchIt! Patch format, created by le717 and rioforce.
                        [General]
                        {0}
                        Version: {1}
                        Author: {2}
                        [Description]
                        {3}
                        [ZIP]
                        {4}{5}.zip
                        '''.format(createname, createver, createauthor, createdesc, createname, createver))

                # Compress the files
                logging.info("Compress files located at {0} into a ZIP archive".format(inputfiles))
                zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)

                # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format.md
                logging.info("Rename ZIP archive to {0}{1}.zip, as defined in {2}".format(createname, createver, "Documentation/PiP Format.md"))
                newzipfile = os.replace(zipfile, createname + createver + ".zip")

                # Declare the Patch and ZIP filenames
                patchfile = "{0}{1}.PiP".format(createname, createver)
                newzipfile = "{0}{1}.zip".format(createname, createver)
                logging.info("The final file names are {0} and {1}".format(patchfile, newzipfile))

                # Move the Patch and ZIP to the folder the compressed files came from
                logging.info("Moving {0} from {1} to {2}".format(patchfile, os.getcwd(), inputfiles))
                movepatch = shutil.move(patchfile, inputfiles)
                logging.info("Moving {0} from {1} to {2}".format(newzipfile, os.getcwd(), inputfiles))
                movezip = shutil.move(newzipfile, inputfiles)
                sleep(0.5)

                # The Patch was created sucessfully!
                logging.info("Exit code '0'")
                logging.info("{0} Version: {1} created and saved to {2}".format(createname, createver, inputfiles))
                print("\n{0} patch for {1} Version: {2} created and saved to\n{3}!\n".format(PatchIt.app, createname, createver, inputfiles))

                # The user does not have the rights to write a PiP in that location
            except PermissionError:
                logging.info("Error number '13'")
                logging.warning("{0} does not have the rights to save {1} {2}".format(PatchIt.app, createname, createver))
                colors.pc("\n{0} does not have the rights to create {1} {2}!\n".format(PatchIt.app, createname, createver), color.FG_LIGHT_RED)

            # Python itself had some I/O error / any exceptions not handled
            except Exception:
                logging.info("Unknown error number")
                logging.warning("{0} ran into an unknown error while trying to create {1} {2}!".format(PatchIt.app, createname, createver))
                colors.pc("\n{0} ran into an unknown error while trying to create {1} {2}!\n".format(PatchIt.app, createname, createver), color.FG_LIGHT_RED)

            finally:
                # Sleep for 2 seconds after displaying creation result before kicking back to the PatchIt! menu.
                    sleep(2)
                    logging.info("Proceeding to main menu")
                    PatchIt.main()

# ------------ End PatchIt! Patch Creation ------------ #