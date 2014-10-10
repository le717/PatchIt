#! /usr/bin/env python3
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
import webbrowser
import constants as const

try:
    # Python 3
    import tkinter as tk
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2
    import Tkinter as tk
    from tkMessageBox import showerror

# User is running < Python 3.3.0
if sys.version_info[:2] < (3, 3):
    root = tk.Tk()
    root.withdraw()
    showerror("Unsupported Python Version!", '''You are running Python {0}.
You need to download Python 3.3.0 or newer to run\n{1} {2} {3}.\n'''.format(
        sys.version[0:5], const.app, const.version, const.minVer))
    webbrowser.open_new_tab("http://python.org/download/")
    raise SystemExit(0)

# The user is running Python 3.3+, continue on
import PatchIt
from Settings import utils

if __name__ == "__main__":
    init = utils.Utils()
    PatchIt.preload(init.openArg)
