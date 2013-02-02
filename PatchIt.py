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

# PatchIt! (formerly known as LEGO Racers Mod Installer) Beta 2 by le717.

import os, sys, time
import zipfile, shutil # Zip extraction and compression, respectively

# Global variables
app = "PatchIt!"
majver = "Version 1"
minver = "Beta 2"
creator = "le717"
game = "LEGO Racers"
exist = os.path.exists

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
            print("compress()")
            compress()
        elif menuopt.lower() == "i":
            print("install()")
            install()
        elif menuopt.lower() == "s":
            print("read()")
            read()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            quit(code=None)
        else:
            main()

def read():
    '''Read PatchIt! settings.ini'''
    # TODO: Remove input and replace with "if path not exist: say so, ask, and main(). if exist: say so and main().
    if exist('settings.ini'):
        with open('settings.ini', 'rt') as settings:
            for line in settings:
                if check() == True:
                    #print("Your {0} installation is located at {1}".format(game, line))
                    changepath = input(r"Would you like to change this? (y\N) ")
                    if changepath.lower() == "y":
                        write()
                    else:
                        main()
                elif check() == False:
                    write()
    elif not exist('settings.ini'):
        #print("if not exist")
        write()

def write():
    '''Write PatchIt! settings.ini'''
    if not exist('settings.ini'):
        gamepath = input("Please enter the path to your {0} installaton:\n".format(game))
        with open('settings.ini', 'wt') as settings: # If I swap this to the long-hand version, major code breakage occurs.
            settings.write(gamepath)
            settings.close

    else:
        gamepath = input("Please enter the path to your {0} installation:\n".format(game))
        settings = open('settings.ini', 'wt')
        settings.write(gamepath)
        settings.close()

def check():
    '''Confirm LEGO Racers installation'''
    #time.sleep(1)
    with open('settings.ini', 'rt') as gamepath:
        gamepath = gamepath.readline()
        if exist(gamepath + "\\GAMEDATA") and exist(gamepath + "\\MENUDATA") and exist(gamepath + "\\LEGORacers.exe"):
            print("{0} installation found at {1}.".format(game, gamepath))
            return True
        else:
            print("Cannot find {0} installation at {1}!".format(game, gamepath))
            return False

def install():
    '''Install PatchIt! patch'''
    install = open('settings.ini', 'r')
    path = install.read()
    zip = zipfile.ZipFile(r'C:\Users\Public\myzipfile.zip') # Temp path until .PiP format is written
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
    compress = open('settings2.ini', 'r') # Temp path until .PiP format is written
    files = compress.read()
    shutil.make_archive(r'C:\Users\Public\myzipfile', format="zip", root_dir=files) # Same as settings2.ini
    compress.close()
    if os.system(files) == 1:
        print("PatchIt! patch created!")
        main()
    else:
        print("PatchIt! patch creation failed. Please try again.")
        main()

if __name__ == "__main__":
    main()
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

