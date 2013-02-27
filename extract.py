#PatchIt! V1.0.1 Stable Patch Installation code

# Import only certain items instead of "the whole toolbox"
import linecache
import PatchIt
import gametips
import zipfile
from os import system
from random import choice
from time import sleep
# Colored text (until GUI is written)
import color
import color.colors as colors
# GUI! :D
import tkinter
from tkinter import filedialog


# ------------ Begin PatchIt! Patch Installation ------------ #

def readpatch():
    '''Reads and Installs PatchIt! Patch'''

    print("\nInstall a {0} Patch".format(PatchIt.app), end="\n")
    # PiP label for Patch selection dialog box
    fileformat = [("PatchIt! Patch", "*.PiP")]
    # Hide the root Tk window
    root = tkinter.Tk()
    root.withdraw()

    # Select the patch file
    # TODO: Make dialog active window automatically and do the same to main window when closed.
    installpatch = filedialog.askopenfilename(
    title="Select a {0} Patch".format(PatchIt.app),
    defaultextension=".PiP",
    filetypes=fileformat)

    # The user clicked the cancel button
    if len(installpatch) == 0:
        colors.pc("\nCould not find a {0} patch to read!".format(PatchIt.app), color.FG_LIGHT_RED)
        sleep(1)
        PatchIt.main()

    # The user selected a patch
    else:
        # Confirm that this is a patch, as defined in Documentation/PiP Format.md
        confirmpatch = linecache.getline(installpatch, 1)
        # It's not a patch! D:
        if confirmpatch != "// PatchIt! Patch format, created by le717 and rioforce.\n": # Validity line
            colors.pc("{0}\n{1}is not a valid {2} patch!".format(confirmpatch, installpatch, PatchIt.app), color.FG_LIGHT_RED)
            sleep(1)
            PatchIt.main()

        # It is a patch! :D
        else:
            # Get all patch details
            installname = linecache.getline(installpatch, 3)
            installver = linecache.getline(installpatch, 4)
            installauthor = linecache.getline(installpatch, 5)
            installdesc = linecache.getline(installpatch, 7)
            # Strip the description for better display
            installdesc = installdesc.strip()
            # Display all the info
            print('\n{0} {1} {2} "{3}"'.format(installname, installver, installauthor, installdesc), end="\n")

            # Strip the name and version to put all the text on one line
            installname = installname.strip("\n")
            installver = installver.strip("\n")
            print("\nDo you wish to install {0} {1}? {2}".format(installname, installver, r"(y\N)"))
            confirminstall = input("\n> ")
            # No, I do not want to install the patch
            if confirminstall.lower() != "y":
                print("\nCanceling installation of {0} {1}...".format(installname, installver))
                sleep(1)
                PatchIt.main()

            # Yes, I do want to install it!
            else:
                linecache.clearcache() # Again, clear cache
                # Read the settings file for installation (LEGO Racers) directory
                installpath = linecache.getline('settings', 2)

                # Create a valid folder path
                installpath = installpath.rstrip("\n")
                installzipfile = linecache.getline(installpatch, 9)

                # Create a vaild ZIP archive
                installzipfile = installzipfile.rstrip("\n")

                # Find the ZIP archive
                ziplocation = installpatch.rstrip("{0}{1}{2}".format(installname, installver, ".PiP"))

                # Display the Racers game tips
                print('\n"' + choice(gametips.gametips) + '"\n')
                try:
                    # Actually extract the ZIP archive
                    extractzip = zipfile.ZipFile(ziplocation + installzipfile, "r")
                    extractzip.extractall(path=installpath)

                    # Close the ZIP archive when we are through
                    zipfile.ZipFile.close(extractzip)

                    # For some reason, it cannot find the ZIP archive
                except FileNotFoundError:
                    # Strip the ID text for a smoother error message
                    installver = installver.lstrip("Version: ")
                    installauthor = installauthor.lstrip("Author: ")
                    colors.pc('''Cannot find files for {0} {1}!
Make sure {2}{3}.zip and {4}{5}.PiP
are in the same folder, and try again.

If the error continues, contact {6}and ask for a fixed version.'''
                    .format(installname, installver, installname, installver, installname, installver, installauthor), color.FG_LIGHT_RED)
                    # There has to be an easier way to format the message without repeating installname/ver 3 times each...
                    # Sleep a bit longer so the error message can be read.
                    sleep(4.5)
                    PatchIt.main()

                '''Windows continually throws up the '*installpath* is not recognized as an internal or external command,
                operable program or batch file.' error, killing the exit codes, and I am unable to neither silence it nor hide it without
                looping back over all the code. So I had to redefine what is a clean exit and what isn't. Thus,
                1 == clean exit, 0, == exit with some error, and anything else is pure fail.
                I believe the error is due the fact I have it attached to the wrong code. The question now is,
                what do I attach it to so I can have proper exit codes?'''

                if system(installpath) == 1:
                    print("\n{0} {1} sucessfully installed!".format(installname, installver))
                    # Always sleep for 2 second after displaying exit code before kicking back to the PatchIt! menu.
                    sleep(2)
                    PatchIt.main()

                elif system(installpath) == 0:
                    print("\nAn unknown error occured while installing {0} {1}.".format(installname, installver))
                    sleep(2)
                    PatchIt.main()

                else:
                    print("\nInstallation of {1} Version {2} failed!".format(app, createname, createver))
                    sleep(2)
                    PatchIt.main()

# ------------ End PatchIt! Patch Installation ------------ #