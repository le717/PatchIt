# LEGO Racers Mod Installer Beta 1.
# Built with Nyan Cat-Athon just because it is a good testing mod.

import os

# Kinda like the ISPP in Inno Setup, changing these changes all code that points back to them, make it easier to completely rebrand the script.
game = "LEGO Racers"
name = "Nyan Cat-Athon Mod"

#class zipfile.ZipInfo(filename="LR_Mod_Nyan-Cat-Athon.zip")

def main():
    print("This will install {0} {1} onto your computer.".format(game, name))
    path = input("Please enter the path to your {0} installation: ".format(game))
    print()
    if [os.path.exists(path + os.sep + "\\LEGORacers.exe"), os.path.exists(path + os.sep + os.path.join("\\MENUDATA")), \
        os.path.exists(path + os.sep + os.path.join("\\GAMEDATA"))]: # Breaking it up for better code reading.
        confirm = input("{0} installation found. This installation will overwrite existing game files.\nDo you wish to continue? ".format(game))
        if confirm.lower() == "y":
            print("Installing {0}.".format(name))
            print("*zip extraction code here*")
            print("Installation complete")
        else:
            print("\nInstallation canceled.")
            SystemExit
    else:
        print("Cannot find {0} installation.".format(game))


if name == "__main__":
    print(name)

main()
