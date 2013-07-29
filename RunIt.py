#! python3
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    But seek ye first the kingdom of YHWH,
    and His righteousness; and all these things
    shall be added unto you. - Matthew 6:33

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

# PatchIt! V1.1.1 Stable Python Version Check,
# PatchIt! Logger, and PatchIt! Launcher
# logging.BasicConfig code based on example from A Byte of Python
# http://www.swaroopch.com/notes/Python
import sys
import os
import webbrowser

# PatchIt! Version Info
from constants import (app, majver, minver)

try:
    # Python 3 import
    import tkinter as tk
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2 import
    import Tkinter as tk
    from tkMessageBox import showerror

# User is not running < Python 3.3.0
if sys.version_info < (3, 3, 0):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap("Icons/PatchItIcon.ico")
    showerror("Unsupported Python Version!", '''You are running Python {0}.
You need to download Python 3.3.0 or newer to run\n{1} {2} {3}.\n'''.format(
    sys.version[0:5], app, majver, minver))

    # Opens only when user clicks OK
    # New tab, raise browser window (if possible)
    webbrowser.open_new_tab("http://python.org/download/")

    # Close PatchIt!  when user presses OK
    raise SystemExit(0)

# (Implied else block here)
# The user is running Python 3.3.x, continue on
import logging
import PatchIt

# Location of PatchIt!
app_folder = os.path.dirname(sys.argv[0])

# ------------ Begin PatchIt! Logging Code ------------ #


def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    try:
        # Location of Logs folder
        logs_folder = os.path.join(app_folder, "Logs")

        # The Logs folder does not exist
        if not os.path.exists(logs_folder):

            # Create the Logs folder
            os.mkdir(logs_folder)

    # -- Begin Logging Configuration -- #

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filename=os.path.join(logs_folder, 'PatchIt.log'),
            # "a" so the Logs is appended to and not overwritten
            # and is created if it does not exist
            filemode='a'
        )

    # -- End Logging Configuration -- #

    except PermissionError:
        root = tk.Tk()
        root.withdraw()
        root.iconbitmap("Icons/PatchItIcon.ico")
        showerror("Insufficient User Rights!",
        '''PatchIt! does not have the user rights to operate!
Please relaunch PatchIt! as an Administrator.''')

        # Close PatchIt! when user presses OK
        raise SystemExit(0)


# ------------ End PatchIt! Logging Code ------------ #

if __name__ == "__main__":
    # Run PatchIt! Initialization
    appLoggingFolder()

    # Write window title (since there is no GUI in PatchIt! itself (yet))
    os.system("title {0} {1} {2}".format(app, majver, minver))
    PatchIt.info()
    PatchIt.args()
    PatchIt.preload()