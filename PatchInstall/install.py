import linecache, random, zipfile
#import gametips
import PatchIt
def readpatch():
    '''Reads and Installs PatchIt! Patch'''
    #global installpatch
    linecache.clearcache()
    #global installpatch
    installpatch = input("\nPlease enter the path to a {0} patch:\n\n> ".format(PatchIt.app))
    if installpatch.lower() == "exit":
        print("\nCanceling installation...")
        PatchIt.main()
    else:
        confirmpatch = linecache.getline(installpatch, 1)
        if confirmpatch != "// PatchIt! Patch format, created by le717 and rioforce.\n": # Validity check
            print(confirmpatch, installpatch + " is not a valid {0} patch.".format(PatchIt.app))
        else:
            #global modinstallname
            modinstallname = linecache.getline(installpatch, 3)
            modinstallver = linecache.getline(installpatch, 4)
            modinstallauthor = linecache.getline(installpatch, 5)
            modinstalldesc = linecache.getline(installpatch, 7)
            print("\n{0} {1} {2} {3}".format(modinstallname, modinstallver, modinstallauthor, modinstalldesc))
            print("Do you wish to install {0}".format(modinstallname), end="")
            confirminstall = input("\n> ")
            if confirminstall.lower() != "y":
                print("\nCanceling installation of {0} {1}".format(modinstallname, modinstallver))
                PatchIt.main()
            else:
                #installfiles()
                linecache.clearcache()
                installpath = linecache.getline('../settings', 2)
                installpath = installpath.rstrip()
                installzipfile = linecache.getline(installpatch, 9)
                installzipfile = installzipfile.rstrip()
                #print('\n"' + random.choice(gametips.gametips) + '"\n')
                zip = zipfile.ZipFile(installpatch + installzipfile)
                zip.extractall(installpath)
                zipfile.ZipFile.close(zip)
                if os.system(installpath) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
                    print("{0} sucessfully installed!".format(modinstallname))
                    PatchIt.main()
                elif os.system(installpath) == 1:
                    print("An unknown error occured while installing {0}.".format(modinstallname))
                    PatchIt.main()
                else:
                    print("Installation of {0} failed!".format(modinstallname))
                    PatchIt.main()