# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# PatchIt! 1.0 Beta 3 by le717 (http://triangle717.wordpress.com).

import os, sys, time # General function modules
import webbrowser, random, linecache # Special purpose modules
import zipfile, shutil # Zip extraction and compression modules, respectively

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, this is built into Python, and doesn't require installing an optional module. :)'''
app = "PatchIt!"
majver = "Version 1"
minver = "Beta 3"
creator = "le717"
game = "LEGO Racers"
exist = os.path.exists

def preload():
    '''Python 3.3 version and PatchIt! first-run check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run PatchIt!
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        time.sleep(2) # Don't open browser immediately
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # New tab, raise browser window (if possible)
        time.sleep(5) # PatchIt! closes after this
    else: # elif sys.version_info >= (3,3)
        if exist('settings'):
            with open('settings', 'r+', encoding='utf-8') as runcheck:
                firstrun = runcheck.read()
                if firstrun == "0": # '0' means this is the first run
                    writesettings()
                else: # This is not the first run
                    main()
        else: # settings does not exist
            writesettings()

def main():
    '''PatchIt! Menu Layout. Will be replaced with a TKinter GUI in Beta 4.'''
    print("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
    print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    menuopt = input("> ")
    while True:
        if menuopt.lower() == "c":
            compress()
        elif menuopt.lower() == "i":
            readpatch()
        elif menuopt.lower() == "s":
            #time.sleep(0.5) # 0.5 second sleep makes it seem like the program is not glitching by running too fast.
            readsettings()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            quit(code=None)
        else:
            main()

def readsettings():
    '''Read PatchIt! settings'''
    if not exist('settings'):
        writesettings()
    elif exist('settings'):
        with open('settings', 'r', encoding='utf-8') as settings:
            settings.seek(3)
            for line in settings:
                if check() ==  True:
                    #time.sleep(0.5)
                    print("\n{0} installation found at {1}".format(game, line))
                    changepath = input(r"Would you like to change this? (y\N)" + "\n> ")
                    if changepath.lower() == "y":
                        time.sleep(0.5)
                        writesettings()
                    else:
                        #print("Canceling...")
                        time.sleep(0.5)
                        main()
                elif check() == False:
                    print("\nCannot find {0} installation at {1}!".format(game, line))
                    writesettings()

def writesettings():
    '''Write PatchIt! settings'''
    if exist('settings') or not exist('settings'):
        gamepath = input("\nPlease enter the path to your {0} installaton:\n> ".format(game))
        if gamepath.lower() == 'exit':
            print("Canceling...")
            time.sleep(0.5)
            main()
        else:
            with open('settings', 'w', encoding='utf-8',) as settings:
                settings.seek(0)
                settings.write("1")
                settings.seek(1)
                settings.write("\n" + gamepath)
                settings.close()
                readsettings()
def check():
    '''Confirm LEGO Racers installation'''
    with open('settings', 'r', encoding='utf-8',) as gamepath:
        gamepath.seek(3)
        gamepath = gamepath.readline()
        if len(gamepath) == 0:
            return False
        elif exist(gamepath + "/GAMEDATA") and exist(gamepath + "/MENUDATA") and exist(gamepath + "/LEGORacers.exe"): # The only three items needed to confirm a Racers installation.
            return True
        else:
            return False

def install():
    '''Install PatchIt! patch'''
    install = open('settings', 'r', encoding='utf-8',)
    install.seek(3)
    path = install.readline()
    zip = zipfile.ZipFile(r'C:\Users\Public\MCIslandOBJ.zip') # Temp code until .PiP format is finalized.
    zip.extractall(path)
    install.close()
    zipfile.ZipFile.close(zip)
    #if OSError:
        #print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        #main()
    if os.system(path) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("*mod name* sucessfully installed!")
        main()
    elif os.system(path) == 1:
        print("An unknown error occured while installing your mod.")
        main()
    else:
        print("Installation *mod name* failed!")
        main()

def compress():
    '''Compress PatchIt! patch'''
    compress = open('settings2.txt', 'r') # Temp code until .PiP format is finalized.
    files = compress.read()
    shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as above.
    compress.close()
    #if OSError:
        #print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        #main()
    if os.system(files) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} patch for *mod name* created!".format(game)) # Temp messages
        main()
    elif os.system(files) == 1:
        print("Creation of {0} patch for *mod name* ended with an unknown error. Please try again.".format(app))
        main()
    else:
        print("Creation of {0} patch for *mod name* failed!".format(app)) # Temp message
        main()

def readpatch():
    linecache.clearcache()
    patchfile = input("Please enter the path to a {0} patch:\n> ".format(app))
    if patchfile.lower() == "exit":
        print("Canceling installation...")
        main()
    else:
        confirmpatch = linecache.getline(patchfile, 1)
        if confirmpatch != "// PatchIt! Patch file, created by le717 and rioforce.\n":
            print(line,
             patchfile + " is not a valid {0} patch.".format(app))
        else:
            modname = linecache.getline(patchfile, 3)
            modver = linecache.getline(patchfile, 4)
            modcreator = linecache.getline(patchfile, 5)
            moddesc = linecache.getline(patchfile, 7)
            print("\n{0} Version {1} Created by {2} {3}".format(modname, modver, modcreator, moddesc))
            print("Do you wish to install {0}".format(modname), end="")
            confirminstall = input("\n> ")
            if confirminstall.lower() == "y":
                install()
            else:
                print("Canceling installation of {0}".format(modname))
                main()


#If PatchIt! is run by itself: preload(). If imported (else): display PatchIt! info.
if __name__ == "__main__":
    preload()
else:
    print("{0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))

