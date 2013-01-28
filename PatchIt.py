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

import os, time

# Global variables
app = "PatchIt!"
majver = "Version 1"
minver = "Beta 2"
creator = "le717"
game = "LEGO Racers"

def menu():
    print("\nPlease make a selection\n")
    print(" 'c' Create a PatchIt! mod")
    print(" 'i' Install a PatchIt! mod")
    print(" 's' PatchIt! Settings")
    print(" 'q' Quit") 
    menuopt = input("> ")
    while True:
        if menuopt == "c":
            print("createmod()")
            break
        elif menuopt.lower() == "i":
            print("extractmod()")
            break
        elif menuopt.lower() == "s":
            settings()
        elif menuopt.lower() == "q":
            return False
        else:
            break # Need to get this working correctly

def settings():
    gamepath = "C:\\Users\\Racers"

    f = open('settings.txt', 'w')
    f.write(gamepath)
    f.close #close the file

    f = open('settings.txt', 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=' ')
    f.close 

    






if __name__ == "__main__":
    print("{0} {1} {2}, created by {3}.".format(app, majver, minver, creator))

settings()
