#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt!
    The standard and simple way to package and install LEGO Racers mods

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
Remove unneded Tkinter files after freezing PatchIt!
"""

import os
import distutils.dir_util


def cleanup(destFolder):
    """Remove unneeded Tkinter files"""
    print("\n")
    # Delete the unneeded items from the freeze
    distutils.dir_util.remove_tree(os.path.join(destFolder, "tcl", "tzdata"))
    distutils.dir_util.remove_tree(os.path.join(destFolder, "tcl", "http1.0"))
    distutils.dir_util.remove_tree(os.path.join(destFolder, "tk", "demos"))
    distutils.dir_util.remove_tree(os.path.join(destFolder, "tk", "images"))
