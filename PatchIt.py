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

def menu():
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
            extract()
        elif menuopt.lower() == "s":
            print("gameread()")
            gameread()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            quit(code=None)
        else:
            menu()

def gameread():
    '''Write PatchIt! settings file'''
    if exist('settings.ini'): 
        settings = open('settings.ini', 'rt')
        path = settings.read()
        settings.close()
        print("Your {0} installation is located at {1}".format(game, path))                
        changepath = input(r"Is this correct? (y\N) ")
        if changepath.lower() == "n":
            gamewrite()
        elif changepath.lower() == "y":
            menu()
        else:
            menu()
    elif not exist('settings.ini'):
       # gamewrite()
        print("Cannot find settings file.")

def gamewrite():
    '''Read PatchIt! settings file'''
    if exist('settings.ini') or not exist('settings.ini'):
        path = input("Please enter the path to your {0} installation:\n".format(game))
        settings = open('settings.ini', 'wt')
        path = settings.write(path)
        print("{0} installation path set to {1}".format(game, path))
        settings.close()
#print("File written in {0} sec".format(time.time() - time_start)) #Debug
            #time.sleep(1)
            #gamecheck()
    #elif exist('settings.ini'):
    #    gamepath = input("Please enter the path to your {0} installation:\n".format(game))
    #    with open('settings.ini', 'wt') as gamepath:
    #        gamepath.write(gamepath)
    #        gamecheck()    


def gamecheck():
    '''Confirm LEGO Racers installation'''
    time.sleep(1)
    with open('settings.ini', 'rt') as gamepath:
        gamepath = gamepath.readline()
        if exist(gamepath + os.sep + "LEGORacers.exe") and exist(gamepath + os.sep + "\\GAMEDATA") \
           and exist(gamepath + os.sep + "\\MENUDATA"): #Splitting lne to improve readability.
            print("{0} installation found at {1}.".format(game, gamepath))
        else:
            print("Cannot find {0} installation at {1}.".format(game, gamepath))
            
def extract():
    with open('settings.ini', 'rt') as gamepath:
        while True:            
                print("This will overwrite existing game files.")
                time.sleep(1)
                print("Installing PatchIt! patch...")
                extract_zip = "7za.exe x test.zip -o{0} -r -y".format(gamepath)
                if os.system(extract_zip) == 0:
                    print("\nInstallation complete!")
                    time.sleep(2)
                    exit(code=None)
                elif os.system(extract_zip) == 1:
                    print("An error ocurred, but exact details are unknown.")
                    time.sleep(2)
                    menu()
                else:
                    print("Installation of {0} failed.".format(name))
                    time.sleep(2)
            #path exists stuff here.

if __name__ == "__main__":
    pass
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

gamewrite()


