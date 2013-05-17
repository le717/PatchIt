#! python3
# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! -  the standard and simple way to package and install mods for LEGO Racers
    Created 2013 Triangle717 <http://triangle717.wordpress.com>

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
# PatchIt! V1.1.0 Unstable Python Version Check, PatchIt! Logger, and PatchIt! Launcher
# logging.BasicConfig code based on example from A Byte of Python
# http://www.swaroopch.com/notes/Python
import sys
import os
import webbrowser
import time

try:
    # Python 3 import
    import tkinter as tk
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2 import
    import Tkinter as tk
    from tkMessageBox import showerror

app = "PatchIt!"
majver = "Version 1.1.0"
minver = "RC2"

# User is not running Python 3.3.0
if sys.version_info < (3,3,0):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap("Icons/PatchItIcon.ico")
    py_ver_error = showerror("Unsupported Python Version!", "You are running Python {0}.\nYou need to download Python 3.3.0 or newer to run\n{1} {2} {3}.\n".format(sys.version[0:5], app, majver, minver))
    #sys.stdout.write("\nYou are running Python {0}.\nYou need to download Python 3.3.0 or newer to run\n{1} {2} {3}.\n".format(sys.version[0:5], app, majver, minver))

    # Opens only when user clicks OK
    webbrowser.open_new_tab("http://python.org/download/") # New tab, raise browser window (if possible)

    # Close PatchIt!
    raise SystemExit

# (Implied else block here)
# The user is running Python 3.3.x, continue on
import logging
import Color as color, Color.colors as colors
import PatchIt

app_path = sys.argv[0].rstrip(os.path.basename(sys.argv[0]))

# ------------ Begin PatchIt! Logging Code ------------ #

def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    try:
        # The Logs folder does not exist in the current directory
        if not os.path.exists(os.path.join(app_path, "Logs")):

            # Create the Logs folder
            logsfolder = os.mkdir(os.path.join(app_path, "Logs"))

    except PermissionError:
        colors.pc("\nPatchIt! does not have the user rights to operate!\nPlease relaunch PatchIt! as an Administrator.", color.FG_LIGHT_RED)
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit

def logConfig():
    '''Set Logging Settings'''
    try:

    # -- Begin Logging Config -- #

        logging.basicConfig(
            level = logging.DEBUG,
            format = "%(asctime)s : %(levelname)s : %(message)s",
            filename = logging_file,
            filemode = 'a+',
        )

    # -- End Logging Config -- #

    # PatchIt! does not have the rights to set the Log Config
    except PermissionError:
        colors.pc("\nPatchIt! does not have the user rights to operate!\nPlease relaunch PatchIt! as an Administrator.", color.FG_LIGHT_RED)

        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit

if __name__ == "__main__":
    # Run PatchIt! Initialization
    appLoggingFolder()
    logging_file = os.path.join(app_path, "Logs", 'PatchIt.log')
    logConfig()
    # Write window title (since there is no GUI in PatchIt! itself)
    os.system("title {0} {1} {2}".format(app, majver, minver))
    PatchIt.info()
    PatchIt.Args()
    PatchIt.preload()