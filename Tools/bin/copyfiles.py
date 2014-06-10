#! /usr/bin/env python3
# -*- coding: utf-8 -*-
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
Copy any files/directories to their requried location during freezing
"""

import os
import distutils.file_util
import distutils.dir_util


def main(srcFiles, destFolder):
    """
    Copy any files/directories to their requried location
    `srcFiles` is an array of files/directories to copy
    `destFolder` is the single destination folder
    """
    print("\n")
    if not os.path.exists(destFolder):
        os.makedirs(destFolder)

    for item in srcFiles:
        if os.path.isfile(item):
            partDir = os.path.join(
                destFolder, item.split(os.path.sep)[-1].split("/")[0])

            if not os.path.exists(partDir):
                os.makedirs(partDir)

            distutils.file_util.copy_file(item, partDir)
        else:
            distutils.dir_util.copy_tree(item, destFolder)
