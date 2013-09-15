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
"""
# LEGO Racers Launcher

import os
import shutil
import subprocess
from constants import app_folder


def run(install_path):
    """Runs LEGO Racers"""
    # Run the game directly
    try:
        subprocess.call(os.path.join(install_path, "LEGORacers.exe"))
        raise SystemExit(0)

    # Except we need admin righs to do it
    except OSError:
        # Change the cwd to C:\Users\MyUser
        os.chdir(os.path.expanduser("~"))
        curDir = os.getcwd()

        # Copy RunAsAdmin from the PatchIt! installation to the cwd
        shutil.copy2(os.path.join(app_folder, "RunAsAdmin.exe"), curDir)
        # Write the required CFG
        with open("RunAsAdmin.cfg", "wt", encoding="utf-8") as f:
            f.write(os.path.join(install_path, "LEGORacers.exe"))

        # Now we can run LEGO Racers
        subprocess.call("RunAsAdmin.exe")

        # Delete the files, and close.
        os.unlink("RunAsAdmin.exe")
        os.unlink("RunAsAdmin.cfg")
        raise SystemExit(0)
