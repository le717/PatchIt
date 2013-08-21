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
#TODO: User-defined location (after searching in {pf}, of course
settings_fol_app = os.path.join(os.path.dirname(sys.argv[0]), "Settings")

# Check if Windows is x64 or x86
# Based on code from Python help for platform module and my own tests
if platform.machine() == "AMD64":
    os_bit = True
else:
    os_bit = False


def main():
    '''Updates PatchIt! to the newest version'''
    pass


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
    elif not os_bit:
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
    #raise SystemExit(0)

    # Write file containing installation using UTF-8 encoding
    with open("PatchItInstall.cfg", "wt", encoding="utf-8") as f:
        f.write("// Some comment here")
        f.write(install_path)
    pass

if __name__ == "__main__":
    # Run updater
    #main()
    SelectPiInstall()
