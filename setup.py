#! /usr/bin/env python3.4-32
# -*- coding: utf-8 -*-
"""PatchIt! - The simple way to package and install LEGO Racers mods.

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

"""

import os
import sys
from cx_Freeze import (setup, Executable)
import constants as const
from Settings.buildgen import BuildNumber

# x86 Python
if sys.maxsize < 2 ** 32:
    destfolder = os.path.join(os.getcwd(), "bin", "Windows")

# x64 Python
else:
    input('''\n64-bit binaries are not frozen.
Please freeze PatchIt! using 32-bit Python 3.3.''')
    raise SystemExit(0)

# Run utility to get the newest version of the readme
# Freeze continues if this has an error
from Tools.bin import (cleanup, copyfiles, readme)
readme.main()

build_exe_options = {"build_exe": destfolder,
                     "create_shared_zip": True,
                     "compressed": True,
                     "optimize": 2,
                     "icon": "Icons/PiIcon.ico",
                     "include_files": ["Build.pickle"],
                     "includes": [
                         "re"
                     ]}

setup(
    name="PatchIt!",
    version="{0}.{1}".format(const.version, BuildNumber.Instance().buildNum),
    author="2013-2014 Triangle717",
    description="PatchIt! Version {0} {1}".format(const.version, const.minVer),
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("RunIt.py", targetName="PatchIt.exe")])

# Copy any required files/directories
filesForCopying = [
    os.path.join("Icons", "PiTk.gif"),
    os.path.join("Icons", "PiIcon.ico"),
    os.path.join("Icons", "cghbnjcGJfnvzhdgbvgnjvnxbv12n1231gsxvbhxnb.jpg")
]
copyfiles.main(filesForCopying, destfolder)

# Run cleanup script to remove unneeded Tkinter files
cleanup.main(destfolder)

# Freeze PatchIt! Uninstaller
print("\nFreezing PatchIt! Uninstaller\n")
from Tools.Uninstaller import setup  # noqa

print("\nDone. :)\n")
