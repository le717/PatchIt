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

import os, sys, time, linecache # General function modules
import webbrowser, random # Special purpose modules
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
gametips = ["Have you heard about the TRUCK DRIVER cheat code? It's fake. Don't believe anyone who tells you otherwise.",
"Only fire missiles when you have a clear shot at your opponents. Otherwise, you'll miss them completely.",
"Developing a good track line will improve your lap times. Stay near corners to prevent a great speed loss when turning.",
"Is Veronica Voltage in your way? Just drive right through her, she won't stop you.",
"Take your foot of the gas when you're hit by enemy missiles or run into by an oil slick - it will increase the chance of your car doing a full 360° spin, instead of turning backwards."]

def preload():
    '''Python 3.3 version and PatchIt! first-run check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run PatchIt!
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        time.sleep(2) # Don't open browser immediately
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # New tab, raise browser window (if possible)
        time.sleep(5) # PatchIt! closes after this
    else: # If you are not running Python 3.3
        if not exist('settings'): # The settings file does not exist
            writesettings()
        else:
            with open('settings', 'r+', encoding='utf-8') as runcheck: # It does exist
                linecache.clearcache()
                firstrun = linecache.getline('settings', 1)
                if firstrun == "0\n": # '0' means this is the first run
                    writesettings()
                else: # This is not the first run
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
            time.sleep(0.5) # 0.5 second sleep makes it seem like the program is not glitching by running too fast.
            readsettings()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            exit()
        else:
            main()

def readsettings():
    '''Read PatchIt! settings'''
    if not exist('settings'): # The settings file does not exist
        writesettings()
    elif exist('settings'): # The setting file does exist
        with open('settings', 'r', encoding='utf-8') as settings:
            settings.seek(3) # Jump to installation path
            for line in settings:
                if check() ==  True: # The defined Racers installation exists
                    time.sleep(0.5)
                    print("\n{0} installation found at {1}".format(game, line))
                    changepath = input(r"Would you like to change this? (y\N)" + "\n\n> ")
                    if changepath.lower() == "y": # I want to change the defined Racers installation path
                        time.sleep(0.5)
                        writesettings()
                    else: # I do not want to change the defined Racers installation path
                        #print("Canceling...")
                        time.sleep(0.5)
                        main()
                elif check() == False: # The defined Racers installation does not exists
                    print("\nCannot find {0} installation at {1}!".format(game, line))
                    writesettings()

def writesettings():
    '''Write PatchIt! settings'''
    if exist('settings') or not exist('settings'): # It does not matter if it exists or not
        gamepath = input("\nPlease enter the path to your {0} installaton:\n\n> ".format(game))
        if gamepath.lower() == 'exit': # I do not want to change the path
            print("Canceling...")
            time.sleep(0.5)
            main()
        else: # I do want to change the path
            with open('settings', 'w', encoding='utf-8',) as settings:
                settings.seek(0)
                settings.write("1") # The first-run code will not be enacted next time
                settings.seek(1)
                settings.write("\n" + gamepath)
                '''Removing this line breaks the entire first-run code.
                Once it writes the path, PatchIt! closes, without doing as much
                as running the path through check() nor going back to main()'''
                settings.close()
                readsettings()
def check():
    '''Confirm LEGO Racers installation'''
    with open('settings', 'r', encoding='utf-8',) as gamepath:
        gamepath.seek(3) # Skip to defined Racers installation path
        gamepath = gamepath.readline()
        if len(gamepath) == 0: # TODO: Fix this
            return False
         # The only three items needed to confirm a Racers installation.
        elif exist(gamepath + "/GAMEDATA") and exist(gamepath + "/MENUDATA") and exist(gamepath + "/LEGORacers.exe"):
            return True
        else:
            return False

def install():
    '''Install PatchIt! patch'''
    with open('settings', 'r', encoding='utf-8') as install:
        install.seek(3)
        path = install.readline()
        print('\n"' + random.choice(gametips) + '"\n')
        zip = zipfile.ZipFile(r'C:\Users\Public\MCIslandOBJ.zip') # Temp code until .PiP format is finalized and code is written.
        zip.extractall(path)
        #install.close()
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
            print("Installation of *mod name* failed!")
            main()

def compressfiles():
    '''Compress PatchIt! patch'''
    modfiles = input("Please enter the path to the files you wish to compress: \n\n> ")
    #with open('settings2.txt', 'r') as compress:  # Temp file until .PiP format is finalized.
        #files = compress.read()
        #shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as above.
    shutil.make_archive(modfiles, format="zip", root_dir=modfiles) # Same as above.
        #compress.close()
    #if OSError:
        #print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        #main()
    if os.system(modfiles) == 1: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} patch for *mod name* created and saved to {1}.zip".format(game, modfiles)) # Temp messages
        main()
    elif os.system(modfiles) == 0:
        print("Creation of {0} patch for *mod name* ended with an unknown error. Please try again.".format(app))
        main()
    else:
        print("Creation of {0} patch for *mod name* failed!".format(app)) # Temp message
        main()

def readpatch():
    linecache.clearcache()
    patchfile = input("Please enter the path to a {0} patch:\n\n> ".format(app))
    if patchfile.lower() == "exit":
        print("Canceling installation...")
        main()
    else:
        confirmpatch = linecache.getline(patchfile, 1)
        if confirmpatch != "// PatchIt! Patch file, created by le717 and rioforce.\n": # Validity check
            print(line, patchfile + " is not a valid {0} patch.".format(app))
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

