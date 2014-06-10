#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    This file is part of PatchIt!

    PatchIt!
    The simple way to package and install LEGO Racers mods

    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

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
PatchIt! Uninstaller v1.0.4
Contains code contributed by JrMasterModelBuilder
https://github.com/JrMasterModelBuilder
"""

import os
import sys
import time
import subprocess


def main(folderPath):
    """
    Uninstall multiple PatchIt! installation
    Code contributed by JrMasterModelBuilder
    """
    i = 0

    # It is assumed another installation exists
    while i < 1000:
        exe_name = "unins{0}.exe".format(str(i).zfill(3))

        if os.path.exists(os.path.join(folderPath, exe_name)):
            # Run uninstaller, passing /SILENT to suppress confirmation boxes
            print("\nRuinning {0}".format(exe_name))
            subprocess.call([os.path.join(folderPath, exe_name), "/SILENT"])

            # Sleep a little to avoid any uninstallation errors
            time.sleep(1.5)
        i += 1

    # Close once everything is uninstalled
    print("\nAll PatchIt! installations had been removed.")
    raise SystemExit(0)

# Run Uninstaller
if __name__ == "__main__":
    try:
        # The user entered a path to the PatchIt! installations
        folderPath = sys.argv[1]

    # The user did not enter a path, use current directory
    except IndexError:
        folderPath = os.getcwd()
    main(folderPath)
