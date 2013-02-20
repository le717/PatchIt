import linecache, random
import os
import zipfile
import PatchIt, gametips
from time import sleep
#from random import choice

# ------------ Begin PatchIt! Patch Installation ------------ #

def readpatch():
    '''Reads and Installs PatchIt! Patch'''
    installpatch = input("\nPlease enter the path to a {0} patch:\n\n> ".format(PatchIt.app))
    if installpatch.lower() == "exit":
        print("\nCanceling installation...")
        PatchIt.main()
    else:
        confirmpatch = linecache.getline(installpatch, 1)
        if confirmpatch != "// PatchIt! Patch format, created by le717 and rioforce.\n": # Validity check
            print(confirmpatch, installpatch + " is not a valid {0} patch.".format(PatchIt.app))
        else:
            installname = linecache.getline(installpatch, 3)
            installver = linecache.getline(installpatch, 4)
            installauthor = linecache.getline(installpatch, 5)
            installdesc = linecache.getline(installpatch, 7)
            #installpatch.close()
            print("\n{0} {1} {2} {3}".format(installname, installver, installauthor, installdesc))
            print("Do you wish to install {0}".format(installname), end="")
            confirminstall = input("\n> ")
            if confirminstall.lower() != "y":
                print("\nCanceling installation of {0} {1}".format(installname, installver))
                PatchIt.main()
            else:
##                extractzip.installfiles(installname, installver, installpatch)
##                extractpatch(installpatch, installname, installver)
                linecache.clearcache()
                installpath = linecache.getline('settings', 2)
                installpath = installpath.rstrip("\n")
                installzipfile = linecache.getline(installpatch, 9)
                installzipfile = installzipfile.rstrip("\n")
                ziplocation = installpatch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))
                print('\n"' + random.choice(gametips.gametips) + '"\n')
                zip_handler = zipfile.ZipFile(ziplocation + installzipfile, "r")
                zip_handler.extractall(path=installpath)
                linecache.clearcache()
                #zipfile.ZipFile.close(zip)

            if os.system(installpath) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
                print("{0} sucessfully installed!".format(installname))
                PatchIt.main()
            elif os.system(installpath) == 1:
                print("An unknown error occured while installing {0}.".format(installname))
                PatchIt.main()
            else:
                print("Installation of {0} failed!".format(installname))
                PatchIt.main()

def extractpatch(installpatch, installname, installver):
    linecache.clearcache()
    installpath = linecache.getline('../settings', 2)
    installpath = installpath.rstrip("\n")
    installzipfile = linecache.getline(installpatch, 9)
    installzipfile = installzipfile.rstrip("\n")
    ziplocation = installpatch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))

    zip_handler = zipfile.ZipFile(ziplocation + installzipfile, "r")
    zip_handler.extractall(path=installpath)
    #installpath.close()

    if os.system(installpath) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} sucessfully installed!".format(installname))
        sleep(1)
        PatchIt.main()
    elif os.system(installpath) == 1:
        print("An unknown error occured while installing {0}.".format(installname))
        sleep(1)
        PatchIt.main()
    else:
        print("Installation of {0} failed!".format(installname))
        sleep(1)
        PatchIt.main()

# ------------ End PatchIt! Patch Installation ------------ #