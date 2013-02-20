# Import only certain items instead of "the whole toolbox"
from PatchIt import (app, main)
from time import sleep
from shutil import (make_archive, move)
from os import (system, replace)
# GUI! :D
import tkinter
from tkinter import filedialog

# ------------ Begin PatchIt! Patch Creation ------------ #

def writepatch():
    '''Writes and compresses PatchIt! Patch'''
    print("\nCreate a {0} Patch".format(app), end="\n")
    # Tells the user how to cancel the process
    print('Type "exit" in the "Name:" field to cancel.', end="\n")
    createname = input("\nName: ")

    # I wanted to quit the process
    if createname.lower() == "exit":
        print("\nCanceling creation...")
        sleep(0.5)
        main()

    # I want to continue on
    else:
        createver = input("Version: ")
        createauthor = input("Author: ")
        createdesc = input("Description: ")

    # PiP file format, as defined in Documentation/PiP Format.md
    with open("{0}{1}.PiP".format(createname, createver), 'wt', encoding='utf-8') as createpatch:
        print("// PatchIt! Patch format, created by le717 and rioforce.", file=createpatch)
        print("[General]", file=createpatch)
        print(createname, file=createpatch)
        print("Version: {0}".format(createver), file=createpatch)
        print("Author: {0}".format(createauthor), file=createpatch)
        print("[Description]", file=createpatch)
        print('"{0}"'.format(createdesc), file=createpatch)
        print("[ZIP]", file=createpatch)
        print("{0}{1}.zip".format(createname, createver), file=createpatch, end="")

    # The files to be compressed
    root = tkinter.Tk()
    root.withdraw()
    inputfiles = filedialog.askdirectory(title="Select the files you wish to compress:")
    if len(inputfiles) == 0:
        print("\nCannot find any files to compress!")
        sleep(1)
        main()

    else:
    # Compresses the files
        zipfile = make_archive(inputfiles, format="zip", root_dir=inputfiles)
        # Rename the ZIP archive to createname + creationver, as defined in Documentation/PiP Format.md
        newzipfile = replace(zipfile, createname + createver + ".zip")

        # Define the Patch and ZIP filenames
        patchfile = "{0}{1}.PiP".format(createname, createver)
        newzipfile = "{0}{1}.zip".format(createname, createver)

        # Move the Patch and ZIP to the folder the compressed files came from
        movepatch = move(patchfile, inputfiles)
        movepatch = move(newzipfile, inputfiles)
        sleep(0.5)

        '''Windows continually throws up the '*inputfiles* is not recognized as an internal or external command,
         operable program or batch file.' error, and I am unable to neither silence it nor hide it with looping back over all the code
         or killing the exit codes. So I had to redefine what is a clean exit and what isn't. Thus,
         1 == clean exit, 0, == exit with some error, and anything else is pure fail.
         Hopefully, I can fix this in Beta 4.'''

        if system(inputfiles) == 1:
            print("\n{0} patch for {1} Version {2} created and saved to {3}!".format(app, createname, createver, inputfiles))
            # Always sleep for 1 second before kicking back to the menu.
            sleep(1)
            main()

        elif system(inputfiles) == 0:
            print("\nCreation of {0} patch for {1} Version {2} completed with an unknown error.".format(app, createname, createver))
            sleep(1)
            main()

        else:
            print("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver))
            sleep(1)
            main()

# ------------ End PatchIt! Patch Creation ------------ #