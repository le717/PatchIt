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
# PatchIt! V1.1.2 Unstable RunAsAdmin Intergration

import os
import subprocess

# Tkinter GUI library
from tkinter import Tk
from tkinter.messagebox import askyesno

# App Logging
import logging

# PatchIt! "Constants"
import constants


def AdminRun():
    """Relaunch PatchIt! with administrator rights"""
    # Draw (then withdraw) root Tkinter window
    root = Tk()
    root.withdraw()
    root.iconbitmap(constants.app_icon)

    admin = askyesno("Relaunch PatchIt?",
'''PatchIt! does not have the user rights to operate!
Would you like to relaunch PatchIt! with Administrator rights?''')

    # If user chooses to relaunch
    if admin:
        # Launch RunAsAdmin to reload PatchIt!
        if (constants.exe_name.endswith("py") or
        constants.exe_name.endswith("pyw")):
            print('''
You are running the raw PatchIt! Python script.
RunAsAdmin will not work at all.''')
        else:
            subprocess.call(
                [os.path.join(constants.app_folder, "RunAsAdmin.exe"),
                constants.exe_name])
        # Now we close PatchIt!, and let RunAsAdmin take over
        # (that is, if this is an exe)
        logging.shutdown()
        raise SystemExit(0)

    # User did not want to relaunch PatchIt!
    else:
        return False