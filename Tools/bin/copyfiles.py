#! /usr/bin/env python3
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
import distutils.file_util
import distutils.dir_util


def main(srcFiles, destFolder):

    """Copy any files/directories to their requried location.

    `srcFiles` is an array of files/directories to copy.
    `destFolder` is the single destination directory.
    """
    print("\nCopying required files and directories")

    # Create the destination folder if needed
    # (it usually does not need to be)
    if not os.path.exists(destFolder):
        os.makedirs(destFolder)

    for item in srcFiles:
        # Copy any files
        if os.path.isfile(item):
            partDir = os.path.join(destFolder, os.path.dirname(item))
            distutils.dir_util.create_tree(partDir, item)
            distutils.file_util.copy_file(item, partDir)

        # Copy any directories
        else:
            rootDir = os.path.join(os.getcwd(), item)
            partDir = os.path.join(destFolder, item)
            distutils.dir_util.copy_tree(rootDir, partDir)
