import PatchIt
import os, shutil

def writepatch():
    global createname
    createname = input("Name: ")
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
    compressfiles()

def compressfiles():
    '''Compress PatchIt! patch'''

    print()
    inputfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
        # TODO: Move Patch File from app directory
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))

    if os.system(inputfiles) == 1:
        print("{0} patch for {1} created and saved to {2}.zip".format(PatchIt.app, createname, inputfiles))
        PatchIt.main()
        #return True
    elif os.system(inputfiles) == 0:
        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(PatchIt.app, createname))
        PatchIt.main()
        #return False
    else:
        print("Creation of {0} patch for {1} failed!".format(PatchIt.app, createname))
        PatchIt.main()
        #return "Fail"