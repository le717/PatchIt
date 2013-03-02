# PatchIt! V1.0.1 Stable Patch Creation code

# Import only certain items instead of "the whole toolbox"
import PatchIt
from time import sleep
import shutil
import zipfile
from os import (system, replace)
import os
import os.path
# Colored text (until complete GUI is written)
import color
import color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog


# ------------ Begin WIP Thumbs.db Checking Code ------------ #

##def thumbsFind(inputfiles):
##    oldzip = zipfile.ZipFile(renamezip, "r")
##    newzip = zipfile.ZipFile(newziparchive, "w")
##    for item in oldzip.infolist():
##        buffer = oldzip.read(item.filename)
##        if (item.filename[-3:]) != ".db":
##            newzip.writestr(item, buffer)
##    newzip.close()
##    oldzip.close()

##for dir, subdirs, files in os.walk(root):
##    for f in files:
##        if f[-4:].lower() == '.vbp':
##            print os.path.join(dir, f)


# ------------ End WIP Thumbs.db Checking Code ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def patchdesc():
    '''Mod Description input and length check'''

    # Because I can't see how to do it any other way
    global createdesc
    createdesc = input("Description: ")
    # 162 characters will mess up PatchIt! entirely
    if len(createdesc) > 161:
            colors.pc("\nYour description is too long! Please write it a bit shorter.\n", color.FG_LIGHT_RED)
            # Loop back through the input if it is longer
            patchdesc()
    else:
        # It fits into the limit, send it back to writepatch()
        return createdesc

def writepatch():
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
##            thumbsFind(inputfiles)
##            if thumbsFind == "muddy":
##                print("\nBad files found!\n")
##                #PatchIt.main()
##                os._exit(0)
##            if thumbsFind == "clean":
                try:
                    # PiP file format, as defined in Documentation/PiP Format.md

                    # BUG! Question Marks in Name/Version fields for Patch Creation throws "Invalid Argument" error
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
                    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
                    # Rename the ZIP archive to createnamecreationver.zip, as defined in Documentation/PiP Format.md
                    renamezip = replace(zipfile, createname + createver + ".zip")

                    # Declare the Patch and ZIP filenames
                    patchfile = "{0}{1}.PiP".format(createname, createver)
                    thezipfile = "{0}{1}.zip".format(createname, createver)

                    oldzip = zipfile.ZipFile("{0}{1}.zip".format(createname, createver), "r")
                    newzip = zipfile.ZipFile("{0}{1}.zip".format(createname, createver), "w")
                    for item in oldzip.infolist():
                        buffer = oldzip.read(item.filename)
                        if (item.filename[-3:]) != ".db":
                            newzip.writestr(item, buffer)
                    newzip.close()
                    oldzip.close()

                    os.remove(renamezip)

                    # Move the Patch and ZIP to the folder the compressed files came from
                    movepatch = shutil.move(patchfile, inputfiles)
                    movezip = shutil.move(newzip, inputfiles)
                    sleep(0.5)

                    '''Windows continually throws up the '*inputfiles* is not recognized as an internal or external command,
                    operable program or batch file.' error, killing the exit codes, and I am unable to neither silence it nor hide it without
                    looping back over all the code. So I had to redefine what is a clean exit and what isn't. Thus,
                    1 == clean exit, 0, == exit with some error, and anything else is pure fail.
                    I believe the error is due the fact I have it attached to the wrong code. The question now is,
                    what do I attach it to so I can have proper exit codes?'''

                    if system(inputfiles) == 1:
                        print("\n{0} patch for {1} Version {2} created and saved to {3}!".format(PatchIt.app, createname, createver, inputfiles))
                        # Always sleep for 2 second after displaying exit code before kicking back to the PatchIt! menu.
                        sleep(2)
                        PatchIt.main()

                    elif system(inputfiles) == 0:
                        print("\nCreation of {0} patch for {1} Version {2} completed with an unknown error.".format(PatchIt.app, createname, createver))
                        sleep(2)
                        PatchIt.main()

                    else:
                        colors.pc("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver), color.FG_LIGHT_RED)
                    #print("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver))
                        sleep(2)
                        PatchIt.main()

                # The user does not have the rights to write a PiP in that location
                except PermissionError:
                    print("\n{0} does not have the rights to save {1} {2} to\n{3}!".format(PatchIt.app, createname, createver, inputfiles))
                    sleep(2)
                    PatchIt.main()

##                    '''Windows continually throws up the '*inputfiles* is not recognized as an internal or external command,
##                    operable program or batch file.' error, killing the exit codes, and I am unable to neither silence it nor hide it without
##                    looping back over all the code. So I had to redefine what is a clean exit and what isn't. Thus,
##                    1 == clean exit, 0, == exit with some error, and anything else is pure fail.
##                    I believe the error is due the fact I have it attached to the wrong code. The question now is,
##                    what do I attach it to so I can have proper exit codes?'''
##
##                    if system(inputfiles) == 1:
##                    print("\n{0} patch for {1} Version {2} created and saved to {3}!".format(PatchIt.app, createname, createver, inputfiles))
##                        # Always sleep for 2 second after displaying exit code before kicking back to the PatchIt! menu.
##                    sleep(2)
##                    PatchIt.main()
##
##                    elif system(inputfiles) == 0:
##                        print("\nCreation of {0} patch for {1} Version {2} completed with an unknown error.".format(PatchIt.app, createname, createver))
##                        sleep(2)
##                        PatchIt.main()
##
##                    else:
##                        colors.pc("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver), color.FG_LIGHT_RED)
##                    #print("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver))
##                        sleep(2)
##                        PatchIt.main()

# ------------ End PatchIt! Patch Creation ------------ #