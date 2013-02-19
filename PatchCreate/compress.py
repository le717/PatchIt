# Import only certain items instead of "the whole toolbox"
from PatchIt import (app, main)
from time import sleep
import os, shutil

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
    inputfiles = input("\nPlease enter the path to the files you wish to compress: \n\n> ")
    # Compresses the files
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
    # Rename the ZIP archive to createname + creationver, as defined in Documentation/PiP Format.md
    newzipfile = os.rename(zipfile, createname + createver + ".zip")

    # TODO: Move PiP file and archive from app directory to inputfiles
    #shutil.move(newzipfile, inputfiles)
    #shutil.move(createpatch, inputfiles)
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))

    sleep(0.5)
    '''Windows continually throws up the '*inputfiles* is not recognized as an internal or external command,
    operable program or batch file.' error, and I am unable to neither silence it nor hide it with looping back over all the code
    or killing the exit codes. So I had to redefine what is a clean exit and what isn't. Thus,
    1 == clean exit, 0, == exit with some error, and anything else is pure fail.
   Hopefully, I can fix this in Beta 4.'''
    if os.system(inputfiles) == 1:
        print("\n{0} patch for {1} Version {2} created and saved to {3}!".format(app, createname, createver, inputfiles))
        # Always sleep for 1 second before kicking back to the menu.
        sleep(1)
        main()

    elif os.system(inputfiles) == 0:
        print("\nCreation of {0} patch for {1} Version {2} completed with an unknown error.".format(app, createname, createver))
        sleep(1)
        main()

    else:
        print("\nCreation of {0} patch for {1} Version {2} failed!".format(app, createname, createver))
        sleep(1)
        main()

# ------------ End PatchIt! Patch Creation ------------ #