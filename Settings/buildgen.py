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

import sys
import os
import pickle

# PatchIt! Constants
import constants as const
from singleton import Singleton


@Singleton
class BuildNumber(object):

    """Generate a build number.

    Generate a new build number upon each launch,
        except when we are running a binary release.
    Stores the build number using pickling v3.

    Exposes three public methods:
    * fetch TODO.
    * getBuild TODO.
    * writeBuild resetBuild {boolean} TODO.
    """

    def __init__(self):
        self.buildNum = self.getBuild()

    def fetch(self):
        return self.buildNum

    def writeBuild(self, resetBuild=False):
        """Reset build number."""
        # Reset the number if one is not given
        if not resetBuild:
            build = "1"
        else:
            build = resetBuild

        # Write the number
        with open(const.buildFile, "wb") as f:
            pickle.dump(build, f)
        return build

    def getBuild(self):
        """Set current build number."""
        # The pickled data cannot be found
        if not os.path.exists(const.buildFile):

            # If this is a frozen exe, it will return None
            # TODO: Support GUI
            if (hasattr(sys, "frozen") and
                    sys.frozen in ("windows_exe", "console_exe")):
                return None

            # This is the raw Python script, get a new number
            elif not (hasattr(sys, "frozen") and
                      sys.frozen not in ("windows_exe", "console_exe")):
                newBuild = self.writeBuild(False)
                return newBuild

        # It does exist, read it
        elif os.path.exists(const.buildFile):
            with open(const.buildFile, "rb") as f:
                build = pickle.load(f)
            return build


class UpdateBuildNumber(object):
    """Increase the build number."""

    def updateBuild(self, buildNum):
        """Increase the build number."""
        # Convert it to an integer
        intBuild = int(buildNum)

        # Increase the build number
        intBuild += 1

        # Reconstruct the entire number, send it off for wrting
        updatedNum = "{0}".format(intBuild)
        BuildNumber.Instance().writeBuild(updatedNum)
        return updatedNum
