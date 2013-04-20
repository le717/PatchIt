#! python3
"""
    This file is part of PatchIt!

    PatchIt! -  the standard yet simple way to package and install mods for LEGO Racers
    Created 2013 Triangle717 <http://triangle717.wordpress.com>

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
# PatchIt! setup script using cx_Freeze.
# Taken from https://github.com/Lyrositor/EBPatcher
# and https://github.com/JrMasterModelBuilder/JAM-Extractor
# With changes by Triangle717

from cx_Freeze import setup, Executable
from PatchIt import majver, minver
import sys, platform

# Append build to the arguments. Just type "python setup.py" and it will compile
if len(sys.argv) == 1: sys.argv[1:] = ["build"]

# Compile into the proper folder depending on the architecture
if platform.architecture('64bit'):
    destfolder = "Compile/Windows64"
if platform.architecture('32bit'):
    destfolder = "Compile/Windows32"

build_exe_options = {"build_exe": destfolder,
                     "create_shared_zip": True,
                     "optimize": 1,
                     "icon": "Icons/PatchItIcon.ico",
                     "compressed": True,
                     "includes": [
                     "modernextract",
                     "moderncompress",
                     "legacyextract",
                     "gametips",
                     "handlejam",
                     "patchit",
                     "color"],
}

setup(
    name = "PatchIt!",
    version = "{0} {1}".format(majver, minver),
    author = "Triangle717",
    description = "PatchIt! Version {0} {1}, created 2013 Triangle717".format(majver, minver),
    license = "GNU GPLv3",
    options = {"build_exe": build_exe_options},
    executables = [Executable("RunIt.py", targetName="PatchIt.exe")]
)