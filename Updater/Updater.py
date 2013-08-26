# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

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
"""
# PatchIt! Updater

import sys
import os
import platform

# Downloads file(s) from the internet
import wget
# Used to catch downloading errors
from urllib.error import HTTPError
# File Dialog Box
from tkinter import (Tk, filedialog)

app = "PatchIt! Updater"
majver = "0.5"
minver = "Unstable"
author = "Triangle717"

# Location of PatchIt! Updater Exe/Py
app_folder = os.path.dirname(sys.argv[0])

# Name of settings file
updater_file = "Updater.cfg"

# URL of file containing newest version of PatchIt!, and link to delta update
# Hosted on the PatchIt! GitHub repo, gh-pages branch
#LinkFile = "http://le717.github.io/PatchIt/NewestRelease.cfg"
LinkFile = "NewestRelease.cfg"

# Manually define the file to download
try:
    LinkFile = sys.argv[1]
# No URL was given, use one from GitHub
except IndexError:
    pass

# Get just the filename (helps simplify the code)
LinkFileName = os.path.basename(LinkFile)

# Check if Windows architectyure is x64 or x86
if platform.machine() == "AMD64":
    os_bit = True
else:
    os_bit = False


# -------- Begin Core Process -------- #

def CloseUpdater():
    '''Closes the updater'''

    # Delete the downloaded file
    #TODO: Reactivate this
    #if os.path.exists(os.path.join(app_folder, LinkFileName)):
        #os.unlink(LinkFileName)

    # Close the Updater
    input("\nPress Enter to close.")
    raise SystemExit(0)


def main():
    '''Updates PatchIt! to the newest version'''

    # Get PatchIt! installation path
    pi_install_path = ReadPiInstall()

    # The check returned False, go write the settings
    if not pi_install_path:
        SelectPiInstall()

    # Location of PatchIt! Settings folder
    pi_settings_fol = os.path.join(pi_install_path, "Settings")

    # Retrieve the newest version and update download
    new_version, new_title, download_link = GetNewVersion()
    print(new_version, new_title)

    # Retrieve the user's version
    cur_version, cur_title = GetCurrentVersion(pi_settings_fol)
    print(cur_version, cur_title)

    # Compare the version numbers and titles
    VersionCompare = CompareVersion(cur_version, new_version)
    TitleCompare = CompareTitle(cur_title, new_title)
    print("Version:", VersionCompare)
    print("Title:", TitleCompare)

    # The user is running a previous version
    if not TitleCompare and not VersionCompare:
        print('''You are running an older version of PatchIt!
({0} {1}, {2} {3}).
Press Enter to begin the update process, or any other key to quit.'''.format(
    cur_version, cur_title, new_version, new_title))
        #TODO: Input here

    # User is running a pre-release, (Unstable, RC1, such like that)
    elif VersionCompare and not TitleCompare:
        print('''You are running a pre-release version of PatchIt!
({0} {1}, {2} {3}).
Press Enter to begin the update process, or any other key to quit.'''.format(
    cur_version, cur_title, new_version, new_title))

        update_prerelease = input("\n> ")

        if update_prerelease:
            CloseUpdater()

        else:
            print("Updating...")

    # It is up-to-date, but offer to update anyway
    elif VersionCompare and TitleCompare:
        print('''Your copy is already up-to-date ({0} {1}).
Press Enter to to update it anyway, or any other key to quit'''.format(
    cur_version, cur_title))

        update_anyway = input("\n> ")

        # User does not want to update
        if update_anyway:
            CloseUpdater()

        # Run the updater
        else:
            #TODO: Run the updater
            print("Updating...")
            pass

    # Close the updater
    CloseUpdater()

# -------- End Core Process -------- #


# -------- Begin Settings Reading -------- #


def ReadPiInstall():
    '''Read's file containing location of PatchIt! installation'''

    # The Updater's settings could not be found, return False
    if not os.path.exists(updater_file):
        return False

    # They exist, read it for the installation
    else:

        # Open it, read just the area containing the byte mark
        with open(updater_file, "rb") as encode_check:
            encoding = encode_check.readline(3)

        if (  # The settings file uses UTF-8-BOM encoding
            encoding == b"\xef\xbb\xbf"
            # The settings file uses UCS-2 Big Endian encoding
            or encoding == b"\xfe\xff\x00"
            # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):

                # The file cannot be used, go write it
                SelectPiInstall()

        with open(updater_file, "rt", encoding="utf-8") as f:
            pi_install_path = f.readlines()[2]

        # Send back the path
        return pi_install_path

# -------- End Settings Reading -------- #


# -------- Begin PatchIt! Installation Search -------- #


def SelectPiInstall():
    '''Searches or asks for user's PatchIt! installation'''

    # Used to detect if user needs to manually define an installation
    found_install = False

    # Path to check for PatchIt! on Windows x64
    x64_path = os.path.join(os.path.expandvars("%ProgramFiles(x86)%"), "PatchIt")

    # Path to check for PatchIt! on Windows x86
    x86_path = os.path.join(os.path.expandvars("%ProgramFiles%"), "PatchIt")

    # Perhaps the Updater is in the same place as PatchIt!, in that case,
    # we need to use a different method for finding an installation
    same_path = os.path.join(os.path.dirname(app_folder), "Settings")

    # The updater resides in the same location as PatchIt!
    if os.path.exists(same_path):

        # It's been found, no need for user to define it
        found_install = True

        # Write the installation to file
        SavePiInstall(os.path.dirname(app_folder))

    # If this is x64 Windows, look for PatchIt in Program Files (x86)
    if os_bit:
        if os.path.exists(os.path.join(x64_path, "PatchIt.exe")):

            # It's been found, no need for user to define it
            found_install = True

            # Write the installation to file
            SavePiInstall(x64_path)

    # If this is x86 Windows, look for PatchIt in Program Files
    else:
        if os.path.exists(os.path.join(x86_path, "PatchIt.exe")):
            print(os.path.join(x86_path, "PatchIt.exe"))

            # It's been found, no need for user to define it
            found_install = True

            # Write the installation to file
            SavePiInstall(x86_path)

    if not found_install:
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
        pi_path = filedialog.askopenfilename(
            parent=root,
            title="Where is PatchIt.exe",
            defaultextension=".exe",
            filetypes=[("PatchIt.exe", "*.exe")]
        )

        # Get the directory PatchIt! is in
        pi_path = os.path.dirname(pi_path)

        # The user clicked the cancel button
        if not pi_path:

            # Give focus back to console window
            root.destroy()

        # Write the installation to file
        SavePiInstall(pi_path)

# -------- End PatchIt! Installation Search -------- #


# -------- Begin Settings Writing -------- #


def SavePiInstall(install_path):
    '''Saves the installation of PatchIt! for later use'''

    # Replace any backslashes with forwardslashes
    if "\\" in install_path:
        install_path = install_path.replace("\\", "/")

    # Write file containing installation using UTF-8 encoding
    with open(updater_file, "wt", encoding="utf-8") as f:
        f.write("// PatchIt! Updater Settings\n")
        f.write("# Location of your PatchIt! installation\n")
        f.write(install_path)

# -------- End Settings Writing -------- #


# -------- Begin Version Identification -------- #


def GetNewVersion():
    '''Download and read file listing newest PatchIt! version'''

    # Download the file with the newest info
    try:
        wget.download(LinkFile)

    # The file could not be downloaded
    #TODO: Remove ValueError when code is near completion
    except (HTTPError, ValueError):
        print('''
{0} could not be downloaded from
{1}

Please report this error to {2} right away.'''.format(LinkFileName,
     LinkFile.strip(LinkFileName), author))
        #CloseUpdater()

    # The file was downloaded, now read it
    with open(os.path.join(app_folder, LinkFileName), "rt",
         encoding="utf-8") as f:
        lines = f.readlines()[:]

    # Assign the proper value for each line
    version_full = "".join(lines[0])
    download_link = "".join(lines[1])

    # Split reading into version number and title
    applepie = version_full.split(" ")
    version = applepie[0]
    title = applepie[1]

    # Clean up the text
    version = version.strip()
    title = title.strip()
    download_link = download_link.strip()

    # Delete readings, since they are no longer needed
    del lines[:]
    del applepie[:]

    return (version, title, download_link)


def GetCurrentVersion(pi_settings_fol):
    '''Gets user's version of PatchIt!'''

    # Full path to file containing PatchIt! version
    pi_settings_file = os.path.join(pi_settings_fol, "PatchIt.cfg")

    # This is pre-v1.1.1 PatchIt!, because the file cannot be found
    if not os.path.exists(pi_settings_file):
        #FIXME: Better message
        #print("Your version of PatchIt! could not be determined.")
        # So it needs updating
        #TODO: Automatically run updater
        pass

    #OPTIMIZE: Consider moving encoding check into seperate function
    # Open it, read just the area containing the byte mark
        with open(pi_settings_file, "rb") as encode_check:
            encoding = encode_check.readline(3)

        if (  # The settings file uses UTF-8-BOM encoding
            encoding == b"\xef\xbb\xbf"
            # The settings file uses UCS-2 Big Endian encoding
            or encoding == b"\xfe\xff\x00"
            # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):

                # The file cannot be used, go write it
                SelectPiInstall()

    # Read PatchIt.cfg to get current version
    with open(pi_settings_file, "rt", encoding="utf-8") as f:
        existing_version = f.readlines()[2]

    # Split reading into version number and title
    bananasplit = existing_version.split(" ")
    version = bananasplit[0]
    title = bananasplit[1]

    # Clean up the text
    version = version.strip()
    title = title.strip()

    # Delete reading, since it is no longer needed
    del bananasplit[:]

    return (version, title)


# -------- End Version Identification -------- #


# -------- Begin Version Comparison -------- #


def CompareVersion(cur_version, new_version):
    '''Compares the version numbers'''

    # Check if the version numbers are different, and send back the result
    if cur_version != new_version:
        return False

    # The versions are the same
    else:
        return True


def CompareTitle(cur_title, new_title):
    '''Compares the version titles'''

    # The titles are not the same
    if cur_title != new_title:
        return False

    # They titles are the same
    else:
        return True


# -------- End Version Comparison -------- #

if __name__ == "__main__":
    # Write window title
    os.system("title {0} {1} {2}".format(app, majver, minver))
    # Run updater
    main()
