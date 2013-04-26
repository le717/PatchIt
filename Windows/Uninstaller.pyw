#! python3
"""
    This file is part of PatchIt!

    PatchIt! -  the standard and simple way to package and install mods for LEGO Racers
    Created 2013 Triangle717 <http://triangle717.wordpress.com>

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

# PatchIt! Recursive Standalone Uninstaller V0.9.1

import os
import time
import subprocess

def main():
    ''' Uninstalls Single PatchIt! Installation'''

    # If a single installation exists
    if os.path.exists(os.path.join(os.getcwd(), "unins000.exe")):
        # Run uninstaller
        subprocess.call(os.path.join(os.getcwd(), "unins000.exe"))
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        second_main()

    # Single installation does not exists, close
    # TODO: Make it go to recursive uninstaller for checking of other installations
    # I've seen unins001.exe exists and not unins000.exe before.
    else:
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        second_main()

def second_main():
    '''Recursive PatchIt! Uninstaller'''

    # Used for recursion
    i = 1

    # Exe name
    exe_name = "unins00" + str(i) + ".exe"

    # If another installation exists
    if os.path.exists(os.path.join(os.getcwd(), exe_name)):
        # Run uninstaller
        subprocess.call(os.path.join(os.getcwd(), exe_name))
        # Sleep just a litte to avoid an error
        time.sleep(1.5)

        # Add 1 to the file name
        i += 1
        # Redefine the Exe name
        new_exe_name = "unins00" + str(i) + ".exe"
        # Run uninstaller
        subprocess.call(os.path.join(os.getcwd(), new_exe_name))
        # Sleep just a litte to avoid an error
        time.sleep(1.5)

        # Loop back through to uninstall any other installations
        # Up to unins009.exe
        second_main()

    # Another installation does not exist
    else:
        raise SystemExit

# Run Uninstaller
if __name__ == "__main__":
    main()