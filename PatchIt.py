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

# PatchIt! 1.0 Beta 3, copyright 2013 le717 (http://triangle717.wordpress.com).

import os, sys, time, linecache # General use modules
import webbrowser, random, gametips # Special purpose modules
import zipfile, shutil # Zip extraction and compression modules, respectively

''' Global variables
This is like the ISPP in Inno Setup. Changing these variables changes anything else that refers back to them.
Thankfully, variables are a key part of Python, and doesn't require installing an optional module. :)'''

app = "PatchIt!"
majver = "Version 1"
minver = "Beta 3"
creator = "le717"
game = "LEGO Racers"
exist = os.path.exists

# ------------ Begin PatchIt! Initialization ------------ #

def preload():
    '''Python 3.3 and PatchIt! first-run check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run PatchIt!
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        # Don't open browser immediately
        time.sleep(2)
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # New tab, raise browser window (if possible)
        # PatchIt! automatically closes after this
        time.sleep(5)
    else: # You are running <= Python 3.3
        # The settings file does not exist
        if not exist('settings'):
            writesettings()
        # The settings file does exist
        else:
            # Settings file does not need to be opened to use linecache
            linecache.clearcache() # Always clear cache before reading
            firstrun = linecache.getline('settings', 1)
            # Remove \n, \r, \t, or any of the like
            firstrun = firstrun.strip()
            # '0' defines a first-run
            if firstrun == "0":
                writesettings()
            # Any other number (Default, 1) means it has been run before
            else:
                main()


def main():
    '''PatchIt! Menu Layout'''
    print("\nHello, and welcome to {0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))
    print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "c":
            compressfiles()
        elif menuopt.lower() == "i":
            readpatch()
        elif menuopt.lower() == "s":
        # 0.5 second sleep makes it seem like the program is not bugged by running so fast.
            time.sleep(0.5)
            readsettings()
        elif menuopt.lower() == "q":
            # Blank space makes everything nice and neat
            print()
            print("Goodbye!")
            time.sleep(1)
            raise SystemExit
        else:
            main()

# ------------ End PatchIt! Initialization ------------ #


# ------------ Begin PatchIt! Settings ------------ #

def readsettings():
    '''Read PatchIt! settings'''
    # The settings file does not exist
    if not exist('settings'):
        writesettings()
    # The setting file does exist
    elif exist('settings'):
        # Use path as listed in gamecheck() for messages
        # The defined installation was not confirmed by gamecheck()
        if gamecheck() == False:
            print("\nCannot find {0} installation at {1}!".format(game, definedgamepath))
            writesettings()
        # The defined installation was confirmed by gamecheck()
        elif gamecheck() ==  True:
            time.sleep(0.5)
            print("\n{0} installation found at {1}".format(game, definedgamepath))
            changepath = input(r"Would you like to change this? (y\N)" + "\n\n> ")
            # Yes, I want to change the defined installation
            if changepath.lower() == "y":
                time.sleep(0.5)
                writesettings()
                # No, I do not want to change the defined installation
            else:
                #print("Canceling...")
                time.sleep(0.5)
                main()

def writesettings():
    '''Write PatchIt! settings'''
     # It does not matter if it exists or not, it has to be written
    if exist('settings') or not exist('settings'):
        newgamepath = input("\nPlease enter the path to your {0} installaton:\n\n> ".format(game))
        # Allow the user to cancel the change
        if newgamepath.lower() == 'exit':
            print("Canceling...")
            time.sleep(0.5)
            main()
        # Continue on with the change
        else:
            with open('settings', 'wt', encoding='utf-8') as settings:
                settings.seek(0)
                # Ensures first-run process will be skipped next time
                settings.write("1")
                settings.seek(1)
                settings.write("\n" + newgamepath)
                '''Removing this line breaks the entire first-run code.
                Once it writes the path, PatchIt! closes, without doing as much
                as running the path through gamecheck() nor going back to main()
                Possible TODO: Find out why this happens and remove it if possible.'''
                settings.close()
                readsettings()
def gamecheck():
    '''Confirm LEGO Racers installation'''
    linecache.clearcache()
    global definedgamepath
    definedgamepath = linecache.getline('settings', 2)
    definedgamepath = definedgamepath.strip()
    # If the settings file was externally edited and the path was removed
    if len(definedgamepath) == 0:
        return False
    # The only three items needed to confirm a LEGO Racers installation.
    elif exist(definedgamepath + "/GAMEDATA") and exist(definedgamepath + "/MENUDATA") and exist(definedgamepath + "/LEGORacers.exe"):
        return True
    # The installation path cannot be found
    else:
        return False

# ------------ End PatchIt! Settings ------------ #


# ------------ Begin PatchIt! Patch Installation ------------ #

def readpatch():
    global installpatch
    linecache.clearcache()
    installpatch = input("Please enter the path to a {0} patch:\n\n> ".format(app))
    if installpatch.lower() == "exit":
        print("Canceling installation...")
        main()
    else:
        confirmpatch = linecache.getline(installpatch, 1)
        if confirmpatch != "// PatchIt! Patch file, created by le717 and rioforce.\n": # Validity check
            print(confirmpatch, installpatch + " is not a valid {0} patch.".format(app))
        else:
            global modinstallname
            modinstallname = linecache.getline(installpatch, 3)
            modinstallver = linecache.getline(installpatch, 4)
            modinstallauthor = linecache.getline(installpatch, 5)
            modinstalldesc = linecache.getline(installpatch, 7)
            print("\n{0} {1} {2} {3}".format(modinstallname, modinstallver, modinstallauthor, modinstalldesc))
            print("Do you wish to install {0}".format(modinstallname), end="")
            confirminstall = input("\n> ")
            if confirminstall.lower() == "y":
                installfiles()
            else:
                print("\nCanceling installation of {0}".format(modinstallname))
                main()

def installfiles():
    '''Install PatchIt! patch'''
    linecache.clearcache()
    installpath = linecache.getline('settings', 2)
    installpath = installpath.rstrip()
    installzipfile = linecache.getline(installpatch, 9)
    installzipfile = installzipfile.rstrip()
    print('\n"' + random.choice(gametips.gametips) + '"\n')
    zip = zipfile.ZipFile(installzipfile)
    zip.extractall(installpath)
    zipfile.ZipFile.close(zip)
    if os.system(installpath) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} sucessfully installed!".format(modinstallname))
        main()
    elif os.system(installpath) == 1:
        print("An unknown error occured while installing {0}.".format(modinstallname))
        main()
    else:
        print("Installation of {0} failed!".format(modinstallname))
        main()

# ------------ End PatchIt! Patch Installation ------------ #


# ------------ Begin PatchIt! Patch Creation ------------ #

def compressfiles():
    '''Compress PatchIt! patch'''
    modfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    #with open('settings2.txt', 'rt') as compress:  # Temp file until .PiP format is finalized.
        #files = compress.read()
        #shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as above.
    shutil.make_archive(modfiles, format="zip", root_dir=modfiles) # Same as above.
        #compress.close()
    #if OSError:
        #print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        #main()
    if os.system(modfiles) == 1: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} patch for {1} created and saved to {2}.zip".format(game, modcreatename, modcreatefiles)) # Temp messages
        main()
    elif os.system(modfiles) == 0:
        print("Creation of {0} patch for {1} ended with an unknown error. Please try again.".format(app, modcreatename))
        main()
    else:
        print("Creation of {0} patch for {1} failed!".format(app, modcreatename)) # Temp message
        main()

# ------------ End PatchIt! Patch Creation ------------ #

#If PatchIt! is run by itself: preload(). If imported (else): display PatchIt! info.
if __name__ == "__main__":
    preload()
else:
    print("{0} {1} {2}, copyright 2013 {3}.".format(app, majver, minver, creator))

