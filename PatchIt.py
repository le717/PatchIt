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
    print("Please make a selection:\n")
    print(" 'c' Create a PatchIt! installation")
    print(" 'i' Install a PatchIt! installation")
    print(" 's' PatchIt! Settings")
    print(" 'q' Quit") 
    menuopt = input("> ")
    while True:
        if menuopt == "c":
            print("compress()")
            break
        elif menuopt.lower() == "i":
            print("extract()")
            break
        elif menuopt.lower() == "s":
            read()
        elif menuopt.lower() == "q":
            print("Goodbye!")
            time.sleep(1)
            raise SystemExit
        else:
            menu()

def read():
    '''Write PatchIt! settings file'''
    if exist('settings.txt'):
        with open('settings.txt', 'rt') as f:
            for line in f:
                print("Your {0} installation is located at {1}".format(game, line))
                
        changepath = input(r"Is this correct? (y\N) ")
        if changepath.lower() == "n":
            write()
        else:
            menu()
    else:
        write()

def write():
    '''Read PatchIt! settings file'''
    if not exist('settings.txt'):
        gamepath = input("Please enter the path to your {0} installation:\n".format(game))
        with open('settings.txt', 'wt') as f:
            f.write(gamepath)
        #f.close()
    else:
        gamepath = input("Please enter the path to your {0} installation:\n".format(game))
        f = open('settings.txt', 'ww')
        f.write(gamepath)
        f.close()

def extract():
    with open('settings.txt', 'rt') as f:
        while True:

if __name__ == "__main__":
    print()
else:
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

menu()


