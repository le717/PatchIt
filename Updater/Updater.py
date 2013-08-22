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

# Location of PatchIt! Settings folder
settings_fol_app = os.path.join(os.path.dirname(sys.argv[0]), "Settings")

# Name of settings file
settings_file = "PatchItInstall.cfg"

# Check if Windows is x64 or x86
# Based on code from Python help for platform module and my own tests
if platform.machine() == "AMD64":
    os_bit = True
else:
    os_bit = False


def main():
    '''Updates PatchIt! to the newest version'''
    pass


def ReadPiInstall():
    '''Read's file containing location of PatchIt! installation'''

    # The Updater's settings could not be found, so write them
    if not os.path.exists(settings_file):
        SelectPiInstall()

    # They exist, read it for the installation
    else:

        # Open it, read just the area containing the byte mark
        with open(settings_file, "rb") as encode_check:
            encoding = encode_check.readline(3)

        if (  # The settings file uses UTF-8-BOM encoding
            encoding == b"\xef\xbb\xbf"
            # The settings file uses UCS-2 Big Endian encoding
            or encoding == b"\xfe\xff\x00"
            # The settings file uses UCS-2 Little Endian
            or encoding == b"\xff\xfe/"):

                # The file cannot be used, go write it
                SelectPiInstall()

        with open(settings_file, "rt", encoding="utf-8") as f:
            pi_install_path = f.readlines()[2]

        # Send back the path
        return pi_install_path


def SelectPiInstall():
    '''Searches or asks for user's PatchIt! installation'''

    # Used to detect if user needs to manually define an installation
    found_install = False

    # Path to check for PatchIt! on Windows x64
    x64_path = os.path.join(os.path.expandvars("%ProgramFiles(x86)%"), "PatchIt")

    # Path to check for PatchIt! on Windows x86
    x86_path = os.path.join(os.path.expandvars("%ProgramFiles%"), "PatchIt")

    # If this is x64 Windows, look for PatchIt in Program Files (x86)
    if os_bit:
        if os.path.exists(os.path.join(x64_path, "PatchIt.exe")):
            print(os.path.join(x64_path, "PatchIt.exe"))

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


def SavePiInstall(install_path):
    '''Saves the installation of PatchIt! for later use'''

    # Replace any backslashes with forwardslashes
    if "\\" in install_path:
        install_path = install_path.replace("\\", "/")

    print(install_path)

    # Write file containing installation using UTF-8 encoding
    with open(settings_file, "wt", encoding="utf-8") as f:
        f.write("// PatchIt! Updater Settings\n")
        f.write("# Location of your PatchIt! installation\n")
        f.write(install_path)
    pass

if __name__ == "__main__":
    # Run updater
    #main()
    #SelectPiInstall()
    ReadPiInstall()
    raise SystemExit(0)