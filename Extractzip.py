import os, time
game ="Blah"
name= "Blah 2"
zip_file = "test.zip"
exist = os.path.exists
def start():
    print("This will install {0} {1} onto your computer.".format(game, name))
    path = input("Please enter the path to your {0} installation: ".format(game))
    print() # I like blank lines. It keeps everything nice and neat (unlike this script at the moment...)
    # The three items needed to confirm a LEGO Racers installation, both 1999 and 2001.
    if os.path.exists(path + os.sep + "\\LEGORacers.exe") and os.path.exists(path + os.sep + os.path.join("\\GAMEDATA"))\
       and os.path.exists(path + os.sep + os.path.join("\\MENUDATA")): # Breaking it up for better code reading.
        confirm = input("{0} installation found. This will overwrite existing game files.\nDo you wish to continue? ".format(game))
        if confirm.lower() == "y":
            print("Installing {0}.".format(name))
            extract_zip = "7za.exe x test.zip -o{1} -r -y".format(zip_file, path)
            if os.system(extract_zip) == 0:
                print("\nInstallation complete!")
            elif os.system(extract_zip) == 1:
                print("An error ocurred, but exact details are unknown.")
            else:
                print("Installation of {0} failed.".format(name))
        else:
            print("\nInstallation canceled.")
            time.sleep(2)
            SystemExit
    else:
        print("Cannot find {0} installation.".format(game))
        time.sleep(2)

def starttwo():
    with open('settings.ini', 'rt') as gamepath:
        for line in gamepath:
            print("This will install {0} {1} onto your computer.".format(game, name))
            print()
##            if exist(gamepath + os.sep + "\\LEGORacers.exe") and exist(gamepath + os.sep + "\\GAMEDATA") and exist(gamepath + os.sep + "\\MENUDATA"):
##          s      confirm = input("{0} installation found. This will overwrite existing game files.\nDo you wish to continue? ".format(game))
##                if confirm.lower() == "y":
##                    print("Installing {0}.".format(name))
            extract_zip = "7za.exe x test.zip -oC:\\Users\\Public\\Racers -r -y"

            #time.sleep(2)
            if os.system(extract_zip) == 0:
                print("\nInstallation complete!")
            elif os.system(extract_zip) == 1:
                print("An error ocurred, but exact details are unknown.")
            else:
                print("Installation of {0} failed.".format(name))
##            print("\nInstallation canceled.")
##            time.sleep(2)
##            exit(name=None)


if __name__ == '__main__':
    starttwo()