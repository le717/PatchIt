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
import json
import logging

import tkinter
from tkinter import filedialog

import constants as const
from Settings import encoding
from singleton import Singleton

__all__ = ("main", "Settings")


def main(auto=False):
    """Game settings user interface."""
    # Create the settings object
    mySettings = Settings.Instance()
    mySettings.readSettings()
    details = mySettings.getDetails()

    # Shortcut to installation path,
    # plus fix if the path is blank
    installPath = details[0]
    gameVersion = details[1]

    if installPath == "":
        installPath = const.appFolder
    if gameVersion not in ("1999", "2001"):
        gameVersion = "unknown"

    # The settings do not exist
    if (
        (auto and not details[2]) or
        (not auto and not details[2])
    ):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showerror("Invalid installation!",
                                     "Cannot find {0} installation at {1}"
                                     .format(const.LRGame, installPath))
        root.destroy()
        return False

    # The settings exist, are valid, and this is user prompt
    if not auto and details[2]:
        print("""
A {0} {1} release was found at

{2}

Would you like to change this?
""".format(const.LRGame, gameVersion, installPath))

        changeInstallPath = input(r"[Y\N] > ")

        # Yes, I want to change the defined installation
        if changeInstallPath.lower() == "y":
            logging.info("User wants to change the settings")
            if not mySettings.getInstallInfo():
                return False

        # No, I do not want to change the defined installation
        else:
            logging.info("""User does not want to change the
defined game installation or pressed an undefined key""")
            return False


@Singleton
class Settings(object):

    """Settings Management.

    Exposes one public method:
    * getDetails {boolean} TODO.
    * getInstallInfo {boolean} TODO.
    """

    def __init__(self):
        """Object-only values."""
        self.__piFirstRun = "1"
        self.__installLoc = ""
        self.__releaseVersion = ""
        self.__settingsData = None
        self.__settingsExist = True
        self.__settingsFormat = "json"

    def getDetails(self):
        """Return installation details."""
        return (self.__installLoc, self.__releaseVersion, self.__settingsExist)

    def _setDetails(self):
        """Set details gathered by from reading."""
        try:
            self.__piFirstRun = self.__settingsData["firstRun"]
            self.__releaseVersion = self.__settingsData["releaseVersion"]
            self.__installLoc = self.__settingsData["installPath"]
            return True

        # One of the keys in the JSON was missing
        except KeyError:
            logging.warning("A required JSON key was missing!")
            return False

    # ------- Begin JSON/CFG Reading and Writing ------- #

    def _writeSettings(self, releaseVersion, installLoc):
        """Write JSON-based settings file."""
        jsonData = {
            "firstRun": "1",
            "installPath": installLoc,
            "releaseVersion": releaseVersion
        }

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(const.settingsFol):
            os.mkdir(const.settingsFol)

        with open(os.path.join(const.settingsFol, const.LRSettings),
                  "wt") as f:
            f.write(json.dumps(jsonData, indent=4, sort_keys=True))
        return True

    def _readSettingsJson(self):
        """Read JSON-based settings file."""
        try:
            with open(os.path.join(const.settingsFol, const.LRSettings),
                      "rt", encoding="utf-8") as f:
                self.__settingsData = json.load(f)
            return True

        # The file is not valid JSON
        except ValueError:
            logging.error("""{0} is not valid JSON!
The content cannot be retrieved!""".format(const.LRSettings))
            return False

    def _convertToJson(self, cfgData):
        """Convert CFG-based settings to JSON-based settings."""
        try:
            # This is a first run, create the settings
            if cfgData[2].strip() == "0":
                logging.info("This is first time PatchIt! has been run")
                self.getInstallInfo()
                return False

            # The settings have been set up before, convert them
            else:
                self._writeSettings(cfgData[4].strip(), cfgData[6].strip())
                self._readSettingsJson()
                self._setDetails()
            return True

        # There was an error reading the settings
        except IndexError:
            logging.warning("There was an error reading the CFG settings!")
            self.getInstallInfo()
            return False

    def _readSettingsCfg(self):
        """Read older CFG-based settings file."""
        with open(os.path.join(const.settingsFol, const.LRSettingsCfg),
                  "rt", encoding="utf_8") as f:
            cfgData = f.readlines()
        return cfgData

    # ------- End JSON/CFG Reading and Writing ------- #

    # ------- Begin Settings Confirmation and Detection ------- #

    def _getVersion(self, exeLoc):
        """Detect game release version."""
        # Open the exe and read a small part of it
        try:
            with open(exeLoc, "rb") as f:
                offset = f.readlines()[1][8:20]

            # This is a 1999 release
            if offset in (b"\xb7S\xfeK\xf32\x90\x18\xf32\x90\x18" or
                          b"bPE\x00\x00L\x01\x08\x00\xf1\xdb)7"):

                logging.info("According to the offset, this is a 1999 release")
                self.__releaseVersion = "1999"

            # This is a 2001 release
            elif offset == b"\xd7\xf2J\x1a\x93\x93$I\x93\x93$I":
                logging.info("According to the offset, this is a 2001 release")
                self.__releaseVersion = "2001"
            return True

        # We could not find the data we wanted (most likely a fake exe)
        except IndexError:
            logging.warning("Game release version could not be determined!")
            self.__releaseVersion = ""
            return False

    def _confirmSettings(self):
        """Confirm information given in settings."""
        # Exe, JAM, and DLL locations
        exeLoc = os.path.join(
            self.__installLoc, "legoracers.exe".lower())
        jamLoc = os.path.join(self.__installLoc, "lego.jam".lower())
        dllLoc = os.path.join(self.__installLoc, "goldp.dll".lower())

        # The settings have never been set up
        if self.__piFirstRun == "0" and self.__settingsExist:
            logging.warning("Settings have not been set up!")
            return False

        # The settings have never been set up
        if not os.path.isdir(self.__installLoc) or not os.path.exists(exeLoc):
            logging.warning("A game installation is not defined!")
            return False

        # Determine the release version
        self._getVersion(exeLoc)

        # The release version was not recognized
        if self.__releaseVersion != ("1999" or "2001"):
            logging.warning("Unrecognized game release version: {0}!".format(
                self.__releaseVersion))

        # The release version is known
        if self.__settingsData is not None:
            logging.info("LEGO Racers Release version {0} detected"
                         .format(self.__settingsData["releaseVersion"]))
            self.__settingsData["releaseVersion"] = self.__releaseVersion

        # The necessary files were found
        if (
            os.path.exists(exeLoc) and
            os.path.exists(jamLoc) and
            os.path.exists(dllLoc)
        ):
            logging.info("LEGO Racers installation confirmed at {0}".format(
                self.__installLoc))
            return True

        # Nope, some files were mising :(
        logging.warning("LEGO Racers installation could not be confirmed!")
        return False

    def _findSettings(self):
        """Locate the settings."""
        # The preferred JSON settings do not exist
        if not os.path.exists(os.path.join(
                              const.settingsFol, const.LRSettings)):
            logging.warning("Could not find settings!")
            self.__settingsFormat = "cfg"

            # Since those could not be found, look for the older CFG settings
            if not os.path.exists(os.path.join(
                                  const.settingsFol, const.LRSettingsCfg)):
                logging.warning("Could not find CFG settings!")
                self.__settingsExist = False
                return False
        return True

    # ------- Begin Settings Confirmation and Detection ------- #

    def getInstallInfo(self):
        """Get details to write settings."""
        # Draw (then withdraw) the root Tk window
        root = tkinter.Tk()
        root.withdraw()

        # Overwrite root display settings
        logging.info("Overwrite root Tk window settings to hide it")
        root.overrideredirect(True)
        root.geometry('0x0+0+0')

        # Show window again, lift it so it can receive the focus
        # Otherwise, it is behind the console window
        root.deiconify()
        root.lift()
        root.focus_force()

        # Select the game installation
        logging.info("Display file dialog requesting game installation")
        newInstallLoc = filedialog.askopenfilename(
            parent=root,
            title="Where is LEGORacers.exe",
            defaultextension=".exe",
            filetypes=[("LEGORacers.exe", "*.exe")]
        )

        # Get the directory the exe is in
        newInstallLoc = os.path.dirname(newInstallLoc)

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # The user clicked the Cancel button
        if not newInstallLoc:
            # Go back to the main menu
            logging.warning(
                "User did not select a new game installation!")
            return False

        logging.info("User selected a new game installation at {0}"
                     .format(newInstallLoc))

        # Confirm given data
        self.__piFirstRun = "1"
        self.__installLoc = newInstallLoc
        if self._confirmSettings():
            # Now that the information has been confirmed,
            # write a settings file
            self._writeSettings(self.__releaseVersion, self.__installLoc)
            self.__settingsExist = True
            self.__settingsFormat = "json"
            return True
        return False

    def readSettings(self):
        """Read settings file."""
        # Confirm the settings exist and are readable
        self._findSettings()

        # The settings could not be found, go write the settings
        if not self.__settingsExist:
            logging.warning("Settings do not exist!")
            if self.getInstallInfo():
                return True
            return False

        # Read the proper file to get the data needed
        if self.__settingsFormat == "json":
            if self._readSettingsJson():
                self._setDetails()

            # We might have encountered some invalid JSON.
            # This means we have to recreate the entire settings
            else:
                logging.warning("The JSON could not be parsed!")
                self.__settingsExist = False
                if self.getInstallInfo():
                    return True
                return False
        else:
            # Rewrite into JSON settings
            cfgData = self._readSettingsCfg()
            self._convertToJson(cfgData)

        # Installation confirmed, our job here is done
        if self._confirmSettings():
            self._writeSettings(self.__releaseVersion, self.__installLoc)
            logging.info("Settings confirmed")
            return True

        # The installation could not be confirmed
        else:
            self.__settingsExist = False
            logging.warning("Settings could not be confirmed!")
            if self.getInstallInfo():
                return True
            return False
