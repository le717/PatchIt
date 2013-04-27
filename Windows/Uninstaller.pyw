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

# PatchIt! Recursive Standalone Uninstaller V1.0

import os
import time
import subprocess

def single_uninstall():
    ''' Uninstalls Single PatchIt! Installation'''

    # If a single installation exists
    if os.path.exists(os.path.join(os.getcwd(), "unins000.exe")):
        # Run uninstaller
        subprocess.call(os.path.join(os.getcwd(), "unins000.exe"))
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        second_main()

    # Single installation does not exist
    else:
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        loop_uninstall()


def loop_uninstall():
    '''Recursive PatchIt! Uninstaller'''

    # Used for recursion
    i = 1

    # It is assumed another installation exists
    while os.path.exists("unins00" + str(i) + ".exe"):
        # Sleep a little to avoid uninstallation error
        time.sleep(3)
        # Run the uninstaller
        subprocess.call("unins00" + str(i) + ".exe")
        # Update uninstaller names
        i += 1
        # The while loop continues until unins009.exe
        # Unknown what happens after unins009.exe, but if you have that many installations...

    # If we assumed incorrectly and another installation doesn't exist, or
    # if all the installations have been uninstalled
    if not os.path.exists("unins00" + str(i) + ".exe"):
        # Close program
        raise SystemExit





# Run Uninstaller
if __name__ == "__main__":
    single_uninstall()