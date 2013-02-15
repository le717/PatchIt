import os, shutil
patchtype = ".PiP"
app = "PatchIt!"
game = "Racers"
def writepatch():
    '''Write PatchIt! Patch'''
    print("\nPlease enter the following information to create your {0} patch.".format(app))
    global modcreatename, modcreatever, modcreatefiles, patchfile
    modcreatename = input("Mod Name: ")
    modcreatever = input("Mod Version: ")
    modcreateauthor = input("Mod Author: ")
    modcreatedesc = input("Mod Description: ")
    modcreatefiles = input("\nPlease enter the path to your modded files: \n\n> ")
    compressfiles(modcreatefiles)
    modcreatename = modcreatename.strip(r" _.-/")
    with open("{0}{1}.PiP".format(modcreatename, modcreatever), 'wt', encoding='utf-8') as createpatch:
        print("// PatchIt! Patch file, created by le717 and rioforce.", file=createpatch)
        print("[General]", file=createpatch)
        print(modcreatename, file=createpatch)
        print("Version: {0}".format(modcreatever), file=createpatch)
        print("Author: {0}".format(modcreateauthor), file=createpatch)
        print("[Description]", file=createpatch)
        print('"{0}"'.format(modcreatedesc), file=createpatch)
        print("[ZIP]", file=createpatch)
        print("{0}{1}.zip".format(modcreatename, modcreatever), file=createpatch, end="")     
    patchfile = "{0}{1}.PiP".format(modcreatename, modcreatever)
    

def compressfiles(modcreatefiles):
    '''Compress PatchIt! patch'''
    #modfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    global zipfile
    zipfile = shutil.make_archive(modcreatefiles, format="zip", root_dir=modcreatefiles) # Same as above.
    os.rename(zipfile, "{0}{1}.zip".format(modcreatename, modcreatever))
    # TODO: Move Patch File from app directory
    if os.system(modcreatefiles) == 1: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} patch for {1} created and saved to {2}.zip".format(game, modcreatename, modcreatefiles)) # Temp messages
        return modcreatefiles
    elif os.system(modcreatefiles) == 0:
        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(app, modcreatename))
        return modcreatefiles
    else:
        print("Creation of {0} patch for {1} failed!".format(app, modcreatename)) # Temp message
        raise SystemExit

writepatch()        
        
        
    
    
