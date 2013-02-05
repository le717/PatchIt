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

def preload():
    '''Python 3.3 version and PatchIt! first-run check'''
    if sys.version_info < (3,4): # You need to have at least Python 3.3 to run PatchIt!
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        time.sleep(2) # Don't open browser immediately
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # New tab, raise browser window
        time.sleep(5) # PatchIt! closes after this
    else: # elif sys.version_info >= (3,3)
        with open('settings.txt', 'r+', encoding='utf-8') as runcheck:
            firstrun = runcheck.read()
            if firstrun == "0": # '0' means this is the first run
                runcheck.seek(0)
                runcheck.write("1\n")
                print(r"1\n") # Debug print
                read()
            else: # This is not the first run
                main()

def main():
    '''PatchIt! Menu Layout. Will be replaced with a TKinter GUI in Beta 4.'''
    print("\nHello, and welcome to {0} {1} {2}, created by {3}.".format(app, majver, minver, creator))
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
            install()
        elif menuopt.lower() == "s":
            time.sleep(0.5) # 0.5 second sleep makes it seem like the program is not glitching by running too fast.
            read()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            quit(code=None)
        else:
            main()

def read():
    '''Read PatchIt! settings.txt'''
    # TODO: Remove input and replace with "if path not exist: say so, ask, and main(). if exist: say so and main().
    if exist('settings.txt'):
        with open('settings.txt', 'rt', encoding='utf-8',) as settings:
            for line in settings:
                if check() == True:
                    time.sleep(0.5)
                    print("{0} installation found at {1}.".format(game, line))
                    changepath = input(r"Would you like to change this? (y\N) ")
                    if changepath.lower() == "y":
                        time.sleep(0.5)
                        write()
                    else:
                        main()
                elif check() == False:
                    print("Cannot find {0} installation at {1}!".format(game, line))
                    write()
    elif not exist('settings.txt'):
        #print("if not exist")
        write()

def write():
    '''Write PatchIt! settings.txt'''
    if exist('settings.txt') or not exist('settings.txt'):
        gamepath = input("Please enter the path to your {0} installaton:\n".format(game))
        if gamepath.lower() == 'exit':
            print("Canceling...")
            #time.sleep(0.5)
            main()
        else:
            with open('settings.txt', 'wt', encoding='utf-8',) as settings: # If I swap this to the long-hand version, major code breakage occurs.
                settings.write(gamepath)
                settings.close


def check():
    '''Confirm LEGO Racers installation'''
    with open('settings.txt', 'rt', encoding='utf-8',) as gamepath:
        gamepath = gamepath.readline()
        if exist(gamepath + "/GAMEDATA") and exist(gamepath + "/MENUDATA") and exist(gamepath + "/LEGORacers.exe"): # The only three items needed to confirm a Racers installation.
            #print("{0} installation found at {1}.".format(game, gamepath))
            return True
        else:
            #print("Cannot find {0} installation at {1}!".format(game, gamepath))
            return False

def install():
    '''Install PatchIt! patch'''
    install = open('settings.txt', 'rt', encoding='utf-8',)
    path = install.read()
    zip = zipfile.ZipFile(r'C:\Users\Public\myzipfile.zip') # Temp code until .PiP format is finalized.
    zip.extractall(path)
    install.close()
    zipfile.ZipFile.close(zip)
    if OSError:
        print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        main()
    elif os.system(path) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("*mod name* sucessfully installed!")
        main()
    elif os.system(path) == 1:
        print("An unknown error occured while installing *mod name*")
    else:
        print("Installation *mod name* failed!")
        main()

def compress():
    '''Compress PatchIt! patch'''
    compress = open('settings2.txt', 'r') # Temp code until .PiP format is finalized.
    files = compress.read()
    shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as above.
    compress.close()
    if OSError:
        print("*mod name* sucessfully installed!") # Only because this is currently the only way I know how to supress Window's error message, but I need a better way...
        main()
    elif os.system(files) == 0: # TODO: Disregard OS error and use only app error, thus bringing the proper exit codes.
        print("{0} patch for *mod name* created!".format(game)) # Temp messages
        main()
    elif os.system(files) == 1:
        print("Creation of {0} patch for *mod name* ended with an unknown error. Please try again.".format(app))
        main()
    else:
        print("Creation of {0} patch for *mod name* failed!".format(app)) # Temp message
        main()

'''If PatchIt! is run by itself, preload(). If imported, display PatchIt! info.'''
if __name__ == "__main__":
    preload()
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

