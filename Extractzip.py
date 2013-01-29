import os, time
exist = os.path.exists
def install():
    if exist('settings.ini'):
        with open('settings.ini', 'rt') as gamepath:
            for line in gamepath:
                gamepath = gamepath.readline()
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
                    print("Installation of mod failed.")
                    time.sleep(2)

if __name__ == '__main__':
    install()

install()