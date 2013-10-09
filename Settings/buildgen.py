# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

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
PatchIt! Build Number Generator
"""

import sys
import os
import pickle

# PatchIt! Constants
from constants import build_file
from singleton import Singleton


@Singleton
class BuildNumber(object):
    """Generate a build number"""

    def __init__(self):
        self.buildnum = self.get_build()

    def fetch(self):
        return self.buildnum

    def write_build(self, reset_build=False):
        """Reset PatchIt! build number"""
        # Reset the number if one is not given
        if not reset_build:
            build = "1"
        else:
            build = reset_build

        # Write the number
        with open(build_file, "wb") as f:
            pickle.dump(build, f)
        return build

    def get_build(self):
        """Sets current PatchIt! build number"""
        # The pickled data cannot be found
        if not os.path.exists(build_file):

            # If this is a frozen exe, it will return None
            if (hasattr(sys, "frozen") and
                    sys.frozen in ("windows_exe", "console_exe")):
                return None

            # This is the raw Python script, get a new number
            elif not (hasattr(sys, "frozen") and
                      not sys.frozen in ("windows_exe", "console_exe")):
                new_build = self.write_build(False)
                return new_build

        # It does exist, read it
        elif os.path.exists(build_file):
            with open(build_file, "rb") as f:
                build = pickle.load(f)
            return build


class UpdateBuildNumber(object):
    """Increase the build number"""

    def update_build(self, build_num):
        """Increase the build number"""
        # Convert it to an integer
        int_build = int(build_num)

        # Increase the build number
        int_build += 1

        # Reconstruct the entire number, send it off for wrting
        updated_num = "{0}".format(int_build)
        BuildNumber.Instance().write_build(updated_num)
        return updated_num
