# http://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports
# http://stackoverflow.com/questions/1054271/how-to-import-a-python-class-that-is-in-a-directory-above
from PatchCreate import compresszip
#import compresszip
#from .compresszip import *
#from .compresszip import compressfiles
import PatchIt
import os

def writepatch():
    #global createname, createver
    createname = input("Name: ")
    return createname
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
    compresszip.compressfiles()

##
##    compresszip.compressfiles()
##
##    if compresszip.compressfiles == True:
##        print("{0} patch for {1} created and saved to {2}.zip".format(PatchIt.app, createname, compresszip.inputfiles))
##        PatchIt.main()
##
##    elif compresszip.compressfiles == False:
##        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(PatchIt.app, createname))
##        PatchIt.main()
##
##    elif compresszip.compressfiles == "Fail":
##        print("Creation of {0} patch for {1} failed!".format(PatchIt.app, createname))
##        PatchIt.main()