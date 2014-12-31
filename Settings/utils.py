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
import sys
import logging
import argparse
import platform

import runasadmin
import constants as const
from singleton import Singleton

__all__ = ("Utils")


@Singleton
class Utils(object):

    """Utility functions.

    Contains utility functions for PatchIt!, including:
    * Logging initialization
    * Windows platform check
    * Command-line parameter initialization
    * App configuration path

    Exposes the following public items:
    * openArg {Boolean} True if the open parameter was correctly invoked.
    * isWindows {Boolean} True if the user is using the Windows platform.
    * configPath {String} App configuration path.
    """

    def __init__(self):
        """Initalize public properties and run utility functions."""
        self.openArg = None
        self.isWindows = "Windows" in platform.platform()
        self.configPath = self._getConfigPath()
        self._startLog()
        self._commandLine()

    def _getConfigPath(self):
        """Get the file path where configuration files will be stored.

        On Windows, the root folder is %AppData%, while on Mac OS X and Linux
        it is ~. On all platforms, the rest of the path is Triangle717/PatchIt.

        @returns {String} The configuration path.
        """
        root = os.path.expanduser("~")
        if self.isWindows:
            root = os.path.expandvars("%AppData%")

        # Create the path if needed
        path = os.path.join(root, "Triangle717", "PatchIt")
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def _commandLine(self):
        """Command-line arguments parser."""
        logging.info("Command-line arguments processor started")
        parser = argparse.ArgumentParser(
            description="{0} {1} Command-line arguments".format(
                const.app, const.version))

        # Command line arguments
        parser.add_argument("-t", "--test",
                            help="""Enable PatchIt! experimental features.
There are currently no experimental features.""",
                            action="store_true")
        parser.add_argument("-o", "--open",
                            help="""Confirm and install a PatchIt! Patch
without going through the menu first""")

        # Register parameters
        args = parser.parse_args()
        testArg = args.test
        openArg = args.open

        # Set the value of the open argument
        self.openArg = openArg
        os.system("title {0} {1} {2}".format(
                  const.app, const.version, const.minVer))

        # Experimental Mode was activated
        if testArg:
            const.testMode = True
            os.system("title {0} Version {1} {2} - Experimental Mode".format(
                      const.app, const.version, const.minVer))
            logging.info("Starting PatchIt! in Experimental Mode")
        return True

    def _startLog(self):
        pythonArch = "x64"
        logsFolder = os.path.join(self.configPath, "Logs")
        loggingFile = os.path.join(logsFolder, "PatchIt.log")

        # Check if Python is x86
        if sys.maxsize < 2 ** 32:
            pythonArch = "x86"

        try:
            # Create the logs folder if needed
            if not os.path.exists(logsFolder):
                os.mkdir(logsFolder)

            logging.basicConfig(
                level=logging.DEBUG,
                format="%(asctime)s : %(levelname)s : %(message)s",
                filename=loggingFile,
                filemode="a"
            )

            logging.info("Begin logging to {0}".format(loggingFile))
            logging.info("You are running {0} {1} {2} on {3} {4}.".format(
                         platform.python_implementation(),
                         pythonArch,
                         platform.python_version(),
                         platform.machine(),
                         platform.platform())
                         )
            logging.info("""
#########################################
{0} v{1}
Created 2013-2015 {2}


If you run into a bug, open an issue at
https://github.com/le717/PatchIt/issues
and attach this file for an quicker fix!
#########################################
                                    """.format(const.app, const.version,
                                               const.creator))
            return True

        except PermissionError:
            # User did not want to reload with Administrator rights
            if not runasadmin.AdminRun().launch(
                    "PatchIt! does not have the user rights to operate!"):
                raise SystemExit(0)
