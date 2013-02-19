#import glob
import os
import zipfile

import linecache

'''zip_files = glob.glob('*.zip')

for zip_filename in zip_files:
    dir_name = os.path.splitext(zip_filename)[0]
    os.mkdir(dir_name)
    zip_handler = zipfile.ZipFile(zip_filename, "r")
    zip_handler.extractall(dir_name)'''





patch = input("Path to patch\n> ")
#patch = "NyanMe.PiP"

installname = linecache.getline(patch, 3)
installver = linecache.getline(patch, 4)

linecache.clearcache()
installpath = linecache.getline('../settings', 2)
installpath = installpath.rstrip("\n")
installzipfile = linecache.getline(patch, 9)
installzipfile = installzipfile.rstrip("\n")
ziplocation = patch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))


   #dir_name = os.path.splitext(installzipfile)[0]
    #os.mkdir(dir_name)
zip_handler = zipfile.ZipFile(ziplocation + installzipfile, "r")
zip_handler.extractall(path=installpath)


if os.system(installpath) == 0:
    print("Sucessfully installed!")
    raise SystemExit
elif os.system(installpath) == 1:
    print("Install with error")
    raise SystemExit
else:
    print("FAIL!")
    raise SystemExit

