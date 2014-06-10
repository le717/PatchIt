#! /usr/bin/env python3.4-32
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    “And behold, I am coming quickly, and My reward is with Me,
    to give to every one according to his work.
    I am the Alpha and the Omega, the Beginning and the End,
    the First and the Last.” - Revelation 22:12-13

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
PatchIt! setup script using cx_Freeze
"""

import os
import sys
from cx_Freeze import (setup, Executable)

# PatchIt! Constants
import constants as const


# Append build command to command-line arguments.
# Just type "python setup.py" and it will freeze
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

# If this is Python x86
if sys.maxsize < 2 ** 32:
    destfolder = os.path.join(os.getcwd(), "bin", "Windows")

# If this is Python x64
else:
    input('''\n64-bit binaries are not frozen.
Please freeze PatchIt! using 32-bit Python 3.3.''')
    raise SystemExit(0)

# Run utility to get the newest version of the readme
# Freeze continues if this has an error
from Tools.bin import (PiReadme, cleanup)
PiReadme.main()

build_exe_options = {"build_exe": destfolder,
                     "create_shared_zip": True,
                     "compressed": True,
                     "optimize": 2,
                     "icon": "Icons/PiIcon.ico",
                     "include_files": ["Build.pickle"],
                     "includes": [
                         "re",
                         "patchit",
                         "color",
                         "runasadmin",
                         "Patch/install",
                         "Patch/create",
                         "Patch/racingtips",
                         "Game/legojam",
                         "Game/JAMExtractor",
                         "Settings/buildgen"
                     ]}

# Get the current build number
from Settings.buildgen import BuildNumber as bg

setup(
    name="PatchIt!",
    version="{0}.{1}".format(const.majVer, bg.Instance().buildNum),
    author="2013-2014 Triangle717",
    description="PatchIt! Version {0} {1}".format(const.majVer, const.minVer),
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("RunIt.py", targetName="PatchIt.exe")])

# Run cleanup script to remove unneeded Tkinter files
cleanup.cleanup(destfolder)

# Freeze PatchIt! Uninstaller
print("\nFreezing PatchIt! Uninstaller\n")
from Tools.Uninstaller import setup  # noqa
print("Done. :)\n")
