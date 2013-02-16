import os, shutil

def compressfiles():
    '''Compress PatchIt! patch'''
    global zipfile, inputfiles

    print()
    inputfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    
    zipfile = shutil.make_archive(inputfiles, format="zip", root_dir=inputfiles)
    
    #newzipfile = os.replace(zipfile, "{0}{1}.zip".format(name, ver))
    
    # TODO: Move Patch File from app directory
    if os.system(inputfiles) == 1:
        #print("{0} patch for {1} created and saved to {2}.zip".format(app, createname, modfiles))
        return True
        #raise SystemExit
 
              
    elif os.system(inputfiles) == 0:
        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".fomat(app, createname))
        return False
        #raise SystemExit
              
    else:
        return "Fail"
        print("Creation of {0} patch for {1} failed!".format(app, createname))
        raise SystemExit
