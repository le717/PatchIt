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
            break
        elif menuopt.lower() == "i":
            print("extract()")
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
    if exist('settings.ini'):
        with open('settings.ini', 'rt') as settings:
            for line in settings:
                if check() == True:
                    #print("Your {0} installation is located at {1}".format(game, line))
                    changepath = input(r"Is this correct? (y\N) ")
                    if changepath.lower() == "n":
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
        with open('settings.ini', 'wt') as settings: # If I swap this to the long-hand version, a major error occurs.
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
            print("Cannot find {0} installation at {1}.".format(game, gamepath))
            return False

def install():
    with open('settings.ini', 'rt') as gamepath:
        while True:
                print("This will overwrite existing game files.")
                print("Installing PatchIt! patch...")
                extract_zip = "7za.exe x test.zip -o{0} -r -y".format(gamepath)
                if os.system(extract_zip) == 0:
                    print("\nInstallation complete!")
                    time.sleep(2)
                    exit(code=None)
                elif os.system(extract_zip) == 1:
                   #print("An error ocurred, but exact details are unknown.")
                    time.sleep(2)
                    main()
                else:
                    print("Installation of {0} failed.".format(name))
                    time.sleep(2)

if __name__ == "__main__":
    main()
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

main()


