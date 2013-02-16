import os, shutil

def compressfiles():
    '''Compress PatchIt! patch'''
    global zipfile, inputfiles
    print()
    inputfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
        # TODO: Move Patch File from app directory
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))
    
    if os.system(inputfiles) == 1:
        return True              
    elif os.system(inputfiles) == 0:
        return False              
    else:
        return "Fail"
        print("Creation of {0} patch for {1} failed!".format(app, createname))
        raise SystemExit
