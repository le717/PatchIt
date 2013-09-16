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
PatchIt! Constants
"""

import sys
import os

# App name and version
app = "PatchIt!"
majver = "1.1.2"
minver = "Unstable"
creator = "Triangle717"

# GLobal game data
LR_game = "LEGO Racers"
LOCO_game = "LEGO LOCO"
LR_settings = "Racers.cfg"
LOCO_settings = "LOCO.cfg"
Pi_settings = "PatchIt.cfg"

# Name of PatchIt! Exe/Py
exe_name = os.path.basename(sys.argv[0])
# Location of PatchIt! Exe/Py
app_folder = os.path.dirname(sys.argv[0])
# Location of Settings folder
settings_fol = os.path.join(app_folder, "Settings")
# PatchIt! App Icon
app_icon = os.path.join(app_folder, "Icons", "PiIcon.ico")
# Build number (v3 Pickle data)
build_file = os.path.join(app_folder, "Build.pickle")


def buildme():
    """Get and set the build number """
    from Settings import buildgen
    build_num = buildgen.get_build()

    # This is a frozen exe and the data is missing; assign a "number"
    if build_num is None:
        build_num = "Unknown"

    # If this is not a frozen exe,
    if not (hasattr(sys, "frozen") and
            not sys.frozen in ("windows_exe", "console_exe")):
        # and if this is not a Stable release,
        if minver != "Stable":
            # increase the build number.
            buildgen.update_build(build_num)
    return build_num
