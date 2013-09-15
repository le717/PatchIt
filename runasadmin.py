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
# PatchIt! V1.1.2 Stable RunAsAdmin Intergration
"""

import os
import subprocess

# Tkinter GUI library
from tkinter import Tk
from tkinter.messagebox import (showerror, askyesno)

# App Logging
import logging

# PatchIt! "Constants"
import constants


class AdminRun(object):
    """Invokes the RunAsAdmin helper utility"""

    def __init__(self):
        """Draw (then withdraw) root Tkinter window"""
        self.main = Tk()
        self.main.withdraw()
        self.main.iconbitmap(constants.app_icon)

    def launch(self, messages):
        """Relaunch PatchIt! with administrator rights"""

        # Display any message(s) properly
        if messages[1:] == []:
            end = ""
        else:
            end = "".join(messages[1:])

        __admin = askyesno("Relaunch PatchIt?",
                           '''{0}
Would you like to relaunch PatchIt! with Administrator rights? {1}'''.format(
    messages[0], end))

        # User does not want to relaunch PatchIt!
        if not __admin:
            logging.info("User does not want to relaunch PatchIt !with Admin rights")
            self.main.destroy()
            return False
        # If user wants to relaunch
        else:
            logging.info("User wants to relaunch PatchIt! with Admin rights")

            # This is the raw Python script. RunAsAdmin will not work
            if (constants.exe_name.endswith("py") or
                    constants.exe_name.endswith("pyw")):
                logging.warning('''This is a raw Python script ({0})
RunAsAdmin.exe cannot operate!'''.format(constants.exe_name))

                showerror("Running Error!",
                          '''You are running a raw Python script ({0}).
RunAsAdmin will not work at all.'''.format(constants.exe_name))
                self.main.destroy()
                return False

            # Launch RunAsAdmin to reload PatchIt!
            else:
                logging.info('''This is an exe ({0}).
Launching RunAsAdmin.exe'''.format(constants.exe_name))

                subprocess.call(
                    [os.path.join(constants.app_folder, "RunAsAdmin.exe"),
                        constants.exe_name])

                # Now we close PatchIt!, and let RunAsAdmin take over
                # (that is, if this is an exe)
                self.main.destroy()
                logging.shutdown()
                raise SystemExit(0)
