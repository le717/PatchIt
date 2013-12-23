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

# Downloads file(s) from the internet
parentdir = "../wget"
# Not happy with editing sys.path... >:(
sys.path.insert(0, parentdir)
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

# Get just the filename (helps simplify the code)
LinkFileName = os.path.basename(LinkFile)

# URL of archive containing RunAsAdmin utility
RunAdminLink = "https://github.com/QuantumCD/RunAsAdmin/releases/download/v1.0.2/RunAsAdmin.exe"

# Get just the filename (helps simplify the code)
RunAdminName = os.path.basename(RunAdminLink)

# Check if Windows architecture is x64 or x86
if platform.machine() == "AMD64":
    os_bit = True
else:
    os_bit = False


# -------- Begin Core Process -------- #

def args():
    """Command-line arguments parser"""
    parser = argparse.ArgumentParser(
        description="{0} {1} {2} Command-line Arguments".format(
            app, majver, minver))

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
    LinkFile = args.link
    RunAdminLink = args.admin
    reloadarg = args.reload

    # Relaunch the updater
    if reloadarg:
        main(DoAdmin=False)

    if LinkFile is not None:
        pass

    if RunAdminLink is not None:
        pass

    #main()


def CloseUpdater():
    """Close the Updater"""
    # Delete the downloaded file
    #TODO: Reactivate this near completion
    #if os.path.exists(os.path.join(app_folder, LinkFileName)):
        #os.unlink(LinkFileName)

    input("\nPress Enter to close.")
    raise SystemExit(0)


def main(DoAdmin=True):
    """Update PatchIt! to the newest version"""
    # Download RunAsAdmin utility
    if DoAdmin:
        RunAdminDL(start=True)

    # Get PatchIt! installation path
    pi_install_path = ReadPiInstall()

    # The check returned False, go write the settings
    if not pi_install_path:
        SelectPiInstall()

    # Location of PatchIt! Settings folder
    pi_settings_fol = os.path.join(pi_install_path, "Settings")

    # Retrieve the newest version and update download
    new_version, new_title, new_build, download_link = GetNewVersion()

    # Retrieve the user's version
    cur_version, cur_title, cur_build = GetCurrentVersion(pi_settings_fol)

    # Compare the version numbers, titles, and builds
    VersionCompare = CompareVersion(cur_version, new_version)
    TitleCompare = CompareTitle(cur_title, new_title)
    print("Version:", VersionCompare)
    print("Title:", TitleCompare)

    # If the build number is available
    if cur_build != "Unknown":
        BuildCompare = CompareBuild(cur_build, new_build)
        print("Build:", BuildCompare)
    else:
        cur_build = False

    print("\nNewest Version: {0} {1} Build {2}".format(
          new_version, new_title, new_build))
    print("Your Version: {0} {1} Build {2}".format(
         cur_version, cur_title, cur_build))

    # The user is running a previous version
    if (not TitleCompare and not VersionCompare and not BuildCompare):
        print('''
You are running an older version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

    # Only the build numbers are different
    if (VersionCompare and TitleCompare and not BuildCompare):
        print('''
You are running an older version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

    # User is running a pre-release (Unstable, RC1, etc)
    elif (VersionCompare and not TitleCompare and not BuildCompare or
    VersionCompare and not TitleCompare and BuildCompare):
        print('''
You are running a pre-release version of PatchIt!
Press Enter to begin the update process, or any other key to quit.''')

        # Prompt to begin update
        update_prerelease = input("\n> ")

        # User does not want to update
        if update_prerelease:
            CloseUpdater()

        else:
            print("Updating...")

    # It is up-to-date, but offer to update anyway
    elif (VersionCompare and TitleCompare and BuildCompare):
        print('''
Your copy is already up-to-date.
Press Enter to to update it anyway, or any other key to quit''')

        # Prompt to begin update
        update_anyway = input("\n> ")

        # User does not want to update
        if update_anyway:
            CloseUpdater()

        # Run the updater
        else:
            #TODO: Run the update process
            print("Updating...")
            pass
    # Close the updater
    CloseUpdater()


def RunAdminDL(start=True):
    """Downloads RunAsAdmin utility for use and possible installation"""
    # Go ahead and download RunAsAdmin
    if start:
        # Download the file with the newest info
        try:
            wget.download(RunAdminLink)

        # The file could not be downloaded
        #TODO: Remove ValueError when code is near completion
        #TODO: Don't delete download, keep it. It might be needed
        except (HTTPError, ValueError):

            # Since the primary download can not be reached, fall back
            # to the backup host.
            try:
                wget.download("https://github.com/le717/PatchIt/raw/rewrite/Windows/RunAsAdmin/RunAsAdmin.exe")

            # The backup download is unavailable too; Tell the user.
            except (HTTPError, ValueError):

                print('''
{0} could not be downloaded from
{1}
It is required for PatchIt! Updater to run.
Please report this error to {2} right away.
'''.format(RunAdminName, RunAdminLink.strip(RunAdminName), author))
                # Close the updater since RunAsAdmin cannot be downloaded
                CloseUpdater()

        # Relaunch with Admin rights, passing parameter to not repeat this step
        subprocess.call(["RunAsAdmin.exe", "--reload"])

    # RunAsAdmin aleady exists in this installation, so delete our download
    else:
        print("Hi.")
        #if not os.path.exists(os.path.join()):
            #os.unlink(os.path.join())
        raise SystemExit(0)


# -------- End Core Process -------- #


# -------- Begin Settings Reading -------- #


def ReadPiInstall():
    """Reads file containing location of PatchIt! installation"""
    # The Updater's own settings could not be found, return False
    if not os.path.exists(updater_file):
        return False

    # They exist, read it for the installation
    else:
        # The file cannot be used, go rewrite it
        if encode_check(updater_file):
            SelectPiInstall()

        with open(updater_file, "rt", encoding="utf-8") as f:
            pi_install_path = f.readlines()[2]

        # Clean up reading
        pi_install_path = pi_install_path.strip()
        return pi_install_path

# -------- End Settings Reading -------- #


# -------- Begin PatchIt! Installation Search -------- #


def SelectPiInstall():
    """Searches or asks for user's PatchIt! installation"""
    # Used to detect if user needs to manually define an installation
    found_install = False

    # Path to check for PatchIt! on Windows x64
    x64_path = os.path.join(os.path.expandvars("%ProgramFiles(x86)%"), "PatchIt")

    # Path to check for PatchIt! on Windows x86
    x86_path = os.path.join(os.path.expandvars("%ProgramFiles%"), "PatchIt")

    # Perhaps the Updater is in the same place as PatchIt!.
    # In that case, use a different method for finding the installation
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

        # Give focus back to console window
        root.destroy()

        # Get the directory PatchIt! is in
        pi_path = os.path.dirname(pi_path)

        # The user clicked the cancel button
        if pi_path:
            # Write the installation to file
            SavePiInstall(pi_path)

# -------- End PatchIt! Installation Search -------- #


# -------- Begin Settings Writing -------- #


def SavePiInstall(install_path):
    """Saves the installation of PatchIt! for later use"""
    # Replace any backslashes with forwardslashes
    if "\\" in install_path:
        install_path = install_path.replace("\\", "/")

    #TODO: Consider using pickle instead
    # Write file containing installation using UTF-8 encoding
    with open(updater_file, "wt", encoding="utf-8") as f:
        f.write("// PatchIt! Updater Settings\n")
        f.write("# Location of your PatchIt! installation\n")
        f.write(install_path)

# -------- End Settings Writing -------- #


# -------- Begin Version Identification -------- #

def encode_check(the_file):
    """Check if file is properly encoded"""
    with open(the_file, "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (  # The settings file uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The settings file uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):
                return True


def GetNewVersion():
    """Download and read file listing newest PatchIt! version"""
    # Download the file with the newest info
    try:
        wget.download(LinkFile)

    # The file could not be downloaded
    #TODO: Remove ValueError when code is near completion
    except (HTTPError, ValueError):
        print('''
{0} could not be downloaded from
{1}

Please report this error to {2} right away.
'''.format(LinkFileName, LinkFile.strip(LinkFileName), author))
        #TODO: Reenable closing
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
    build = applepie[3]

    # Clean up the text
    version = version.strip()
    title = title.strip()
    build = build.strip()
    download_link = download_link.strip()

    # Delete readings, since they are no longer needed
    del lines[:]
    del applepie[:]
    return (version, title, build, download_link)


def GetCurrentVersion(pi_settings_fol):
    """Gets user's version of PatchIt!"""
    # Full path to file containing PatchIt! version
    pi_settings_file = os.path.join(pi_settings_fol, "PatchIt.cfg")

    # This is pre-v1.1.1 PatchIt!, because the file cannot be found
    if not os.path.exists(pi_settings_file):
        print('''Your version of PatchIt! could not be determined.
Press Enter to begin the update process, or any other key to quit.''')
        # So it needs updating

        # Prompt to begin update
        update_me = input("\n> ")

        # User does not want to update
        if update_me:
            CloseUpdater()
        else:
            #TODO: Run the update process
            pass

    # The file cannot be used, go rewrite it
    if encode_check(pi_settings_file):
        print('''ERROR: Cannnot determine your version of PatchIt!.
Please go run PatchIt! then launch the Updater again.''')
        CloseUpdater()

    # Read PatchIt.cfg to get current version
    with open(pi_settings_file, "rt", encoding="utf-8") as f:
        existing_version = f.readlines()[2]

    # Split reading into version number and title
    bananasplit = existing_version.split(" ")
    version = bananasplit[0]
    title = bananasplit[1]
    # Get the build number
    try:
        build = bananasplit[3]
    # The build number system was not yet implemented (v1.1.0 and v1.1.1)
    except IndexError:
        build = "Unknown"

    # Clean up the text
    version = version.strip()
    title = title.strip()
    build = build.strip()

    # Delete reading, since it is no longer needed
    del bananasplit[:]
    return (version, title, build)


# -------- End Version Identification -------- #


# -------- Begin Version Comparison -------- #


def CompareVersion(cur_version, new_version):
    """Compares the version numbers"""
    # Check if the version numbers are different, and send back the result
    if cur_version != new_version:
        return False

    # The versions are the same
    else:
        return True


def CompareTitle(cur_title, new_title):
    """Compares the version titles"""
    # The titles are not the same
    if cur_title != new_title:
        return False

    # They titles are the same
    else:
        return True


def CompareBuild(cur_build, new_build):
    """Compares the builds numbers"""
    # Convert numbers to an integer
    int_cur_build = int(cur_build)
    int_new_build = int(new_build)

    # The new build number is greater than the old one
    if int_new_build > int_cur_build:
        return False

    # They build numbers are the same
    else:
        return True

# -------- End Version Comparison -------- #


def DownloadUpdate(UpdateDL, InstallPath):
    """Download and install the delta update"""

    # Perform final RunAsAdmin cleanup
    RunAdminDL(start=False)

if __name__ == "__main__":
    # Write window title
    os.system("title {0} {1} {2}".format(app, majver, minver))
    # Run updater
    #args()
    main(DoAdmin=True)
