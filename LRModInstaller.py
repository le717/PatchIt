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



# LEGO Racers Mod Installer Beta 1.
# Built with Nyan Cat-Athon because it is a good mod.

import os, time

# Kinda like the ISPP in Inno Setup, changing these changes all code that points back to them, make it easier to completely rebrand the script.
game = "LEGO Racers"
name = "Nyan Cat-Athon Mod"
zip_file = "LR_Mod_Nyan-Cat-Athon.zip"

def main():
    '''Controls all functions of the application. Might be broken up later.'''
    print("This will install {0} {1} onto your computer.".format(game, name))
    path = input("Please enter the path to your {0} installation: ".format(game))
    print() # I like blank lines. It keeps everything nice and neat (unlike this script at the moment...)
    # The three items needed to confirm a LEGO Racers installation, both 1999 and 2001.
    if os.path.exists(path + os.sep + "\\LEGORacers.exe") and os.path.exists(path + os.sep + os.path.join("\\GAMEDATA"))\
       and os.path.exists(path + os.sep + os.path.join("\\MENUDATA")): # Breaking it up for better code reading.
        confirm = input("{0} installation found. This will overwrite existing game files.\nDo you wish to continue? ".format(game))
        if confirm.lower() == "y":
            print("Installing {0}.".format(name))
            extract_zip = "7za.exe x {0} -o{1} -r -y".format(zip_file, path) # Need to get ZipFile module (or equal function) working to support more than just Windows.
            if os.system(extract_zip) == 0:
                print("\nInstallation complete!")
                time.sleep(2) # Instead of closing as soon as that after any result, sleep for 2 seconds to let the user actually see the result.
                SystemExit # Because I cannot get break working...
            elif os.system(extract_zip) == 1:
                print("An error ocurred, but exact details are unknown.")
                time.sleep(2)
                SystemExit
            else:
                print("Installation of {0} failed.".format(name))
                time.sleep(2)
                SystemExit
        else:
            print("\nInstallation canceled.")
            time.sleep(2)
            SystemExit
    else:
        print("Cannot find {0} installation.".format(game))
        time.sleep(2)


if name == "__main__":
    print(name)

main()
