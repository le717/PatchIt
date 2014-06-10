#! /usr/bin/env python3.4-32
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    This file is part of PatchIt!

    PatchIt!
    The simple way to package and install LEGO Racers mods

    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PatchIt! is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.

-------------------------------------
PatchIt! Uninstaller setup script using cx_Freeze.
"""

import os
import sys
from cx_Freeze import (setup, Executable)

# Append build command to command-line arguments.
# Just type "python setup.py" and it will freeze
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

# Hides any text from the console window
base = "Win32GUI"

# If this is Python x86
if sys.maxsize < 2 ** 32:
    destfolder = os.path.join(os.path.dirname(__file__), "bin")

# If this is Python x64
else:
    input('''\n64-bit binaries are not frozen.
Please freeze PatchIt! Uninstaller using 32-bit Python 3.3.''')
    raise SystemExit(0)

build_exe_options = {"build_exe": destfolder,
                     "includes": ["subprocess", "re"],
                     "optimize": 2,
                     "icon": "../../Icons/PiIcon.ico"}

# The script is being run from the main setup.py,
# so define the proper location of the app icon
if not os.path.isfile(build_exe_options["icon"]):
    build_exe_options["icon"] = "Icons/PiIcon.ico"

setup(
    name="PatchIt! Uninstaller",
    version="1.0.4",
    author="2013-2014 Triangle717",
    description="PatchIt! Uninstaller v1.0.4",
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable(os.path.join(os.path.dirname(__file__),
                 "PiUninstaller.pyw"), targetName="PiUninstaller.exe",
                            base=base)])
