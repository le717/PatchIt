"""
    PatchIt! -  the standard yet simple way to packaging and install mods for LEGO Racers
    Copyright 2013 Triangle717 <http://triangle717.wordpress.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
# PatchIt! V1.0.3 Stable Logging code

# logging.BasicConfig code based on example from A Byte of Python
# http://www.swaroopch.com/notes/Python

import os, logging, time
import color, color.colors as colors

# ------------ Begin PatchIt! Logging Code ------------ #

def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    try:
        # The Logs folder does not exist in the current directory
        if not os.path.exists(os.path.join(os.getcwd(), "Logs")):

            # Create the Logs folder
            logsfolder = os.mkdir(os.path.join(os.getcwd(), "Logs"))
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

    # PatchIt! does not have the righst to set the Log Config
    except PermissionError:
        colors.pc("\nPatchIt! does not have the user rights to operate!\nPlease relaunch PatchIt! as an Administrator.", color.FG_LIGHT_RED)
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit


# AKA if this is imported as a module
if "__main__" != __name__:
    appLoggingFolder()
    logging_file = os.path.join(os.getcwd(), "Logs", 'TheWritingsofPatchIt.log')
    logConfig()

# ------------ End PatchIt! Logging Code ------------ #