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
    #print("\nHello, and welcome to {0} {1} {2}, created by {3}.".format(app, majver, minver, creator))
    print('''\nPlease make a selection:
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
            print("gamecheck()")
            gamecheck()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            print('''time.sleep(1)
            quit(code=None)''')
            time.sleep(1)
            quit(code=None)
        else:
            menu()

def gameread():
    '''Write PatchIt! settings.ini'''
    if exist('settings.ini'):
        with open('settings.ini', 'rt') as settings:
            for line in settings:
                print("Your {0} installation is located at {1}".format(game, line))
                
        changepath = input(r"Is this correct? (y\N) ")
        if changepath.lower() == "n":
            gamewrite()
        else:
            menu()
    else:
        gamewrite()

def gamewrite():
    '''Read PatchIt! settings.ini'''
    if not exist('settings.ini'):
        gamefile = input("Please enter the path to your {0} installation:\n".format(game))
        with open('settings.ini', 'wt') as gamepath:
            #time_start = time.time()
            gamepath.write(gamefile)
            #print("File written in {0} sec".format(time.time() - time_start)) #Debug
            time.sleep(1)
            gamecheck()
    else:
        gamecheck()
        #gamepath = input("Please enter the path to your {0} installation:\n".format(game))
        #with open('settings.txt', 'wt') as f:
        #    f.write(gamepath)

def gamecheck():
    '''Confirm LEGO Racers installation'''
    time.sleep(1)
    with open('settings.ini', 'rt') as gamepath:
        gamepath = gamepath.readline()
        if exist(gamepath + os.sep + "LEGORacers.exe") and exist(gamepath + os.sep + "\\GAMEDATA") \
           and exist(gamepath + os.sep + "\\MENUDATA"): #Splitting lne to improve readability.
            print("{0} installation found at {1}.".format(game, gamepath))
            menu()
        else:
            print("Cannot find {0} installation at {1}.".format(game, gamepath))
            
def extract():            
    print("This will overwrite existing game files.")
    time.sleep(1)
    print("Installing {0} patch...".format(app))
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
            
if __name__ == "__main__":
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

menu()


