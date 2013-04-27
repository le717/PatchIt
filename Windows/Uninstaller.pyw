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

# PatchIt! Recursive Uninstaller V1.0.1

import os
import time
import subprocess

def single_uninstall():
    ''' Uninstalls Single PatchIt! Installation'''

    # If a single installation exists
    if os.path.exists(os.path.join(os.getcwd(), "unins000.exe")):
        print("\nRunning unins000.exe...")
        # Run uninstaller
        subprocess.call(os.path.join(os.getcwd(), "unins000.exe"))
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        print("\nSwitching to Recursive Uninstaller")
        loop_uninstall()

    # Single installation does not exist
    else:
        print("\nunins000.exe does not exist")
        # Sleep just a litte to avoid an error
        time.sleep(1.5)
        # Go to recursive uninstaller
        print("\nSwitching to Recursive Uninstaller")
        loop_uninstall()


def loop_uninstall():
    '''Recursive PatchIt! Uninstaller
    Code contributed by JrMasterModelBuilder'''

    # Used for recursion
    i = 1

    # It is assumed another installation exists
    while i < 1000:
        exe_name  ="unins" + str(i).zfill(3) + ".exe"
        if os.path.exists(exe_name):

            # Run the uninstaller
            print("\nRuinning {0}...".format(exe_name))
            subprocess.call(exe_name)
            # Sleep a little to avoid uninstallation error
            time.sleep(2)

        # Update uninstaller name
        i += 1

if not os.path.exists("PatchIt.exe"):
    print("\nThis is not a valid PatchIt! installation!\n")
    raise SystemExit

# Run Uninstaller if this is a valid PatchIt! Installation
if __name__ == "__main__":
    single_uninstall()