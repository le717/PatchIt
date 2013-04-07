#!python3
"""
    This file is part of PatchIt!

    PatchIt! -  the standard yet simple way to package and install mods for LEGO Racers
    Copyright 2013 Triangle717 <http://triangle717.wordpress.com>

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
# PatchIt! V1.1.0 Unstable Python Version Check and PatchIt! Launcher
import sys, os, webbrowser, time

app = "PatchIt!"
majver = "Version 1.1.0"
minver = "Unstable"

# Write window title (since there is no GUI)
os.system("title {0} {1} {2}".format(app, majver, minver))

# User is not running Python 3.3.1
if sys.version_info < (3,3,1):
    sys.stdout.write("\nYou need to download Python 3.3.1 to run {0} {1} {2}.\n".format(app, majver, minver))

    # Don't open browser immediately
    time.sleep(2)
    webbrowser.open_new_tab("http://python.org/download") # New tab, raise browser window (if possible)

    # Close PatchIt!
    raise SystemExit

# (Implied else block here)
# The user is running Python 3.3.1, import PatchIt
import PatchIt
if __name__ == "__main__":
    # Run PatchIt! Initialization
    PatchIt.cmdArgs()
    PatchIt.preload()


