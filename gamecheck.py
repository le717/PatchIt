import os

exist = os.path.exists

'''def gamecheck():
    with open('settings.txt', 'rt') as gamepath:
        for line in gamepath:
            gamepath.readline()
            if exist(gamepath + os.sep + "LEGORacers.exe") and exist(gamepath + os.sep + "\\GAMEDATA") \
               and exist(gamepath + os.sep + "\\MENUDATA"):
                print("Installation found.")
                return True
            else:
                print("Cannot find.")
                return False'''
            

#gamepath = "C:\\Users\\Public\\Racers2"
def gamecheck():
    readfile()
    if exist(gamepath + os.sep + "LEGORacers.exe") and exist(gamepath + os.sep + "\\GAMEDATA") \
       and exist(gamepath + os.sep + "\\MENUDATA"):
        print("Installation found.")
        return True
    else:
        print("Cannot find.")
        return False


def readfile():
    f = open('settings.txt') # if no mode is specified, ‚r‚ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        print(line, end='')
    f.close() # close the file



readfile()
