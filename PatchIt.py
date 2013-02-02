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

import os, sys, time, webbrowser
import zipfile, shutil # Zip extraction and compression, respectively

# Global variables
app = "PatchIt!"
majver = "Version 1"
minver = "Beta 3"
creator = "le717"
game = "LEGO Racers"
exist = os.path.exists

def preload():
    if sys.version_info < (3,3):
        print("You need to download Python 3.3 or greater to run {0} {1} {2}.".format(app, majver, minver))
        webbrowser.open("http://python.org/download", new=2, autoraise=True)
        time.sleep(5)
    else:
        main()

def main():
    '''PatchIt! Menu Layout'''
    print("\nHello, and welcome to {0} {1} {2}, created by {3}.".format(app, majver, minver, creator))
    print('''Please make a selection:\n
[c] Create a PatchIt! Patch
[i] Install a PatchIt! Patch
[s] PatchIt! Settings
[q] Quit''')
    menuopt = input("> ")
    while True:
        if menuopt == "c":
            #print("compress()")
            compress()
        elif menuopt.lower() == "i":
            #print("install()")
            install()
        elif menuopt.lower() == "s":
            #print("read()")
            time.sleep(0.5)
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
        with open('settings.txt', 'rt') as settings:
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
            with open('settings.txt', 'wt') as settings: # If I swap this to the long-hand version, major code breakage occurs.
                settings.write(gamepath)
                settings.close


def check():
    '''Confirm LEGO Racers installation'''
    with open('settings.txt', 'rt') as gamepath:
        gamepath = gamepath.readline()
        if exist(gamepath + "\\GAMEDATA") and exist(gamepath + "\\MENUDATA") and exist(gamepath + "\\LEGORacers.exe"):
            #print("{0} installation found at {1}.".format(game, gamepath))
            return True
        else:
            #print("Cannot find {0} installation at {1}!".format(game, gamepath))
            return False

def install():
    '''Install PatchIt! patch'''
    install = open('settings.txt', 'r')
    path = install.read()
    zip = zipfile.ZipFile(r'C:\Users\Public\myzipfile.zip') # Temp code until .PiP format is written
    zip.extractall(path)
    install.close()
    zipfile.ZipFile.close(zip)
    if os.system(path) == 1:
        print("PatchIt! patch installed! :D")
        main()
    else:
        print("PatchIt! patch installation failed. Please try again.")
        main()

def compress():
    '''Compress PatchIt! patch'''
    compress = open('settings2.txt', 'r') # Temp code until .PiP format is written
    files = compress.read()
    shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as above.
    compress.close()
    if os.system(files) == 1:
        print("PatchIt! patch created!") # Temp message
        main()
    else:
        print("PatchIt! patch creation failed. Please try again.") # Temp message
        main()

if __name__ == "__main__":
    preload()
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

