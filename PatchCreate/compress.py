import PatchIt
import os, time, shutil

def writepatch():
    '''Writes and compresses PatchIt! Patch'''
    print("\nCreate a {0} Patch".format(PatchIt.app), end="\n")
    print('Type "exit" in the "Name:" field to cancel.', end="\n")
    createname = input("\nName: ")
    if createname.lower() == "exit":
        print("\nCanceling creation...")
        time.sleep(0.5)
        PatchIt.main()
    else:
        createver = input("Version: ")
        createauthor = input("Author: ")
        createdesc = input("Description: ")

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

    inputfiles = input("\nPlease enter the path to the files you wish to compress: \n\n> ")
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
    newzipfile = os.rename(zipfile, createname + createver + ".zip")
    #fileslocation = inputfiles.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))
    #shutil.move(newzipfile, inputfiles)
    #shutil.move(createpatch, inputfiles)
        # TODO: Move Patch File from app directory
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))
    time.sleep(0.5)

    if IOError:
        print("")
        if os.system(inputfiles) == 0:
            print("{0} patch for {1} created and saved to {2}".format(PatchIt.app, createname, inputfiles))
            PatchIt.main()
        elif os.system(inputfiles) == 1:
            print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(PatchIt.app, createname))
            PatchIt.main()
        else:
            print("Creation of {0} patch for {1} failed!".format(PatchIt.app, createname))
            PatchIt.main()