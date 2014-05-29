# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013-2014 Triangle717 <http://Triangle717.WordPress.com/>

    PatchIt! is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PatchIt! is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.

-------------------------------------
PatchIt! Updater: Quickly update your installation of PatchIt! to
the newest version using delta updates.
"""

import sys
import os
import platform
import subprocess
import argparse
import tarfile
import json

# Downloads file(s) from the internet
parentdir = "../wget"
# Not happy with editing sys.path... >:(
sys.path.insert(0, parentdir)
import wget

# Used to catch downloading errors
from urllib.error import (HTTPError, URLError)
# File Dialog Box
from tkinter import (Tk, filedialog)

app = "PatchIt! Updater"
majVer = "0.5"
minVer = "Unstable"
author = "Triangle717"

# Location of PatchIt! Updater Exe/Py
appFolder = os.path.dirname(sys.argv[0])

# Name of settings file
updaterFile = "Updater.json"

# URL of file containing newest version of PatchIt!, and link to delta update
# Hosted on the PatchIt! GitHub repo, gh-pages branch
#LinkFile = "http://le717.github.io/PatchIt/NewestRelease.json"
linkFile = "NewestRelease.json"

# Get just the filename (helps simplify the code)
linkFileName = os.path.basename(linkFile)

# URL of archive containing RunAsAdmin utility
runAdminLink = "https://github.com/QuantumCD/RunAsAdmin/releases/download/v1.0.2/RunAsAdmin.exe"

# Get just the filename (helps simplify the code)
runAdminName = os.path.basename(runAdminLink)

# Check if Windows architecture is x64 or x86
if platform.machine() == "AMD64":
    osBit = True
else:
    osBit = False


# -------- Begin Core Process -------- #

def args():
    """Command-line arguments parser"""
    parser = argparse.ArgumentParser(
        description="{0} {1} {2} Command-line Arguments".format(
            app, majVer, minVer))

    # Reload argument
    parser.add_argument("-r", "--reload",
                        help='Reloads PatchIt! Updater using the RunAsAdmin utility',
                        action="store_true")

     # Alternate download link
    parser.add_argument("-l", "--link",
                        help='''Alternate download location for updated PatchIt! releases''')

    # Alternate RunAsAdmin link
    parser.add_argument("-a", "--admin",
                        help='''Alternate download location for RunAsAdmin utility''')

    # Register all the parameters
    args = parser.parse_args()

    # Declare parameters
    linkArg = args.link
    runAdminArg = args.admin
    reloadArg = args.reload

    # Relaunch the updater
    if reloadArg:
        main(useAdmin=False)

    if linkArg is not None:
        pass

    if runAdminArg is not None:
        pass

    #main()


def closeUpdater():
    """Close the Updater"""
    # Delete the downloaded file
    #TODO: Reactivate this near completion
    #if os.path.exists(os.path.join(appFolder, linkFileName)):
        #os.unlink(linkFileName)

    input("\nPress Enter to close.")
    raise SystemExit(0)


def main(useAdmin=True):
    """Update PatchIt! to the newest version"""
    # Download RunAsAdmin utility
    if useAdmin:
        runAdminDL(start=True)

    # Get PatchIt! installation path
    piInstallPath = readPiInstall()

    # The check returned False, go write the settings
    if not piInstallPath:
        selectPiInstall()

    # Location of PatchIt! Settings folder
    piSettingsFol = os.path.join(piInstallPath, "Settings")

    # Retrieve the newest version and update download
    newVersion, newTitle, newBuild, downloadLink = getNewVersion()

    # Retrieve the user's version
    curVersion, curTitle, curBuild = getCurrentVersion(piSettingsFol)

    # Compare the version numbers, titles, and builds
    versionCompare = compareVersion(curVersion, newVersion)
    titleCompare = compareTitle(curTitle, newTitle)
    print("Version:", versionCompare)
    print("Title:", titleCompare)

    # If the build number is available
    if curBuild != "Unknown":
        buildCompare = compareBuild(curBuild, newBuild)
        print("Build:", buildCompare)
    else:
        curBuild = False

    print("\nNewest Version: {0} {1} Build {2}".format(
          newVersion, newTitle, newBuild))
    print("Your Version: {0} {1} Build {2}".format(
          curVersion, curTitle, curBuild))

    # The user is running a previous version
    if (not titleCompare and not versionCompare and not buildCompare):
        print('''
You are running an older version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

    # Only the build numbers are different
    if (versionCompare and titleCompare and not buildCompare):
        print('''
You are running an older version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

    # User is running a pre-release (Unstable, RC1, etc)
    elif (versionCompare and not titleCompare and not buildCompare or
          versionCompare and not titleCompare and buildCompare):
        print('''
You are running a pre-release version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

        # Prompt to begin update
        updatePrerelease = input("\n> ")

        # User does not want to update
        if updatePrerelease:
            closeUpdater()

        else:
            print("Updating...")

    # It is up-to-date, but offer to update anyway
    elif (versionCompare and titleCompare and buildCompare):
        print('''
Your copy is already up-to-date.
Press Enter to to update it anyway, or any other key to quit''')

        # Prompt to begin update
        updateAnyway = input("\n> ")

        # User does not want to update
        if updateAnyway:
            closeUpdater()

        # Run the updater
        else:
            #TODO: Run the update process
            print("Updating...")
            pass
    closeUpdater()


def runAdminDL(start=True):
    """Downloads RunAsAdmin utility for use and possible installation"""
    #TODO: Respect --admin parameter
    # Go ahead and download RunAsAdmin
    if start:
        # Download the file with the newest info
        try:
            wget.download(runAdminLink)

        # The file could not be downloaded
        #TODO: Remove ValueError when code is near completion
        #TODO: Don't delete download, keep it. It might be needed
        except (HTTPError, URLError, ValueError):

            # Since the primary download can not be reached, fall back
            # to the backup host.
            try:
                wget.download("https://github.com/le717/PatchIt/raw/rewrite/Tools/Windows/RunAsAdmin/RunAsAdmin.exe")

            # The backup download is unavailable too; Tell the user.
            except (HTTPError, URLError, ValueError):

                print('''
{0} could not be downloaded from
{1}
It is required for PatchIt! Updater to run.
Please report this error to {2} right away.
'''.format(runAdminName, runAdminLink.strip(runAdminName), author))
                # Close the updater since RunAsAdmin cannot be downloaded
                closeUpdater()

        # Relaunch with Admin rights, passing parameter to not repeat this step
        subprocess.call(["RunAsAdmin.exe", "--reload"])

    # RunAsAdmin aleady exists in this installation, so delete our download
    else:
        print("Hi.")
        #if os.path.exists(os.path.join()):
            #os.unlink(os.path.join())
        raise SystemExit(0)


# -------- End Core Process -------- #


# -------- Begin Settings Reading -------- #


def readPiInstall():
    """Reads file containing location of PatchIt! installation"""
    # The Updater's own settings could not be found, return False
    if not os.path.exists(updaterFile):
        return False

    # It exists, read it for the installation
    else:
        with open(updaterFile, "rt") as f:
            settingsData = json.load(f)

        return settingsData["installPath"]

# -------- End Settings Reading -------- #


# -------- Begin PatchIt! Installation Search -------- #


def selectPiInstall():
    """Searches or asks for user's PatchIt! installation"""
    # Used to detect if user needs to manually define an installation
    foundInstall = False

    # Path to check for PatchIt! on Windows x64
    x64Path = os.path.join(os.path.expandvars("%ProgramFiles(x86)%"),
                            "PatchIt")

    # Path to check for PatchIt! on Windows x86
    x86Path = os.path.join(os.path.expandvars("%ProgramFiles%"), "PatchIt")

    # Perhaps the Updater is in the same place as PatchIt!.
    # In that case, use a different method for finding the installation
    samePath = os.path.join(os.path.dirname(appFolder), "Settings")

    # The updater resides in the same location as PatchIt!
    if os.path.exists(samePath):
        # It's been found, no need for user to define it
        foundInstall = True
        # Write the installation to file
        savePiInstall(os.path.dirname(appFolder))

    # If this is x64 Windows, look for PatchIt in Program Files (x86)
    if osBit:
        if os.path.exists(os.path.join(x64Path, "PatchIt.exe")):
            # It's been found, no need for user to define it
            foundInstall = True
            # Write the installation to file
            savePiInstall(x64Path)

    # If this is x86 Windows, look for PatchIt in Program Files
    else:
        if os.path.exists(os.path.join(x86Path, "PatchIt.exe")):
            # It's been found, no need for user to define it
            foundInstall = True
            # Write the installation to file
            savePiInstall(x86Path)

    if not foundInstall:
        print('''Could not find a valid PatchIt! installation!
Please select your PatchIt! installation.''')

        # Draw (then withdraw) the root Tk window
        root = Tk()
        root.withdraw()

        # Overwrite root display settings
        root.overrideredirect(True)
        root.geometry('0x0+0+0')

        # Show window again, lift it so it can receive the focus
        # Otherwise, it is behind the console window
        root.deiconify()
        root.lift()
        root.focus_force()

        # Select PatchIt.exe
        piPath = filedialog.askopenfilename(
            parent=root,
            title="Where is PatchIt.exe",
            defaultextension=".exe",
            filetypes=[("PatchIt.exe", "*.exe")]
        )

        # Give focus back to console window
        root.destroy()

        # Get the directory PatchIt! is in
        piPath = os.path.dirname(piPath)

        # The user clicked the cancel button
        if piPath:
            # Write the installation to file
            savePiInstall(piPath)

# -------- End PatchIt! Installation Search -------- #


# -------- Begin Settings Writing -------- #


def savePiInstall(installLoc):
    """Saves the installation of PatchIt! for later use"""
    # Replace any backslashes with forwardslashes
    if "\\" in installLoc:
        installLoc = installLoc.replace("\\", "/")

    jsonData = {"installPath": installLoc}

    # Write JSON file containing installation
    with open(updaterFile, "wt") as f:
        f.write(str(jsonData).replace("'", '"'))

# -------- End Settings Writing -------- #


# -------- Begin Version Identification -------- #

def encodeCheck(theFile):
    """Check if file is properly encoded"""
    with open(theFile, "rb") as f:
        encoding = f.readline(3)

    # UTF-8BOM, UCS-2 Big Endian, UCS-2 Little Endian, respectivl
    if encoding in (b"\xef\xbb\xbf", b"\xfe\xff\x00", b"\xff\xfe/"):
        return True
    return False


def getNewVersion():
    """Download and read file listing newest PatchIt! version"""
    # Download the file with the newest info
    try:
        wget.download(linkFile)

    # The file could not be downloaded
    #TODO: Remove ValueError when code is near completion
    except (HTTPError, URLError, ValueError):
        print('''
{0} could not be downloaded from
{1}

Please report this error to {2} right away.
'''.format(linkFileName, linkFile.strip(linkFileName), author))
        #TODO: Reenable closing
        #CloseUpdater()

    # The file was downloaded, now read it
    with open(os.path.join(appFolder, linkFileName), "rt",
              encoding="utf-8") as f:
        lines = f.readlines()[:]

    # Assign the proper value for each line
    fullVersion = "".join(lines[0])
    downloadLink = "".join(lines[1])

    # Split reading into version number and title
    applepie = fullVersion.split(" ")
    version = applepie[0]
    title = applepie[1]
    build = applepie[3]

    # Clean up the text
    version = version.strip()
    title = title.strip()
    build = build.strip()
    downloadLink = downloadLink.strip()

    # Delete readings, since they are no longer needed
    del lines[:]
    del applepie[:]
    return (version, title, build, downloadLink)


def getCurrentVersion(piSettingsFol):
    """Gets user's version of PatchIt!"""
    # Full path to file containing PatchIt! version
    piSettingsFile = os.path.join(piSettingsFol, "PatchIt.cfg")

    # This is pre-v1.1.1 PatchIt!, because the file cannot be found
    if not os.path.exists(piSettingsFile):
        print('''Your version of PatchIt! could not be determined.
Press Enter to begin the update process, or any other key to quit.''')
        # So it needs updating

        # Prompt to begin update
        updateMe = input("\n> ")

        # User does not want to update
        if updateMe:
            closeUpdater()
        else:
            #TODO: Run the update process
            pass

    # The file cannot be used, go rewrite it
    if encodeCheck(piSettingsFile):
        print('''ERROR: Cannnot determine your version of PatchIt!.
Please go run PatchIt! then launch the Updater again.''')
        closeUpdater()

    # Read PatchIt.cfg to get current version
    with open(piSettingsFile, "rt", encoding="utf_8") as f:
        existingVersion = f.readlines()[2]

    # Split reading into version number and title
    bananaSplit = existingVersion.split(" ")
    version = bananaSplit[0]
    title = bananaSplit[1]
    # Get the build number
    try:
        build = bananaSplit[3]
    # The build number system was not yet implemented (v1.1.0 and v1.1.1)
    except IndexError:
        build = "Unknown"

    # Clean up the text
    version = version.strip()
    title = title.strip()
    build = build.strip()

    # Delete reading, since it is no longer needed
    del bananaSplit[:]
    return (version, title, build)


# -------- End Version Identification -------- #


# -------- Begin Version Comparison -------- #


def compareVersion(curVersion, newVersion):
    """Compares the version numbers"""
    # Check if the version numbers are different, and send back the result
    if curVersion != newVersion:
        return False

    # The versions are the same
    else:
        return True


def compareTitle(curTitle, newTitle):
    """Compares the version titles"""
    # The titles are not the same
    if curTitle != newTitle:
        return False

    # They titles are the same
    else:
        return True


def compareBuild(curBuild, newBuild):
    """Compares the builds numbers"""
    # Convert numbers to an integer
    intCurBuild = int(curBuild)
    intNewBuild = int(newBuild)

    # The new build number is greater than the old one
    if intNewBuild > intCurBuild:
        return False

    # They build numbers are the same
    else:
        return True

# -------- End Version Comparison -------- #


def downloadUpdate(updateDL, installLoc):
    """Download and install the delta update"""

    # Perform final RunAsAdmin cleanup
    runAdminDL(start=False)

if __name__ == "__main__":
    # Write window title
    os.system("title {0} {1} {2}".format(app, majVer, minVer))
    # Run updater
    #args()
    main(useAdmin=True)
