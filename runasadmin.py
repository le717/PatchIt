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

import os
import subprocess

# Tkinter GUI library
import tkinter
from tkinter.messagebox import (showerror, askyesno)

# App Logging
import logging

# PatchIt! Constants
import constants as const


class AdminRun(object):

    """Invokes the RunAsAdmin helper utility."""

    def __init__(self):
        """Create root Tkinter window."""
        self.__main = tkinter.Tk()
        self.__main.withdraw()
        self.__main.iconbitmap(const.appIcon)

    def launch(self, messages):
        """Relaunch PatchIt! with administrator rights."""
        # Display any message(s) properly
        if messages[1:] == []:
            end = ""
        else:
            end = "".join(messages[1:])

        admin = askyesno("Relaunch PatchIt?", """{0}
Would you like to relaunch PatchIt! with Administrator rights? {1}""".format(
                         messages[0], end))

        # User does not want to relaunch PatchIt!
        if not admin:
            logging.warning("User does not want to relaunch with Admin rights")
            self.__main.destroy()
            return False

        # If user wants to relaunch
        else:
            logging.info("User wants to relaunch with Admin rights")

            # This is the raw Python script. RunAsAdmin will not work
            if (const.exeName.endswith("py") or
                    const.exeName.endswith("pyw")):
                logging.warning("""This is a raw Python script ({0})
RunAsAdmin.exe cannot operate!""".format(const.exeName))

                showerror("Running Error!",
                          """You are running a raw Python script ({0}).
RunAsAdmin will not work at all.""".format(const.exeName))
                self.__main.destroy()
                return False

            # Launch RunAsAdmin to reload PatchIt!
            else:
                logging.info("""This is an exe ({0}).
Launching RunAsAdmin.exe""".format(const.exeName))

                subprocess.call([os.path.join(
                    const.appFolder, "RunAsAdmin.exe"), const.exeName])

                # Now we close PatchIt!, and let RunAsAdmin take over
                self.__main.destroy()
                logging.shutdown()
                raise SystemExit(0)
