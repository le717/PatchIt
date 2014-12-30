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
from Settings import utils
from Settings.buildgen import BuildNumber

app = "PatchIt!"
version = "1.1.3"
minVer = "Unstable"
creator = "Triangle717"
testMode = False

LRGame = "LEGO Racers"
LRSettings = "Racers.json"
LRSettingsCfg = "Racers.cfg"
piSettings = "PatchIt.json"

exeName = os.path.basename(sys.argv[0])
appFolder = os.path.dirname(sys.argv[0])
settingsFol = os.path.join(utils.Utils().configPath, "Settings")

appIcon = os.path.join(appFolder, "Icons", "PiIcon.ico")
# Build number (Pickle v3)
buildFile = os.path.join(appFolder, "Build.pickle")


def getBuildNumber():
    """Retrieve and update the build number."""
    bn = BuildNumber.Instance()
    buildNum = bn.buildNum
    bn.updateBuild(buildNum)

    # This is a frozen exe and the data is missing, assign a "number"
    if buildNum is None:
        buildNum = "Unknown"
    return buildNum
