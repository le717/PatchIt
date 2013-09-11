#! python3.3-32
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

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
"""
# PatchIt! Uninstaller setup script using cx_Freeze.
# Taken from https://github.com/Lyrositor/EBPatcher
# and https://github.com/JrMasterModelBuilder/JAM-Extractor
# With changes by Triangle717

from cx_Freeze import (setup, Executable)
import sys

# Append build command to command-line arguments.
# Just type "python setup.py" and it will freeze
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

# Hides any text from the console window
base = "Win32GUI"

# If this is Python x86
if sys.maxsize == 2147483647:
    destfolder = "Uninstaller"

# If this is Python x64
else:
    input('''\n64-bit binaries are not frozen.
Please freeze PatchIt! Uninstaller using 32-bit Python 3.3.''')
    raise SystemExit(0)

build_exe_options = {"build_exe": destfolder,
                     "includes": ["subprocess", "re"],
                     "icon": "../Icons/PatchItIcon.ico"}

setup(
    name="PatchIt! Uninstaller",
    version="1.0.2.2",
    author="2013 Triangle717",
    description="PatchIt! Uninstaller Version 1.0.2.2",
    license="GNU GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("Uninstaller.pyw", targetName="PiUninstaller.exe",
         base=base)])