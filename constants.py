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
from datetime import datetime

# App name and version
appName = "PatchIt!"
majVer = "1.1.3"
minVer = "Unstable"
creator = "Triangle717"
currentYear = datetime.now().year

# Global game data
LRGame = "LEGO Racers"
LRSettings = "Racers.json"
LRSettingsCfg = "Racers.cfg"
piSettings = "PatchIt.json"

# Name of PatchIt! Exe/Py
exeName = os.path.basename(sys.argv[0])
# Location of PatchIt! Exe/Py
appFolder = os.path.abspath(os.getcwd())
# Location of Settings folder
settingsFol = os.path.join(appFolder, "Settings")
# PatchIt! Icon
appIcon = os.path.join(appFolder, "Icons", "PiIcon.ico")
# Build number (v3 Pickle data)
buildFile = os.path.join(appFolder, "Build.pickle")


def getBuildNumber():
    """Retrieve and update the build number."""
    from Settings.buildgen import (BuildNumber, UpdateBuildNumber)
    bn = BuildNumber.Instance()
    buildNum = bn.fetch()

    # This is a frozen exe and the data is missing; assign a "number"
    if buildNum is None:
        buildNum = "Unknown"

    # If this is not a frozen exe,
    if not (hasattr(sys, "frozen") and
            sys.frozen not in ("windows_exe", "console_exe")):
        # and if this is not a Stable release,
        if minVer != "Stable":
            # then increase the build number.
            UpdateBuildNumber().updateBuild(buildNum)
    return buildNum
